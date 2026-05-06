#!/usr/bin/env python3
"""
Import OnlyKey docs from trustcrypto/trustcrypto.github.io (Jekyll) to docmd format.

Reads from: /tmp/onlykey-source/trustcrypto.github.io/
Writes to:  /Users/t/Documents/GitHub/onlykey-docs/

Conversions:
- Jekyll frontmatter -> docmd-compatible frontmatter (preserves title, description from summary, slug)
- {% include callout.html content="..." type="X" %} -> docmd :::callout / :::tip / :::note / :::warning / :::danger / :::info
- {% include note.html content="..." %} -> :::note
- {% include warning.html content="..." %} -> :::warning
- {% include important.html content="..." %} -> :::warning (no separate "important" in docmd; closest match)
- {% include tip.html content="..." %} -> :::tip
- {% include image.html file="X" max-width="N" %} -> standard markdown image
- Kramdown {#anchor} on headings preserved as-is (most modern processors support it)
- URLs: docs.crp.to/X.html, docs.onlykey.io/X.html, /X.html -> /X (extensionless)
- Asset references in body: rewritten to images/ relative path
"""

import os, re, shutil, sys, json
from pathlib import Path

SRC = Path('/tmp/onlykey-source/trustcrypto.github.io')
DST = Path('/Users/t/Documents/GitHub/onlykey-docs')
DOCS = DST / 'docs'
IMAGES_OUT = DST / 'assets'  # docmd convention: project-root assets/

REPORT = []  # list of dicts to summarize


# ---------- Frontmatter ----------
def split_frontmatter(text):
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end > 0:
            fm_raw = text[4:end]
            body = text[end + 4:].lstrip('\n')
            fm = {}
            for ln in fm_raw.split('\n'):
                m = re.match(r'^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$', ln)
                if m:
                    fm[m.group(1)] = m.group(2)
            return fm, body
    return {}, text


def write_frontmatter(fm):
    """Write a clean YAML frontmatter block."""
    lines = ['---']
    for k, v in fm.items():
        if v is None:
            continue
        # If value contains characters needing quoting, quote it
        s = str(v)
        if any(c in s for c in [':', '#', '"', "'", '\n', '[', ']']):
            s = json.dumps(s)  # JSON quoting is YAML-compatible for our cases
        lines.append(f'{k}: {s}')
    lines.append('---')
    return '\n'.join(lines) + '\n'


# ---------- Jekyll include macros ----------
INCLUDE_RE = re.compile(
    r'\{%\s*include\s+(\S+\.html)\s+(.*?)\s*%\}',
    re.DOTALL,
)

# Map Jekyll callout/alert types to docmd container kinds.
# docmd supports common containers: tip, note, warning, danger, info, callout
TYPE_MAP = {
    'default':  'callout',
    'primary':  'info',
    'success':  'tip',
    'info':     'info',
    'warning':  'warning',
    'danger':   'danger',
    'tip':      'tip',
    'note':     'note',
    'important':'warning',  # no exact docmd match; warning is closest
}


def parse_include_attrs(s):
    """Parse a Jekyll include's attribute list into a dict.
    e.g.  content="text" type="default"  ->  {'content': 'text', 'type': 'default'}
    Handles double-quoted values with escaped internal quotes minimally."""
    attrs = {}
    # Match key="value" pairs; value may contain anything except an unescaped quote.
    for m in re.finditer(r'(\w+)\s*=\s*"((?:[^"\\]|\\.)*)"', s):
        k, v = m.group(1), m.group(2)
        # Unescape \" if any
        v = v.replace('\\"', '"')
        attrs[k] = v
    return attrs


def convert_callout(name, attrs):
    """Convert a callout-like include to a docmd container block."""
    content = attrs.get('content', '').strip()
    if name == 'callout.html':
        ctype = attrs.get('type', 'default')
        kind = TYPE_MAP.get(ctype, 'callout')
    elif name == 'note.html':
        kind = 'note'
    elif name == 'warning.html':
        kind = 'warning'
    elif name == 'tip.html':
        kind = 'tip'
    elif name == 'important.html':
        kind = 'warning'  # closest match
    else:
        # Unknown include — keep raw and flag for review
        return None

    return f':::{kind}\n{content}\n:::'


def convert_image(attrs):
    fname = attrs.get('file', '')
    if not fname:
        return None
    # Some Jekyll image.html includes use a path prefix or an alt
    alt = attrs.get('alt', '')
    return f'![{alt}](/assets/{fname})'


