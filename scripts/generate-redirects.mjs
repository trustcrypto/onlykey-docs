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
 * Run AFTER `docmd build`, against the generated `site/` directory.
 */
import { readdirSync, statSync, existsSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const SITE = process.argv[2] || 'site';

// Old slug -> current slug for pages that were renamed during migration.
const LEGACY_ALIASES = {
  internationaledition: 'ite',
  vitrualmachines: 'virtualmachines',
  'keepassxc-2-1-0': 'keepassxc-upgrade',
};

function stub(target) {
  // target is the extensionless, trailing-slash path relative to site root
  // (e.g. "duousersguide/"). Relative targets keep this working under both
  // a custom domain (root) and project-pages (/<repo>/) deployments.
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting&hellip;</title>
<link rel="canonical" href="/${target}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=${target}">
<script>location.replace("${target}" + location.hash);</script>
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
  const out = join(SITE, `${slug}.html`);
  if (existsSync(out)) continue; // never clobber a real built file (e.g. 404.html)
  writeFileSync(out, stub(`${slug}/`));
  written++;
}

// Legacy renamed-page aliases.
for (const [oldSlug, newSlug] of Object.entries(LEGACY_ALIASES)) {
  if (!slugs.includes(newSlug)) continue; // target page must exist
  const out = join(SITE, `${oldSlug}.html`);
  if (existsSync(out)) continue;
  writeFileSync(out, stub(`${newSlug}/`));
  written++;
}

console.log(`[redirects] wrote ${written} .html redirect stubs into ${SITE}/`);
