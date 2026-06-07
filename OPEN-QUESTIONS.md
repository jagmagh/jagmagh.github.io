# Open Questions

Things deferred, unfinished, or worth revisiting. Address these in future sessions.

---

## Role Definition Document (inputs/)

- [ ] **Content refinement**: document is structurally complete; further polish deferred — this is what was in progress at session 3
- [x] **v2.txt**: deleted — `build_v2.py` is the authoritative source
- [x] **Intended audience / use**: external / public
- [x] **Jekyll exclusion**: `inputs/`, `work/`, `outputs/` added to `exclude:` in `_config.yml` — Jekyll will not process or serve these directories
- [x] **Folder structure**: `work/` holds scripts and intermediate files; `outputs/` holds final deliverables; `inputs/` retained but empty

---

## Content — Personal Sections

- [ ] **About section**: further refinement deferred — user said "we can keep tweaking the personal sections further...but lets do that for another time"
- [x] **Profile photo** (`img/profile.png`): confirmed as actual photo — no change needed.
- [x] **Header tagline**: "Enterprise Architecture · Digital Transformation · AI-Augmented Architecture" — keeping as-is. Revisit after seeing traffic patterns.
- [x] **Portfolio card images**: keeping generic icons — clean and proportionate at current size. No change needed.

---

## Content — Blog

- [x] **Image 2** (`img/2026-06-07-image2.jpg`): decided not to use — closed.
- [ ] **More blog posts**: first post is live. Continue publishing — the infrastructure is in place.
- [ ] **Blog post excerpt for home preview**: currently set manually in front matter. Establish a habit: always set `excerpt:` in front matter for every new post.

---

## Technical

- [ ] **Local dev environment**: Ruby not installed, Docker Desktop not installed. Install one of these to enable local preview before pushing. RubyInstaller (Ruby+Devkit 3.2.x x64) from rubyinstaller.org is the recommended path.
- [x] **Contact form (Formspree)**: wired up — `js/contact_me_static.js` now POSTs to `https://formspree.io/f/xjgdyrwg` with AJAX. Test after deploying to confirm emails arrive.
- [x] **Floating label focus colour on Contact section**: fixed — `section.success .floating-label-form-group-with-focus label { color: #fff }` overrides the teal-on-teal issue.
- [x] **Google Search Console**: verified and sitemap submitted. Fixed `url:` to `https://www.jagmagh.com` (missing protocol was breaking sitemap URLs) and added `jekyll-sitemap` plugin.
- [x] **Bing Webmaster Tools**: verified and sitemap submitted.
- [x] **Travis CI**: `.travis.yml` deleted — redundant since GitHub Pages auto-builds on every push.

---

## HTTPS

- [x] **Switch site to HTTPS**: complete — HTTPS enforced and working on www.jagmagh.com.

---

## Social & SEO

- [x] **Stack Overflow link**: verified correct and active.
- [x] **LinkedIn link**: verified correct.
- [x] **Credits modal** (`_includes/creditsModal.html`): reviewed — attributions correct. Blog post hero image is Gemini-generated, no attribution needed.
- [ ] **RSS feed** (`feed.xml`): Jekyll generates this automatically. Consider whether to promote it.
