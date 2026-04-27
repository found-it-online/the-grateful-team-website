# Creative Brief — TGT Website v1.0: Public Recruitment Site (v1-03)

| Field | Details |
|-------|---------|
| **Project Name** | The Grateful Team — Website v1.0 |
| **Brand / Client** | The Grateful Team (TGT) |
| **Point of Contact** | Luis Vecchio — luisvecchio91@gmail.com / (616) 366-3725 |
| **Date Created** | 2026-04-24 |
| **Revision** | v1-03 (updated 2026-04-26 — multi-page conversion) |
| **Builder** | Lauren Milligan (pro bono) |
| **Launch Deadline** | **May 5, 2026** |
| **Staging URL** | staging.laurenmilligan.pro/tgt |
| **Production URL** | thegratefulteam.com |

**Status:** [x] Draft | [ ] Approved | [ ] In Progress | [ ] Delivered

> ⚠️ **Brief approval needed from Luis by April 27** to hit the May 5 launch date.

### Changelog from v1-02
1. **Project Type changed** from "single-page" to **multi-page, mobile-first**.
2. Added **top navigation + mobile drawer** so riders can find rider-facing content without scroll-hunting on Home.
3. New page set: **Home, WAM Event Details, Group Rides & Events, Packing List, Gear Recommendations, FAQ, Members.**
4. Existing single-page content (mission, season report, join form, socials, IG embed) **stays on Home** — no copy is lost, just reframed as the home page of a multi-page site.
5. **Find Team Member Resources** CTA now links to the new `/members.html` page rather than the Drive link directly (Drive still lives on that page).
6. Added **Information Architecture** section documenting nav structure.
7. Added **Per-Page Briefs** for each new page with content scope and section outlines.
8. Updated **Deliverables** for shared nav/footer partials and a shared CSS file.
9. Open Items expanded: training ride schedule, social calendar, gear research, FAQ drafts.

---

## Overview

The Grateful Team (TGT) is a Grand Rapids, MI charity cycling team raising funds for children fighting critical illnesses through Make-A-Wish. The team is ~50 riders strong — all ages, all fitness levels — united by bikes, music, community, and an eclectic spirit.

v1.0 is the public face of TGT: a **multi-page** site that replaces the current Linktree. It has two jobs: bring in new riders and give current members a quick path to team resources. The site uses a top navigation with a "The Ride" dropdown so practical rider-facing content (event details, packing list, gear recommendations) lives on dedicated pages instead of buried under a long scroll.

---

## Objective

Convert West Michigan cyclists, charity supporters, and community members into team inquiries. Drive join-form submissions that trigger an automated Klaviyo welcome sequence. Establish TGT's first real web presence with discoverable, shareable URLs for each major content area.

**Success metric:** Join form submissions + Klaviyo subscriber signups from day 1.

---

## Project Type

Website — static, **multi-page**, mobile-first

---

## Target Audience

| Attribute | Details |
|-----------|---------|
| **Who** | West Michigan adults with a passion for cycling, charity, or community |
| **Age range** | 20–65+ |
| **Motivation** | Meaningful athletic challenge, Make-A-Wish mission, fun community |
| **Pain point** | No TGT web presence to learn about or join the team |
| **Goal on site** | Understand TGT → feel the vibe → submit interest to join |

Secondary: Current TGT members who need quick access to the Drive folder, Strava club, and rider resources.

---

## Deliverables

| Asset | Notes |
|-------|-------|
| 7 HTML pages | Home, WAM Event Details, Events, Packing List, Gear, FAQ, Members |
| Shared `nav.html` + `footer.html` partials | Injected via small `nav.js`; one source of truth for nav |
| Shared `assets/css/site.css` | Extracted from existing v1-02 `<style>` block + nav rules |
| Cloudflare Worker | Form submission handler → Klaviyo Subscribe API |
| Behold.so widget | Instagram feed embed (public TGT account, on Home) |
| Klaviyo list/form | Subscribe endpoint for join form |

---

## Information Architecture

### Top Nav (desktop)

```
[TGT logo]    The Ride ▾    FAQ    Members    [Join the Team →]
```

**The Ride** dropdown:
- WAM Event Details
- Group Rides & Events
- Packing List
- Gear Recommendations

