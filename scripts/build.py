#!/usr/bin/env python3
"""Build the committed static homepage. Python 3.9+; no dependencies."""
import argparse
import html
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from string import Template
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]

def esc(value):
    return html.escape(str(value), quote=True)

def load(name):
    return json.loads((ROOT / 'content' / f'{name}.json').read_text(encoding='utf-8'))

def url(value):
    """Validate web URLs and checked-in relative assets at build time."""
    parts = urlsplit(value)
    if parts.scheme:
        if parts.scheme not in ('https', 'http', 'mailto'):
            raise ValueError(f'Unsupported URL: {value}')
    elif not value.startswith('#'):
        target = (ROOT / parts.path).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            raise ValueError(f'Missing local file: {value}')
    return esc(value)

def link_target(href):
    """Preserve the homepage when opening another page or a local document."""
    if href.startswith('#') or urlsplit(href).scheme == 'mailto':
        return ''
    return 'target="_blank" rel="noopener noreferrer"'

class InlineHTML(HTMLParser):
    """Small, explicit markup vocabulary for biography and news."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.output = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in ('a', 'strong', 'em', 'br'):
            raise ValueError(f'Unsupported inline tag: {tag}')
        if tag == 'a':
            href = dict(attrs).get('href', '')
            self.output.append(f'<a href="{url(href)}" {link_target(href)}>')
        else:
            self.output.append(f'<{tag}>')
        if tag != 'br':
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise ValueError(f'Unbalanced inline tag: {tag}')
        self.output.append(f'</{tag}>')

    def handle_data(self, data):
        self.output.append(esc(data))

def rich(value):
    parser = InlineHTML()
    parser.feed(value)
    parser.close()
    if parser.stack:
        raise ValueError('Unclosed inline markup')
    return ''.join(parser.output)

def anchor(label, href, classes='', extra=''):
    return f'<a class="{esc(classes)}" href="{url(href)}" {link_target(href)} {extra}>{esc(label)}</a>'

def publication(pub, site):
    ident = pub['id']
    if not re.fullmatch(r'[a-z0-9-]+', ident):
        raise ValueError(f'Invalid publication ID: {ident}')
    for field in ('title', 'year', 'venue', 'authors', 'description', 'links'):
        if not pub.get(field):
            raise ValueError(f'{ident}: missing {field}')
    media = pub['media']
    if not media.get('alt') or media.get('fit', 'contain') != 'contain':
        raise ValueError(f'{ident}: scientific figures must have alt text and fit=contain')
    poster = media.get('poster', media['image'])
    width = media.get('poster_width', media['width'])
    height = media.get('poster_height', media['height'])
    authors = []
    for author in pub['authors']:
        name = author['name']
        if name.rstrip('*') == site['name']:
            authors.append(f'<strong>{esc(name)}</strong>')
        elif author.get('url'):
            authors.append(anchor(name, author['url']))
        else:
            authors.append(esc(name))
    badge = f'<span class="badge">{esc(pub["venue"])} {pub["year"]}</span>'
    if pub.get('award'):
        badge += f'<span class="badge badge-award">{esc(pub["award"])}</span>'
    video = ''
    buttons = anchor('View figure ↗', media['image'], 'figure-link',
                     f'aria-label="View research figure for {esc(pub["title"])}"')
    if media.get('video'):
        video = f'''<video class="demo-video" muted loop playsinline preload="none"
            poster="{url(poster)}" data-src="{url(media['video'])}"
            aria-label="{esc(pub['title'])} — silent project demonstration"></video>'''
        buttons = f'''<button class="demo-toggle" type="button" hidden
            aria-label="Play demo for {esc(pub['title'])}" aria-pressed="false">Play demo</button>''' + buttons
    image = f'<img src="{url(poster)}" alt="{esc(media["alt"])}" width="{width}" height="{height}" loading="lazy" decoding="async">'
    if not video:
        image = f'<a class="figure-open" href="{url(media["image"])}" {link_target(media["image"])} aria-label="Enlarge research figure for {esc(pub["title"])}">{image}</a>'
    caption = f'<figcaption>{buttons}</figcaption>' if video else ''
    links = ''.join(anchor(link['label'], link['url'], 'paper-link') for link in pub['links'])
    return f'''<article class="publication" id="{ident}" aria-labelledby="title-{ident}">
        <figure class="paper-figure">
          <div class="media-stage">
            {image}
            {video}
          </div>
          {caption}
        </figure>
        <div class="paper-copy">
          <div class="paper-meta">{badge}</div>
          <h3 id="title-{ident}">{anchor(pub['title'], pub['url'])}</h3>
          <p class="authors">{', '.join(authors)}</p>
          <p class="paper-description">{esc(pub['description'])}</p>
          <nav class="paper-links" aria-label="Resources for {esc(pub['title'])}">{links}</nav>
        </div>
      </article>'''

def news_rows(items):
    result = []
    for item in items:
        if not re.fullmatch(r'\d{4}-\d{2}', item['date']):
            raise ValueError(f'Invalid news date: {item["date"]}')
        result.append(f'<li><time datetime="{esc(item["date"])}">{esc(item["label"])}</time><div>{rich(item["html"])}</div></li>')
    return '\n'.join(result)

def render():
    site, pubs, news, background = (load(n) for n in ('site', 'publications', 'news', 'background'))
    if any(p['year'] < 2021 for p in pubs):
        raise ValueError('Keep 2020–2018 papers in content/archive, not the active publication list.')
    ids = [p['id'] for p in pubs]
    if len(ids) != len(set(ids)):
        raise ValueError('Publication IDs must be unique')
    pinned = [p['featured_order'] for p in pubs if 'featured_order' in p]
    if any(not isinstance(n, int) or n < 1 for n in pinned) or len(pinned) != len(set(pinned)):
        raise ValueError('featured_order must be a unique positive integer')
    pubs.sort(key=lambda p: (p.get('featured_order', 100000), -p['year']))
    news.sort(key=lambda n: n['date'], reverse=True)
    visible = site['news_visible']
    older_news = ''
    if news[visible:]:
        older_news = f'''<details class="news-archive"><summary>Earlier news <span aria-hidden="true">+</span></summary>
          <ul class="news-list">{news_rows(news[visible:])}</ul></details>'''
    buttons = ''.join(anchor(item['label'], item['url'], 'button') for item in site['links'])
    scholarly = next(item['url'] for item in site['links'] if item['label'] == 'Google Scholar')
    analytics = site.get('analytics')
    visitor_map = ''
    if analytics and analytics.get('enabled', True):
        visitor_map = f'''<section class="visitor-section" aria-labelledby="visitor-title">
          <h2 id="visitor-title">Visitors</h2>
          <a class="visitor-map" href="{url(analytics['url'])}" target="_blank" rel="noopener noreferrer" aria-label="Open visitor counts and geographic statistics on {esc(analytics['provider'])}">
            <img src="{url(analytics['image'])}" alt="{esc(analytics['alt'])}" width="{int(analytics['width'])}" height="{int(analytics['height'])}" loading="eager" referrerpolicy="no-referrer-when-downgrade">
          </a>
          <a class="text-link" href="{url(analytics['url'])}" target="_blank" rel="noopener noreferrer">Visitor statistics &amp; locations ↗</a>
        </section>'''
    blocks = []
    for section in background:
        items = ''.join(f'<li>{esc(item)}</li>' for item in section['items'])
        if section['title'] == 'Academic Services':
            # Keep the full historical reviewer list available without overwhelming the page.
            chair, conferences, journals = section['items']
            items = f'<li>{esc(chair)}</li><li><details><summary>Conference program committees &amp; reviewing</summary><p>{esc(conferences.partition(": ")[2])}</p></details></li><li>{esc(journals)}</li>'
        blocks.append(f'<section class="background-card"><h3>{esc(section["title"])}</h3><ul>{items}</ul></section>')
    person = {'@context':'https://schema.org','@type':'Person','name':site['name'],'url':site['url'],'image':site['url']+site['portrait'],'jobTitle':site['role'],'worksFor':{'@type':'Organization','name':site['organization']},'sameAs':[l['url'] for l in site['links'] if l['url'].startswith('https:') and l['label']!='CV']}
    data = dict(
        name=esc(site['name']), description=esc(site['description']), canonical=url(site['url']),
        favicon_url='images/nvidia.png?v='+hashlib.sha256((ROOT/'images/nvidia.png').read_bytes()).hexdigest()[:10],
        css_url='assets/site.css?v='+hashlib.sha256((ROOT/'assets/site.css').read_bytes()).hexdigest()[:10],
        js_url='assets/site.js?v='+hashlib.sha256((ROOT/'assets/site.js').read_bytes()).hexdigest()[:10],
        email=url(next(item['url'] for item in site['links'] if item['label'] == 'Email')),
        role=esc(site['role']), organization=esc(site['organization']),
        portrait=url(site['portrait']), portrait_url=url(site['url']+site['portrait']),
        bio=''.join(f'<p>{rich(p)}</p>' for p in site['bio']),
        social_buttons=buttons, research_interest=rich(site['research_interest']),
        news=news_rows(news[:visible]), older_news=older_news,
        scholar=url(scholarly),
        publications='\n'.join(publication(p,site) for p in pubs),
        background='\n'.join(blocks), visitor_map=visitor_map, structured_data=json.dumps(person,ensure_ascii=False).replace('<','\\u003c')
    )
    output = Template((ROOT/'templates/page.html').read_text(encoding='utf-8')).substitute(data)
    return '\n'.join(line.rstrip() for line in output.splitlines()) + '\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify generated HTML is current without writing.')
    args = parser.parse_args()
    output = render()
    target = ROOT/'index.html'
    if args.check:
        if target.read_text(encoding='utf-8') != output:
            raise SystemExit('index.html is stale. Run python3 scripts/build.py')
        print('OK: content, local assets, IDs and generated HTML are valid.')
    else:
        target.write_text(output,encoding='utf-8')
        print('Built index.html')

if __name__ == '__main__':
    main()
