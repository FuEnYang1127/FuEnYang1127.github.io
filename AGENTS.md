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
- Selected Publications has three filters: All (default), Robot Intelligence and
  Multimodal AI. Derive membership from the existing `robotics` boolean: true is
  Robot Intelligence; every other active publication is Multimodal AI. Keep the
  approved publication order within each filter. Future entries inherit this rule.
  Hide the filter controls without JavaScript and keep every paper readable.
  Pause videos immediately when their cards are hidden; preserve lazy loading,
  reduced-motion behavior, keyboard operation and direct paper anchors.
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
  including the 2022 paper. Current active selection totals 18 papers. Unselected
  entries live in `content/archive/`; original assets remain available.
- Pin ThinkWorld = 1, DreamX = 2, MAWAM = 3, PhysCaP = 4, TT-VidT = 5, Scal3R = 6,
  ReactVAU = 7, per the owner's latest ordering.
  Remaining papers sort newest first, preserving input order within each year.
- MAWAM uses Preprint 2026 and the Robot Intelligence marker. Preserve its approved
  author URLs; Jing Wang links to https://scholar.google.com/citations?user=cdL5PqgAAAAJ&hl=en.
  Use the owner-provided staging Project URL until a replacement is authorized.
  Its official 6.6-second coordinated towel-folding clip retains the complete
  16:9 frame and source file timeline, with the existing silent-loop controls.
- ThinkWorld, DreamX and PhysCaP are robotics work and their main-conference
  submissions are under review. Workshop acceptances must be shown as workshops,
  separate from main venues. ThinkWorld: RoboWM and PTA at NeurIPS 2026. PhysCaP:
  Robot Learning Workshop at NeurIPS 2026 and Agentic Robotics at CoRL 2026.
  DreamX: Scaling H2R at CoRL 2026 (https://scaling-h2r-corl.github.io/).
  October 2026 News announces DreamX and PhysCaP at their respective CoRL workshops.
- On November 4, 2026, the owner authorized DreamX's resource release:
  Project https://cvlab-kaist.github.io/DreamX/, arXiv https://arxiv.org/abs/2611.05377
  and PDF https://arxiv.org/pdf/2611.05377. Its release hold is cleared; Code is pending.
  All three new entries use the owner-requested “Preprint 2026” badge, with
  workshop acceptances displayed separately.
- The owner approved this three-paper preview and authorized publication.
  On October 28, 2026, the owner
  authorized ThinkWorld's release: Project https://thinkworld-project.github.io/,
  arXiv https://arxiv.org/abs/2610.37666 and PDF https://arxiv.org/pdf/2610.37666.
  ThinkWorld remains Preprint 2026; Code/Model are still pending.
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

The owner-approved introduction centers on generalizable and agentic robot intelligence,
with robot agents, world–action modeling and embodied reasoning as the research directions and autonomous
improvement and zero-shot generalization as capabilities. In the introduction, bold only
“generalizable and agentic robot intelligence”; keep the research-direction list plain.
The introduction says “learn from experience across embodiments” to express the
owner’s requested cross-embodiment experience.
The Research Interests paragraph begins “My research focuses on generalizable
and agentic robot intelligence.” In this paragraph, bold “generalizable and agentic robot intelligence”,
“long horizons”, “self-improve” and “zero-shot generalization”. Use “self-improve through interaction”. Discuss robot agents combining perception, world–action modeling
and embodied reasoning to understand how humans solve problems, reason about physical
dynamics and anticipate action outcomes. The goal is learning from experience across
embodiments, long-horizon planning, improvement through interaction and zero-shot
generalization to new scenes, tasks and embodiments. Keep learning across embodiments
explicit in both the introduction and Research Interests; use zero-shot generalization
for the target generalization capability.
The exact approved copy lives in content/site.json; do not restore the earlier
three-highlight research paragraph or the former biography.

News uses `news_visible_since: "2026-02"`: February 2026 and all newer updates
remain expanded. Only earlier dates go into Earlier news. Preserve this date
boundary rather than a fixed item count, so future news stays visible.

News: keep the X-REASON invited talk (September 8, 2026) immediately after
the existing September 2026 paper news; newer months appear above both. Its title, provided by the owner,
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
