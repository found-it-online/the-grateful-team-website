#!/usr/bin/env python3
"""
Fetch multiple pages of GET /clubs/{id}/activities, dedupe by activity id,
write JSON array for update_stats.py. Uses STRAVA_ACCESS_TOKEN or ACCESS_TOKEN.
"""
import json
import os
import sys
import urllib.error
import urllib.request

CLUB_ID = '1302442'
PER_PAGE = 100
MAX_PAGES = int(os.environ.get('STRAVA_CLUB_ACTIVITY_PAGES', '8'))


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

        for a in chunk:
            if not isinstance(a, dict):
                continue
            aid = a.get('id')
            if aid is None or aid in seen:
                continue
            seen.add(aid)
            merged.append(a)

        if len(chunk) < PER_PAGE:
            break

    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(merged, fh)

    print('wrote {} club activities ({})'.format(len(merged), out_path))
    if len(merged) == 0:
        print(
            'warning: no club activities returned — OAuth athlete must be in club 1302442; '
            'token needs activity:read (and refresh token valid).',
            file=sys.stderr,
        )


if __name__ == '__main__':
    main()
