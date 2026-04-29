import json
import sys
from datetime import datetime, timezone

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

with open('/tmp/team.json')         as f: team          = json.load(f)
with open('/tmp/donations.json')    as f: raw_donations  = json.load(f)
with open('/tmp/participants.json') as f: raw_parts      = json.load(f)

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

print('Done: {} donations, {} riders'.format(len(donations), len(raw_parts)))
