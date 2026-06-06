# Open Questions

Things deferred, unfinished, or worth revisiting. Address these in future sessions.

---

## Content — Personal Sections

- [ ] **About section**: further refinement deferred — user said "we can keep tweaking the personal sections further...but lets do that for another time"
- [ ] **Profile photo** (`img/profile.png`): current image is a placeholder. Replace with an up-to-date professional photo.
- [ ] **Header tagline**: review whether the three skill descriptors still feel right after seeing the site live for a while.
- [ ] **Portfolio card images**: the three icons (033-strategy.png, 025-design-1.png, 012-idea.png) are generic. Consider replacing with more relevant visuals.

---

## Content — Blog

- [ ] **Image 2** (`img/2026-06-07-image2.jpg`): uploaded but not placed anywhere in the blog post. Decide where (if anywhere) it should go.
- [ ] **More blog posts**: first post is live. Continue publishing — the infrastructure is in place.
- [ ] **Blog post excerpt for home preview**: currently set manually in front matter. Establish a habit: always set `excerpt:` in front matter for every new post.

---

## Technical

- [ ] **Local dev environment**: Ruby not installed, Docker Desktop not installed. Install one of these to enable local preview before pushing. RubyInstaller (Ruby+Devkit 3.2.x x64) from rubyinstaller.org is the recommended path.
- [ ] **Contact form (Formspree)**: the form currently posts to `//formspree.io/{{ site.email }}`. Verify this is active and receiving submissions. May need a Formspree account setup at formspree.io.
- [ ] **Floating label focus colour on Contact section**: when a user clicks into a form field, the label turns teal (matching the background — invisible). The CSS rule `floating-label-form-group-with-focus label { color: primary }` needs to be overridden to white for the contact section.
- [ ] **Google/Bing verification**: `_config.yml` has empty `google_verify` and `bing_verify` fields. Fill if SEO verification is needed.
- [ ] **Travis CI** (`.travis.yml`): currently only runs `jekyll build`. Now that GitHub Pages auto-builds on push, Travis CI may be redundant. Consider removing or updating.

---

## HTTPS

- [x] **Switch site to HTTPS**: DNS CNAME for `www` corrected from `jagmagh.com` → `jagmagh.github.io`. DNS check now green in GitHub Pages settings. SSL certificate being provisioned by Let's Encrypt — once issued (~15-30 min after 2026-06-07 session), click "Enforce HTTPS" in GitHub Settings → Pages. No further action needed.

---

## Social & SEO

- [ ] **Stack Overflow link**: currently points to `stackoverflow.com/users/372871/jagmag`. Verify this is still the correct/active profile.
- [ ] **LinkedIn link**: `linkedin.com/in/jagmagh/` — verify correct.
- [ ] **Credits modal** (`_includes/creditsModal.html`): not reviewed. Check its content is appropriate.
- [ ] **RSS feed** (`feed.xml`): Jekyll generates this automatically. Consider whether to promote it.
