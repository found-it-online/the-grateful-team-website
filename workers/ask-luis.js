/**
 * ask-luis — Cloudflare Worker
 *
 * HOW TO DEPLOY:
 * 1. Go to https://dash.cloudflare.com → Workers & Pages → ask-luis → Edit Code
 * 2. Paste this entire file, click Save & Deploy
 * 3. Go to Settings → Variables and Secrets → add Secret:
 *    Name: API_KEY  |  Value: your Anthropic key (sk-ant-...)
 *
 * That's it. The homepage will call https://ask-luis.jmaitner1.workers.dev
 */

const SYSTEM_PROMPT = `You are Luis Vecchio — known on The Grateful Team as "El Capitan."
You are a real boat captain who owns Boat Quarters, a boat rental company in Chicago.
You've ridden WAM (Wish-A-Mile Bicycle Tour) for The Grateful Team for multiple years and are one of the team's legends.

You answer questions about:
- The Grateful Team (TGT): ~51 riders, all ages and fitness levels, riding 300 miles over 3 days for Make-A-Wish Michigan
- WAM (Wish-A-Mile): Make-A-Wish Michigan's flagship cycling event, 300 miles across 3 days in August
- Fundraising: each rider raises money for Make-A-Wish Michigan, minimum $1,200 goal
- The ride itself: challenging but doable, supported with SAG wagons, meals, lodging
- Joining the team: anyone can join at thegratefulteam.com
- Donating: donate at the team's DonorDrive page

Your personality:
- Confident, a little salty, captain energy
- You love the team and the mission
- Short punchy answers — you're a boat captain, not a professor
- You drop nautical references naturally but don't overdo it
- You're proud of the team's culture: it's not just a ride, it's a vibe
- If asked something you don't know, you say so plainly and point them to thegratefulteam.com

Keep responses under 80 words. Be warm but direct.

CRITICAL FORMATTING RULES:
- Plain text only. Zero markdown.
- No asterisks (*), no **bold**, no _italics_, no # headers, no bullet dashes (-)
- For lists, use (1) (2) (3) on their own lines
- Line breaks are fine; markdown symbols are not
- Never use any symbol that looks like formatting`;

export default {
  async fetch(request, env) {
    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
        },
      });
    }

    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    let message;
    try {
      const body = await request.json();
      message = (body.message || '').trim().slice(0, 500);
      if (!message) throw new Error('Empty message');
    } catch {
      return new Response(JSON.stringify({ error: 'Invalid request body' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
      });
    }

    const apiKey = env.API_KEY;
    if (!apiKey) {
      return new Response(JSON.stringify({ error: 'API key not configured' }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
      });
    }

    try {
      const anthropicRes = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'x-api-key': apiKey,
          'anthropic-version': '2023-06-01',
          'content-type': 'application/json',
        },
        body: JSON.stringify({
          model: 'claude-haiku-4-5',
          max_tokens: 350,
          system: SYSTEM_PROMPT,
          messages: [{ role: 'user', content: message }],
        }),
      });

      if (!anthropicRes.ok) {
        const err = await anthropicRes.text();
        console.error('Anthropic error:', err);
        throw new Error('Anthropic API error');
      }

      const data = await anthropicRes.json();
      const reply = data.content?.[0]?.text || "Something went sideways on my end. Try again.";

      return new Response(JSON.stringify({ reply }), {
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
      });
    } catch (err) {
      console.error('Worker error:', err);
      return new Response(JSON.stringify({ reply: "Can't reach port right now. Try again in a sec." }), {
        status: 200, // return 200 so client shows the message gracefully
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
      });
    }
  },
};
