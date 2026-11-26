---
title: age with OnlyKey
description: Encrypt and decrypt files with age, rage and typage using a post-quantum X-Wing key on your OnlyKey - derived from a label or stored on the device.
slug: age
last_updated: Nov, 25, 2026
keywords: OnlyKey, age, rage, typage, post-quantum, X-Wing, ML-KEM, age-plugin-onlykey
---

# age with OnlyKey

[age](https://age-encryption.org) is a simple, modern file encryption tool. With firmware 3.1.0, OnlyKey can hold the key that decrypts your age files. The key is a post-quantum hybrid X-Wing key (ML-KEM-768 + X25519), the same kind age 1.3 uses for its own post-quantum recipients, and its private half never leaves the OnlyKey.

Files you encrypt this way are standard age files. They open with age, rage and typage, and with the [OnlyKey web app](/webcrypt#age).

:::note
**Requirements:** OnlyKey firmware 3.1.0 or later ([Upgrade Guide](/upgradeguide)) and python-onlykey 1.3.1 or later, which needs Python 3.10 or newer. To decrypt you also need an age tool that supports plugins: age 1.1 or later, or rage.
:::

## Choose a key: derived or stored {#derived-or-stored}

| | Derived key | Stored key |
| --- | --- | --- |
| **What it is** | Derived on demand from a label you choose, such as `work` or your email address | An X-Wing key generated in an ECC slot (ECC1-ECC16) |
| **Setup** | None | Generate it once, in config mode |
| **Backup** | Nothing extra: the same OnlyKey (or one restored from its backup) and the same label give the same key | Included in your OnlyKey backup |
| **How many** | As many as you have labels | Up to 16, one per ECC slot |
| **Same key in the web app** | Yes, with the same label | No |
| **Confirmation setting** | Web and agent derived keys | Stored keys |

Most people should use a **derived** key. Use a stored key if you want a key that is not tied to a label, or to keep age keys in specific slots.

## Install age-plugin-onlykey {#install}

age-plugin-onlykey comes with python-onlykey. Install it with the `age` extra:

```
$ pip3 install "onlykey[age]"
```

:::note
**Intel Macs:** install `cryptography` version 48 or older first, then python-onlykey:

```
$ pip3 install "cryptography<49"
$ pip3 install "onlykey[age]"
```
:::

The plugin must be on your PATH, because age finds it by name. Check with:

```
$ age-plugin-onlykey --version
```

On Linux, also install the [OnlyKey udev rule](/linux).

## Use a derived key {#derived-keys}

:::callout
**Step 1.** Pick a label and save an identity file for it. The label can be any text; the same label always gives the same key.

```
$ age-plugin-onlykey --derived --label work --generate > work-identity.txt
```

The file contains the identity line age needs, plus the key's recipient in two spellings as comments. Nothing is written to the OnlyKey.
:::

:::callout
**Step 2.** Get the recipient (the public key) to encrypt to:

```
$ age-plugin-onlykey --derived --label work --recipient --native > work-recipient.txt
```

`--native` prints the standard `age1pq1…` recipient, which age 1.3, typage, and rage or older age with `age-plugin-pq` encrypt to **without** age-plugin-onlykey installed. Without `--native` you get an `age1onlykey1…` recipient, which needs the plugin to encrypt. Both are the same key. Post-quantum recipients are about 2,000 characters long, so keep them in a file.
:::

:::callout
**Step 3.** Encrypt a file:

```
$ age -R work-recipient.txt -o report.pdf.age report.pdf
```

Anyone can do this step with your recipient; the OnlyKey is not needed to encrypt.
:::

:::callout
**Step 4.** Decrypt it. Plug in and unlock your OnlyKey, run age with the identity file, and confirm on the OnlyKey when asked:

```
$ age -d -i work-identity.txt -o report.pdf report.pdf.age
Confirm on OnlyKey: press any button, or if it is set to challenge-code mode enter 3 1 5
```
:::

## Use a stored key {#stored-keys}

:::warning "⚠️ Warning"
Generating a stored key **replaces any key already in that slot**. The default is ECC1; choose another slot with `--slot` (101-116 are ECC1-ECC16).
:::

:::callout
**Step 1.** Put the OnlyKey into [config mode](/user-input-modes#config-mode).
:::

:::callout
**Step 2.** Generate the key on the OnlyKey and save the identity file:

```
$ age-plugin-onlykey --generate --slot 101 > onlykey-identity.txt
```
:::

:::callout
**Step 3.** Remove and reinsert the OnlyKey to leave config mode, unlock it, and get the recipient:

```
$ age-plugin-onlykey --recipient --slot 101 --native > onlykey-recipient.txt
```
:::

:::callout
**Step 4.** Encrypt and decrypt as for a derived key:

```
$ age -R onlykey-recipient.txt -o secret.txt.age secret.txt
$ age -d -i onlykey-identity.txt -o secret.txt secret.txt.age
```
:::

Make a new [backup](/usersguide#secure-encrypted-backup-anywhere) after generating a stored key.

## Confirming on the OnlyKey {#confirm}

Every decryption asks you to confirm on the OnlyKey. How depends on the [user input mode](/user-input-modes):

- **Derived keys** follow the **Web and agent derived keys** setting: button press (default), challenge code, or no press.
- **Stored keys** follow the **Stored keys** setting: button press or challenge code.

The plugin always prints the three-digit challenge code with its prompt, because a key in challenge-code mode shows nothing on the device itself. Enter the digits on the OnlyKey within 20 seconds.

:::tip "💡 Pro Tip"
For unattended scripts that decrypt with derived keys, set **Web and agent derived keys** to **None (no confirmation)**. While it is set, the web app can also decrypt with derived keys without a press whenever the OnlyKey is unlocked, so leave it off unless you need it.
:::

## Compatibility {#compatibility}

The plugin writes and reads standard age v1 files with `mlkem768x25519` recipient stanzas, as defined in the [age specification](https://github.com/C2SP/C2SP/blob/main/age.md). Tested with age 1.3.2 and 1.1.1, rage 0.12.1 and typage 0.3.1.

| Tool | Encrypt to your OnlyKey | Decrypt with your OnlyKey |
| --- | --- | --- |
| age 1.3 or later | Yes, with the `age1pq1…` recipient (no plugin) or the `age1onlykey1…` recipient (plugin) | Yes, with age-plugin-onlykey |
| age 1.1 or 1.2 | Yes, with the `age1onlykey1…` recipient, or with `age-plugin-pq` for `age1pq1…` | Yes, with age-plugin-onlykey |
| rage | Yes, with the plugin, or with `age-plugin-pq` | Yes, with age-plugin-onlykey |
| typage (JavaScript) | Yes, with the `age1pq1…` recipient | No: typage has no plugins. Use the [OnlyKey web app](/webcrypt#age) |
| OnlyKey web app | Yes, derived keys | Yes, derived keys |

:::note
age does not let a file mix post-quantum and classic recipients, because that would defeat the post-quantum protection. Encrypt to other people's post-quantum (`age1pq1…`) recipients alongside yours, or make a separate file for classic recipients.
:::

## In the web app {#web-app}

The [web app](/webcrypt#age) at [apps.onlykey.io](https://apps.onlykey.io) has **Encrypt › AGE** and **Decrypt › AGE** pages for derived keys:

1. Enter the label. The page shows the identity line and the `age1pq1…` recipient for it, the same as `age-plugin-onlykey --derived --label …` gives.
2. To encrypt, type the text and select **Encrypt**. The page writes an ASCII-armored age file.
3. To decrypt, paste an armored age file and select **Decrypt**, then confirm on the OnlyKey.

The web app can use derived keys unless [Webcrypt Access](/user-input-modes#webcrypt-access) is set to **Off**.

A file encrypted on the command line opens in the web app with the same label, and the other way around. Armored files open in age, rage and typage as they are.

## Good to know {#notes}

- **The identity file is not a secret key.** It only tells the plugin which OnlyKey key to use: the slot for a stored key, or the label for a derived key. Without your OnlyKey and its PIN it decrypts nothing. A derived identity does contain the label text, so pick labels you don't mind others seeing.
- **The label is the key.** A different label, or a single changed character, gives a different key. Write your labels down.
- **The [Password Vault](/vault) uses the same derived keys**, with the label `vault:` followed by the service name.
- **Windows:** use python-onlykey 1.3.1 or later; earlier versions wrote line endings age rejects.

## Related pages {#related}

- [Post-quantum keys](/pqc) - every post-quantum key type OnlyKey supports
- [Password Vault](/vault)
- [User input modes and Webcrypt Access](/user-input-modes)
- [age](https://age-encryption.org), [rage](https://github.com/str4d/rage), [typage](https://github.com/FiloSottile/typage)
