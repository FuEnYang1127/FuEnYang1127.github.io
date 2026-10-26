# Fu-En Yang · Research homepage

A static academic homepage for GitHub Pages. The owner updates it through an
assistant: send a paper link, news item or requested edit in chat; the assistant
updates the data, builds, verifies and shows a preview before publishing.

No runtime framework, build packages, API keys or npm installation are needed.
All text and publication links remain usable without JavaScript.

## Source of truth

| Content | File |
| --- | --- |
| Bio, portrait, research-interest paragraph, profile links, visitor statistics | `content/site.json` |
| Active selected papers, authors, venues, ordering, summaries, images/videos | `content/publications.json` |
| Unselected older papers | `content/archive/` |
| News | `content/news.json` |
| Academic service, awards and teaching | `content/background.json` |
| Layout | `templates/page.html` |
| Typography and visual design | `assets/site.css` |
| Videos and unavailable-map handling | `assets/site.js` |

`index.html` is generated and committed. Do not edit it directly.

Links to pages, author websites, papers, CV/PDFs and full-size figures open in a
new tab. The builder applies this to content links automatically. Only same-page
`#` navigation stays in the current tab; email links open the configured mail app.

## Build and preview

Python 3.9+; standard library only:

```sh
python3 scripts/build.py
python3 scripts/build.py --check
python3 scripts/preview.py
```

Open <http://127.0.0.1:4173>. Stop with Ctrl+C. An occupied port can be changed with
`--port 4174`. Generated HTML also opens directly from the filesystem.

## Publication format

```json
{
  "id": "short-paper-name",
  "title": "Full publication title",
  "year": 2026,
  "venue": "ECCV",
  "venue_full": "European Conference on Computer Vision",
  "authors": [{"name": "Fu-En Yang"}, {"name": "Coauthor", "url": "https://example.org/"}],
  "url": "https://example.org/project/",
  "description": "One or two factual sentences from the paper or project.",
  "links": [{"label": "Project", "url": "https://example.org/project/"}],
  "media": {
    "image": "assets/media/paper.webp",
    "alt": "Meaningful description of the complete figure.",
    "width": 1000,
    "height": 600,
    "fit": "contain",
    "source": "https://example.org/project/figure.png"
  }
}
```

Use `featured_order` only for explicitly pinned papers: Scal3R = 1 and ReactVAU = 2.
Other papers sort by descending year, with stable input ordering within a year.
For 2023 and earlier, the active list retains only Efficient Model Personalization
(ICCV 2023) and Adversarial Teacher-Student (NeurIPS 2021). All other earlier work,
including 2022, is archived. The current list has 13 papers. There is no topic taxonomy or filter UI.
`award` is optional. `Fu-En Yang`, including an optional `*`, is automatically bold.
Author order must match the original paper.

For video, add `media.video`, `media.poster`, `poster_width`, `poster_height`,
`video_source` and `video_note`. Prefer short silent MP4/H.264 excerpts with complete
frames and a static poster. Videos fetch only when visible, support pause, and
respect reduced motion / data saving. Fast-ThinkAct and ThinkAct deliberately use
static official teasers, per the owner's preference. Clicking a static figure opens
its full-size version. Publications use separate rounded cards inspired by the
reference site, with desktop thumbnails capped at 350px wide / 220px high. Never
crop scientific figures or add a fixed blank canvas. Research Interests starts
with the owner-approved positioning about generalizable and agentic robot
intelligence, using concise bold emphasis without colored marker backgrounds.
Use Title Case for section headings.

Biography, research interests and news accept only inline `<a href>`, `<strong>`,
`<em>` and `<br>` markup. All other fields are plain text. News uses `YYYY-MM` dates;
`news_visible` controls the initial list before the native archive disclosure.

## Fonts and visitors

Typography matches the reference site: Noto Sans for body and paper text, Google
Sans for major headings, both self-hosted with their SIL Open Font License files.
Body / authors / summaries use 16px text and 24px line height. Paper titles use
20.48px, weight 600; section headings use Google Sans 32px, weight 700. See
`assets/fonts/README.txt` for exact font URLs and licenses. The former NVIDIA Sans /
Inter stack was removed at the owner's request.

The footer reuses the original ClustrMaps image and public statistics link from
this site's previous homepage. Its endpoint and image URL live in `site.json`.
The map loads lazily; if unavailable, JavaScript hides the broken image and leaves
the dashboard link. Availability and visitor counts are controlled by ClustrMaps.
Do not fabricate a count, replace the site ID or create an analytics account.

## Appearance and news updates

The site is Light only, including when the operating system prefers dark mode.
The owner removed the theme switch and preference logic. Any `fu-en-theme` value
saved by an earlier preview is ignored. Typography and paper layout stay the same.
All social buttons, including CV, use the same neutral style.

The favicon is the owner's selected option C: an original SVG industrial robot
arm with a green precision gripper, designed for legibility at 16–32px. Its URL
includes a content hash to refresh older cached icons.

News dates use `YYYY-MM`; equal-month entries preserve the JSON order. The
September 2026 X-REASON invited talk is deliberately second, and its exact title
comes from the owner's slide. The official event date and source URL are recorded
in that entry for future editing. The internship link points to NVIDIA Research Taiwan.

## Review and publish

Read `AGENTS.md`. Build and run `--check`; verify desktop and mobile rendering,
publication ordering and older-paper selection, image proportions, relative assets, news
expansion, Light styling under either system preference, video playback, reduced motion, visitor fallback and no-JavaScript
content. Show screenshots and the local preview to the owner. Push only after the
owner approves that revision. GitHub Actions verifies generated HTML; it does not
publish. GitHub Pages serves the committed files; `.nojekyll` skips Jekyll.

Original images and PDFs are preserved, and the first redesign is recoverable in
Git history. Design began with a reference to [Sifei Liu](https://sifeiliu.net/) and
was independently revised to the owner's preferences. The original homepage was
based on [Jon Barron's template](https://github.com/jonbarron/website).
