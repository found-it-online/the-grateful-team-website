/**
 * Sends new Google Form submissions to GitHub repository_dispatch → merges into assets/data/rider-intake.json
 *
 * SETUP (one-time)
 * 1. Repo → Settings → Secrets → Actions → add RIDER_INTAKE_WEBHOOK_SECRET (generate a random long string).
 *    Use the SAME value below in script property RIDER_WEBHOOK_SECRET.
 * 2. GitHub user → Developer settings → Fine-grained PAT (or classic) with repo write on found-it-online/the-grateful-team-website.
 *    Script property GITHUB_PAT.
 * 3. Script Editor → Project Settings → Script properties:
 *      GITHUB_OWNER    = found-it-online
 *      GITHUB_REPO     = the-grateful-team-website
 *      GITHUB_PAT      = …
 *      RIDER_WEBHOOK_SECRET = (same as GitHub RIDER_INTAKE_WEBHOOK_SECRET)
 * 4. Triggers → Add Trigger → From spreadsheet “On form submit” → Function onFormSubmit
 *
 * IMPORTANT: Question titles below must match your live form wording (titles only, asterisks stripped).
 */

const FORM_TITLE_KEYS = {
  'Full Name (as it appears on DonorDrive)': 'name',
  'DonorDrive Participant Slug or URL': 'donorSlug',
  'Nickname (for the front of your trading card)': 'nickname',
  'How many WAM seasons have you completed (including this one)?': 'years',
  'Your Initials': 'initials',
  'Favorite Grateful Dead song (or lyric line)': 'song',
  'Your Rider Bio': 'bio',
  'Fun Fact ⚡': 'funFact',
  'Which of these badges apply to you? (check all that fit)': 'badgesCheckbox',
  'Any other badge ideas or notes for your card?': 'badgeNotes',
  'Have you uploaded a profile photo to your DonorDrive page?': 'photoUploaded',
  'Anything you want us to know or include on your card?': 'notes',
};

function onFormSubmit(e) {
  const props = PropertiesService.getScriptProperties();
  const pat = props.getProperty('GITHUB_PAT');
  const owner = props.getProperty('GITHUB_OWNER') || 'found-it-online';
  const repo = props.getProperty('GITHUB_REPO') || 'the-grateful-team-website';
  const secret = props.getProperty('RIDER_WEBHOOK_SECRET');

  if (!pat || !secret) throw new Error('Set GITHUB_PAT and RIDER_WEBHOOK_SECRET in Script properties');

  const named = {};
  e.response.getItemResponses().forEach(function (ir) {
    let title = ir.getItem().getTitle().replace(/\s*\*$/,'').trim();
    const mapKey = FORM_TITLE_KEYS[title];
    if (!mapKey) return;
    let ans = ir.getResponse();
    if (ans === '') ans = null;
    named[mapKey] = ans;
  });

  let badges = named.badgesCheckbox;
  if (badges && !Array.isArray(badges)) badges = [badges];
  if (!badges) badges = [];

  const extraNotes = [];
  if (named.badgeNotes) extraNotes.push('Badge notes: ' + named.badgeNotes);
  if (named.photoUploaded) extraNotes.push('DonorDrive photo uploaded: ' + named.photoUploaded);
  if (named.notes) extraNotes.push(String(named.notes));

  const bioBase = named.bio ? String(named.bio) : '';
  const bioExtras = extraNotes.length ? '\n\n' + extraNotes.join('\n') : '';

  const clientPayload = {
    secret: secret,
    name: String(named.name || '').trim(),
    donorSlug: String(named.donorSlug || '').trim(),
    nickname: String(named.nickname || '').trim(),
    years: named.years != null ? String(named.years).trim() : '1',
    initials: String(named.initials || '').trim(),
    song: String(named.song || '').trim(),
    bio: bioBase + bioExtras,
    funFact: named.funFact ? String(named.funFact).trim() : '',
    badges: badges,
  };

  const url = 'https://api.github.com/repos/' + owner + '/' + repo + '/dispatches';
  const body = {
    event_type: 'rider-card-intake',
    client_payload: clientPayload,
  };

  const res = UrlFetchApp.fetch(url, {
    method: 'post',
    contentType: 'application/json',
    muteHttpExceptions: true,
    headers: {
      Authorization: 'Bearer ' + pat,
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
    },
    payload: JSON.stringify(body),
  });

  const code = res.getResponseCode();
  if (code < 200 || code >= 300) {
    throw new Error('GitHub dispatch failed: HTTP ' + code + ' — ' + res.getContentText().slice(0, 500));
  }
}
