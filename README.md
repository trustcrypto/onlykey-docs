# OnlyKey Documentation (docmd)

This repository contains the OnlyKey documentation, migrated from the Jekyll-based
[trustcrypto/trustcrypto.github.io](https://github.com/trustcrypto/trustcrypto.github.io)
to [docmd](https://docmd.io).

## Quick start

```bash
npm install
npx @docmd/core dev
```

Open http://localhost:3000.

## Build

```bash
npx @docmd/core build
```

Static site is emitted into `site/`.

## Migration

The initial migration was performed by `scripts/import_from_trustcrypto.py`. It reads
the source repo from `/tmp/onlykey-source/trustcrypto.github.io` (clone it first if you
want to re-run) and writes converted markdown into `docs/`. See
`scripts/import-report.md` for what was imported and which pages have warnings that
need editorial review.

## Status

- [x] Initial migration complete (28 pages, 224 images)
- [ ] Editorial cleanup pass
- [ ] URL/redirect strategy
- [ ] Hosting decision (Cloudflare Pages, GitHub Pages, Netlify, self-host)
