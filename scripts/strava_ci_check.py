#!/usr/bin/env python3
"""
GitHub Actions helper: verify OAuth token maps to an athlete and that athlete is in club 1302442.
Reads STRAVA_ACCESS_TOKEN or ACCESS_TOKEN from the environment.
Does not exit non-zero (caller decides); prints GitHub workflow annotations.
"""
import json
import os
import sys
import urllib.error
import urllib.request

CLUB_ID = 1302442


def _get_json(url, token):
    req = urllib.request.Request(
        url,
        headers={
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
        },
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode('utf-8'))


def main():
    token = (os.environ.get('STRAVA_ACCESS_TOKEN') or os.environ.get('ACCESS_TOKEN') or '').strip()
    if not token:
        print('::warning::strava_ci_check: no STRAVA_ACCESS_TOKEN', file=sys.stderr)
        return

    try:
        me = _get_json('https://www.strava.com/api/v3/athlete', token)
    except urllib.error.HTTPError as e:
        body = ''
        try:
            body = e.read().decode('utf-8', errors='replace')[:400]
        except Exception:
            pass
        print(
            '::error::Strava GET /athlete failed HTTP {} — {}'.format(e.code, body),
            file=sys.stderr,
        )
        return
    except Exception as e:
        print('::error::Strava GET /athlete failed: {}'.format(e), file=sys.stderr)
        return

    aid = me.get('id')
    first = (me.get('firstname') or '').strip()
    last = (me.get('lastname') or '').strip()
    print(
        '::notice::Strava OAuth athlete (this account must be IN club {}): id={} name=\"{} {}\"'.format(
            CLUB_ID, aid, first, last
        )
    )

    member_ids = set()
    for page in range(1, 16):
        url = 'https://www.strava.com/api/v3/clubs/{}/members?per_page=200&page={}'.format(
            CLUB_ID, page
        )
        try:
            chunk = _get_json(url, token)
        except urllib.error.HTTPError as e:
            print(
                '::warning::club members page {} HTTP {}'.format(page, e.code),
                file=sys.stderr,
            )
            break
        except Exception as e:
            print('::warning::club members fetch failed: {}'.format(e), file=sys.stderr)
            break
        if not isinstance(chunk, list) or not chunk:
            break
        for m in chunk:
            if not isinstance(m, dict):
                continue
            ath = m.get('athlete') if isinstance(m.get('athlete'), dict) else {}
            mid = m.get('id') or m.get('athlete_id') or ath.get('id')
            if mid is not None:
                member_ids.add(int(mid))
        if len(chunk) < 200:
            break

    if aid is not None and int(aid) in member_ids:
        print('::notice::OAuth athlete {} is in the club member list (first {} pages).'.format(
            aid, page
        ))
    elif aid is not None:
        print(
            '::error::OAuth athlete id {} is NOT in club {} member pages checked ({} ids). '
            'Log into Strava as THAT account and click Join on the club — roster athleteId overrides '
            'do not grant API access.'.format(aid, CLUB_ID, len(member_ids)),
            file=sys.stderr,
        )

    # Sample club activities — proves endpoint + documents payload shape in logs
    try:
        acts = _get_json(
            'https://www.strava.com/api/v3/clubs/{}/activities?per_page=3&page=1'.format(CLUB_ID),
            token,
        )
    except urllib.error.HTTPError as e:
        print(
            '::error::GET /clubs/{}/activities HTTP {}'.format(CLUB_ID, e.code),
            file=sys.stderr,
        )
        return

    if not isinstance(acts, list):
        print('::warning::club activities response is not a list: {}'.format(type(acts).__name__))
        return

    print('::notice::Club activities sample: {} row(s) on page 1 (per_page=3).'.format(len(acts)))
    if acts:
        sample = acts[0]
        if isinstance(sample, dict):
            keys = sorted(sample.keys())
            print('::notice::First activity keys: {}'.format(', '.join(keys)))
            ath = sample.get('athlete')
            print(
                '::notice::First activity athlete field type={} keys={}'.format(
                    type(ath).__name__,
                    sorted(ath.keys()) if isinstance(ath, dict) else str(ath),
                )
            )


if __name__ == '__main__':
    main()