def replace_includes(body, page_path):
    """Find every {% include ... %} and convert or flag."""
    warnings = []

    def repl(m):
        name = m.group(1)
        attrs_raw = m.group(2)
        attrs = parse_include_attrs(attrs_raw)

        if name in ('callout.html', 'note.html', 'warning.html', 'tip.html', 'important.html'):
            out = convert_callout(name, attrs)
            if out:
                return out
            warnings.append(f'Unhandled callout variant: {name} {attrs_raw}')
            return m.group(0)
        if name == 'image.html':
            out = convert_image(attrs)
            if out:
                return out
            warnings.append(f'image.html missing file attr: {attrs_raw}')
            return m.group(0)
        # Unknown include — leave in place, flag for review
        warnings.append(f'Unrecognized Jekyll include: {name}')
        return m.group(0)

    new_body = INCLUDE_RE.sub(repl, body)
    return new_body, warnings


# ---------- Other Jekyll cleanup ----------
LIQUID_RAW_RE = re.compile(r'\{%\s*raw\s*%\}(.*?)\{%\s*endraw\s*%\}', re.DOTALL)
LIQUID_IF_RE = re.compile(r'\{%\s*if\s+[^%]*%\}.*?\{%\s*endif\s*%\}', re.DOTALL)
LIQUID_VAR_RE = re.compile(r'\{\{\s*[^}]+\s*\}\}')

# Internal link rewrites: docs.crp.to/X.html, docs.onlykey.io/X.html, /X.html -> /X
INTERNAL_HOST_LINK_RE = re.compile(
    r'https?://docs\.(?:crp\.to|onlykey\.io)(/[A-Za-z0-9_/\-\.]*)\.html(\#[A-Za-z0-9_-]+)?'
)
# Bare /X.html -> /X (only if it looks like an internal docs link)
BARE_HTML_LINK_RE = re.compile(
    r'(?<![A-Za-z0-9])/([A-Za-z0-9_-]+)\.html(\#[A-Za-z0-9_-]+)?(?![A-Za-z0-9])'
)


def rewrite_links(body):
    warnings = []

    def host_repl(m):
        path = m.group(1).rstrip('/')
        anchor = m.group(2) or ''
        if not path or path == '/':
            return f'/{anchor.lstrip("#") and "#" + anchor.lstrip("#") or ""}'
        slug = path.lstrip('/')
        return f'/{slug}{anchor}'

    body = INTERNAL_HOST_LINK_RE.sub(host_repl, body)

    def bare_repl(m):
        slug = m.group(1)
        anchor = m.group(2) or ''
        return f'/{slug}{anchor}'

    body = BARE_HTML_LINK_RE.sub(bare_repl, body)

    # GitHub raw image URLs -> /assets/X
    body = re.sub(
        r'https?://raw\.githubusercontent\.com/trustcrypto/trustcrypto\.github\.io/[^/]+/images/',
        '/assets/',
        body,
    )
    # Legacy docs.{crp.to,onlykey.io}/images/X -> /assets/X
    body = re.sub(
        r'https?://docs\.(?:crp\.to|onlykey\.io)/images/',
        '/assets/',
        body,
    )
    # Bare images/X (markdown) -> /assets/X
    body = re.sub(r'(\]\()images/', r'\1/assets/', body)
    body = re.sub(r'(src=")images/', r'\1/assets/', body)
    body = re.sub(r'(href=")images/', r'\1/assets/', body)

    return body, warnings


def liquid_cleanup(body):
    warnings = []
    # Preserve raw blocks: drop the {% raw %} {% endraw %} wrapper but keep contents
    body = LIQUID_RAW_RE.sub(lambda m: m.group(1), body)
    # Flag any remaining {% if %} blocks
    if LIQUID_IF_RE.search(body):
        warnings.append('Liquid {% if %} block present — left as-is, needs editorial review')
    # Flag remaining {{ ... }} variable references
    if LIQUID_VAR_RE.search(body):
        warnings.append('Liquid {{ variable }} reference present — left as-is, needs editorial review')
    return body, warnings


# ---------- Main per-file processing ----------
def transform_file(src_path, rel_slug):
    """Read source, transform, return (frontmatter_dict, body, warnings)."""
    with open(src_path, 'r', encoding='utf-8') as f:
        text = f.read()

    fm, body = split_frontmatter(text)

    # Build the output frontmatter for docmd
    out_fm = {}
    if fm.get('title'):
        # Strip surrounding quotes if present
        t = fm['title'].strip('"').strip("'")
        out_fm['title'] = t
    if fm.get('summary'):
        out_fm['description'] = fm['summary'].strip('"').strip("'")
    # Slug derived from permalink or filename
    slug_source = fm.get('permalink', '').strip('"').strip("'") or rel_slug
    slug = slug_source.replace('.html', '').lstrip('/')
    out_fm['slug'] = slug
    if fm.get('last_updated'):
        out_fm['last_updated'] = fm['last_updated'].strip('"').strip("'")
    if fm.get('keywords'):
        kw = fm['keywords'].strip('"').strip("'")
        out_fm['keywords'] = kw

    warnings = []
    body, w = replace_includes(body, src_path)
    warnings.extend(w)
    body, w = liquid_cleanup(body)
    warnings.extend(w)
    body, w = rewrite_links(body)
    warnings.extend(w)

    return out_fm, body, warnings