Logo links to Home. **Join the Team** is a primary CTA button (orange/gold) — always visible. Active page is marked with `aria-current="page"` and a subtle underline/color shift.

### Mobile Nav

Hamburger top-right opens a full-height drawer:
- Home
- The Ride (expanded inline — no nested dropdown):
  - WAM Event Details
  - Group Rides & Events
  - Packing List
  - Gear Recommendations
- FAQ
- Members
- **Join the Team** (full-width CTA at bottom of drawer)

### Footer (every page)

Three columns on desktop, stacked on mobile:
- **The Ride:** WAM Event, Group Rides, Packing List, Gear
- **Team:** FAQ, Members, Join
- **Find Us:** Instagram, Facebook, Strava, makeawish.org/michigan

Plus copyright line.

---

## Site Map

| # | Page | URL | Status by May 5 | Owner |
|---|------|-----|-----------------|-------|
| 1 | Home | `/` (index.html) | **Full** — already built; add nav/footer | Lauren |
| 2 | WAM Event Details | `/wam-event.html` | **Full** — copywriter research | Copy + Lauren |
| 3 | Group Rides & Events | `/events.html` | **Light** — Zoo de Mack confirmed; training "coming soon" | Copy + Luis |
| 4 | Packing List | `/packing-list.html` | **Full** — content provided | Copy polish + Lauren |
| 5 | Gear Recommendations | `/gear.html` | **Full** — single curated page | Copywriter |
| 6 | FAQ | `/faq.html` | **Full** — copywriter drafts from starter Qs | Copywriter |
| 7 | Members | `/members.html` | **Light** — Drive + Strava + member blurb | Lauren + Luis |

No dedicated "About" page — mission, fundraising, season report, and team identity stay on Home.

---

## Per-Page Briefs

### 1. Home (`index.html`)

Existing v1-02 sections stay (in this order):

1. **Hero** — full-width team photo (`assets/images/team-photo-cover-image.jpg`), headline, primary CTA "Join the Team" → anchors to in-page join form, secondary CTA "Find Team Member Resources" → links to `/members.html`.
2. **Mission + Fundraising** — TGT mission, 2026 fundraising goal, Make-A-Wish impact framing.
3. **Stuff We're Proud Of (Season Report)** — light Strava-flavored 2×2 tile grid, awards as the hero, all-time totals strip above. (See v1-02 brief for full design direction — unchanged.)
4. **Join the Team** — playful section header, form (First/Last/Email) → Cloudflare Worker → Klaviyo. Form-on-purple contrast rule still applies.
5. **Group Rides & Training Events** — short module summarizing Zoo de Mack 2026 with a "See full event calendar →" link to `/events.html`. (The full calendar lives on the Events page; Home keeps a teaser.)
6. **Find Us On the Socials** — icon row: Instagram, Facebook, Strava, others Luis confirms.
7. **Instagram Feed (Follow Along)** — Behold.so embed.
8. **Footer** (shared partial).

The shared top nav sits **above** the hero on every page. Section anchors continue to work for in-page jumping (e.g., `#join`).

### 2. WAM Event Details (`wam-event.html`)

Hero: "What is the Wish-A-Mile?" with event imagery.

