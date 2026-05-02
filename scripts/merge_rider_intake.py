#!/usr/bin/env python3
"""
Merge a single rider from GitHub repository_dispatch client_payload into assets/data/rider-intake.json.

Expected client_payload (repository_dispatch event_type: rider-card-intake):
  secret          — must match repo secret RIDER_INTAKE_WEBHOOK_SECRET
  name            — DonorDrive display name (required)
  donorSlug       — participant id or slug from URL (required)
  nickname        — (required)
  initials        — (required)
  song            — (required)
  bio             — (required)
  funFact         — optional string
  badges          — optional list of strings
  years           — optional int, default 1 (first WAM season)

New form riders are always stored as tier \"rookie\" for the trading card.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTAKE_PATH = ROOT / "assets" / "data" / "rider-intake.json"


def _slug_from_url_or_id(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        raise ValueError("donorSlug empty")
    if s.startswith("http"):
        m = re.search(r"/participants/([^/?#]+)/?", s, re.I)
        if m:
            return m.group(1)
    return s.strip("/ ")


def load_intake() -> dict:
    if not INTAKE_PATH.is_file():
        return {"nextId": 52, "riders": []}
    return json.loads(INTAKE_PATH.read_text(encoding="utf-8"))


def save_intake(data: dict) -> None:
    INTAKE_PATH.parent.mkdir(parents=True, exist_ok=True)
    INTAKE_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    evt_path = os.environ.get("GITHUB_EVENT_PATH")
    if not evt_path:
        print("GITHUB_EVENT_PATH not set", file=sys.stderr)
        sys.exit(1)

    raw = Path(evt_path).read_text(encoding="utf-8-sig")
    event = json.loads(raw)
    payload = event.get("client_payload") or {}

    want = os.environ.get("RIDER_INTAKE_WEBHOOK_SECRET", "")
    got = payload.get("secret") or ""
    if not want or got != want:
        print("Invalid or missing client_payload.secret", file=sys.stderr)
        sys.exit(1)

    required = ["name", "donorSlug", "nickname", "initials", "song", "bio"]
    missing = [k for k in required if not str(payload.get(k) or "").strip()]
    if missing:
        print(f"Missing required fields: {missing}", file=sys.stderr)
        sys.exit(1)

    data = load_intake()
    riders = data.get("riders")
    if not isinstance(riders, list):
        riders = []

    next_id = int(data.get("nextId") or 52)
    donor_slug = _slug_from_url_or_id(str(payload["donorSlug"]))

    years = payload.get("years")
    try:
        years_i = int(years) if years is not None and str(years).strip() else 1
    except ValueError:
        years_i = 1
    years_i = max(1, min(years_i, 20))

    badges = payload.get("badges") or []
    if isinstance(badges, str):
        badges = [b.strip() for b in badges.split(",") if b.strip()]
    if not isinstance(badges, list):
        badges = []
    badges = [str(b).strip() for b in badges if str(b).strip()]
    if not badges:
        badges = ["🌱 WAM Rookie", "💙 From Spoke to Hope", "⚡ Wish Hero"]

    fun_fact = str(payload.get("funFact") or "").strip() or ""

    initials = str(payload["initials"]).strip().upper()[:4]

    new_rider = {
        "id": next_id,
        "name": str(payload["name"]).strip(),
        "nickname": str(payload["nickname"]).strip(),
        "donorSlug": donor_slug,
        "tier": "rookie",
        "years": years_i,
        "song": str(payload["song"]).strip(),
        "initials": initials,
        "bio": str(payload["bio"]).strip(),
        "funFact": fun_fact,
        "badges": badges,
        "stats": {"spirit": 8, "grit": 7},
        "source": "google-form-intake",
    }

    key = new_rider["name"].lower()
    if any(r.get("name", "").strip().lower() == key for r in riders):
        print(f"Duplicate rider name in intake queue: {new_rider['name']}", file=sys.stderr)
        sys.exit(1)

    riders.append(new_rider)
    data["riders"] = riders
    data["nextId"] = next_id + 1

    save_intake(data)
    print(f"Merged rider id={next_id} name={new_rider['name']!r}")
    print(f"nextId is now {data['nextId']}")


if __name__ == "__main__":
    main()
