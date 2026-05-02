#!/usr/bin/env python3
"""
Fetch multiple pages of GET /clubs/{id}/activities, dedupe activities,
write JSON array for update_stats.py. Uses STRAVA_ACCESS_TOKEN or ACCESS_TOKEN.

Strava sometimes omits activity `id` on club feed objects — use a stable fallback key
so we do not drop every row (that produced empty strava-rides.json).
"""
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request

CLUB_ID = '1302442'
PER_PAGE = 100
MAX_PAGES = int(os.environ.get('STRAVA_CLUB_ACTIVITY_PAGES', '8'))


def _dedupe_key(activity, page, index_in_page):
    """Stable key for deduping; Strava club activities may omit top-level id."""
    aid = activity.get('id')
    if aid is not None:
        return ('id', str(aid))
    athlete = activity.get('athlete') if isinstance(activity.get('athlete'), dict) else {}
    blob = json.dumps(
        {
            'athlete_id': athlete.get('id'),
            'name': activity.get('name'),
            'distance': activity.get('distance'),
            'moving_time': activity.get('moving_time'),
            'elapsed_time': activity.get('elapsed_time'),
            'sport_type': activity.get('sport_type'),
            'page': page,
            'idx': index_in_page,
        },
        sort_keys=True,
        default=str,
    )
    return ('hash', hashlib.sha256(blob.encode('utf-8')).hexdigest()[:32])


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else '/tmp/strava_activities.json'
    token = (os.environ.get('STRAVA_ACCESS_TOKEN') or os.environ.get('ACCESS_TOKEN') or '').strip()
    if not token:
        print('missing STRAVA_ACCESS_TOKEN / ACCESS_TOKEN', file=sys.stderr)
        sys.exit(1)

    seen = set()
    merged = []

    for page in range(1, max(1, MAX_PAGES) + 1):
        url = (
            'https://www.strava.com/api/v3/clubs/{cid}/activities?per_page={pp}&page={pg}'
            .format(cid=CLUB_ID, pp=PER_PAGE, pg=page)
        )
        req = urllib.request.Request(
            url,
            headers={
                'Authorization': 'Bearer ' + token,
                'Accept': 'application/json',
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read().decode('utf-8')
                chunk = json.loads(raw)
        except urllib.error.HTTPError as e:
            err_body = ''
            try:
                err_body = e.read().decode('utf-8', errors='replace')[:500]
            except Exception:
                pass
            print(
                'club activities page {} HTTP {}: {} {}'.format(
                    page, e.code, e.reason, err_body
                ),
                file=sys.stderr,
            )
            break
        except (urllib.error.URLError, ValueError) as e:
            print('club activities page {} error: {}'.format(page, e), file=sys.stderr)
            break

        if not isinstance(chunk, list):
            break

        for idx, a in enumerate(chunk):
            if not isinstance(a, dict):
                continue
            key = _dedupe_key(a, page, idx)
            if key in seen:
                continue
            seen.add(key)
            merged.append(a)

        if len(chunk) < PER_PAGE:
            break

    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(merged, fh)

    print('wrote {} club activities ({})'.format(len(merged), out_path))
    if len(merged) == 0:
        print(
            'warning: no club activities merged — if GET returned rows but ids were missing, '
            'dedupe fallback should still capture them; otherwise OAuth athlete may not be in club '
            '1302442 or Strava returned an empty list (see strava_ci_check.py logs).',
            file=sys.stderr,
        )


if __name__ == '__main__':
    main()
