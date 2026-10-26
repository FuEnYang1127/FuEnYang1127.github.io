# Working on Fu-En Yang's homepage

The owner updates this site through assistants and does not plan to read source.
Preserve a straightforward, lightweight workflow. Preview every revision before
pushing; wait for the owner's approval of that preview before publication.

## Current visual and content preferences

- Clean white background, dark readable text, stronger / larger typography and
  bright green accents. Publication presentation must follow sifeiliu.net: distinct
  rounded paper cards with small, balanced left-side figures and paper details on
  the right. Do not replace them with a flat list. The rest of the page stays white.
- Light version only. No theme toggle, system-driven dark style or stored theme
  preference logic. The owner explicitly removed Dark mode.
- The owner requested the original NVIDIA favicon again. Use the existing
  `images/nvidia.png`, with the correct PNG MIME type and a content-hashed URL.
  Do not replace it with another custom robot or agent icon.
- The visible footer credit is only “Original homepage based on Jon Barron’s
  template.” Link to https://github.com/jonbarron/website. Do not add the Sifei Liu
  design-inspiration credit back.
- CV uses the same neutral button treatment as the other profile links.
- No FY logo or initials in the header. Keep Fu-En's portrait on the right,
  circular and flush, with no padded white frame or decorative card.
- One **Research Interests** paragraph with concise bold key phrases, no colored
  underlines / marker backgrounds. Use Title Case for section headings. No
  “What I work on” heading or research-theme cards.
- One publication list, **no topic classification or filter buttons**.
- Links to other pages, author sites, papers, project pages, code, CV/PDFs and
  enlarged figures open a new tab with `target="_blank" rel="noopener noreferrer"`.
  Same-page `#` navigation stays in the current tab; email uses `mailto:` normally.
- Show all currently selected 2024+ papers. For 2023 and earlier, retain only
  `fl` (ICCV 2023, Efficient Model Personalization) and `dgneurips21` (NeurIPS
  2021, Adversarial Teacher-Student). Remove all other older works from the page,
  including the 2022 paper. Current active selection totals 14 papers. Unselected
  entries live in `content/archive/`; original assets remain available.
- TT-VidT is first (`featured_order: 1`), Scal3R second (`featured_order: 2`),
  and ReactVAU third (`featured_order: 3`), per the owner’s latest ordering.
  Remaining papers sort newest first, preserving input order within each year.
- Fast-ThinkAct uses the official efficiency teaser showing “9.3× faster”,
  with no comparison video. ThinkAct uses the official representative conceptual
  teaser about reinforced reasoning, adaptation, planning and self-correction.
- Scientific figures retain their full content and natural aspect ratio. Cap desktop thumbnails at 350px wide and 220px high, with natural image
  proportions. No fixed-height blank frames, cropping, stretching or fictional
  research imagery.
- The owner supplied their MapMyVisitors embed code for `web/1c93a`, associated
  with `https://fuenyang1127.github.io/`. Use the supplied image widget and preserve
  its tracking key in `content/site.json`. It loads eagerly to register page
  visits, at its natural 180 × 114 dimensions. The image and statistics link open
  the same dashboard in a new tab. Show no visible Visitors heading above the
  map; retain an accessible section label. Do not restore unavailable ClustrMaps URLs or
  use another site's widget. Never fabricate visitor counts or locations.

The Research Interests paragraph (not the opening biography) must begin: “My research focuses on generalizable
and agentic robot intelligence.” Explicitly emphasize world modeling, physical
dynamics and imagined futures, along with world–action modeling and agentic
robotics in the following text, with three concise bold highlights and no marker
background. The opening biography should give a substantive summary of predictive models,
embodied reasoning and robot learning without repeating the same paragraph.
Do not change the focus back to generic physical AI wording.

News: the X-REASON invited talk (September 8, 2026) must be the second update,
following the existing September 2026 paper news. Its title, provided by the owner,
is “Thinking through Word to World: Embodied Reasoning from Imagination”. Use past
tense (“I gave an invited talk”), and link to https://xreason-workshop.github.io/.
The NVIDIA Research internship mention links to https://research.nvidia.com/labs/twn/.

## Source files and build

- Content: `content/site.json`, `publications.json`, `news.json`, `background.json`.
- Layout: `templates/page.html`; styles: `assets/site.css`; optional video behavior:
  `assets/site.js`. `index.html` is generated; do not hand-edit it.
- Build: `python3 scripts/build.py`; validate: `python3 scripts/build.py --check`.
- Preview: `python3 scripts/preview.py` (localhost:4173).
- Keep plain HTML/CSS/JS and a standard-library Python build. No framework or
  package-manager migration unless the owner asks.
- Typography must match sifeiliu.net, replacing the rejected NVIDIA/Inter stack:
  self-hosted Noto Sans 400–700 for body / paper text, Google Sans 700 for main
  headings. Body, authors and summaries: 16px / 24px; hero copy: 16.32px / 24.48px;
  paper titles: 20.48px / 23.04px, weight 600; section headings: 32px / 36px;
  metadata: 13.12px, weight 700; paper links: 12px, weight 600. No negative tracking.
  Both font families have their bundled SIL OFL licenses in assets/fonts/.

## Safe updates

Preserve exact titles, author order, coauthor links, equal-contribution markers,
conference names, years and awards. New content must be grounded in the paper or
its official project page; do not infer publication acceptance from an arXiv date.
Media provenance is recorded beside each publication. Keep original images and
PDF files. Follow explicit paper ordering and the older-paper selection above when adding work.

Run the builder / check and review desktop and phone rendering. Check overflow,
all local images and links, the news archive, featured ordering, video play/pause,
reduced motion, and no-JavaScript content. Test the visitor image failure state:
when the map provider is unavailable, hide the whole visitor section, including
its dashboard link. Disabled analytics must render no external tracking requests.
Use a local branch; do not overwrite other changes. Do not push, merge or publish
until the owner has reviewed and approved the current preview.
