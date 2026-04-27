# Design Mockup — TGT Website v1.0

**Project:** The Grateful Team — Public Recruitment Site  
**Designer:** Lauren Milligan  
**Status:** Draft — Pending Luis Approval  
**Last updated:** 2026-04-24

---

## Design Philosophy

Grateful Dead concert poster meets charity cycling — warm, joyful, textured, and alive. Every visual decision should feel like it came from the community that built this team: eclectic, earnest, and a little bit wild. Nothing corporate. Nothing cold.

---

## Design Tokens

### Color System

| Token | Hex | Role |
|-------|-----|------|
| `--color-night` | `#1A0E2B` | Hero bg, form section, footer bg |
| `--color-night-mid` | `#2D1550` | Form field bg, mid-dark sections |
| `--color-purple` | `#4A1F6B` | Section accents, award badges, milestones section bg |
| `--color-purple-light` | `#6B3A8E` | Hover states, focus rings |
| `--color-orange` | `#D45F1A` | **Primary CTA** — buttons, active elements |
| `--color-orange-dark` | `#A8480E` | Button hover/active states |
| `--color-red` | `#8B2232` | Section eyebrows, earthy accent, group rides gradient start |
| `--color-gold` | `#C9943A` | **Brand gold** — section labels, numbers, highlights |
| `--color-gold-light` | `#E0B454` | Gold hover states |
| `--color-blue` | `#4A8FAB` | Links, tertiary accents, Instagram handle |
| `--color-cream` | `#F5EDD6` | Light section backgrounds, body text on dark |
| `--color-cream-dark` | `#E8D9B8` | Alternate light bg, card borders |

**Accessibility:** All text/background combinations target minimum 4.5:1 contrast ratio (WCAG AA). Cream `#F5EDD6` on Night `#1A0E2B` = 14.2:1. Orange `#D45F1A` on Night = 4.6:1.

### Typography

**Google Fonts — add to `<head>`:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Josefin+Slab:wght@400;600;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">
```

| Role | Family | Weight | Notes |
|------|--------|--------|-------|
| Headlines | Abril Fatface | 400 (display) | Bold editorial poster energy — GD concert poster feel |
| Subheads / UI labels | Josefin Slab | 600, 700 | Geometric slab, vintage character, legible small |
| Body / buttons / UI | Lato | 400, 700 | Clean, highly readable, widely supported |

**Type Scale (desktop → mobile):**

| Token | Desktop | Mobile | Family |
|-------|---------|--------|--------|
| `--text-hero` | 80px / 5rem | 44px / 2.75rem | Abril Fatface |
| `--text-h1` | 48px / 3rem | 36px / 2.25rem | Abril Fatface |
| `--text-h2` | 32px / 2rem | 26px / 1.625rem | Abril Fatface |
| `--text-display-num` | 64px / 4rem | 48px / 3rem | Abril Fatface |
| `--text-label` | 14px / 0.875rem | 13px / 0.8125rem | Josefin Slab 700, uppercase, ls 0.1em |
| `--text-body` | 18px / 1.125rem | 16px / 1rem | Lato 400, lh 1.65 |
| `--text-body-sm` | 16px / 1rem | 15px / 0.9375rem | Lato 400 |
| `--text-cta` | 18px / 1.125rem | 16px / 1rem | Lato 700, uppercase, ls 0.06em |
| `--text-caption` | 14px / 0.875rem | 13px / 0.8125rem | Lato 400 |

### Spacing

Base unit: **8px**. Section vertical padding: **80px desktop / 48px mobile**. Max content width: **1200px**.

| Token | Value |
|-------|-------|
| `--space-xs` | 8px |
| `--space-sm` | 16px |
| `--space-md` | 24px |
| `--space-lg` | 48px |
| `--space-xl` | 80px |
| `--space-2xl` | 120px |

### Border Radius

| Element | Radius |
|---------|--------|
| Buttons | 4px |
| Cards | 8px |
| Form inputs | 4px |
| Badges/pills | 999px (full) |

---

## Responsive Breakpoints

| Name | Breakpoint | Notes |
|------|-----------|-------|
| Mobile | 375px | Primary design target — all layouts designed mobile-first |
| Tablet | 768px | 2-column layouts activate |
| Desktop | 1280px | Max content width 1200px, centered |

---

## Section Specifications

---

### Section 1: Hero

**Background:** `#1A0E2B` solid  
**Photo treatment (when assets received):** Full-bleed team photo at 25–30% opacity behind a dark overlay gradient `linear-gradient(to bottom, rgba(26,14,43,0.7) 0%, rgba(26,14,43,0.4) 50%, rgba(26,14,43,0.85) 100%)`  
**Fallback (no photo):** Radial gradient `radial-gradient(ellipse at center, #2D1550 0%, #1A0E2B 70%)` — no flat color  
**Height:** `100svh` minimum  
**Layout:** Flex column, centered (horizontal + vertical), max-content-width 800px, padding 0 24px

