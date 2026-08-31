#!/usr/bin/env node
/**
 * generate-redirects.mjs
 *
 * The legacy Jekyll site (trustcrypto.github.io) served pages at flat
 * `/<slug>.html` URLs. The docmd site serves extensionless `/<slug>/`,
 * so every old inbound `.html` link 404s. This script writes a small
 * client-side redirect stub at `site/<slug>.html` for each built page so
 * those old URLs keep working. The `#anchor` is preserved (e.g.
 * `app.html#app-desktop` -> `/app/#app-desktop`).
 *
 * It also fixes the site-wide 404: docmd's built-in `site/404.html` template
 * renders untranslated i18n keys ("pageNotFound", "returnHome"), and GitHub
 * Pages serves that file — not our own `docs/404.md` page — on any miss.
 * We overwrite it with the rendered `site/404/index.html`, re-pathed to
 * absolute URLs so it works from any depth.
 *
 * Run AFTER `docmd build`, against the generated `site/` directory.
 */
import { readdirSync, statSync, existsSync, writeFileSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const SITE = process.argv[2] || 'site';

// Old URL slug -> current target path (relative to site root, trailing slash,
// optional #anchor). Covers pages renamed during the docmd migration AND
// docs.crp.to-era standalone pages whose content was folded into another page.
const LEGACY_ALIASES = {
  internationaledition: 'ite/',
  vitrualmachines: 'virtualmachines/',
  'keepassxc-2-1-0': 'keepassxc-upgrade/',
  // docs.crp.to-era quickstart pages, now sections of the agent page.
  gpgagentquickstart: 'onlykey-agent/#gpg-agent-quickstart-guide',
  sshagentquickstart: 'onlykey-agent/#ssh-agent-quickstart-guide',
  agentquickstart: 'onlykey-agent/',
  'onlykey-agent-quickstart': 'onlykey-agent/',
};

function stub(target) {
  // target is a path relative to site root, e.g. "duousersguide/" or
  // "onlykey-agent/#gpg-agent-quickstart-guide". Relative targets keep this
  // working under both a custom domain (root) and project-pages (/<repo>/).
  const hasAnchor = target.includes('#');
  // Only append the inbound hash when the target doesn't already carry one.
  const jsTarget = hasAnchor
    ? JSON.stringify(target)
    : `${JSON.stringify(target)} + location.hash`;
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting&hellip;</title>
<link rel="canonical" href="/${target}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=${target}">
<script>location.replace(${jsTarget});</script>
</head>
<body>Redirecting to <a href="${target}">/${target}</a>&hellip;</body>
</html>
`;
}

if (!existsSync(SITE)) {
  console.error(`[redirects] site dir not found: ${SITE}`);
  process.exit(1);
}

// One stub per built page directory that contains an index.html.
const slugs = readdirSync(SITE).filter((name) => {
  if (name === 'assets') return false;
  const dir = join(SITE, name);
  return statSync(dir).isDirectory() && existsSync(join(dir, 'index.html'));
});

let written = 0;
for (const slug of slugs) {
  if (slug === '404') continue; // 404 is handled below, never a redirect stub
  const out = join(SITE, `${slug}.html`);
  if (existsSync(out)) continue; // never clobber a real built file
  writeFileSync(out, stub(`${slug}/`));
  written++;
}

// Legacy renamed / absorbed page aliases.
for (const [oldSlug, target] of Object.entries(LEGACY_ALIASES)) {
  const targetSlug = target.split('#')[0].replace(/\/$/, '');
  if (!slugs.includes(targetSlug)) {
    console.warn(`[redirects] skipping ${oldSlug}.html — target page "${targetSlug}" not built`);
    continue;
  }
  const out = join(SITE, `${oldSlug}.html`);
  if (existsSync(out)) continue;
  writeFileSync(out, stub(target));
  written++;
}

console.log(`[redirects] wrote ${written} .html redirect stubs into ${SITE}/`);

// ---------------------------------------------------------------------------
// Site-wide 404.
// docmd emits its own site/404.html from an internal template that ships
// untranslated i18n placeholders. GitHub Pages serves /404.html for every
// unmatched path, so that broken template is what visitors actually see.
// Replace it with our rendered docs/404.md page (site/404/index.html), with
// its depth-1 relative paths rewritten to absolute so it renders correctly
// no matter how deep the missing URL was.
// ---------------------------------------------------------------------------
const rendered404 = join(SITE, '404', 'index.html');
if (existsSync(rendered404)) {
  const html = readFileSync(rendered404, 'utf8')
    // href="../x" / src="../x" -> href="/x"
    .replace(/((?:href|src)=")\.\.\//g, '$1/')
    // url(../x) inside inline styles
    .replace(/(url\((['"]?))\.\.\//g, '$1/')
    // docmd's inline bootstrap computes asset roots relative to page depth;
    // the 404 is served from arbitrary depths, so pin them to the site root.
    .replace(/(var (?:root|siteRoot) = )"\.\.\/"/g, '$1"/"');
  writeFileSync(join(SITE, '404.html'), html);
  console.log('[redirects] replaced site/404.html with the rendered docs/404.md page');
} else {
  console.warn('[redirects] site/404/index.html not found — left docmd default 404.html in place');
}
