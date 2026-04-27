# Creative Brief — TGT Website v1.0: Public Recruitment Site (v1-02)

| Field | Details |
|-------|---------|
| **Project Name** | The Grateful Team — Website v1.0 |
| **Brand / Client** | The Grateful Team (TGT) |
| **Point of Contact** | Luis Vecchio — luisvecchio91@gmail.com / (616) 366-3725 |
| **Date Created** | 2026-04-24 |
| **Revision** | v1-02 (updated 2026-04-26 from Lauren's review) |
| **Builder** | Lauren Milligan (pro bono) |
| **Launch Deadline** | **May 5, 2026** |
| **Staging URL** | staging.laurenmilligan.pro/tgt |
| **Production URL** | thegratefulteam.com |

**Status:** [x] Draft | [ ] Approved | [ ] In Progress | [ ] Delivered

> ⚠️ **Brief approval needed from Luis by April 25** to hit the May 5 launch date.

### Changelog from v1
1. Hero now uses the real team photo (`team-photo-cover-image.jpg`) as a full-width cover image.
2. Hero CTAs simplified to **Join the Team** + **Find Team Member Resources**.
3. "Awards & Milestones" → renamed **"Stuff We're Proud Of"** with a lighter, more playful Strava-style treatment (light tiles, removed year-over-year comparison box, more visual weight on awards).
4. Group Rides & Training Events section moved to sit **below** the Join the Team section.
5. Join section copy reworked to a more playful tone (e.g. "Ready to grant some wishes? Join the team!").
6. Form styling rule added: never use purple form fields on a purple section background — fields must contrast with their section.
7. New **"Find Us On the Socials"** section added directly above the Instagram feed — Facebook, Strava, Instagram, and any other active accounts.

---

## Overview

The Grateful Team (TGT) is a Grand Rapids, MI charity cycling team raising funds for children fighting critical illnesses through Make-A-Wish. The team is ~50 riders strong — all ages, all fitness levels — united by bikes, music, community, and an eclectic spirit.

v1.0 is the public face of TGT: a single-page site that replaces the current Linktree. It has two jobs: bring in new riders, and give current members a quick path to team resources.

---

## Objective

Convert West Michigan cyclists, charity supporters, and community members into team inquiries. Drive join-form submissions that trigger an automated Klaviyo welcome sequence. Establish TGT's first real web presence.

**Success metric:** Join form submissions + Klaviyo subscriber signups from day 1.

---

## Project Type

Website — static, single-page, mobile-first

---

## Target Audience

| Attribute | Details |
|-----------|---------|
| **Who** | West Michigan adults with a passion for cycling, charity, or community |
| **Age range** | 20–65+ |
| **Motivation** | Meaningful athletic challenge, Make-A-Wish mission, fun community |
| **Pain point** | No TGT web presence to learn about or join the team |
| **Goal on site** | Understand TGT → feel the vibe → submit interest to join |

Secondary: Current TGT members who need the Google Drive resource link.

---

## Deliverables

| Asset | Notes |
|-------|-------|
| Single HTML page | All sections below, mobile-first, Tailwind CSS |
| Cloudflare Worker | Form submission handler → Klaviyo Subscribe API |
| Behold.so widget | Instagram feed embed (public TGT account) |
| Klaviyo list/form | Subscribe endpoint for join form |

---

## Site Sections

### 1. Hero
- **Hero image:** Full-width team photo — `assets/images/team-photo-cover-image.jpg` (the post-ride group shot with "We Ride for Kai" / "We Ride for Jeremiah" banners). Treat as a true cover image — let it breathe at the top of the page.
- Bold headline overlaying or sitting just below the photo, capturing TGT's spirit (cycling + Make-A-Wish + community).
- **Primary CTA:** "Join the Team" → anchors to the join form
- **Secondary CTA:** "Find Team Member Resources" → anchors to (or links out to) the team Google Drive
- On mobile, headline + CTAs stack cleanly below the image; image should not be cropped so tightly that faces are lost.

### 2. Mission + Fundraising
- TGT mission statement (draft: "TGT raises funds for children fighting critical illnesses through Make-A-Wish. We're an eclectic community of riders — all ages, all backgrounds — united by bikes, music, and a shared love of doing something meaningful.")
- 2026 fundraising goal (confirm with Luis)
- Make-A-Wish impact framing

### 3. Stuff We're Proud Of (Season Report)

| Year | Riders | Goal | Raised | Awards |
|------|--------|------|--------|--------|
| 2023 | 12 | $35,000 | $34,648 | — |
| 2024 | 42 | $100,000 | $115,026.82 | Top Fundraising Team (Large), Spirit of the WAM |
| 2025 | 41 | $115,000 | $115,611.84 | Top Fundraising Team (Large) |
| 2026 | 49 | $115,000 | In progress | — |

**Section header:** "Stuff We're Proud Of" — friendly and human, not "Awards & Milestones."

**Design direction — light, playful, Strava-flavored:**
- **Tiles are light** (cream/off-white/soft gold), not dark. Think Strava's activity feed on a sunny day, not a corporate dashboard.
- 2×2 grid of season cards (one per year). Each card shows:
  - Season year as the header
  - Total funds raised as the hero stat
  - Horizontal progress bar (raised vs. goal) with % label
  - Rider count
  - Award badges styled like Strava trophies — given **more visual weight than the stats** (bigger, more colorful, prominently placed). Awards are the hero of this section.
- **Removed:** the year-over-year delta / comparison box from v1. No "+$80K from 2023" comparisons. Each season stands on its own.
- Years that beat the goal still get a "New Record!" banner — keep it but in a fun sticker style, not a banner ad.
- 2026 card shows in-progress state with an animated pulsing bar and current rider count.
- All-time totals strip above the cards (total raised, total top-team awards, current rider count) — light tile style, also playful.
- Tone: cycling stats *high-five*, not cycling stats *audit*.

### 4. Join the Team
- **Section header copy:** Playful, not solemn. e.g. "Ready to grant some wishes? Join the team." (Replaces v1's "ready for something real" line.)
- 2–3 sentences on what membership looks like — keep it warm and casual.
- Form fields: First name, Last name, Email
- Submit → Cloudflare Worker → Klaviyo subscribe → confirmation message shown inline
- No page reload
- **Form styling rule:** If the section background is purple (or any dark brand color), the form fields must use a **lighter** fill (cream, white, soft neutral) so input boxes are clearly readable. Never put purple-on-purple form fields. Same logic applies to any other dark section bg.

### 5. Group Rides & Training Events
- Zoo de Mack 2026 — May 16, Mackinaw City, ~51-mile ride
- **Position:** Sits **below** the Join the Team section. (Moved from v1, where it lived above Join. The pitch comes first; the calendar comes after.)

### 6. Current Team Members — Access Your Resources
- Brief line: "Already riding with us? Everything you need is in the team Drive."
- CTA button: "Open Team Resources" → Google Drive folder link (URL needed from Luis)

### 7. Find Us On the Socials
- **New section** sitting directly above the Instagram feed embed.
- Section header: "Find Us On the Socials"
- Big, friendly icon row linking to every active TGT account:
  - Instagram (@the_grateful_team)
  - Facebook
  - Strava Club
  - Any others Luis confirms (TikTok, YouTube, etc.)
- Each icon links out in a new tab; icons styled in brand colors (no generic gray social row).

### 8. Instagram Feed
- Behold.so embed showing latest @the_grateful_team posts
- Section header: "Follow Along"

### 9. Footer
- Repeat key links (Drive resources, Strava, Instagram, Facebook)
- Copyright

---

## Brand Guidelines

> **Assets pending:** Logo, brand photography, and confirmed color palette coming from Google Drive (Luis to share with hire@laurenmilligan.pro). Design specs will be finalized once assets are received. Development and copy can proceed in parallel.

### Design Direction
- **Soul:** Grateful Dead visual culture — warm, joyful, a little wild, never corporate
- **Palette:** Deep purples, burnt oranges, earthy reds, faded golds, sky blues (to be confirmed against brand assets)
- **Typography:** Bold, expressive headlines — slab-serif or hand-drawn character; body text clean and readable
- **Imagery:** Real TGT photography — rides, group moments, finish lines. Authentic over stock.
- **Iconography:** Roses, lightning bolts, or cycling motifs (if they fit the brand)
- **Avoid:** Generic nonprofit look, cold/sterile SaaS design, corporate sans-serif everywhere, full-page grid backgrounds, dark-on-dark form fields

### Voice
See `voice-reference-luis-vecchio.md` for full reference.
- Warm, inclusive ("we"), casual but purposeful
- Enthusiastic without being over-the-top
- Community-first, practical
- **Lean playful** — section headers and CTAs should sound like a friend inviting you to a ride, not a nonprofit asking for money.

---

## Key Messages

1. **TGT rides for Make-A-Wish kids** — the ride has meaning beyond the miles
2. **All are welcome** — any age, any fitness level, just show up
3. **This is your team** — community, music, bikes, fun

### CTAs
- **Primary:** "Join the Team" (form submission)
- **Secondary:** "Find Team Member Resources" (Google Drive, members only)
- **Tertiary:** Social follows via the new "Find Us On the Socials" row (Instagram, Facebook, Strava)

---

## Architecture

| Layer | Tool | Why |
|-------|------|-----|
| Hosting | Cloudflare Pages (Lauren's account) | Free, fast, already configured |
| Code | HTML / Tailwind CSS / Vanilla JS | No framework needed for a static page |
| Form handler | Cloudflare Worker | Free serverless, secure way to call Klaviyo API |
| Instagram | Behold.so (free plan) | Easiest public embed without API approval wait |
| Strava | Link to TGT Strava Club | Embed requires OAuth app — not worth it for v1.0 |
| Email | Klaviyo Subscribe API | Lauren already has account + MCP tools |

---

## Inspiration & References

| Reference | What to borrow |
|-----------|---------------|
| Grateful Dead visual identity | Color warmth, texture, joyful personality |
| Real TGT Instagram (@the_grateful_team) | Authentic photography direction |
| Make-A-Wish Michigan (wish.org/michigan) | Mission framing, emotional tone |
| Strava activity feed (light theme) | "Stuff We're Proud Of" tile layout — light cards, prominent trophies |

---

## Timeline

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Brief sent to Luis | 2026-04-25 | Pending |
| **Luis brief approval** | **2026-04-25** | ⚠️ Blocking |
| Google Drive assets received | 2026-04-26 | Pending — Luis to share |
| Design specs locked | 2026-04-26 | Not started |
| Copy drafted | 2026-04-26 | Not started |
| Dev: repo + Pages setup | 2026-04-26 | Not started |
| Dev: build + integrations | 2026-04-27–29 | Not started |
| Klaviyo flow tested end-to-end | 2026-04-29 | Not started |
| Staging live | 2026-05-01 | Not started |
| Luis staging review | 2026-05-02–03 | Not started |
| Revisions complete | 2026-05-04 | Not started |
| DNS cutover + launch | **2026-05-05** | Not started |

---

## Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Brief approval | Luis | Pending — needed Apr 25 |
| 2 | Google Drive folder URL | Luis | Pending — needed Apr 26 |
| 3 | TGT Strava Club URL | Luis | Pending — needed Apr 26 |
| 4 | Full social account list (FB, Strava, IG, others?) for "Find Us On the Socials" | Luis | Pending — needed Apr 26 |
| 5 | DonorDrive team page URL | Luis | Pending — nice-to-have v1.0 |
| 6 | 2026 fundraising goal amount | Luis | Pending — needed for copy |
| 7 | Logo + brand assets | Luis | Pending — share via Drive |
| 8 | Instagram confirmed public (@the_grateful_team) | Lauren | Verify before Behold setup |