**Logo:**
- Source: `tgt-logo-1x1.png` (use SVG when available)
- Size: 80px × 80px
- Position: Centered, 48px from top of viewport
- Treatment: `filter: brightness(0) invert(1)` if logo is dark — confirm once assets received

**Headline:**
```
"Ride for Something Real."
```
- Font: Abril Fatface, 80px desktop / 44px mobile
- Color: `#F5EDD6`
- Line-height: 1.05
- Margin-top: 32px from logo
- Max-width: 720px

**Subheadline:**
```
"50 riders. One mission. Zero prerequisites."
```
- Font: Josefin Slab 700, 22px desktop / 18px mobile
- Color: `#C9943A`
- Letter-spacing: 0.02em
- Margin-top: 20px

**Body paragraph:**
```
"The Grateful Team rides for children fighting critical illnesses through 
Make-A-Wish. Cyclists of every age and fitness level — united by bikes, 
music, and doing something that matters."
```
- Font: Lato 400, 18px / 16px mobile
- Color: `#F5EDD6` at 80% opacity (`rgba(245,237,214,0.80)`)
- Line-height: 1.65
- Max-width: 560px
- Margin-top: 24px

**CTA Group:**
- Margin-top: 40px
- Flex row desktop, flex column mobile, gap 16px

| Button | Style |
|--------|-------|
| "Join the Team" (primary) | bg `#D45F1A`, text `#F5EDD6`, Lato 700, 18px, uppercase ls 0.06em, padding 16px 40px, border-radius 4px. Hover: bg `#A8480E` |
| "Ride with us on Strava →" (secondary) | No bg, border 1.5px `#C9943A`, text `#C9943A`. Hover: bg `#C9943A`, text `#1A0E2B` |

**Scroll indicator:**
- Animated chevron-down SVG, `#C9943A`, 24px, position absolute bottom 32px centered
- Animation: subtle bounce `translateY(0px → 8px)` 1.2s ease-in-out infinite

---

### Section 2: Mission + Fundraising

**Background:** `#F5EDD6`  
**Padding:** 80px 0 desktop / 48px 0 mobile  
**Layout:** 2-column (60%/40% split) desktop, stacked mobile

**Left Column — Mission:**

*Eyebrow label:*
- Text: "Our Mission"
- Font: Josefin Slab 700, 14px, uppercase, ls 0.1em
- Color: `#8B2232`
- Margin-bottom: 16px

*Headline:*
```
"We ride for kids who need a miracle."
```
- Font: Abril Fatface, 48px desktop / 36px mobile
- Color: `#1A0E2B`
- Line-height: 1.05
- Max-width: 480px

*Body:*
```
"TGT raises funds for children fighting critical illnesses through 
Make-A-Wish. We're an eclectic community of riders — all ages, all 
backgrounds — united by bikes, music, and a shared love of doing 
something meaningful."
```
- Font: Lato 400, 18px
- Color: `#1A0E2B` at 78%
- Line-height: 1.65
- Margin-top: 24px

*Make-A-Wish attribution:*
- Text: "Proud fundraising team for Make-A-Wish Michigan"
- Font: Josefin Slab 600, 14px, uppercase, ls 0.08em
- Color: `#8B2232` at 80%
- Margin-top: 24px
- Optional: small Make-A-Wish star icon (⭐ or SVG) inline before text

