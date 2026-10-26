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
- The profile role line is emphasized: 18px / weight 600 on desktop, at least
  16px on phones. NVIDIA Research uses dark green `#315e16` and weight 700.
  On phones, place role and affiliation on separate lines and hide the separator;
  do not shrink this text at 320px. Keep the original body / paper typography.
- No FY logo or initials in the header. Keep Fu-En's portrait on the right,
  circular and flush, with no padded white frame or decorative card.
- One **Research Interests** paragraph with concise bold key phrases, no colored
  underlines / marker backgrounds. Use Title Case for section headings. No
  “What I work on” heading or research-theme cards.
- One publication list, **no topic classification or filter buttons**.
- The owner wants robotics work highlighted consistently, including future papers.
  The owner-approved design uses a green outlined-star “Robot Intelligence” badge beside
  the venue for Fast-ThinkAct (`fast-thinkact`), GR00T N1.6 (`gr16`) and ThinkAct
  (`thinkact`). Set `"robotics": true` on future robotics entries to reuse it.
  This marker does not change publication ordering or conference / award badges.
  Apply the same treatment to future robotics entries.
- Links to other pages, author sites, papers, project pages, code, CV/PDFs and
  enlarged figures open a new tab with `target="_blank" rel="noopener noreferrer"`.
  Same-page `#` navigation stays in the current tab; email uses `mailto:` normally.
- Show all currently selected 2024+ papers. For 2023 and earlier, retain only
  `fl` (ICCV 2023, Efficient Model Personalization) and `dgneurips21` (NeurIPS
  2021, Adversarial Teacher-Student). Remove all other older works from the page,
  including the 2022 paper. Current active selection totals 17 papers. Unselected
  entries live in `content/archive/`; original assets remain available.
- Pin ThinkWorld = 1, DreamX = 2, PhysCaP = 3, TT-VidT = 4, Scal3R = 5,
  ReactVAU = 6, per the owner's latest ordering.
  Remaining papers sort newest first, preserving input order within each year.
- ThinkWorld, DreamX and PhysCaP are robotics work and their main-conference
  submissions are under review. Workshop acceptances must be shown as workshops,
  separate from main venues. ThinkWorld: RoboWM and PTA at NeurIPS 2026. PhysCaP:
  Robot Learning Workshop at NeurIPS 2026 and Agentic Robotics at CoRL 2026.
- ThinkWorld and DreamX have `release_hold: true`: titles are plain text and
  `links` must remain empty. Do not publish their project, PDF, arXiv or code URLs,
  including in public content metadata or provenance. Reference URLs are held in
  private local notes outside the repo; the owner will supply release links later.
  All three new entries use the owner-requested “Preprint 2026” badge, with
  workshop acceptances displayed separately.
- The owner approved this three-paper preview and authorized publication.
  ThinkWorld and DreamX's resource release holds remain in force: approval to
  publish the cards does not authorize publishing their held project/paper URLs.
- GR00T N1.6 uses the full official 26.9-second policy rollout as a silent
  800 × 450 MP4, with its matching poster, natural aspect ratio, play/pause
  controls and on-screen caption identifying the source’s 2.5× playback speed.
  Preserve lazy loading, reduced-motion behavior and the original static image.
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

News uses `news_visible_since: "2026-02"`: February 2026 and all newer updates
remain expanded. Only earlier dates go into Earlier news. Preserve this date
boundary rather than a fixed item count, so future news stays visible.

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
