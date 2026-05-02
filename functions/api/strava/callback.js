/**
 * Cloudflare Pages Function — GET /api/strava/callback
 * Exchanges ?code= for tokens. Register this exact URL in the Strava API app
 * as the redirect / callback. Copy refresh_token into GitHub secret STRAVA_REFRESH_TOKEN.
 */
export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const err = url.searchParams.get('error');
  const desc = url.searchParams.get('error_description') || '';
  if (err) {
    return htmlResponse(
      `Strava returned an error: ${escapeHtml(err)} ${escapeHtml(desc)}`,
      400
    );
  }
  const code = url.searchParams.get('code');
  const state = url.searchParams.get('state') || '';
  if (!code || !env.STRAVA_ADMIN_KEY || state !== env.STRAVA_ADMIN_KEY) {
    return htmlResponse('Invalid or missing code/state.', 400);
  }
  if (!env.STRAVA_CLIENT_ID || !env.STRAVA_CLIENT_SECRET) {
    return htmlResponse('Strava client env vars missing on Pages.', 500);
  }

  const body = new URLSearchParams({
    client_id: env.STRAVA_CLIENT_ID,
    client_secret: env.STRAVA_CLIENT_SECRET,
    code,
    grant_type: 'authorization_code',
  });

  const tokRes = await fetch('https://www.strava.com/oauth/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body,
  });
  const raw = await tokRes.text();
  if (!tokRes.ok) {
    return htmlResponse(`Token exchange failed (${tokRes.status}):\n${escapeHtml(raw)}`, 502);
  }

  let data;
  try {
    data = JSON.parse(raw);
  } catch {
    return htmlResponse('Invalid JSON from Strava.', 502);
  }

  const rt = data.refresh_token || '';
  const at = data.access_token || '';
  const athlete = data.athlete || {};
  const who = [athlete.firstname, athlete.lastname].filter(Boolean).join(' ');

  const page = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Strava connected</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 42rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }
    code, pre { background: #f4f4f5; padding: 0.2em 0.4em; border-radius: 4px; word-break: break-all; font-size: 0.85rem; }
    pre { padding: 1rem; overflow-x: auto; }
    .ok { color: #166534; }
  </style>
</head>
<body>
  <h1 class="ok">Strava tokens</h1>
  <p>Authorized as <strong>${escapeHtml(who || 'athlete')}</strong>.</p>
  <p><strong>Next:</strong> In the repo → Settings → Secrets → update <code>STRAVA_REFRESH_TOKEN</code> with the refresh token below (GitHub Actions uses it for club sync).</p>
  <p>If Strava issued a new refresh token, the previous one stops working — update the secret immediately.</p>
  <h2>Refresh token</h2>
  <pre id="rt">${escapeHtml(rt)}</pre>
  <h2>Access token (short-lived; for debugging only)</h2>
  <pre>${escapeHtml(at)}</pre>
</body>
</html>`;

  return new Response(page, {
    status: 200,
    headers: { 'Content-Type': 'text/html; charset=utf-8' },
  });
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function htmlResponse(message, status) {
  const body = `<!DOCTYPE html><html><head><meta charset="utf-8"/><title>Error</title></head><body><pre>${escapeHtml(message)}</pre></body></html>`;
  return new Response(body, {
    status,
    headers: { 'Content-Type': 'text/html; charset=utf-8' },
  });
}
