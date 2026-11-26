---
title: Password Vault
description: Keep passwords, API keys and other secrets in your browser, each encrypted to a post-quantum key on your OnlyKey. Requires firmware 3.1.0.
slug: vault
last_updated: Nov, 25, 2026
keywords: OnlyKey, vault, password vault, secrets, age, X-Wing, post-quantum, web app
---

# Password Vault

The Password Vault at [apps.onlykey.io/app/vault](https://apps.onlykey.io/app/vault) keeps passwords, API keys and other secrets in your browser. Each secret is encrypted to its own post-quantum key on your OnlyKey, so reading it needs your OnlyKey, and the vault stores nothing your browser could read on its own.

You can also open it from the OnlyKey App: **Tools › Password Vault**.

:::note
**Requirements:** OnlyKey firmware 3.1.0 or later ([Upgrade Guide](/upgradeguide)), and [Webcrypt Access](/user-input-modes#webcrypt-access) set to anything but **Off**. The vault uses derived keys only, so **Derived keys only** works.
:::

## How it works {#how-it-works}

- **One key per secret.** For each service name, the OnlyKey derives an X-Wing key pair (ML-KEM-768 + X25519) from its web-derivation key and the label `vault:` plus the service name. Nothing is stored on the OnlyKey, and the private key never leaves it.
- **Each secret is an age file.** The page encrypts the secret to that key as a standard [age](/age) file: X-Wing wraps a random file key, and the secret is encrypted with ChaCha20-Poly1305.
- **Only ciphertext is stored, in this browser.** The age files are kept in the browser's IndexedDB storage for apps.onlykey.io. Nothing is sent to a server.
- **Unlocking needs the OnlyKey.** To read a secret, the page sends the file's X-Wing ciphertext to the OnlyKey over the [encrypted connection](/webcrypt#transit-v2). The OnlyKey decapsulates it and returns the shared secret only after you confirm.

## Store a secret {#store}

:::callout
**Step 1.** Plug in and unlock your OnlyKey, then open [apps.onlykey.io/app/vault](https://apps.onlykey.io/app/vault).
:::

:::callout
**Step 2.** Enter a service name (for example `github`) and the secret.
:::

:::callout
**Step 3.** Select **Encrypt & Store with OnlyKey**. Getting the public key needs no button press. The page shows the age file it saved; it is safe to copy, commit or share, because only your OnlyKey can open it.
:::

## Read a secret {#unlock}

:::callout
**Step 1.** Find the entry under **Stored credentials** and choose to unlock it.
:::

:::callout
**Step 2.** Confirm on the OnlyKey. Tap any button, or if your OnlyKey is set to challenge-code mode, press the three buttons the page shows, in order.
:::

Choose how long an unlocked entry stays open:

- **Unlock with OnlyKey every use**
- **Session: 30 minutes**
- **Session: 8 hours**
- **Session: until page closes**

Unlocked entries are kept in memory only. **Lock all sessions** closes them at once, as does closing the page.

How you confirm is set by the **Web and agent derived keys** [user input mode](/user-input-modes). With **None (no confirmation)**, the vault opens entries without a button press whenever the OnlyKey is unlocked.

## Back up and move your vault {#backup}

:::warning "⚠️ Export your vault"
The vault lives in this browser's storage. Clearing your browsing data for apps.onlykey.io, or using a different browser or computer, leaves you without your entries unless you have exported them.
:::

- **Export vault (JSON)** saves every entry as a file you can keep anywhere. It holds only age files, so it is safe to store in a cloud folder.
- **Import vault** loads an export into another browser.

The same OnlyKey and service name always give the same key pair. An exported vault therefore opens on any computer with that OnlyKey, or with an OnlyKey restored from its [backup](/usersguide#secure-encrypted-backup-anywhere).

## Open a vault entry on the command line {#command-line}

Every entry is an ordinary age file, so you can open it without the browser. **Copy age file** and **Copy age identity** give you the file and the identity line for that entry. With [age-plugin-onlykey](/age#install) installed:

```
$ age -d -i github-identity.txt github.age
```

The identity is the same as `age-plugin-onlykey --derived --label vault:github --identity`.

## Related pages {#related}

- [age with OnlyKey](/age)
- [Post-quantum keys](/pqc)
- [OnlyKey web app](/webcrypt)
- [User input modes and Webcrypt Access](/user-input-modes)
