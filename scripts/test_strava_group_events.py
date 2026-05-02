"""
Test Strava club group_events API (not in the public Swagger list, but used in the wild).

Web URL example:
  https://www.strava.com/clubs/1302442/group_events/3485775290960780042/occurrences/...

From that you get club_id=1302442 and event_id=3485775290960780042.
The long `occurrences/...` slug is for the website; the REST API usually exposes
occurrences as fields on the event object returned by the list or detail call.

Requires the same env vars as GitHub Actions:
  STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, STRAVA_REFRESH_TOKEN

PowerShell:
  $env:STRAVA_CLIENT_ID="..."
  $env:STRAVA_CLIENT_SECRET="..."
  $env:STRAVA_REFRESH_TOKEN="..."
  python scripts/test_strava_group_events.py [club_id] [event_id]

If event_id is omitted, only GET /clubs/{id}/group_events is tried.
"""

from __future__ import annotations

import json
import os
import sys
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def refresh_access_token():
    cid = os.environ.get("STRAVA_CLIENT_ID")
    secret = os.environ.get("STRAVA_CLIENT_SECRET")
    refresh = os.environ.get("STRAVA_REFRESH_TOKEN")
    if not all([cid, secret, refresh]):
        print(
            "Missing env: STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, STRAVA_REFRESH_TOKEN",
            file=sys.stderr,
        )
        sys.exit(1)
    data = urlencode(
        {
            "client_id": cid,
            "client_secret": secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh,
        }
    ).encode()
    req = Request(
        "https://www.strava.com/api/v3/oauth/token",
        data=data,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read().decode())
    return body["access_token"]


def get_json(url: str, token: str) -> tuple[int, object | str]:
    req = Request(
        url,
        headers={"Authorization": f"Bearer {token}"},
        method="GET",
    )
    try:
        with urlopen(req, timeout=30) as resp:
            raw = resp.read().decode()
            try:
                return resp.getcode(), json.loads(raw)
            except json.JSONDecodeError:
                return resp.getcode(), raw[:2000]
    except HTTPError as e:
        try:
            err_body = e.read().decode()[:2000]
        except OSError:
            err_body = ""
        return e.code, err_body


def main():
    club_id = sys.argv[1] if len(sys.argv) > 1 else "1302442"
    event_id = sys.argv[2] if len(sys.argv) > 2 else None

    token = refresh_access_token()
    print("Token refresh OK.\n")

    list_url = f"https://www.strava.com/api/v3/clubs/{club_id}/group_events"
    code, data = get_json(list_url, token)
    print(f"GET {list_url}")
    print(f"  Status: {code}")
    if isinstance(data, (dict, list)):
        print(json.dumps(data, indent=2)[:12000])
        if isinstance(data, list) and event_id:
            ids = [str(x.get("id", "")) for x in data if isinstance(x, dict)]
            if event_id in ids:
                print(f"\n  (Event {event_id} found in list.)")
            else:
                sample = ids[:5]
                print(
                    f"\n  (Event {event_id} not in first page; sample ids: {sample} ...)"
                )
    else:
        print(f"  Body: {data}")
    print()

    if event_id:
        # Detail (resource_state 3). Note: /clubs/{id}/group_events/{id} returns 404 — not a valid path.
        path = f"https://www.strava.com/api/v3/group_events/{event_id}"
        c2, d2 = get_json(path, token)
        print(f"GET {path}")
        print(f"  Status: {c2}")
        if isinstance(d2, (dict, list)):
            print(json.dumps(d2, indent=2)[:8000])
        else:
            print(f"  Body: {d2}")
        print()


if __name__ == "__main__":
    main()
