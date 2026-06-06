# Decisions

Key decisions made and the rationale behind them. Read before making architectural or content changes.

---

## Identity & Branding

| Decision | Rationale |
|---|---|
| Name on site: **Jagmag** (not Husain) | Personal preference — explicit instruction |
| Title: **"Enterprise Architecture · Digital Transformation · AI-Augmented Architecture"** | First two are domains; third changed from "Cloud-Native Platforms" (dated) and from "AI-Augmented Architect" (role, not domain) to "AI-Augmented Architecture" (consistent domain framing) |
| Primary colour: **#2E86AB** (Slate Teal) | Original cornflower blue (#6495ED) was too dark/saturated. Also fixed a bug: original `primary-rgb` value "24,288,156" was invalid (288 > 255), breaking hover overlays on Skills cards. |

---

## Architecture

| Decision | Rationale |
|---|---|
| Portfolio items moved to **`_portfolio/` collection** | `_posts` is Jekyll's native blog collection. Using it for portfolio cards meant any real blog post would appear in the Skills grid. Clean separation: `_portfolio` for skills, `_posts` for blog. |
| Blog at **`/blog`** (separate page) + preview on home page | User wanted a dedicated blog URL AND discoverability on the home page. Home preview shows ≤5 recent posts, hidden entirely if no posts exist. |
| Nav Blog link scrolls to **`#blog` section** (not `/blog`) | Consistent with all other nav items which scroll to home page sections. `/blog` is reached via "View all posts" button in the preview section. |
| `future: true` in `_config.yml` | GitHub Pages builds in UTC; Singapore is UTC+8. Posts dated today would be invisible if built before 8am SGT. Setting future: true avoids silent post suppression. |
| `gem "webrick"` added to Gemfile | Ruby 3.0+ removed webrick from stdlib. Jekyll 3.x uses it as the dev server. Required for local `jekyll serve`. |

---

## Content

| Decision | Rationale |
|---|---|
| About section: references Temus in **past tense** | Jagmag left Temus. Current role: Principal Solutions Architect at Zuhlke Engineering. |
| Current engagement: discovery assessment for a **Singapore authority responsible for improving population fitness** | Client not named by name — use this descriptor. |
| FMEA removed from Solving Complex Problems | Incorrect attribution — user confirmed. |
| LinkedIn post used as **styled intro callout** in blog post | Punchier than the article opening; also used as the post `excerpt` for the blog listing. |
| `post.excerpt` set explicitly in front matter | Jekyll's auto-generated excerpt was causing title duplication on the blog listing page. Explicit front matter excerpt gives full control. |

---

## Infrastructure

| Decision | Rationale |
|---|---|
| `www` DNS CNAME changed from `jagmagh.com` → `jagmagh.github.io` | Original CNAME pointed to apex domain, not GitHub Pages directly. GitHub requires the `www` subdomain to resolve to `jagmagh.github.io` for SSL certificate provisioning via Let's Encrypt. Apex domain A records (185.199.x.x) left unchanged. |
| HTTPS enforced via GitHub Pages | Free SSL from Let's Encrypt. No code changes required — purely a GitHub Settings → Pages configuration. |

---

## Styling

| Decision | Rationale |
|---|---|
| Contact section: `class="success"` (teal bg) | Alternating section backgrounds: Header (teal) → About (white) → Skills (teal) → Blog (white) → Contact (teal). Blog added as a new section required Contact to pick up the colour to maintain the pattern. |
| Contact section: `hr.star-light` not `hr.star-primary` | `star-primary` uses `background-color: #fff` on the star glyph — creates a visible white box on coloured backgrounds. `star-light` uses the primary colour as background, matching correctly. |
| Contact button: `btn-outline` not `btn-success` | `btn-success` (green) blends into teal background. `btn-outline` gives white border/text — same style as hero section CTA. |
| Post layout: `col-lg-10 col-lg-offset-1` | Original `col-lg-8 col-lg-offset-2` left too much whitespace. |
| List item font size: `.post-content ul li, ol li { font-size: 20px }` | Jekyll's kramdown doesn't wrap single/tight list items in `<p>` tags, so they miss the global `p { font-size: 20px }` rule. Generic CSS fix in post layout covers all current and future posts. |
| `.post-intro ul li { font-size: 17px }` — more specific override | `.post-content ul li` (20px) also applies inside `.post-intro`. Intro paragraph text is 17px; this rule brings list items in the callout block into line. |
| Skills icons: `max-width: 160px` on `.portfolio-link` | Default 400px made icons fill the full column and look oversized. 160px is proportionate in the 3-column layout. |
| Favicon: SVG-first with ICO fallback | `favicon.svg` (teal rounded square, white "J") declared first in `head.html`; browsers that don't support SVG favicons fall back to the existing `favicon.ico`. |
