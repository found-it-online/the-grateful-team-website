import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path


def _env_int(name, default):
    raw = os.environ.get(name)
    if raw is None or str(raw).strip() == '':
        return default
    try:
        return int(raw)
    except ValueError:
        return default

def roster_override_athlete_ids(roster_path='roster.html'):
    p = Path(roster_path)
    if not p.exists():
        return set()
    text = p.read_text(encoding='utf-8')
    i = text.find('const STRAVA_ATHLETE_OVERRIDES = {')
    if i == -1:
        return set()
    brace0 = text.find('{', i)
    depth = 0
    end = brace0
    for j in range(brace0, len(text)):
        if text[j] == '{':
            depth += 1
        elif text[j] == '}':
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    block = text[brace0:end]
    ids = set(re.findall(r'athleteId:\s*(\d+)', block))
    return ids


def _parse_activity_date_iso(s):
    if not s or not isinstance(s, str):
        return None
    s = s.strip()
    if not s:
        return None
    try:
        if s.endswith('Z'):
            dt = datetime.fromisoformat(s.replace('Z', '+00:00'))
        else:
            dt = datetime.fromisoformat(s)
        return dt.astimezone(timezone.utc).date()
    except ValueError:
        return None


def merge_rider_strava_grit(raw_activities, now_iso):
    """
    Per mapped athlete (STRAVA_ATHLETE_OVERRIDES), sum Strava club activity distance (meters)
    for activities on/after countsSince. Grit on cards = miles / max_miles * 10 (cap 10), max_miles default 500.
    Recomputed each run from the merged club activity JSON (no incremental ride counts).
    """
    roster_ids = roster_override_athlete_ids()
    roster_set = set()
    for aid in roster_ids:
        aid_s = str(int(aid)) if str(aid).isdigit() else str(aid).strip()
        if aid_s:
            roster_set.add(aid_s)

    stats_path = Path('assets/data/rider-stats.json')
    stats_path.parent.mkdir(parents=True, exist_ok=True)

    if stats_path.exists():
        with stats_path.open(encoding='utf-8') as fh:
            data = json.load(fh)
            if not isinstance(data, dict):
                data = {}
    else:
        data = {}

    if not isinstance(data.get('byAthleteId'), dict):
        data['byAthleteId'] = {}

    utc_now = datetime.now(timezone.utc)
    default_lb = max(1, _env_int('STRAVA_GRIT_DEFAULT_LOOKBACK_DAYS', 21))
    seed_lb = max(0, _env_int('STRAVA_GRIT_SEED_LOOKBACK_DAYS', 0))

    if data.get('countsSince') is None:
        data['countsSince'] = (utc_now.date() - timedelta(days=default_lb)).strftime('%Y-%m-%d')
    elif seed_lb > 0:
        floor_date = utc_now.date() - timedelta(days=seed_lb)
        try:
            cur = datetime.strptime(data['countsSince'][:10], '%Y-%m-%d').date()
            if cur > floor_date:
                data['countsSince'] = floor_date.strftime('%Y-%m-%d')
        except ValueError:
            data['countsSince'] = floor_date.strftime('%Y-%m-%d')

    counts_since_day = datetime.strptime(data['countsSince'][:10], '%Y-%m-%d').date()

    max_miles = max(1.0, float(_env_int('STRAVA_GRIT_MAX_MILES', 500)))
    data['gritMaxTrainingMiles'] = max_miles

    totals_m = {}
    activities = raw_activities if isinstance(raw_activities, list) else []

    for a in activities:
        if not isinstance(a, dict):
            continue
        athlete = a.get('athlete')
        aid_val = None
        if isinstance(athlete, dict):
            aid_val = athlete.get('id')
        elif isinstance(athlete, (int, float)):
            aid_val = int(athlete)
        if aid_val is None:
            aid_val = a.get('athlete_id')
        start_raw = (
            a.get('start_date')
            or a.get('start_date_local')
            or ''
        )
        if aid_val is None:
            continue
        try:
            aid_s = str(int(aid_val))
        except (TypeError, ValueError):
            aid_s = str(aid_val).strip()
            if not aid_s:
                continue
        if aid_s not in roster_set:
            continue
        day = _parse_activity_date_iso(start_raw)
        # Club feed sometimes omits dates; Strava still only returns "recent" rows — include for grit.
        if day is None:
            day = counts_since_day
        if day < counts_since_day:
            continue
        dist = float(a.get('distance') or 0)
        if dist < 0:
            dist = 0.0
        totals_m[aid_s] = totals_m.get(aid_s, 0.0) + dist

    for aid in roster_ids:
        aid_s = str(int(aid)) if str(aid).isdigit() else str(aid).strip()
        if not aid_s:
            continue
        node = data['byAthleteId'].setdefault(aid_s, {})
        if not isinstance(node, dict):
            node = {}
            data['byAthleteId'][aid_s] = node
        node['totalDistanceMeters'] = round(totals_m.get(aid_s, 0.0), 2)
        node.pop('gritCount', None)
        node['lastFetched'] = now_iso

    data['seenActivityIds'] = []
    data['updatedAt'] = now_iso

    for aid_s, payload in list(data['byAthleteId'].items()):
        if isinstance(payload, dict):
            payload['lastFetched'] = now_iso

    with stats_path.open('w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2)

    mi_total = sum(
        float((v or {}).get('totalDistanceMeters', 0) or 0)
        for v in data['byAthleteId'].values()
        if isinstance(v, dict)
    ) * 0.000621371
    print('rider-stats.json written ({} roster ids, {} keys, ~{:.0f} mi summed club distance, grit max {} mi)'.format(
        len(roster_ids), len(data['byAthleteId']), mi_total, int(max_miles)))

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

with open('/tmp/team.json')         as f: team          = json.load(f)
with open('/tmp/donations.json')    as f: raw_donations  = json.load(f)
with open('/tmp/participants.json') as f: raw_parts      = json.load(f)
try:
    with open('/tmp/strava_activities.json') as f:
        raw_strava_activities = json.load(f)
except FileNotFoundError:
    raw_strava_activities = []
try:
    with open('/tmp/strava_members.json') as f:
        raw_strava_members = json.load(f)
except FileNotFoundError:
    raw_strava_members = []
try:
    with open('/tmp/strava_group_events.json') as f:
        raw_strava_group_events = json.load(f)
except FileNotFoundError:
    raw_strava_group_events = []

# team-stats.json
stats = {
    'sumDonations':    team.get('sumDonations', 0),
    'fundraisingGoal': team.get('fundraisingGoal', 115000),
    'numParticipants': team.get('numParticipants', 0),
    'updatedAt': now,
}
with open('assets/data/team-stats.json', 'w') as f:
    json.dump(stats, f, indent=2)
print('team-stats.json written')

# activity-feed.json (DonorDrive often returns oldest-first; store newest-first)
def _donation_sort_key(d):
    return d.get('createdDateUTC') or ''

donations = [
    {
        'displayName':      d.get('displayName', 'A supporter'),
        'amount':           d.get('amount', 0),
        'recipientName':    d.get('recipientName', ''),
        'donorIsRecipient': d.get('donorIsRecipient', False),
        'isRegFee':         d.get('isRegFee', False),
        'createdDateUTC':   d.get('createdDateUTC', now),
    }
    for d in raw_donations
]
donations.sort(key=_donation_sort_key, reverse=True)

participants = [
    {
        'displayName':    p.get('displayName', ''),
        'createdDateUTC': p.get('createdDateUTC', now),
    }
    for p in raw_parts
]

feed = {
    'updatedAt':    now,
    'donations':    donations,
    'participants': participants,
}
with open('assets/data/activity-feed.json', 'w') as f:
    json.dump(feed, f, indent=2)
print('activity-feed.json written')

# participants.json (avatars for member cards)
avatar_data = [
    {
        'participantID':  p.get('participantID'),
        'displayName':    p.get('displayName', ''),
        'avatarImageURL': p.get('avatarImageURL') if p.get('isCustomAvatarImage') else None,
        'sumDonations':   p.get('sumDonations', 0),
        'fundraisingGoal': p.get('fundraisingGoal', 1200),
        'numDonations':   p.get('numDonations', 0),
    }
    for p in raw_parts
]
with open('assets/data/participants.json', 'w') as f:
    json.dump(avatar_data, f, indent=2)
print('participants.json written')

# strava-rides.json (training rides from Strava club API)
strava_rides = []
for a in raw_strava_activities if isinstance(raw_strava_activities, list) else []:
    athlete = a.get('athlete')
    aid_out = None
    if isinstance(athlete, dict):
        aid_out = athlete.get('id')
        athlete_name = ' '.join(
            filter(None, [athlete.get('firstname', ''), athlete.get('lastname', '')])
        ).strip()
    elif isinstance(athlete, (int, float)):
        aid_out = int(athlete)
        athlete_name = ''
    else:
        athlete_name = ''
    if aid_out is None:
        aid_out = a.get('athlete_id')
    strava_rides.append({
        'id': a.get('id'),
        'name': a.get('name', 'Untitled ride'),
        'athleteName': athlete_name or 'Club Rider',
        'athleteId': aid_out,
        'distanceMeters': a.get('distance', 0),
        'movingTimeSec': a.get('moving_time', 0),
        'elevationGainMeters': a.get('total_elevation_gain', 0),
        'sportType': a.get('sport_type', a.get('type', 'Ride')),
        'startDateUTC': a.get('start_date') or a.get('start_date_local') or now,
        'startDateLocal': a.get('start_date_local') or a.get('start_date') or now,
        'activityUrl': 'https://www.strava.com/activities/{}'.format(a.get('id')) if a.get('id') else 'https://www.strava.com/clubs/1302442',
        'clubUrl': 'https://www.strava.com/clubs/1302442',
    })

with open('assets/data/strava-rides.json', 'w') as f:
    json.dump({
        'updatedAt': now,
        'clubId': 1302442,
        'clubUrl': 'https://www.strava.com/clubs/1302442',
        'rides': strava_rides,
    }, f, indent=2)
print('strava-rides.json written')

# strava-members.json (club member directory with profile links)
strava_members = []
for m in raw_strava_members if isinstance(raw_strava_members, list) else []:
    athlete_obj = m.get('athlete') if isinstance(m.get('athlete'), dict) else {}
    first = (m.get('firstname') or athlete_obj.get('firstname') or '').strip()
    last = (m.get('lastname') or athlete_obj.get('lastname') or '').strip()
    full = ' '.join(filter(None, [first, last])).strip()
    athlete_id = m.get('id') or m.get('athlete_id') or athlete_obj.get('id')
    strava_members.append({
        'athleteId': athlete_id,
        'firstName': first,
        'lastName': last,
        'displayName': full if full else 'Club Rider',
        'profileUrl': 'https://www.strava.com/athletes/{}'.format(athlete_id) if athlete_id else None,
        'clubUrl': 'https://www.strava.com/clubs/1302442',
    })

with open('assets/data/strava-members.json', 'w') as f:
    json.dump({
        'updatedAt': now,
        'clubId': 1302442,
        'clubUrl': 'https://www.strava.com/clubs/1302442',
        'members': strava_members,
    }, f, indent=2)
print('strava-members.json written')

# strava-group-events.json (scheduled club rides — GET /clubs/{id}/group_events)
CLUB_NUM = 1302442
CLUB_URL = 'https://www.strava.com/clubs/{}'.format(CLUB_NUM)
group_events_out = []
raw_ge = raw_strava_group_events if isinstance(raw_strava_group_events, list) else []
for e in raw_ge:
    if not isinstance(e, dict):
        continue
    eid = e.get('id')
    if eid is None:
        continue
    org = e.get('organizing_athlete') or {}
    org_name = ' '.join(
        filter(None, [org.get('firstname'), org.get('lastname')])
    ).strip()
    group_events_out.append({
        'id': eid,
        'title': e.get('title') or 'Club ride',
        'description': e.get('description'),
        'activityType': e.get('activity_type'),
        'upcomingOccurrences': e.get('upcoming_occurrences') or [],
        'startDatetime': e.get('start_datetime'),
        'timezone': e.get('zone'),
        'address': e.get('address'),
        'organizerName': org_name or None,
        'eventUrl': '{}/group_events/{}'.format(CLUB_URL, eid),
        'clubUrl': CLUB_URL,
    })


def _first_occurrence_iso(ev):
    occ = ev.get('upcomingOccurrences') or []
    return occ[0] if occ else '9999-12-31T23:59:59Z'


group_events_out.sort(key=_first_occurrence_iso)

with open('assets/data/strava-group-events.json', 'w') as f:
    json.dump({
        'updatedAt': now,
        'clubId': CLUB_NUM,
        'clubUrl': CLUB_URL,
        'events': group_events_out,
    }, f, indent=2)
print('strava-group-events.json written ({} events)'.format(len(group_events_out)))

merge_rider_strava_grit(raw_strava_activities, now)

print('Done: {} donations, {} riders, {} strava rides, {} strava members, {} group events'.format(
    len(donations), len(raw_parts), len(strava_rides), len(strava_members), len(group_events_out)))
