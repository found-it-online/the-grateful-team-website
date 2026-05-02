/**
 * Cloudflare Pages Function — GET /api/strava/authorize
 * Starts Strava OAuth. Requires ?k= matching STRAVA_ADMIN_KEY in Pages env.
 * In Strava app settings, set Authorization Callback Domain to your Pages host
 * (e.g. the-grateful-team-website.pages.dev) and add redirect URL:
 *   https://<host>/api/strava/callback
 */
export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const k = url.searchParams.get('k') || '';
  if (!env.STRAVA_ADMIN_KEY || k !== env.STRAVA_ADMIN_KEY) {
    return new Response('Unauthorized — use the admin link with the shared key.', {
      status: 401,
      headers: { 'Content-Type': 'text/plain; charset=utf-8' },
    });
  }
  if (!env.STRAVA_CLIENT_ID) {
    return new Response('STRAVA_CLIENT_ID missing in Pages environment.', {
      status: 500,
      headers: { 'Content-Type': 'text/plain; charset=utf-8' },
    });
  }
  const redirectUri =
    env.STRAVA_REDIRECT_URI || `${url.origin}/api/strava/callback`;
  const params = new URLSearchParams({
    client_id: env.STRAVA_CLIENT_ID,
    redirect_uri: redirectUri,
    response_type: 'code',
    approval_prompt: 'force',
    scope: 'read,activity:read_all',
    state: k,
  });
  return Response.redirect(
    `https://www.strava.com/oauth/authorize?${params.toString()}`,
    302
  );
}
