# Project State

**Site**: www.jagmagh.com  
**Repo**: `D:\www.jagmagh.com\jagmagh.github.io` → GitHub: `jagmagh/jagmagh.github.io`  
**Hosting**: GitHub Pages (custom domain via CNAME)  
**Stack**: Jekyll 3.8.5 · Freelancer Bootstrap Theme · Formspree (contact form)  
**Last session**: 2026-06-07  
**HTTPS status**: DNS correct (CNAME → jagmagh.github.io ✓), certificate being provisioned — click "Enforce HTTPS" in GitHub Settings → Pages once available

---

## Working Tree Status

All changes below are **local only — not yet committed**. Review and commit when ready.

### Modified files
- `Gemfile` — added `gem "webrick"` for Ruby 3.x compatibility
- `_config.yml` — title, description, skills tagline, colours, footer, collections, future: true
- `_includes/about.html` — full rewrite with accurate bio
- `_includes/contact.html` — teal background, star-light divider, btn-outline Send button, text-center
- `_includes/modals.html` — updated to use `site.portfolio`
- `_includes/nav.html` — Blog link added, smooth scroll fix, menu order (About · Skills · Blog · Contact)
- `_includes/portfolio_grid.html` — col-sm-4 layout, skill titles added and centred, site.portfolio
- `_layouts/default.html` — blog_preview include added

### New files
- `_portfolio/project-1.md` — Technology Strategy (moved from _posts, lorem ipsum replaced)
- `_portfolio/project-2.md` — Digital Transformation (moved from _posts, lorem ipsum replaced)
- `_portfolio/project-3.md` — Solving Complex Problems (moved from _posts, lorem ipsum replaced)
- `_includes/blog_preview.html` — home page blog preview (5 recent posts, hidden if none)
- `_layouts/blog_page.html` — layout for /blog listing page
- `_layouts/post.html` — layout for individual blog posts (table styles, list font fix, post-intro callout)
- `blog.html` — /blog listing page
- `_posts/2026-06-07-agentic-ai-the-stack-and-the-harder-question.md` — first blog post

### Deleted files
- `_posts/2019-03-06-project-1.markdown`
- `_posts/2019-03-06-project-2.markdown`
- `_posts/2019-03-06-project-3.markdown`

### Images added
- `img/2026-06-07-image1.jpg` — hero image for blog post (full-width below tagline)
- `img/2026-06-07-image2.jpg` — uploaded but not yet placed in post
- `img/2026-06-07-image3.png` — 2×2 AI risk quadrant diagram (Part 3 of blog post)

---

## Site Structure (current)

```
Home (/)
├── Header — "Jagmag H K" · Enterprise Architecture · Digital Transformation · AI-Augmented Architecture
├── About — bio rewritten from resume + Zuhlke current role
├── Skills — 3 portfolio cards (Technology Strategy, Digital Transformation, Solving Complex Problems)
├── Blog — preview of 5 most recent posts (hidden if no posts)
├── Contact — teal background, Formspree form
└── Footer — Locations Worked · Social (Stack Overflow, LinkedIn) · Credits

/blog — full post listing
/[year]/[month]/[day]/[slug]/ — individual post pages
```

---

## DNS & HTTPS

- `www.jagmagh.com` CNAME → `jagmagh.github.io` ✓ (fixed from `jagmagh.com` this session)
- Apex domain A records → GitHub IPs ✓ (already correct, unchanged)
- SSL certificate: being provisioned by Let's Encrypt — **one remaining action**: click "Enforce HTTPS" in GitHub Settings → Pages once checkbox becomes available

---

## Local Tooling

- **Ruby**: not installed. Download RubyInstaller (Ruby+Devkit 3.2.x x64) from rubyinstaller.org
- **Docker Desktop**: CLI present but Desktop not installed
- **Local preview command** (once Ruby installed):
  ```powershell
  cd D:\www.jagmagh.com\jagmagh.github.io
  bundle install
  bundle exec jekyll serve
  ```
- **GitHub Pages deploy**: push to `master` → auto-builds in ~1-2 min. Hard refresh (Ctrl+Shift+R) after deploy to clear CSS cache.
- **Timezone note**: `future: true` added to `_config.yml` to avoid SGT/UTC date mismatch hiding posts.