**Right Column — 2026 Goal Card:**

- Background: `#4A1F6B`
- Padding: 48px 40px
- Border-radius: 8px
- Optional subtle texture: very faint cross-hatch pattern at 5% opacity (`background-image: repeating-linear-gradient(...)`)

*Eyebrow:*
- Text: "2026 Fundraising Goal"
- Font: Josefin Slab 700, 14px, uppercase, ls 0.1em
- Color: `#C9943A`

*Goal amount:*
- Text: "$115,000"
- Font: Abril Fatface, 64px desktop / 48px mobile
- Color: `#F5EDD6`
- Margin-top: 12px

*Gold rule:*
- 2px `#C9943A`, width 48px, margin: 20px auto

*Supporting text:*
- Text: "All proceeds benefit Make-A-Wish Michigan"
- Font: Lato 400, 16px
- Color: `#F5EDD6` at 75%
- Text-align: center

---

### Section 3: Awards & Milestones — Season Report

**Background:** `#1A0E2B`  
**Padding:** 80px 0 desktop / 56px 0 mobile

**Section Header:**

*Eyebrow:*
- Text: "By the Numbers"
- Font: Josefin Slab 700, 14px, uppercase, ls 0.1em
- Color: `#C9943A`

*Headline:*
```
"Season Report."
```
- Font: Abril Fatface, 48px desktop / 36px mobile
- Color: `#F5EDD6`
- Line-height: 1.05

*Sub-copy:*
```
"We set our sights higher each season — and then we beat them."
```
- Font: Lato 400, 18px
- Color: `#F5EDD6` at 65%
- Margin-top: 16px

---

#### All-Time Totals Strip

A single row of 4 summary stats spanning the full content width above the cards. Styled like a Strava summary banner.

**Container:**
- Background: `#4A1F6B`
- Border-radius: 8px
- Padding: 28px 40px
- Flex row, `justify-content: space-around`, max-width 960px, centered
- Margin: 40px auto 48px
- On mobile: 2×2 grid, padding 24px

**Four stats:**

| Stat | Value | Label |
|------|-------|-------|
| Total Raised | $265,287 | 3 Completed Seasons |
| Current Roster | 49 Riders | 2026 Season |
| Top Team Awards | 2 | WAM Large Team Division |
| Seasons Together | 3 Complete | + 1 In Progress |

*Per stat:*
- Value: Abril Fatface, 36px desktop / 28px mobile, `#F5EDD6`
- Label: Josefin Slab 600, 12px, uppercase, ls 0.08em, `#C9943A`, margin-top 4px

*Separator between stats:* `1px solid rgba(201,148,58,0.25)` vertical rule (hidden on mobile)

---

#### Season Cards Grid

**Container:** 2×2 grid desktop, 1-column mobile, gap 24px, max-width 960px, centered

**Card anatomy:**

```
┌─────────────────────────────────────┐
│ [ACCENT STRIP — 4px top border]     │
│                                     │
│  SEASON 2024  ·  BREAKOUT YEAR      │ ← eyebrow
│                                     │
│  $115,027                           │ ← hero stat
│  RAISED                             │ ← stat label
│                                     │
│  ████████████████████░  115%        │ ← progress bar
│  Goal: $100,000         NEW RECORD  │ ← goal + badge
│                                     │
│  ┌──────────────┐  ┌─────────────┐  │
│  │  42 RIDERS   │  │  +$80K      │  │ ← mini stats
│  │              │  │  FROM 2023  │  │
│  └──────────────┘  └─────────────┘  │
│                                     │
│  🏆 Top Fundraising Team            │ ← award badges
│  ✨ Spirit of the WAM               │
└─────────────────────────────────────┘
```

**Card base style:**
- Background: `#2D1550`
- Border-radius: 8px
- Border: `1px solid rgba(74,31,107,0.6)`
- Padding: 28px
- Box-shadow: `0 4px 24px rgba(0,0,0,0.3)`

**Card top accent strip:** 4px solid border-top, color varies per year (see table below)

**Per-card spec:**

