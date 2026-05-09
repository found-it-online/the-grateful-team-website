# WAM Event Page Revisions — Working Brief

**Branch:** `lauren-wam-event-revisions` (off `main`)
**Created:** 2026-05-09
**Source:** [revisions-lm.md](revisions-lm.md)
**Target page:** [wam-event.html](wam-event.html)
**Live preview after deploy:** https://the-grateful-team-website.pages.dev/wam-event.html

---

## The 6 Revisions

### R1 — Hero numerals
**Source quote:**
> Page title. Use numbers 3 and 300 and 1 instead of spelling it out. Align the numbers so they are align left and text sits to the right.
> Example:
>     3   Days
>     300 Miles
>     1   Amazing reason

**Current state:** [wam-event.html:23-25](wam-event.html#L23-L25) — H1 reads "Three days. Three hundred miles.<br>One pretty good reason."

**Owner mix:** Designer (layout) + Copywriter (label words) + Developer (HTML/CSS).

**Decisions resolved:** none locked yet — Designer to spec layout, Copywriter to confirm labels.

---

### R2 — Carpooling copy in Dates section
**Source quote:**
> replace 'we leave from grand rapids' with something that says we'll likely have car pooling options from a few starting points: grand rapids, muskegon area, and others. once we get closer to the event we'll put a plan together.

**Current state:** [wam-event.html:42](wam-event.html#L42) — "The 39th annual ride, Friday through Sunday. Mark it now — we leave Grand Rapids together."

**Owner mix:** Copywriter (primary).

**Decisions resolved:** Mention Grand Rapids and Muskegon area explicitly + "and others" or similar phrasing — final wording is the copywriter's call within Luis's voice.

---

### R3 — Calendar icon for Dates section
**Source quote:**
> Give the dates section a fitting calendar icon

**Current state:** No icon on the Dates section ([wam-event.html:38-44](wam-event.html#L38-L44)).

**Owner mix:** Designer (icon choice/style/placement) + Developer (inline SVG).

**Decisions resolved:** Match existing icon style (outlined, currentColor stroke, ~18-24px) per Instagram SVG at [index.html:738-742](index.html#L738-L742) unless designer flags better choice.

---

### R4 — Strava-style route graphic
**Source quote:**
> add a section graphic that looks like a strava route

**Current state:** [wam-event.html:46-83](wam-event.html#L46-L83) — Location & Route section has the H2, intro paragraph, destinations table, and shorter-day footnote. No graphic.

**Owner mix:** Designer (primary — produces SVG asset) + Developer (placement + responsive sizing).

**Decisions resolved:** "Real route, brand-styled" (per user 2026-05-09 ans).

**⚠ Open dependency:** Real route source material. Checked `assets/data/strava-rides.json` — has 92 activities but ALL have `distance: null`, no Strava IDs, no polylines, no GPX data. Cannot use for route reconstruction. **Designer needs source material from one of:**
- A GPX export from Jackson's (or another rider's) past WAM 300 Strava activity — message Jackson
- The official WAM 300 route map published by Make-A-Wish Michigan ([wish.org/michigan](https://wish.org/michigan/) — search for the 39th annual tour)
- An OpenStreetMap-rendered route from the Marshall→Holland→Kalamazoo→Marshall waypoint sequence

**Designer should pick the easiest path that produces a faithful brand-styled SVG.** Save asset at `assets/images/wam-route-strava.svg`.

---

### R5 — Photo gallery placeholder
**Source quote:**
> Below the table of destinations I want to include a basic photo gallery of a few images from past rides. we can add the photos later when you are ready.

**Current state:** Nothing below the destinations table except the shorter-day footnote at [wam-event.html:79-81](wam-event.html#L79-L81).

**Owner mix:** Designer (layout, placeholder treatment) + Copywriter (section heading + alt-text strategy) + Developer (markup + CSS).

**Decisions resolved:** "Ship with placeholders" (per user 2026-05-09 ans). Tasteful placeholder tiles, not lorem images.

**Open question for designer/copywriter:** column count, aspect ratio, total tile count.

---

### R6 — Parallax "What to Expect" with emoji
**Source quote:**
> I want to have a scrolling parallax with animation that shows the features of the ride with emojis that represent the details. SAG is a support van, Medic is a bandaid, Bike Repair Technicians can show a bicycle, and Police escort.

**Current state:** [wam-event.html:85-97](wam-event.html#L85-L97) — bulleted list with 5 items: SAG/medics/mechanics/police, rest stops, catered meals, overnight stops, finish line.

**Owner mix:** Designer (motion spec) + Copywriter (per-card microcopy) + Developer (IntersectionObserver + CSS transforms).

**Decisions resolved:**
- "Add 1-2 more cards for parity" (per user 2026-05-09 ans). Total card count = 5-6.
- Required: SAG (🚐 or 🚌), Medic (🩹), Bike Repair (🚲), Police escort (🚓)
- Copywriter picks 1-2 more from: Rest Stops, Catered Meals, Overnight Stops, Finish Line.

**Anti-pattern guard:** No animation library. IntersectionObserver + CSS transforms only. Must respect `prefers-reduced-motion: reduce`.

---

## Existing Convention Recon (for the agents)

**CSS section system** ([assets/css/site.css:347-426](assets/css/site.css)):
- `.page-hero` + `.page-hero-inner` for top-of-page hero
- `.section-cream`, `.section-tile`, `.section-night`, `.section-purple` — alternating section backgrounds
- Each gets `.section-eyebrow` + `.section-h2` + `.prose` children

**Typography:**
- H1 hero: Abril Fatface, clamp(2.5rem, 6vw, 4rem), `var(--color-cream)`
- H2 section: see `.section-h2` definition
- Body: DM Sans

**Icon convention:** inline SVG, no font-icon system. Reference: Instagram outline icon at [index.html:738-742](index.html#L738-L742).

**JS convention:** vanilla, no deps, `defer` loaded. Reference: [wam-event.html:129](wam-event.html#L129) — `<script src="/assets/js/nav.js" defer></script>`.

**Currently zero parallax/scroll-reveal infra exists** — R6 introduces the first instance.

**Currently zero photo gallery components exist** — R5 introduces the first instance.

---

## Phase Assignments (which agent runs when)

| Phase | Agent | Deliverable file | Blocks on |
|---|---|---|---|
| 2a | `/designer` | `wam-event-revisions-design-spec.md` + `assets/images/wam-route-strava.svg` | R4 source material |
| 2b | `/copywriter` | `wam-event-revisions-copy.md` | nothing — runs in parallel with 2a |
| 3 | `/dev` | edits to `wam-event.html`, `assets/css/site.css`, new `assets/js/wam-features.js` | 2a + 2b complete |
| 4 | (orchestrator) | PR + merge | 3 complete |

---

## Acceptance Criteria (full feature)

- All 6 revisions live on `/wam-event.html` at the deploy preview URL
- Hero numerals align as specified at desktop AND mobile breakpoints
- Calendar icon inherits `.section-eyebrow` color
- Strava SVG scales responsively, doesn't overflow at 375px width
- Photo gallery placeholders are present and don't read as broken images
- Parallax cards reveal smoothly on scroll in Chrome and Safari
- Reduced-motion preference disables all motion, all content visible immediately
- Zero new hex colors in HTML — all colors via `var(--color-*)`
- Zero `<style>` blocks added to HTML
- Zero animation library imports
- Zero browser console errors

---

## Notes

- IG feed work tracked separately at [project_tgt_instagram_feed.md](../../../.claude/projects/-Users-laurenmilligan--code/memory/project_tgt_instagram_feed.md) — not affected by this branch.
- `static.yml` workflow is dead code (only triggers on `jackson` branch); Cloudflare Pages does the actual deploy on any push to `main`. Fixing/deleting `static.yml` is out of scope for this PR.
- Apex domain `thegratefulteam.com` still 301-redirects to Linktree. Pages preview lives only on `the-grateful-team-website.pages.dev`. Out of scope for this PR.
