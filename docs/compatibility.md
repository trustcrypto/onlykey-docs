---
title: Version Compatibility
description: Which OnlyKey firmware works with which web app, OnlyKey App, onlykey-cli and onlykey-agent, and what each feature needs.
slug: compatibility
last_updated: Nov, 25, 2026
keywords: OnlyKey, compatibility, versions, firmware, app, web app, onlykey-cli, onlykey-agent
---

# Version Compatibility

Use this page to check which versions of the OnlyKey software go with your firmware. To see your firmware version, open the OnlyKey App or run `onlykey-cli fwversion`. To upgrade, follow the [Upgrade Guide](/upgradeguide).

## By firmware version {#by-firmware}

| | Firmware 3.1.0 | Firmware 3.0.4 or older |
| --- | --- | --- |
| **Web app** | [apps.onlykey.io](https://apps.onlykey.io) (web app 4.0.0) | [apps.crp.to](https://apps.crp.to) |
| **OnlyKey App** | 6.0.0, needed to change the 3.1.0 settings in the app | 6.0.0, or 5.5.0 (5.3.6 on Windows) |
| **onlykey-cli** (python-onlykey) | 1.3.1, needed for post-quantum keys, age and the 3.1.0 settings | 1.3.1 or older |
| **onlykey-agent** | 1.1.17, needed for `derived-v2` keys | 1.1.17 or older |
| **Python** | 3.10 or newer for onlykey-cli 1.3.1 and onlykey-agent 1.1.17 | Same |

If a key on firmware 3.0.4 or older is plugged in at apps.onlykey.io, the page says that no OnlyKey answered and links to apps.crp.to. OnlyKey App 6.0.0 shows the 3.1.0-only settings only when the OnlyKey has firmware 3.1.0 or later.

## By feature {#by-feature}

| Feature | Firmware | Also needs |
| --- | --- | --- |
| [Post-quantum keys](/pqc) (ML-KEM-768, X-Wing) | 3.1.0 | onlykey-cli 1.3.1 |
| [Composite PQC OpenPGP keys](/pqc#composite-pgp) | 3.1.0 | onlykey-cli 1.3.1 and Node.js to load; web app 4.0.0 to use |
| [age](/age) | 3.1.0 | python-onlykey 1.3.1 with `[age]`; age 1.1+ or rage to decrypt |
| [Password Vault](/vault) | 3.1.0 | web app 4.0.0 |
| [User input modes](/user-input-modes) (three separate settings) | 3.1.0 | OnlyKey App 6.0.0 or onlykey-cli 1.3.1 |
| [Webcrypt Access](/user-input-modes#webcrypt-access) | 3.1.0 | OnlyKey App 6.0.0 or onlykey-cli 1.3.1 |
| Encrypted, authenticated web app connection ([transit v2](/webcrypt#transit-v2)) | 3.1.0 | web app 4.0.0 |
| SSH/GPG `derived-v2` keys | 3.1.0 | onlykey-agent 1.1.17 |
| SSH and GPG with Windows OpenSSH and Gpg4win | Any | onlykey-agent 1.1.17 |
| GnuPG 2.5 decryption with onlykey-agent | Any | onlykey-agent 1.1.17 |
| SSH/GPG keys from earlier versions | Any | Unchanged: onlykey-agent keeps the original derivation unless you ask for `derived-v2` |

## OnlyKey and OnlyKey DUO {#duo}

OnlyKey and OnlyKey DUO use the same firmware file from 3.1.0 on. There is one firmware edition; the International Travel Edition was removed in 3.1.0.