| Field | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|
| Accent color | `#8B2232` | `#4A8FAB` | `#C9943A` | `#D45F1A` |
| Eyebrow | "Season 2023 · Year One" | "Season 2024 · Breakout Year" | "Season 2025 · Back to Back" | "Season 2026 · In Progress" |
| Hero stat | $34,648 | $115,027 | $115,612 | — |
| Goal | $35,000 | $100,000 | $115,000 | $115,000 |
| Progress % | 99% | 115% | 100% | Animated |
| Bar fill | `#8B2232` | `#4A8FAB` | `#C9943A` | `#D45F1A` (pulsing) |
| Riders | 12 | 42 | 41 | 49 |
| YoY delta | "Year One" | "+$80K from 2023" | "+$585 from 2024" | "+8 riders from 2025" |
| Banner | — | "New Record" | "Goal Met" | "Ride in Progress" |
| Awards | — | Top Team + Spirit of WAM | Top Team | — |

**Eyebrow:**
- Font: Josefin Slab 700, 13px, uppercase, ls 0.08em
- Color: card's accent color (e.g. `#4A8FAB` for 2024)
- Margin-bottom: 16px

**Hero stat number:**
- Font: Abril Fatface, 44px desktop / 36px mobile
- Color: `#F5EDD6`
- Line-height: 1.0

**Stat label ("RAISED"):**
- Font: Josefin Slab 700, 12px, uppercase, ls 0.1em
- Color: `#F5EDD6` at 50%
- Margin-top: 4px

**Progress bar:**
- Container: Full width, height 10px, background `rgba(245,237,214,0.10)`, border-radius 999px
- Margin-top: 20px
- Fill: Rounded bar using card's accent color
- Fill width: `min(percentage, 100%)` — bars never overflow the container
- For 2024 (115%): bar is fully filled + a small overflow pill `+15%` in accent color appended to the right of the container
- 2026 bar: 0% fill + CSS `@keyframes pulse` animation on opacity `0.3 → 0.8` over 1.4s ease-in-out infinite; accent color `#D45F1A`; width 20% (suggests motion, not emptiness)

**Goal line below bar:**
- Text: "Goal: $35,000" — Lato 400, 13px, `#F5EDD6` at 45%
- Inline at left
- "New Record" / "Goal Met" / "Ride in Progress" badge at right (see badge spec below)

**Banner badge (top-right of goal line):**

| State | Text | Style |
|-------|------|-------|
| Exceeded goal | "New Record" | bg `#C9943A`, text `#1A0E2B`, Josefin Slab 700, 11px uppercase, pill padding 3px 10px |
| Met goal | "Goal Met" | bg `#4A1F6B`, border 1px `#C9943A`, text `#C9943A`, same font |
| In progress | "Ride in Progress" | no bg, text `#D45F1A` italic, Lato 13px |
| Year one, short | — | no badge |

**Mini stats row:**
- Two side-by-side stat pills, flex row, gap 12px, margin-top 20px
- Each pill: bg `rgba(245,237,214,0.06)`, border `1px solid rgba(245,237,214,0.1)`, border-radius 6px, padding 12px 16px
- Stat value: Abril Fatface, 22px, `#F5EDD6`
- Stat label: Josefin Slab 600, 11px uppercase ls 0.08em, `#F5EDD6` at 45%, margin-top 2px

*Left pill:* Rider count ("42") + label ("Riders")  
*Right pill:* YoY delta ("+$80K") + label ("From 2023") — "Year One" for 2023 card; "+8 Riders" for 2026 card

**Award badges (bottom of card):**
- Separator: `1px solid rgba(245,237,214,0.08)`, margin: 20px 0 16px
- Each badge: flex row, align-items center, gap 8px
- Icon: trophy SVG 16px (`#C9943A`) for Top Team; star SVG 16px (`#C9943A`) for Spirit of WAM
- Text: Lato 400, 14px, `#F5EDD6` at 80%
- Gap between badges: 10px
- No awards? Section hidden entirely (2023 and 2026 cards have no awards row)

**2026 card — special treatment:**
- Hero stat: replaced with "—" in `#F5EDD6` at 30%, Abril Fatface 44px
- Below hero: "Season underway" — Lato italic 15px, `#F5EDD6` at 45%
- Progress bar: pulsing animation (see above)
- YoY pill (right): "+8 Riders" from 2025
- No award badges section
- Subtle "Join us" CTA link at bottom of card: "Want to be in this report? Join the team →" — Lato italic 14px, `#C9943A`, href anchors to `#join`

