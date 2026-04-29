import json
import sys
from datetime import datetime, timezone

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

with open('/tmp/team.json')         as f: team          = json.load(f)
with open('/tmp/donations.json')    as f: raw_donations  = json.load(f)
with open('/tmp/participants.json') as f: raw_parts      = json.load(f)
try:
    with open('/tmp/strava_activities.json') as f:
        raw_strava_activities = json.load(f)
except FileNotFoundError:
    raw_strava_activities = []

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

# activity-feed.json
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
    athlete = a.get('athlete') or {}
    athlete_name = ' '.join(filter(None, [athlete.get('firstname', ''), athlete.get('lastname', '')])).strip()
    strava_rides.append({
        'id': a.get('id'),
        'name': a.get('name', 'Untitled ride'),
        'athleteName': athlete_name or 'Club Rider',
        'athleteId': athlete.get('id'),
        'distanceMeters': a.get('distance', 0),
        'movingTimeSec': a.get('moving_time', 0),
        'elevationGainMeters': a.get('total_elevation_gain', 0),
        'sportType': a.get('sport_type', a.get('type', 'Ride')),
        'startDateUTC': a.get('start_date', now),
        'startDateLocal': a.get('start_date_local', a.get('start_date', now)),
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

print('Done: {} donations, {} riders, {} strava rides'.format(len(donations), len(raw_parts), len(strava_rides)))