Sections:
- **The Event** — what WAM is, why it exists (Make-A-Wish Michigan's signature fundraiser).
- **Dates** — 2026 ride dates (copywriter to confirm against makeawish.org/michigan/wam).
- **Location & Start/Finish** — current route (copywriter to verify).
- **The Route** — total miles, daily mileage breakdown, terrain notes.
- **What to Expect** — overnight stops, support vehicles, rest stops, meals.
- **Fundraising Commitment** — minimum, how funds flow to Make-A-Wish.
- **Official Info** — large CTA → makeawish.org/michigan (or confirmed deep link).
- Cross-link tiles → Packing List, Gear, FAQ.

### 3. Group Rides & Events (`events.html`)

Sections:
- **Zoo de Mack 2026** — May 16, Mackinaw City, ~51-mile ride.
- **Weekly Training Rides** — placeholder block; populated when Luis sends day/time/meet point/pace groups.
- **Social Events** — placeholder for kickoff, post-ride party, fundraisers.
- **Strava Club** — link to follow.
- "Have a ride to add? Email us." footer block.

### 4. Packing List (`packing-list.html`)

Hero + intro: "Packing for WAM is part-art, part-science. Here's what veteran riders bring."

Two main blocks (split into Definitely Needed / Luxuries within each):

**Non-Bike Stuff**

*Definitely needed:*
- Sleeping setup (most riders use air mattresses or camping pads, indoor or in tents)
- Toiletries + towel
- Change of clothes for after the ride
- Sandals or flip flops
- Ibuprofen (or drug of choice)
- Device chargers

*Luxuries:*
- Massage gun

**Bike Stuff**

*Definitely needed:*
- Bike
- Headlamp + tail light
- Helmet
- Gloves
- Shoes
- Bibs or shorts (bring 2 pair)
- Extra tubes or sealant
- Water bottles

*Luxuries:*
- Bluetooth speaker
- Portable tire pump or CO2
- Bike multi-tool
- Bike computer (speed, mileage, route info)

Visual: two-column "Definitely needed" / "Luxuries" tiles per block, checkbox-style icons. Cross-link → Gear Recommendations.

### 5. Gear Recommendations (`gear.html`)

Single curated page, no individual review URLs in v1. Disclaimer at top: "These are picks from veteran TGT riders. No affiliate links — just stuff that works."

Categories (copywriter researches and drafts 2–3 picks per category):
- Bibs & Shorts
- Helmets
- Shoes & Pedals
- Lights (front + rear)
- Saddles & Comfort
- Hydration & Nutrition
- Tools & Repair (multi-tool, CO2, pump)
- Tech (bike computer, speakers)
- Sleep Setup (pads, tents)

Each item: photo, name + price band ($/$$/$$$), 2–3 sentence blurb, "Buy / Learn more" outbound link.

### 6. FAQ (`faq.html`)

Accordion or simple Q&A list. Copywriter drafts from these starter questions:
- Do I need to be in elite shape?
- What does it cost to join?
- Is there a fundraising minimum?
- I've never done a long ride — can I still join?
- What gear do I need to start?
- How does training work?
- What's the time commitment?
- Can my partner / friend / dog come?
- Where does the money actually go?
- How do I get on the team for 2026?

### 7. Members (`members.html`)

Lightweight gated-feel landing for current riders.
- Hero: "Welcome back, riders."
- Big tile → Google Drive team folder (URL from Luis).
- Big tile → Strava Club (URL from Luis).
- Optional Klaviyo "team-only" email signup if Luis wants a separate list.
- Member-only contact info / leadership group chat link (Luis to confirm).

---

## Brand Guidelines

> **Assets pending:** Logo, brand photography, and confirmed color palette coming from Google Drive (Luis to share with hire@laurenmilligan.pro). All design specs from v1-02 carry over unchanged.

### Design Direction
- **Soul:** Grateful Dead visual culture — warm, joyful, a little wild, never corporate.
- **Palette:** Deep purples, burnt oranges, earthy reds, faded golds, sky blues (TBC against brand assets).
- **Typography:** Bold, expressive headlines (Abril Fatface / slab); body Lato. Already wired in v1-02.
- **Imagery:** Real TGT photography — rides, group moments, finish lines.
- **Iconography:** Roses, lightning bolts, or cycling motifs where they fit.
- **Avoid:** Generic nonprofit look, cold/sterile SaaS design, full-page grid backgrounds, dark-on-dark form fields, purple-on-purple form fields.

### Voice
See `voice-reference-luis-vecchio.md` for full reference.
- Warm, inclusive ("we"), casual but purposeful.
- Enthusiastic without being over-the-top.
- Lean playful — section headers and CTAs sound like a friend inviting you to a ride, not a nonprofit asking for money.

---

## Key Messages

1. **TGT rides for Make-A-Wish kids** — the ride has meaning beyond the miles.
2. **All are welcome** — any age, any fitness level, just show up.
3. **This is your team** — community, music, bikes, fun.

### CTAs
- **Primary:** "Join the Team" (form on Home, button in nav).
- **Secondary:** "Find Team Member Resources" → `/members.html`.
- **Tertiary:** Social follows via "Find Us On the Socials" row + footer.

---

## Architecture

| Layer | Tool | Why |
|-------|------|-----|
| Hosting | Cloudflare Pages (Lauren's account) | Free, fast, already configured |
| Code | HTML / Tailwind CSS / Vanilla JS | No framework needed for static multi-page |
| Shared partials | Vanilla `nav.js` fetches `partials/nav.html` + `partials/footer.html` | One source of truth for nav across 7 pages, no build step |
| Form handler | Cloudflare Worker | Free serverless, secure way to call Klaviyo API |
| Instagram | Behold.so (free plan) | Public embed, Home only |
| Strava | Link to TGT Strava Club | OAuth not worth it for v1.0 |
| Email | Klaviyo Subscribe API | Account + MCP tools already in place |

### File structure

```
website-v1-public/
├── index.html               (renamed from index-v1-02.html, nav/footer extracted)
├── wam-event.html
├── events.html
├── packing-list.html
├── gear.html
├── faq.html
├── members.html
├── partials/
│   ├── nav.html
│   └── footer.html
├── assets/
│   ├── css/site.css         (extracted from index-v1-02 <style> block)
│   ├── js/nav.js            (mobile drawer toggle + partial inject + active-page highlight)
│   └── images/...           (existing)
├── creative-brief-v1-03.md  (this file)
├── creative-brief-v1-02.md  (history)
└── index-v1-02.html         (history snapshot)
```

---

## Inspiration & References

| Reference | What to borrow |
|-----------|---------------|
| Grateful Dead visual identity | Color warmth, texture, joyful personality |
| Real TGT Instagram (@the_grateful_team) | Authentic photography direction |
| Make-A-Wish Michigan (wish.org/michigan) | Mission framing, emotional tone |
| Strava activity feed (light theme) | "Stuff We're Proud Of" tile layout |

---

## Timeline

| Milestone | Target | Status |
|-----------|--------|--------|
| v1-03 brief drafted | 2026-04-26 | ✅ Done |
| **Luis approves v1-03 brief** | **2026-04-27** | ⚠️ Blocking |
| Google Drive assets received | 2026-04-26 | Pending — Luis |
| Copywriter research + drafts (WAM, Gear, FAQ) | 2026-04-28 | Not started |
| Nav + footer partials + shared CSS extract | 2026-04-28 | Not started |
| All 7 pages scaffolded | 2026-04-29 | Not started |
| Content populated (Home, WAM, Packing, Gear, FAQ) | 2026-04-30 | Not started |
| Light pages populated (Events, Members) | 2026-05-01 | Not started |
| Klaviyo flow tested end-to-end | 2026-05-01 | Not started |
| Staging live | 2026-05-02 | Not started |
| Luis staging review | 2026-05-03 | Not started |
| Revisions complete | 2026-05-04 | Not started |
| **DNS cutover + launch** | **2026-05-05** | Not started |

---

## Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Approve v1-03 brief | Luis | Pending — needed Apr 27 |
| 2 | Google Drive folder URL (for Members page) | Luis | Pending |
| 3 | TGT Strava Club URL | Luis | Pending |
| 4 | Full social account list (FB, Strava, IG, others?) | Luis | Pending |
| 5 | DonorDrive team page URL | Luis | Nice-to-have v1.0 |
| 6 | 2026 fundraising goal amount | Luis | Pending — needed for Home copy |
| 7 | Logo + brand assets | Luis | Pending — share via Drive |
| 8 | 2026 WAM dates + route confirmation | Copywriter via wish.org/michigan | New for v1-03 |
| 9 | Training ride schedule (day, time, meet point, pace groups) | Luis | New for v1-03 |
| 10 | Social event calendar (kickoff, post-ride party) | Luis | New for v1-03 |
| 11 | Member-only group chat / Slack link | Luis | New for v1-03 |
| 12 | Gear research — 2–3 picks per category with blurbs + outbound links | Copywriter | New for v1-03 |
| 13 | FAQ drafts — 10 starter Qs answered in TGT voice | Copywriter | New for v1-03 |
| 14 | Instagram confirmed public (@the_grateful_team) | Lauren | Verify before Behold setup |
