# Open Questions

Things deferred, unfinished, or worth revisiting. Address these in future sessions.

---

## Role Definition Document (inputs/)

- [ ] **Content refinement**: document is structurally complete; further polish deferred — this is what was in progress at session 3
- [ ] **v2.txt out of sync**: `work/Solution Architect Role Re-Definition v2.txt` no longer matches `build_v2.py` (it predates the session 3 changes). Either update the txt to match, or treat `build_v2.py` as the authoritative source and remove the txt
- [ ] **Intended audience / use**: is this for internal Zuhlke use, client-facing, or personal positioning? Answer affects tone, level of specificity in 5.3/5.4, and whether it should be published (e.g. as a blog post or white paper)
- [x] **Jekyll exclusion**: `inputs/`, `work/`, `outputs/` added to `exclude:` in `_config.yml` — Jekyll will not process or serve these directories
- [x] **Folder structure**: `work/` holds scripts and intermediate files; `outputs/` holds final deliverables; `inputs/` retained but empty

---

## Content — Personal Sections

- [ ] **About section**: further refinement deferred — user said "we can keep tweaking the personal sections further...but lets do that for another time"
- [x] **Profile photo** (`img/profile.png`): confirmed as actual photo — no change needed.
- [ ] **Header tagline**: review whether the three skill descriptors still feel right after seeing the site live for a while.
- [ ] **Portfolio card images**: the three icons (033-strategy.png, 025-design-1.png, 012-idea.png) are generic. Consider replacing with more relevant visuals.

---

## Content — Blog

- [x] **Image 2** (`img/2026-06-07-image2.jpg`): decided not to use — closed.
- [ ] **More blog posts**: first post is live. Continue publishing — the infrastructure is in place.
- [ ] **Blog post excerpt for home preview**: currently set manually in front matter. Establish a habit: always set `excerpt:` in front matter for every new post.

---

## Technical

- [ ] **Local dev environment**: Ruby not installed, Docker Desktop not installed. Install one of these to enable local preview before pushing. RubyInstaller (Ruby+Devkit 3.2.x x64) from rubyinstaller.org is the recommended path.
- [ ] **Contact form (Formspree)**: the form currently posts to `//formspree.io/{{ site.email }}`. Verify this is active and receiving submissions. May need a Formspree account setup at formspree.io.
- [ ] **Floating label focus colour on Contact section**: when a user clicks into a form field, the label turns teal (matching the background — invisible). The CSS rule `floating-label-form-group-with-focus label { color: primary }` needs to be overridden to white for the contact section.
- [ ] **Google/Bing verification**: `_config.yml` has empty `google_verify` and `bing_verify` fields. Fill if SEO verification is needed.
- [x] **Travis CI**: `.travis.yml` deleted — redundant since GitHub Pages auto-builds on every push.

---

## HTTPS

- [x] **Switch site to HTTPS**: complete — HTTPS enforced and working on www.jagmagh.com.

---

## Social & SEO

- [x] **Stack Overflow link**: verified correct and active.
- [x] **LinkedIn link**: verified correct.
- [ ] **Credits modal** (`_includes/creditsModal.html`): not reviewed. Check its content is appropriate.
- [ ] **RSS feed** (`feed.xml`): Jekyll generates this automatically. Consider whether to promote it.
