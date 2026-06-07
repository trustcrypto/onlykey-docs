# OnlyKey Docs (docmd) — Pre-Publish Review

Review of the migrated docmd site at `http://127.0.0.1:3000` against the source at `docs/`.
All issues below marked **Fixed** were corrected in the markdown source; the site was rebuilt and re-verified.

## Summary

| Area | Found | Status |
|------|-------|--------|
| Broken internal page links | 7 | Fixed |
| Broken in-page / cross-page anchors | 30 | Fixed |
| Pages broken by leftover HTML (rendered as raw code) | 2 (FAQ, Home) | Fixed |
| Leftover Jekyll `{% include %}` tags | 25 files | Fixed |
| Leftover sample/placeholder page | 1 (`go.md`) | Fixed |
| Files whose URL didn't match canonical slug | 3 | Fixed (renamed) |
| Old-domain (`docs.crp.to`) cross-links | 8 | Fixed |
| Duplicate heading IDs | 2 | Fixed |
| FontAwesome icons not rendering | ~28 | Fixed (tags removed) |
| Insecure/legacy external links | several | Flagged below |

After fixes: **0 broken internal links, 0 broken anchors** (verified programmatically against the rebuilt HTML).

---

## Critical issues (fixed)

### 1. FAQ page was completely broken
`faq.md` was raw Bootstrap accordion HTML (`<div class="panel-collapse collapse">` + jQuery `data-toggle`). docmd has no Bootstrap, and because the HTML was indented it rendered as a literal **code block** — the entire page dumped its markup as monospaced text.

**Fix:** Rewrote the FAQ in clean markdown — each question is now a heading (so it appears in the "On this page" TOC, is searchable, and is deep-linkable) with the answer as prose/lists. Also fixed a typo ("by OnlyKey" → "my OnlyKey") and a missing word ("does not utilize encryption").

### 2. Homepage cards were stripped to bare links
`index.md` used Bootstrap `panel`/`col-md-3` grid + FontAwesome icons. These collapsed into a run-on list of links ("User's Guide DUO User's Guide").

**Fix:** Rebuilt the four cards using docmd's native `:::grids` / `:::card` / `:::button` containers. Renders as a proper card grid with buttons.

---

## Links & navigation (fixed)

### 3. Broken page links — slug vs filename
docmd routes by **filename**, ignoring the `slug:` frontmatter. Three pages therefore lived at the wrong URL, breaking every link to them:

- `internationaledition.md` served `/internationaledition`, but everything links to `/ite` (6 links).
- `vitrualmachines.md` (note the typo) served `/vitrualmachines`, but links use `/virtualmachines`.
- `keepassxc-2-1-0.md` served `/keepassxc-2-1-0` instead of the canonical `/keepassxc-upgrade`.

**Fix:** Renamed the three files to `ite.md`, `virtualmachines.md`, `keepassxc-upgrade.md`. This fixes all links **and** preserves the canonical URLs from the old site (important for existing inbound links). Stale build directories from the old names were removed from `site/`.

### 4. Broken anchors (30) — docmd's hierarchical heading IDs
For headings **without** an explicit `{#id}`, docmd builds *nested* IDs (e.g. "OnlyKey Chrome App" became `onlykey-app-about-onlykey-chrome-app`). Links written for flat IDs (`/app#onlykey-chrome-app`) therefore 404'd. Affected pages: `app`, `command-line`, `onlykey-agent`, `features`, `security`, `upgradeguide`.

**Fix:** Added explicit `{#id}` attributes to the linked headings so they match (and match the old site's anchors). Also corrected two genuinely mis-pointed links:
- `security.md` linked `/features#Yubico-one-time-password` → corrected to `/usersguide#Yubico-one-time-password`.
- `onlykey-agent.md` linked `/usersguide#challenge-mode` (no such section) → `/usersguide#derived-challenge-mode`.

### 5. Old documentation domain in cross-links
Internal pages were linked via the **old** `docs.crp.to` domain.

**Fix:** Converted in-site cross-links to relative paths (`/linux`, `/wsl`, `/mobile`) and changed the generic "OnlyKey Documentation" links to `https://docs.onlykey.io`.

---

## Cleanup (fixed)

- **Jekyll leftovers:** removed `{% include links.html %}` from all 25 pages (was rendering as literal text).
- **Sample page:** deleted `go.md` ("Sample 1 Topic (Product 1)") — leftover from the docmd starter theme; it was showing in the sidebar.
- **Duplicate heading IDs:** `features.md` had two `{#uninitialized-onlykey}` (fixed the "Locked OnlyKey" one to `{#locked-onlykey}`); `security.md` had two `{#software-app-security}` (fixed "OnlyKey Firmware" to `{#software-firmware-security}`).

---

### 6. FontAwesome icons removed
Pages `usersguide`, `duousersguide`, `app`, `importpgp`, `linux` used FontAwesome 4 inline icons (`<i class="fa fa-apple">`, decorative down-arrows). docmd doesn't load FontAwesome, so they rendered invisibly. Per your choice, the empty `<i class="fa ...">` tags were stripped for a clean, dependency-free look. Link/button text (e.g. **macOS**, **Windows**, **Linux**) is preserved.

---

## Flagged external links (review at your discretion — not changed)

- `http://www.crp.to/p/` (`app.md`) — "OnlyKey order" link is `http://` and the `/p/` path looks incomplete; verify it still resolves (vs. `https://onlykey.io/products`).
- `https://docs.crp.to/49-onlykey-blink.rules` (`full-disk-encryption.md`) — a raw file on the old docs host; confirm it still exists or rehost it.
- Several reference links use `http://` (NIST, apache.org, wassenaar.org, etc.) — work, but `https://` is preferable where available.
- Mixed casing `www.Yubico.com` vs `www.yubico.com` — cosmetic.
- Beta-7 firmware download URLs in `legacyupgradeguide.md` — legacy guide; left as-is.

External link **targets** were not fetched/validated for liveness — let me know if you want me to crawl them.

---

## Before publishing
Run a clean build so no stale artifacts ship:

```bash
rm -rf site && npx @docmd/core build
```