**Mobile:** Single-column stack, full width cards, all padding reduced to 20px

---

### Section 4: Group Rides & Training Events

**Background:** `linear-gradient(135deg, #8B2232 0%, #D45F1A 100%)`  
**Padding:** 80px 0 desktop / 48px 0 mobile

**Section Header:**

*Eyebrow:*
- Text: "Ride With Us"
- Font: Josefin Slab 700, 14px, uppercase, ls 0.1em
- Color: `#F5EDD6` at 75%

*Headline:*
```
"First group ride: Zoo de Mack."
```
- Font: Abril Fatface, 48px desktop / 36px mobile
- Color: `#F5EDD6`

**Event Card:**
- Background: `#F5EDD6`
- Padding: 40px
- Border-radius: 8px
- Max-width: 640px
- Centered (margin: 40px auto 0)
- Box-shadow: `0 8px 32px rgba(26,14,43,0.25)`

*Date badge:*
- Text: "May 16, 2026"
- Style: Pill, bg `#1A0E2B`, text `#C9943A`, Josefin Slab 700, 13px, uppercase, ls 0.08em
- Padding: 6px 16px

*Event title:*
- Text: "Zoo de Mack 2026"
- Font: Abril Fatface, 32px
- Color: `#1A0E2B`
- Margin-top: 16px

*Event details (icon + text rows):*
```
📍  Mackinaw City → The Highlands, Northern Michigan
🚲  ~51 miles, point-to-point
🎉  Finish line fiesta 2–6 PM · Mackinac Island evening
```
- Icon: 20px line SVG icons in `#8B2232` (or emoji fallback)
- Text: Lato 400, 16px, `#1A0E2B` at 78%
- Gap between rows: 12px
- Margin-top from title: 24px

*Separator:* `1px solid #E8D9B8`, margin 24px 0

*Event description:*
```
"Whether you're a seasoned rider or just getting back on the bike — 
this is how the season starts. Point A to Point B through northern 
Michigan, the whole team alongside you."
```
- Font: Lato 400, 18px
- Color: `#1A0E2B` at 72%
- Line-height: 1.65

*Implied CTA (no button — funnels to join form):*
- Text: "Join the team to ride with us →"
- Font: Lato 400 italic, 16px
- Color: `#4A1F6B`
- Href: `#join` (anchors to Section 5)
- Margin-top: 20px

---

### Section 5: Join the Team

**Background:** `#1A0E2B`  
**Padding:** 96px 0 desktop / 64px 0 mobile  
**Layout:** Centered column, max-width 560px, padding 0 24px

**Section Header:**

*Eyebrow:*
- Text: "Become a Member"
- Font: Josefin Slab 700, 14px, uppercase, ls 0.1em
- Color: `#C9943A`

*Headline:*
```
"Ready to ride for something real?"
```
- Font: Abril Fatface, 48px desktop / 36px mobile
- Color: `#F5EDD6`
- Line-height: 1.05

*Subtext:*
```
"Drop us your info and we'll reach out to get you on the roster. 
All ages, all fitness levels — just show up."
```
- Font: Lato 400, 18px / 16px mobile
- Color: `#F5EDD6` at 72%
- Line-height: 1.65
- Margin-top: 16px

**Form:**
- Margin-top: 40px
- `id="join"` on the section element (CTA anchor target)

*Layout:*
- First Name + Last Name: Side-by-side on desktop (50%/50% with 16px gap), stacked on mobile
- Email: Full width below

*Field style:*
- Background: `#2D1550`
- Border: `1.5px solid #4A1F6B`
- Border-radius: 4px
- Padding: 14px 16px
- Font: Lato 400, 16px, `#F5EDD6`
- Placeholder: `#F5EDD6` at 35%
- Focus state: border `#C9943A`, `box-shadow: 0 0 0 3px rgba(201,148,58,0.18)`
- Transition: border-color 150ms ease, box-shadow 150ms ease

