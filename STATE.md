# Project State

**Site**: www.jagmagh.com  
**Repo**: `D:\www.jagmagh.com\jagmagh.github.io` → GitHub: `jagmagh/jagmagh.github.io`  
**Hosting**: GitHub Pages (custom domain via CNAME)  
**Stack**: Jekyll 3.8.5 · Freelancer Bootstrap Theme · Formspree (contact form)  
**Last session**: 2026-06-07 (session 3–4)  
**HTTPS status**: DNS correct (CNAME → jagmagh.github.io ✓), certificate being provisioned — click "Enforce HTTPS" in GitHub Settings → Pages once available

---

## Working Tree Status

All website changes are **committed and live** on GitHub Pages (pushed to `master`). The `inputs/` directory is intentionally untracked by git.

_(All website file changes committed and pushed — see git log for detail)_

---

## Deliverable: Solution Architect Role Definition (v2)

**Last updated**: 2026-06-07 (session 3)  
**Status**: Generated — content refinement in progress  
**Output file**: `outputs/Solution Architect Role Re-Definition v2.docx`  
**Generator**: `work/build_v2.py` (python-docx — run `python work/build_v2.py` to regenerate)  
**Style template**: `inputs/Solution Architect Role Re-Definition.docx` (original source DOCX — externally authored; styles/numbering inherited)  
**Content source**: `work/Solution Architect Role Re-Definition v2.txt` (note: may be out of sync with build script — see open questions)  
**Note**: `inputs/`, `work/`, `outputs/` are all excluded from Jekyll builds and untracked by git

### Document structure (8 sections)

| # | Title | Notes |
|---|---|---|
| 1 | Purpose | Scopes the document to the architect's role in an AI-native world |
| 2 | Operating Premise | Three shifts: construction, breadth, judgment |
| 3 | What Judgment Is | Defines "judgment" concretely — new section in v2 |
| 4 | How the Role Has Changed | Colour-coded table on landscape page (red/yellow/green) |
| 5 | Where the Architect's Value Has Gravitated | Billable offerings — 5A (independent) and 5B (within implementation) |
| 6 | Supporting Discipline: Building for Knowledge | Internal practice — not billed, keeps judgment credible |
| 7 | The Governing Filter | Governing question: does this compound? |
| 8 | Summary | One-paragraph close |

**Section 5 sub-sections**: 5.1 Pre-Sales Solutioning · 5.2 Decision Guidance · 5.3 Platform/Vendor/Transformation · 5.4 Trusted Technology Advisory · 5.5 Architectural Decisions and Risk Ownership during the Build

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

### Published blog posts

| Date | Slug | Title |
|---|---|---|
| 2026-07-18 | `2026-07-18-agentic-ai-the-stack-and-the-harder-question` | Agentic AI: Model Autonomy, and the Harder Question |
| 2026-07-10 | `2026-07-10-solution-architect-operating-model-ai-native-world` | The Architect's Operating Model in an AI-Native World |

Note: both posts are future-dated relative to time of writing (2026-06-07). `future: true` in `_config.yml` ensures they render locally; GitHub Pages will hold them until the stated date unless `future: true` is also in the live config (it is).

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
