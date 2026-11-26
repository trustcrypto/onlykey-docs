---
title: OnlyKey WebCrypt (Web App)
description: Encrypt, decrypt and sign messages and files in your browser with OnlyKey - PGP, post-quantum PGP, age and the Password Vault. Web app 4.0 at apps.onlykey.io.
slug: webcrypt
last_updated: Nov, 25, 2026
keywords: OnlyKey, WebCrypt, web app, OpenPGP, PGP, age, post-quantum, Vault, Keybase, Protonmail
---

# OnlyKey WebCrypt (Web App)

## About

OnlyKey WebCrypt is the OnlyKey web app. It encrypts, decrypts and signs messages and files directly in your browser, with the private keys kept on your OnlyKey. Nothing you encrypt is sent over the Internet: the page runs entirely in your browser and talks to the OnlyKey over USB through FIDO2, so no drivers or software are needed.

Web app 4.0 adds post-quantum encryption with [age](#age) and [composite PQC PGP keys](#pqc-pgp), a [Password Vault](/vault), and an [encrypted, authenticated connection](#transit-v2) to the OnlyKey.

## Which site to use {#which-site}

| Your OnlyKey firmware | Web app |
| --- | --- |
| **3.1.0 or later** | [apps.onlykey.io](https://apps.onlykey.io) |
| **3.0.4 or older** | [apps.crp.to](https://apps.crp.to) |

A key on firmware 3.0.4 or older cannot answer on apps.onlykey.io. The page then says that no OnlyKey is connected and links to apps.crp.to. To upgrade, see the [Upgrade Guide](/upgradeguide).

The OnlyKey App's **Tools** tab opens these pages on apps.onlykey.io.

## What the web app can do {#pages}

| Page | What it does |
| --- | --- |
| [Encrypt › Message](https://apps.onlykey.io/app/encrypt) and [Decrypt › Message](https://apps.onlykey.io/app/decrypt) | PGP messages with the keys stored on your OnlyKey |
| [Encrypt › File](https://apps.onlykey.io/app/encrypt-file) and [Decrypt › File](https://apps.onlykey.io/app/decrypt-file) | PGP files |
| [Encrypt › PQC-PGP](https://apps.onlykey.io/app/pqc-encrypt) and [Decrypt › PQC-PGP](https://apps.onlykey.io/app/pqc-decrypt) | Messages with composite post-quantum PGP keys |
| [Encrypt › AGE](https://apps.onlykey.io/app/age-encrypt) and [Decrypt › AGE](https://apps.onlykey.io/app/age-decrypt) | age files with derived post-quantum keys |
| [Search](https://apps.onlykey.io/app/search) | Find a Keybase user or Protonmail address to send to |
| [Vault](https://apps.onlykey.io/app/vault) | The [Password Vault](/vault) |
| Home page: **Set Time for OTP 2FA** | Sets the OnlyKey's clock so it can generate TOTP codes when the OnlyKey App is not running |

The web app works in desktop and mobile browsers that support FIDO2 security keys. See [Mobile](/mobile) for phones and tablets.

## PGP with keys stored on OnlyKey {#openpgp-action}

WebCrypt works with [Keybase](https://keybase.io) and [Protonmail](https://proton.me) to find other people's public keys, so you can encrypt to someone by name. Your own PGP key must be loaded onto the OnlyKey first; see [OpenPGP Keys](/importpgp#generating-keys).

### Send an encrypted message or file {#send}

:::callout
**Step 1.** Find the recipient: open [Search](https://apps.onlykey.io/app/search) and look up their Keybase username or Protonmail address, then follow the link in the results. Or go straight to [Encrypt › Message](https://apps.onlykey.io/app/encrypt) or [Encrypt › File](https://apps.onlykey.io/app/encrypt-file).
:::

:::callout
**Step 2.** Enter the recipient's Keybase username or Protonmail address, or paste their public key. Several recipients are supported.
:::

:::callout
**Step 3.** To sign, enter your own Keybase username or Protonmail address and choose **Encrypt and Sign** (or **Sign Only**). Under **Key slot**, leave **Auto** or pick the RSA or ECC slot that holds your key.
:::

:::callout
**Step 4.** Enter the message or choose the file, then select **Encrypt and Sign**. If you are signing, confirm on the OnlyKey when asked.
:::

Paste the encrypted message into an email, chat or anywhere else.

### Receive an encrypted message or file {#receive}

:::callout
**Step 1.** Open [Decrypt › Message](https://apps.onlykey.io/app/decrypt) or [Decrypt › File](https://apps.onlykey.io/app/decrypt-file).
:::

:::callout
**Step 2.** Enter the sender's Keybase username or Protonmail address to verify the signature, or choose **Decrypt Only**. Under **Key slot**, leave **Auto** or pick the slot that holds your key.
:::

:::callout
**Step 3.** Paste the message or choose the file (usually ending in `.gpg`), select **Decrypt and Verify**, and confirm on the OnlyKey.
:::

A decrypted file downloads automatically.

The web app reads messages encrypted with OCB, messages to NIST-curve ECC keys, and keys made by GnuPG 2.4 and 2.5.

:::tip "💡 Pro Tip"
You can let anyone send you encrypted messages by putting a link in your email signature:

*Send me a secure [message](https://apps.onlykey.io/app/encrypt?type=e&recipients=bobsmith2) or [file](https://apps.onlykey.io/app/encrypt-file?type=e&recipients=bobsmith2)*

Replace `bobsmith2` with your Keybase username. The page can also make the link for you: **Get and Copy Share Link**.
:::

## Post-quantum PGP {#pqc-pgp}

The **PQC-PGP** pages use composite post-quantum OpenPGP keys (ML-DSA-65 + Ed25519 signing, ML-KEM-768 + X25519 encryption). The private key must already be loaded on your OnlyKey with `onlykey-cli loadpqc`; the browser never writes private keys. The web app does not create composite keys either: the Decrypt page still mentions a key generator on the Encrypt page, but there is none. To create a key, see [Create the key](/pqc#create-composite).

- **Encrypt:** paste the recipient's armored composite public key and your message. Encrypting needs only their public key.
- **Sign:** choose the PQC slot (1-4) that holds your key and confirm on the OnlyKey.
- **Decrypt:** paste your public key and the encrypted message, choose your PQC slot, and confirm on the OnlyKey.
- **Verify:** paste the signer's public key and the signed message. This runs in the browser only.

## age {#age}

The **AGE** pages encrypt and decrypt with a post-quantum X-Wing key that the OnlyKey derives from a label you choose. Nothing is stored on the OnlyKey, and the same label gives the same key here and in [age-plugin-onlykey](/age).

:::callout
**Step 1.** Open [Encrypt › AGE](https://apps.onlykey.io/app/age-encrypt) and enter a label, such as your email address. The page shows the identity line and the `age1pq1…` recipient for that label.
:::

:::callout
**Step 2.** Type your text and select **Encrypt**. The page writes an ASCII-armored age file.
:::

:::callout
**Step 3.** To read it, open [Decrypt › AGE](https://apps.onlykey.io/app/age-decrypt), enter the same label, paste the age file, select **Decrypt** and confirm on the OnlyKey.
:::

The files open with age, rage and typage, and files they write open here. Give the `age1pq1…` recipient to anyone who wants to send you files: age 1.3 and typage encrypt to it with no plugin. See [age with OnlyKey](/age) for the command line.

## Password Vault {#vault}

The [Password Vault](/vault) keeps secrets in your browser, each encrypted to its own derived post-quantum key on the OnlyKey.

## Confirming on the OnlyKey {#confirm}

Operations that use a key ask you to confirm on the OnlyKey: tap any button, or if your OnlyKey is set to challenge-code mode, press the three buttons the page shows, in order. Stored PGP keys follow the **Stored keys** setting and the age pages and Vault follow **Web and agent derived keys**. See [User input modes](/user-input-modes).

If the OnlyKey refuses an operation or the time runs out, the page shows the OnlyKey's own message.

## What the web app may use {#webcrypt-access}

**Webcrypt Access** (firmware 3.1.0) controls what the web app may do with your OnlyKey:

- **Stored and derived keys** (default): PGP with stored keys, PQC-PGP, age and the Vault.
- **Derived keys only:** age and the Vault. Stored PGP keys are out of the web app's reach.
- **Off:** the web app cannot reach the OnlyKey at all.

If stored-key use is not allowed, the PGP pages say so and show how to enable it. To change the setting, see [Webcrypt Access](/user-input-modes#webcrypt-access).

## Benefits

### Universal Support

This is accomplished by using the FIDO2 communication channel to communicate with a USB hardware device. The universal support for FIDO2 allows the web application to be used anywhere FIDO2 is supported including browsers on Android, iPhone (iOS 13.3+), Windows, Mac OS, Linux, and Chromebook. The web app can also be released as a native app that does not require a web browser if this is preferred. [More information on Android/iOS support](/mobile)

### Key Management

In addition to universal support, OnlyKey WebCrypt works with Keybase and Protonmail for easy user key management. Key management is one of the most difficult issues to solve when it comes to encrypting messages and files.

### Better than a PGP key server

The first step in secure communication is often finding the person to communicate with and having assurance that it is them. By identifying users from their Keybase registered social media profiles, domains, PGP fingerprints, or known Protonmail email address, this provides higher assurance of user identity than use of traditional PGP key servers.

### Better than a Smart Card

Smart cards are a popular way for enterprises to keep cryptographic keys protected but they are not known for being easy to use and are definitely not universally supported. OnlyKey provides similar function to a token/smart card but no drivers or software is required. Additionally, physical user presence is required to process secure messages/files. This is in contrast to Smart cards which only require a PIN code that can in some cases be captured and replayed without physical user presence resulting in security compromise.

### Better than OpenPGP  

OpenPGP is widely used but not known for being easy to use. There have been efforts such as Keybase and Protonmail that make OpenPGP easier to use but require that private keys are accessible in software or the cloud. This means that in some cases user’s OpenPGP keys may be compromised by phishing attacks, malware, or software vulnerabilities. OnlyKey WebCrypt supports OpenPGP keys that are compatible with Protonmail, Keybase, Mailvelope, GPG, and others while allowing users to securely keep their keys offline and protected.

## Security Goals {#security-goals}

**Make encryption easy**: you shouldn't have to be technologically savvy to use PGP or age, or worry that malware on your computer could expose your private keys.

**Keys stay on the OnlyKey**: private keys are never sent to the browser. The page sends the OnlyKey what it needs to sign or decrypt, and the OnlyKey returns only the result after you confirm.

**Serverless**: all encryption and decryption runs in your own browser. Your messages, files and Vault entries are never sent to a server.

**Private**: no logins, no data retention, no tracking, no ads.

**Encrypted connection to the OnlyKey**: every message between the page and the OnlyKey is encrypted and authenticated. See [transit v2](#transit-v2).

**Phishing prevention**: the OnlyKey answers the WebCrypt extension only on apps.onlykey.io and apps.crp.to. The list is built into the firmware, so other websites cannot use it.

**Open source and auditable**: the source is on [GitHub](https://github.com/trustcrypto/apps.onlykey.io).

## Societal Impact Goals {#society-goals}

The issues solved by OnlyKey WebCrypt are issues that affect many at-risk communities such as human rights
activists and journalists.

### Universal support
Many journalists may travel and may have to make do with whatever internet connection that is available such as using a shared computer or a mobile device. OnlyKey WebCrypt does not require installing software, all that is needed is a USB port, a common web browser (i.e. Chrome, Firefox), and an internet connection.

### Ease of Use
It is often the case that secure solutions are not adopted not because of lack of availability but that they require considerable technical skills. For example, installing smart card software may require command line utilities and a high level of technical proficiency. At-risk communities may not have the technical proficiency to do this, with OnlyKey there are no commands necessary, setup is as easy as following step by step directions to generate a private key on Keybase and load onto the OnlyKey. This opens up the solution to a much wider range of at-risk communities.

### Post-quantum protection
Messages and files that need to stay private for years can be encrypted with [post-quantum keys](/pqc), designed to resist future quantum computers, using the age and PQC-PGP pages.

## Technical Specs {#technical-specs}

### Communication channel {#communication-channel}

The web app talks to the OnlyKey through the FIDO2 (WebAuthn) API that browsers already provide. Requests are carried inside FIDO2 authentication requests and replies inside FIDO2 responses, through an OnlyKey extension that the firmware answers only for apps.onlykey.io and apps.crp.to. Ordinary FIDO2 sign-in to websites is separate and is not affected.

FIDO2 itself does not encrypt data between the browser and a security key, so any program that can read USB traffic could read it. WebCrypt adds its own encryption on top.

### Transit encryption v2 {#transit-v2}

With firmware 3.1.0 and web app 4.0, every message between the page and the OnlyKey is encrypted and authenticated:

1. **Connect.** The page and the OnlyKey each make a new X25519 key pair for the session and exchange public keys. The OnlyKey also reports its firmware version and sets its clock.
2. **Session key.** Both sides compute the X25519 shared secret and hash it with SHA-256 to get a 256-bit AES key. The private halves are discarded.
3. **Every message** is encrypted with AES-256-GCM under the session key. The IV is built from the message direction and a message counter, each frame carries its counter, and the 16-byte authentication tag is checked before anything is used.
4. **Replays are refused.** A frame whose counter goes backwards, or whose tag does not verify, is discarded.

Older firmware used an earlier version of this channel, which the web app at apps.crp.to still speaks.

## Licenses

Thanks to http://tilomitra.github.io/prettypages/

Copyright 2012 Yahoo! Inc. All rights reserved. Licensed under the BSD License. http://yuilibrary.com/license/

Thanks to Ron Garret for originally posting a serverless implementation of U2F here - https://github.com/rongarret/u2f-test

The MIT License (MIT)
Copyright (c) 2019 CryptoTrust LLC.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Cryptography Notice

This distribution includes cryptographic software. The country in which you currently reside may have restrictions on the import, possession, use, and/or re-export to another country, of encryption software.
BEFORE using any encryption software, please check your country's laws, regulations and policies concerning the import, possession, or use, and re-export of encryption software, to see if this is permitted.
See <https://www.wassenaar.org/> for more information.

The U.S. Government Department of Commerce, Bureau of Industry and Security (BIS), has classified this software as Export Commodity Control Number (ECCN) 5D002.C.1, which includes information security software using or performing cryptographic functions with asymmetric algorithms.
The form and manner of this distribution makes it eligible for export under the License Exception ENC Technology Software Unrestricted (TSU) exception (see the BIS Export Administration Regulations, Section 740.13) for both object code and source code.

The following cryptographic software is included in this distribution:

   "OpenPGP.js" - https://github.com/openpgpjs/openpgpjs
   "noble-post-quantum" - https://github.com/paulmillr/noble-post-quantum
   "noble-curves" - https://github.com/paulmillr/noble-curves
   "noble-hashes" - https://github.com/paulmillr/noble-hashes
   "RFC4880 Implementation in IcedCoffeeScript" - https://github.com/keybase/kbpgp
   "Port of TweetNaCl cryptographic library to JavaScript" - https://github.com/dchest/tweetnacl-js
   "A native implementation of TLS in Javascript and tools to write crypto-based and network-heavy webapps" - https://github.com/digitalbazaar/forge

For more information on export restrictions see: https://www.apache.org/licenses/exports/

## Source

- [Web app 4.0 (apps.onlykey.io) on GitHub](https://github.com/trustcrypto/apps.onlykey.io)
- [Web app for firmware 3.0.4 and older (apps.crp.to) on GitHub](https://github.com/onlykey/onlykey.github.io)
