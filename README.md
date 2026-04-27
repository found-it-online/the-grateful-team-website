# The Grateful Team — Website v1.0

Public recruitment site for The Grateful Team (TGT), a Grand Rapids charity cycling team raising funds for Make-A-Wish Michigan.

**Production:** thegratefulteam.com (DNS cutover at launch)
**Staging:** *.pages.dev URL from Cloudflare Pages
**Builder:** Lauren Milligan (pro bono)
**Brief:** [creative-brief-v1-03.md](creative-brief-v1-03.md)

## Stack

- Static HTML, no framework
- Tailwind-flavored hand-rolled CSS in `assets/css/site.css`
- Shared `nav.html` / `footer.html` partials injected via `assets/js/nav.js`
- Cloudflare Pages hosting + (forthcoming) Worker for join-form → Klaviyo

## Local development

```sh
python3 -m http.server 8765
# open http://localhost:8765
```

## Pages

- `/` — Home (hero, mission, season report, join form, socials, IG)
- `/wam-event.html` — WAM Event Details
- `/events.html` — Group Rides &amp; Events
- `/packing-list.html` — Packing List
- `/gear.html` — Gear Recommendations
- `/faq.html` — FAQ
- `/members.html` — Member Resources

## File structure

```
.
├── index.html               # Home
├── *.html                   # Sub-pages
├── partials/                # Shared nav + footer (injected by nav.js)
├── assets/
│   ├── css/site.css         # All styles
│   ├── js/nav.js            # Partial injection, drawer, dropdown, active-page
│   ├── images/              # Hero photo
│   └── logos/               # TGT logo
├── creative-brief-v1-03.md  # Active brief
├── creative-brief-v1-02.md  # History
├── index-v1-00.html         # History
└── index-v1-02.html         # History
```