*Label style:*
- Font: Josefin Slab 700, 13px, uppercase, ls 0.08em
- Color: `#C9943A`
- Margin-bottom: 6px

*Submit button:*
- Full width
- Background: `#D45F1A`
- Text: "Join the Team" — Lato 700, 18px, uppercase, ls 0.06em, `#F5EDD6`
- Padding: 18px
- Border-radius: 4px
- Border: none
- Margin-top: 24px
- Hover: bg `#A8480E`, transition 150ms
- Loading state: "Joining..." + spinner (CSS, `#F5EDD6`)
- Disabled (while submitting): opacity 0.7, cursor not-allowed

*Confirmation message (replaces form on success):*
- Animated fade-in
- Checkmark icon: SVG circle ✓, stroke `#C9943A`, 48px
- Headline: "You're in!" — Abril Fatface, 40px, `#F5EDD6`
- Body: "Check your email — we'll be in touch with everything you need to ride with us." — Lato 400, 18px, `#F5EDD6` at 72%

*Error state (inline, below field):*
- Font: Lato 400, 14px, color `#E86B5A` (warm red, not jarring against dark bg)
- Text examples: "First name is required." / "Enter a valid email address."

---

### Section 6: Current Team Members

**Background:** `#F5EDD6`  
**Padding:** 56px 0 desktop / 40px 0 mobile  
**Layout:** Centered column, max-width 480px  
**Intent:** Purposefully understated — members know what they need

*Eyebrow:*
- Text: "Already on the team?"
- Font: Josefin Slab 700, 13px, uppercase, ls 0.1em
- Color: `#8B2232`
- Margin-bottom: 12px

*Text:*
```
"Everything you need is in the team Drive."
```
- Font: Abril Fatface, 32px
- Color: `#1A0E2B`

*CTA Button:*
- Text: "Open Team Resources"
- Prepend: Google Drive icon SVG, 16px, `#1A0E2B`
- Style: Outlined — border 2px `#1A0E2B`, text `#1A0E2B`, bg transparent
- Font: Lato 700, 16px, uppercase, ls 0.06em
- Padding: 14px 32px
- Border-radius: 4px
- Hover: bg `#1A0E2B`, text `#F5EDD6`
- Margin-top: 24px
- Href: Google Drive folder URL (pending from Luis)

---

### Section 7: Instagram Feed

**Background:** `#2D1550`  
**Padding:** 80px 0 desktop / 56px 0 mobile

*Eyebrow:*
- Text: "The Team in Action"
- Font: Josefin Slab 700, 14px, uppercase, ls 0.1em
- Color: `#C9943A`

*Headline:*
```
"Follow Along"
```
- Font: Abril Fatface, 48px desktop / 36px mobile
- Color: `#F5EDD6`

*Handle link:*
- Text: "@the_grateful_team"
- Font: Lato 400, 18px
- Color: `#4A8FAB`
- Href: Instagram profile URL
- Hover: `#5BA8C4`, underline
- Margin-top: 12px

**Behold.so Widget:**
- Max-width: 1200px, centered
- Grid: 3×3 desktop (9 posts), 2×4 tablet, 1×6 mobile
- No caption overlay — photos displayed clean
- Hover: `transform: scale(1.02)`, transition 200ms ease
- Margin-top: 40px

**Follow Button:**
- Text: "Follow on Instagram"
- Prepend: Instagram icon SVG, 18px
- Style: Outlined — border 1.5px `#C9943A`, text `#C9943A`, bg transparent
- Font: Lato 700, 16px, uppercase, ls 0.06em
- Padding: 12px 28px
- Border-radius: 4px
- Hover: bg `#C9943A`, text `#1A0E2B`
- Margin-top: 32px

---

### Section 8: Footer

**Background:** `#0F0820`  
**Padding:** 48px 0  
**Layout:** 3-column desktop (1fr 1fr 1fr), stacked mobile (center-aligned)

*Top separator:* `1px solid rgba(74,31,107,0.4)` (faint purple line), full width, above columns

