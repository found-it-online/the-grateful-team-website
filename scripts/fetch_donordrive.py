"""
Download raw DonorDrive JSON for CI. Writes /tmp/*.json consumed by update_stats.py.
Stdlib urllib only — avoids curl -f quirks and CRLF-breaking bash \\ line continuations.
"""

from __future__ import annotations

import json
import sys
import time
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE = 'https://makeawishmichigan.donordrive.com/api/teams/5450'
HEADERS = {
    'Accept': 'application/json',
    'User-Agent': (
        'Mozilla/5.0 (compatible; TGT-StatsRefresh/1.0; +https://thegratefulteam.com)'
    ),
}
TIMEOUT = 30
ATTEMPTS = 4


def _http_get(url: str) -> tuple[int, bytes]:
    req = Request(url, headers=HEADERS, method='GET')
    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            return resp.getcode(), resp.read()
    except HTTPError as e:
        return e.code, e.read()


def fetch(url: str) -> bytes:
    last_exc: BaseException | None = None
    for attempt in range(ATTEMPTS):
        try:
            code, body = _http_get(url)
            if code == 200:
                return body
            preview = body[:700].decode('utf-8', errors='replace')
            raise RuntimeError(f'HTTP {code} — {preview}')
        except BaseException as e:
            last_exc = e
            wait = min(30, (attempt + 1) * 3)
            print(f'::warning::GET {url!r} ({attempt + 1}/{ATTEMPTS}): {e}', file=sys.stderr)
            if attempt < ATTEMPTS - 1:
                time.sleep(wait)
    assert last_exc is not None
    raise last_exc


def save_valid_json(raw: bytes, dest: str) -> None:
    json.loads(raw.decode('utf-8'))
    with open(dest, 'wb') as f:
        f.write(raw)
    print(f'Wrote {dest} ({len(raw)} bytes)')


def main() -> None:
    print('Fetching team...')
    save_valid_json(fetch(f'{BASE}'), '/tmp/team.json')

    donation_urls = (f'{BASE}/donations?limit=100', f'{BASE}/donations')
    donations_raw = None
    for u in donation_urls:
        print(f'Fetching donations… {u}')
        try:
            donations_raw = fetch(u)
            break
        except BaseException:
            continue
    if donations_raw is None:
        raise SystemExit('All donation URLs failed.')
    save_valid_json(donations_raw, '/tmp/donations.json')

    print('Fetching participants...')
    save_valid_json(
        fetch(f'{BASE}/participants?limit=100&orderBy=displayName'),
        '/tmp/participants.json',
    )
    print('All DonorDrive fetches complete.')


if __name__ == '__main__':
    main()
