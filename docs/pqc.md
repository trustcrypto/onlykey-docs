---
title: Post-Quantum Keys
description: Store and use post-quantum keys on OnlyKey - ML-KEM-768 and X-Wing keys, and composite post-quantum OpenPGP keys. Requires firmware 3.1.0.
slug: pqc
last_updated: Nov, 25, 2026
keywords: OnlyKey, post-quantum, PQC, ML-KEM, ML-DSA, X-Wing, OpenPGP, age
---

# Post-Quantum Keys

Firmware 3.1.0 adds post-quantum keys to OnlyKey. They are designed to keep what you encrypt today safe even against a future quantum computer, and like every other OnlyKey key, the private half never leaves the device.

OnlyKey supports four kinds:

| Key | Where it lives | What it does | Made by | Used with |
| --- | --- | --- | --- | --- |
| **X-Wing** (ML-KEM-768 + X25519) | An ECC slot (ECC1-ECC16) | Decryption | The OnlyKey itself, or loaded | [age](/age) with a stored key |
| **ML-KEM-768** | An ECC slot (ECC1-ECC16) | Decryption | The OnlyKey itself, or loaded | Your own tools, through the python-onlykey library |
| **Composite PQC OpenPGP key** (ML-DSA-65 + Ed25519 signing, ML-KEM-768 + X25519 encryption) | A PQC slot (PQC1-PQC4) | Signing and decryption | Made off the device, then loaded | The [web app](/webcrypt#pqc-pgp) and onlykey-cli |
| **Derived X-Wing** | Nothing is stored | Decryption | Derived on demand from a label | [age](/age), the [web app's age pages](/webcrypt#age) and the [Password Vault](/vault) |

Derived X-Wing keys need no setup at all, so most people start there: see [age with OnlyKey](/age).

:::note
**Requirements:** OnlyKey firmware 3.1.0 or later ([Upgrade Guide](/upgradeguide)), and for the command line [python-onlykey](/command-line) 1.3.1 or later (Python 3.10 or newer). Writing a key to the device requires [config mode](/user-input-modes#config-mode).
:::

## Why hybrid keys {#why-hybrid}

Every post-quantum key on OnlyKey except the plain ML-KEM-768 key pairs a post-quantum algorithm with a classic elliptic-curve one. An attacker has to break both to read your data, so a hybrid key is no weaker than the classic key you use today, and stays safe if a quantum computer breaks the classic half.

- **ML-KEM-768** is the NIST post-quantum key-encapsulation standard (FIPS 203).
- **ML-DSA-65** is the NIST post-quantum signature standard (FIPS 204).
- **X-Wing** combines ML-KEM-768 and X25519 into one key, as specified in [draft-connolly-cfrg-xwing-kem](https://datatracker.ietf.org/doc/draft-connolly-cfrg-xwing-kem/). It is the key type age uses for its post-quantum recipients.
- **Composite OpenPGP keys** follow [RFC 9980](https://www.rfc-editor.org/rfc/rfc9980), Post-Quantum Cryptography in OpenPGP: algorithm 30 (ML-DSA-65+Ed25519) for signing and algorithm 35 (ML-KEM-768+X25519) for encryption.

## ML-KEM-768 and X-Wing keys in ECC slots {#ecc-slot-keys}

An ML-KEM-768 or X-Wing key uses one of the 16 ECC slots (ECC1-ECC16), the same slots that hold Ed25519, NIST P-256 and secp256k1 keys. The slot stores only the key's seed; the full key is expanded from it each time it is used. These keys decrypt only.

### Generate a key on the OnlyKey {#generate}

The OnlyKey can create the key itself, so the private key never exists anywhere else.

:::callout
**Step 1.** Put the OnlyKey into [config mode](/user-input-modes#config-mode).
:::

:::callout
**Step 2.** Generate the key. `w` is X-Wing and `m` is ML-KEM-768; `d` marks it for decryption.

```
$ onlykey-cli genkey ECC1 w d
$ onlykey-cli genkey ECC2 m d
```

onlykey-cli prints the public key as hex.
:::

:::callout
**Step 3.** (Optional) Give the slot a label so you can tell the keys apart:

```
$ onlykey-cli setkey ECC1 label "age X-Wing key"
```
:::

To use an X-Wing key with age, generate it with `age-plugin-onlykey --generate` instead, which also writes the identity file age needs. See [age with a stored key](/age#stored-keys).

### Load an existing key {#load}

To load a key you already have, give onlykey-cli its seed in hex: 32 bytes for X-Wing, 64 bytes (d‖z) for ML-KEM-768.

```
$ onlykey-cli setkey ECC1 w d <64 hex characters>
$ onlykey-cli setkey ECC2 m d <128 hex characters>
```

:::warning "⚠️ Warning"
A key loaded from your computer has existed outside the OnlyKey. Delete the seed from your computer once it is loaded and backed up.
:::

### Use an ECC-slot key {#use-ecc}

- **X-Wing:** encrypt and decrypt files with [age](/age#stored-keys).
- **ML-KEM-768:** for developers building their own tools. The python-onlykey library (`onlykey.age_plugin.onlykey_hid.OnlyKeyPQ`) can read the public key and ask the OnlyKey to decapsulate an ML-KEM-768 ciphertext. age uses X-Wing, not plain ML-KEM-768.

Each use asks you to confirm on the OnlyKey, as set by the **stored keys** [user input mode](/user-input-modes).

## Composite post-quantum OpenPGP keys {#composite-pgp}

A composite PQC OpenPGP key is a complete OpenPGP key whose signing key is ML-DSA-65+Ed25519 and whose encryption subkey is ML-KEM-768+X25519. OnlyKey holds up to four, in slots **PQC1-PQC4**.

:::note
PQC1-PQC4 are the same four slots as RSA1-RSA4. Each slot holds either an RSA key or a composite key. onlykey-cli uses the PQC name for composite keys and refuses to mix them up.
:::

### Create the key {#create-composite}

OnlyKey cannot generate a composite key, so you create it on your computer and then load it. Both ways below make a key that onlykey-cli 1.3.1 loads and that other RFC 9980 software, such as rPGP, can encrypt to and verify.

::: tabs

== tab OpenPGP.js (recommended)

python-onlykey already includes the OpenPGP.js build that `loadpqc` uses to read key files, and it can also create composite keys. The [make-pqc-key.js](/assets/make-pqc-key.js) script uses it, so you need nothing beyond what `loadpqc` already needs: python-onlykey 1.3.1 or newer and [Node.js](https://nodejs.org) 18 or newer.

:::callout
**Step 1.** Download [make-pqc-key.js](/assets/make-pqc-key.js).
:::

:::callout
**Step 2.** Run it with your name and email address. It asks for a passphrase twice; the passphrase protects the private key file.

```
$ node make-pqc-key.js "Your Name" you@example.com
Passphrase for the private key:
Repeat the passphrase:
Fingerprint: 1C5227B0F12EAAC82F269472222BE5E84817091F6851CFBAB8FF923D6B11044F
Wrote you@example.com-pqc-secret.asc (private key: load it with onlykey-cli loadpqc)
Wrote you@example.com-pqc-public.asc (public key: share it, and keep a copy)
```
:::

== tab rsop

[rsop](https://codeberg.org/heiko/rsop) 0.12 or newer, a command-line OpenPGP tool built on rPGP, also creates the key. Install it with `cargo install rsop` (this needs [Rust](https://rustup.rs)). Packaged versions can be older: `rsop version --extended` must list `pqc: yes`.

Put the passphrase in a file, then run:

```
$ rsop generate-key --profile security --with-key-password passphrase.txt "Your Name <you@example.com>" > you-pqc-secret.asc
$ rsop extract-cert < you-pqc-secret.asc > you-pqc-public.asc
$ rm passphrase.txt
```

The `security` profile makes the key OnlyKey needs.

:::

**Other OpenPGP software** that supports RFC 9980 works if the key has this layout:

- a v6 key with an **ML-DSA-65+Ed25519** primary key, and
- an **ML-KEM-768+X25519** encryption subkey as its **first** subkey.

onlykey-cli 1.3.1 reads only the first subkey, so a key that has another subkey (for signing or authentication) before the encryption subkey does not load.

:::warning "⚠️ Keep your public key"
The OnlyKey cannot give your composite public key back once the private key is loaded. Keep the public key file; you need it to receive messages and to verify your signatures.
:::

:::note
**GnuPG cannot create or use these keys.** GnuPG follows a different post-quantum format (LibrePGP) and does not read OpenPGP v6 keys, so composite keys work with OnlyKey through the web app and onlykey-cli, not through GnuPG or onlykey-agent. See [onlykey-agent and post-quantum keys](/onlykey-agent#pqc).
:::

### Load the key onto OnlyKey {#loadpqc}

`loadpqc` is the only way a composite key reaches the device. The browser never writes private keys to an OnlyKey.

:::callout
**Step 1.** Install [Node.js](https://nodejs.org) and make sure `node` is on your PATH. onlykey-cli uses it to read the key file.
:::

:::callout
**Step 2.** Put the OnlyKey into [config mode](/user-input-modes#config-mode).
:::

:::callout
**Step 3.** Load the private key file into a PQC slot, with its passphrase as the last argument. On macOS and Linux, `read -rs` reads the passphrase without showing it or saving it in your shell history:

```
$ read -rs PQC_PASS
$ onlykey-cli loadpqc you@example.com-pqc-secret.asc PQC1 "$PQC_PASS"
Loaded composite PQC PGP key from you@example.com-pqc-secret.asc (160 bytes) into PQC1
$ unset PQC_PASS
```

You can also type the passphrase directly in the command, but it is then saved in your shell history.
:::

:::callout
**Step 4.** Create a new [backup](/usersguide#secure-encrypted-backup-anywhere). Composite keys are included in OnlyKey backups. Then delete the private key file from your computer, or move it somewhere offline. Keep the public key file.
:::

The device stores the four private seeds of the key (160 bytes). If you already have them as a raw blob, `onlykey-cli setkey PQC1 p <320 hex characters>` loads it directly.

### Use a composite key {#use-composite}

**In the web app.** Open [apps.onlykey.io](https://apps.onlykey.io), go to **Encrypt** or **Decrypt**, and choose **PQC-PGP**:

- **Encrypt** to someone's composite public key: paste their armored public key and your message. Encryption needs only their public key, so the OnlyKey is not involved.
- **Sign** a message with the key in your PQC slot: choose the slot (1-4) and confirm on the OnlyKey.
- **Decrypt** a message sent to you: paste your public key and the message, choose the slot, and confirm on the OnlyKey.
- **Verify** a signed message: paste the signer's public key. This runs in the browser only.

The web app can use stored keys only if [Webcrypt Access](/user-input-modes#webcrypt-access) allows it, which it does by default.

**On the command line.** `onlykey-cli signpqc` and `decryptpqc` run one half of a composite operation on the device (the Ed25519 or ML-DSA-65 signature, or the X25519 or ML-KEM-768 decapsulation). They are building blocks for scripts and other OpenPGP software, not a replacement for a PGP program. See [Key Config Options](/command-line#signpqc).

Each use asks you to confirm on the OnlyKey, as set by the **stored keys** [user input mode](/user-input-modes).

## See which keys are on your OnlyKey {#check}

`onlykey-cli getkeylabels` lists the labels of the key slots (PQC1-PQC4 appear as RSA Key 1-4). `onlykey-cli capabilities` shows whether your firmware supports post-quantum keys (the `PQC` flag) and which key types it accepts.

## Related pages {#related}

- [age with OnlyKey](/age) - post-quantum file encryption, derived or stored keys
- [Password Vault](/vault) - secrets stored as age files to derived X-Wing keys
- [User input modes and Webcrypt Access](/user-input-modes) - how each key is confirmed
- [Command-line utility](/command-line) - every onlykey-cli command