def collect_image_refs(body):
    """Find every /assets/X.png reference in the body."""
    refs = set()
    for m in re.finditer(r'/assets/([A-Za-z0-9._/-]+)', body):
        refs.add(m.group(1))
    return refs


def main():
    if not SRC.exists():
        print(f'ERROR: source not found at {SRC}', file=sys.stderr)
        sys.exit(1)

    DOCS.mkdir(parents=True, exist_ok=True)
    IMAGES_OUT.mkdir(parents=True, exist_ok=True)

    # Files to import: pages/mydoc/*.md, pages/product1/*.md, index.md, 404.md
    sources = []
    sources.append((SRC / 'index.md', 'index'))
    if (SRC / '404.md').exists():
        sources.append((SRC / '404.md', '404'))
    for f in sorted((SRC / 'pages' / 'mydoc').glob('*.md')):
        sources.append((f, f.stem))
    for f in sorted((SRC / 'pages' / 'product1').glob('*.md')):
        sources.append((f, f.stem))

    referenced_images = set()
    pages_imported = 0
    pages_with_warnings = 0

    for src_path, rel_slug in sources:
        try:
            fm, body, warnings = transform_file(src_path, rel_slug)
        except Exception as e:
            REPORT.append({
                'file': str(src_path.relative_to(SRC)),
                'status': 'failed',
                'error': str(e),
            })
            continue

        out_path = DOCS / f'{rel_slug}.md'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(write_frontmatter(fm))
            f.write('\n')
            f.write(body)
            if not body.endswith('\n'):
                f.write('\n')

        referenced_images |= collect_image_refs(body)
        pages_imported += 1
        if warnings:
            pages_with_warnings += 1
        REPORT.append({
            'file': str(src_path.relative_to(SRC)),
            'output': str(out_path.relative_to(DST)),
            'slug': fm.get('slug'),
            'title': fm.get('title'),
            'warnings': warnings,
        })

    # Copy referenced images
    src_images_dir = SRC / 'images'
    images_copied = 0
    images_missing = []
    for ref in sorted(referenced_images):
        src_img = src_images_dir / ref
        dst_img = IMAGES_OUT / ref
        if src_img.exists():
            dst_img.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_img, dst_img)
            images_copied += 1
        else:
            images_missing.append(ref)

    # Also copy ALL images from source images dir, even if not directly referenced —
    # safer for security docs where some images are linked via includes we may have missed.
    images_extra = 0
    for src_img in src_images_dir.rglob('*'):
        if not src_img.is_file():
            continue
        rel = src_img.relative_to(src_images_dir)
        dst_img = IMAGES_OUT / rel
        if not dst_img.exists():
            dst_img.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_img, dst_img)
            images_extra += 1

    # Write import report
    report_path = DST / 'scripts' / 'import-report.md'
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('# Import Report — OnlyKey Docs to docmd\n\n')
        f.write(f'**Source:** trustcrypto/trustcrypto.github.io (branch: pages)\n')
        f.write(f'**Target:** {DST}\n')
        f.write(f'**Generated:** import_from_trustcrypto.py\n\n')
        f.write(f'## Summary\n')
        f.write(f'- Pages imported: **{pages_imported}**\n')
        f.write(f'- Pages with warnings: **{pages_with_warnings}**\n')
        f.write(f'- Images directly referenced and copied: **{images_copied}**\n')
        f.write(f'- Additional images copied from source images/ dir: **{images_extra}**\n')
        f.write(f'- Images referenced but missing from source: **{len(images_missing)}**\n\n')
        if images_missing:
            f.write(f'### Missing images\n')
            for m in images_missing:
                f.write(f'- `{m}`\n')
            f.write('\n')
        f.write('## Pages\n\n')
        for item in REPORT:
            if item.get('status') == 'failed':
                f.write(f'### ❌ {item["file"]}\n')
                f.write(f'- Error: {item.get("error")}\n\n')
                continue
            f.write(f'### {item["file"]} -> {item["output"]}\n')
            f.write(f'- Title: {item.get("title")}\n')
            f.write(f'- Slug: `{item.get("slug")}`\n')
            if item.get('warnings'):
                f.write(f'- Warnings:\n')
                for w in item['warnings']:
                    f.write(f'  - {w}\n')
            f.write('\n')

    print(f'\nDONE.')
    print(f'  Pages imported:  {pages_imported}')
    print(f'  Pages with warn: {pages_with_warnings}')
    print(f'  Images copied:   {images_copied} (referenced) + {images_extra} (extras)')
    print(f'  Images missing:  {len(images_missing)}')
    print(f'  Report:          {report_path}')


if __name__ == '__main__':
    main()