**Column 1 — Logo & Tagline:**
- Logo: `tgt-logo-1x1.png`, height 48px, `filter: brightness(0) invert(1)` if needed
- Tagline: "Riding for Make-A-Wish since 2023."
- Font: Lato 400, 14px
- Color: `#F5EDD6` at 45%
- Margin-top: 8px

**Column 2 — Social Links:**
*Label:*
- Text: "Find Us"
- Font: Josefin Slab 700, 13px, uppercase, ls 0.1em
- Color: `#C9943A`
- Margin-bottom: 12px

*Links (flex column, gap 10px):*
- Instagram → `@the_grateful_team`
- Facebook → TGT Facebook page (URL pending)
- Strava Club → TGT Strava Club (URL pending)

*Link style:*
- Flex row, align-items center, gap 8px
- Icon: 18px SVG, `#F5EDD6` at 60%
- Text: Lato 400, 14px, `#F5EDD6` at 60%
- Hover: icon + text `#C9943A`

**Column 3 — Copyright:**
- "© 2026 The Grateful Team. All rights reserved."
- Font: Lato 400, 13px, `#F5EDD6` at 35%
- "Built with ♥ by Lauren Milligan"
- Font: Lato 400, 12px, `#F5EDD6` at 25%
- Vertical-align: bottom (align to base of column)

---

## Section Dividers

Between alternating light/dark sections, use a subtle motif to signal the transition. Options:

1. **Thin centered rule** (1px `--color-gold` at 30%, width 80px) with a small inline icon:
   - Between hero → mission: lightning bolt ⚡ SVG
   - Between milestones → group rides: bicycle wheel SVG
   - Between join → members: rose 🌹 SVG (text fallback)
2. **Angled cut:** `clip-path: polygon(0 0, 100% 4%, 100% 100%, 0% 100%)` — subtle 4% angle creates momentum without breaking flow (optional, assess with Luis)

---

## Visual Decorative Elements

**Sourced / approved for v1.0:**
- Lightning bolt SVG (custom draw — simple, 3px stroke, `#C9943A`)
- Rose SVG (simple outline, fills with section color)
- Bicycle wheel icon (line SVG for event section)

**Excluded from v1.0 (save for v2.0+):**
- Full concert poster texture overlays — too heavy without confirmed brand photos
- Skull imagery — not the right tone for a charity/recruiting page
- Tie-dye or swirl background patterns — can clash with readability

---

## Assets Needed Before Dev Build

| Asset | Owner | Format Needed | Deadline |
|-------|-------|--------------|----------|
| TGT logo — SVG preferred | Luis (via Drive) | SVG + PNG transparent | Apr 26 |
| Team photography (hero, group shots, finish lines) | Luis (via Drive) | JPG min 2400px wide | Apr 26 |
| Confirmed brand colors (if different from above) | Luis | Hex codes or Pantone | Apr 26 |
| Trophy + star SVG icons (for award badges in Season Report) | Lauren (draw or source) | SVG | Apr 27 |
| Google Drive folder URL (team resources) | Luis | URL | Apr 26 |
| Strava Club URL | Luis | URL | Apr 26 |
| DonorDrive team page URL | Luis | URL | Apr 26 (nice to have) |
| Instagram account public status confirmed | Lauren | Verify | Apr 25 |

---

## Notes for Developer Handoff

- **Fonts:** Load via Google Fonts `display=swap` for performance
- **Images:** Use `loading="lazy"` on all below-fold images; `loading="eager"` + `fetchpriority="high"` on hero
- **Season Report cards:** Each card's progress bar fill width is a CSS custom property (`--progress: 99%`) set inline — easy to update per card. The 2026 pulsing bar uses `@keyframes pulse` on `opacity` only; width stays fixed at 20% to suggest motion
- **Form:** Vanilla JS `fetch()` to Cloudflare Worker endpoint — no page reload; handle `success`, `error`, and `loading` states in DOM
- **Behold.so:** Use their embed `<div data-behold-id="...">` — test against account before dev to confirm feed is public
- **Accessibility:** All SVG icons need `aria-label` or adjacent visually-hidden text; form inputs need associated `<label>` elements (not just placeholder text)
- **Dark sections:** Test real contrast ratios with axe DevTools before handoff — palette designed to meet AA, verify empirically
