---
title: User Input Modes and Webcrypt Access
description: Choose how OnlyKey asks you to confirm each kind of key operation, and what the OnlyKey web app may use. Firmware 3.1.0 settings, set in the OnlyKey App or onlykey-cli.
slug: user-input-modes
last_updated: Nov, 25, 2026
keywords: OnlyKey, user input mode, challenge code, button press, webcrypt policy, config mode, settings
---

# User Input Modes and Webcrypt Access

When a computer asks OnlyKey to sign, decrypt or derive a key, OnlyKey waits for you to confirm on the device. **User input modes** choose how you confirm, separately for each kind of key. **Webcrypt Access** chooses which keys the OnlyKey web app may use at all.

The settings change only how an operation is approved. They never change a key: the same key signs or decrypts in every mode.

## The three user input modes {#modes}

| Setting in the OnlyKey App | onlykey-cli | Applies to | Choices |
| --- | --- | --- | --- |
| **SSH/GPG derived keys** | `derivedkeymode` | Keys [onlykey-agent](/onlykey-agent) derives for SSH and GPG identities (`ECC32` and `derived-v2`) | Challenge code, Button press |
| **Stored keys (PGP, SSH, RSA and ECC slots)** | `storedkeymode` | Every key loaded or generated in a slot: RSA1-RSA4, PQC1-PQC4 and ECC1-ECC16, for PGP, SSH, age and composite PQC keys | Challenge code, Button press |
| **Web and agent derived keys** | `webderivemode` | Keys derived from a label: the [web app](/webcrypt) (age pages and [Password Vault](/vault)) and [age-plugin-onlykey](/age) `--derived` | Challenge code, Button press, None |

**Button press** is the default for all three. OnlyKey writes it when the key is new or has been factory reset, before you set a PIN.

:::note
A key first set up on firmware older than 3.0.2 asks for a challenge code for stored and SSH/GPG derived keys until you change those settings, because that firmware did not write a default. Updating the firmware keeps your settings. To switch to button press, put the OnlyKey into config mode and save **Button press** for both in the OnlyKey App, or run `onlykey-cli storedkeymode 1` and `onlykey-cli derivedkeymode 1`.
:::

| Choice | onlykey-cli value | What you do |
| --- | --- | --- |
| **Challenge code** | `0` | Press the three buttons the requesting app shows, in order |
| **Button press** | `1` | Tap any button |
| **None (no confirmation)** | `2` | Nothing: the operation runs as soon as it arrives, whenever the OnlyKey is unlocked |

:::warning "⚠️ None (no confirmation)"
**None** is for unattended tools, such as a script that decrypts age files with derived keys. While it is set, the web app can also derive and decrypt with derived keys without a press. It is available for **Web and agent derived keys** only; release firmware refuses it for SSH/GPG derived keys and stored keys. Leave it off unless you need it.
:::

:::note
The OnlyKey App cannot read these settings back from the device. If you are not sure how your OnlyKey is set, choose a mode and save it.
:::

## The challenge code {#challenge-code}

In challenge-code mode the OnlyKey lights up and waits for three button presses. The app that made the request shows you which three:

- The web app shows them on the page.
- onlykey-agent and age-plugin-onlykey print them next to "Confirm on OnlyKey".

The three digits are calculated from the request itself, so a code shown for one request does not approve another. OnlyKey uses buttons 1-6; OnlyKey DUO uses buttons 1-3. You have 20 seconds to confirm. If the time runs out or the code is wrong, the OnlyKey shows red and the request is refused.

## Webcrypt Access {#webcrypt-access}

Webcrypt Access controls what the OnlyKey web app may do with your OnlyKey, through the OnlyKey FIDO2 extension.

| Setting in the OnlyKey App | onlykey-cli | The web app can use |
| --- | --- | --- |
| **Stored and derived keys** | `webcryptpolicy 1` | Keys stored on the OnlyKey (PGP, including composite PQC keys) and derived keys. This is the default. |
| **Derived keys only** | `webcryptpolicy 0` | Derived keys only: age pages and the Password Vault. Stored PGP keys stay out of its reach. |
| **Off - the web app cannot reach this key** | `webcryptpolicy 2` | Nothing, derived keys included. |

- Only [apps.onlykey.io](https://apps.onlykey.io) and [apps.crp.to](https://apps.crp.to) can use the OnlyKey FIDO2 extension. The list is built into the firmware and cannot be changed. Other websites cannot use it.
- Ordinary FIDO2 and WebAuthn sign-in to websites is not affected by this setting.
- If you turned the FIDO2 extension off on firmware 3.0.4, it stays off after upgrading until you save a Webcrypt Access choice.

## Change the settings {#change}

All four settings can be changed only in [config mode](#config-mode).

### In the OnlyKey App {#change-app}

:::callout
**Step 1.** Put the OnlyKey into [config mode](#config-mode) and open the OnlyKey App.
:::

:::callout
**Step 2.** Go to **Preferences**.
:::

:::callout
**Step 3.** Under **User Input Modes**, choose a mode for each kind of key you want to change and select **Save User Input Modes**. Nothing is preselected, and only the kinds you chose are written.
:::

:::callout
**Step 4.** Under **Webcrypt Access**, choose what the web app can use and save it.
:::

:::callout
**Step 5.** Remove and reinsert the OnlyKey to leave config mode.
:::

The **Web and agent derived keys** and **Webcrypt Access** settings appear only when the OnlyKey has firmware 3.1.0 or later.

### With onlykey-cli {#change-cli}

With the OnlyKey in config mode:

```
$ onlykey-cli storedkeymode 1
$ onlykey-cli derivedkeymode 1
$ onlykey-cli webderivemode 0
$ onlykey-cli webcryptpolicy 0
```

`onlykey-cli capabilities` shows which modes your firmware accepts for each setting. See the [command-line reference](/command-line#onlykey-preferences-options).

## Config mode {#config-mode}

Loading keys and changing these settings need config mode, so that only someone who knows the PIN can make the change.

::: tabs
== tab OnlyKey
1. Unlock the OnlyKey.
2. Hold down button **6** for 5 seconds or more, then release. The light turns off.
3. Enter your PIN.

The OnlyKey flashes red while it is in config mode.
== tab OnlyKey DUO
1. Hold down button **1** for 10 seconds or more, then release. The light turns off.
2. If a PIN is set, re-enter it.

The OnlyKey flashes red while it is in config mode.
:::

The OnlyKey is not usable for anything else while it is in config mode. Remove and reinsert it to leave config mode.

:::note
OnlyKey App 6.0.0 shows an OnlyKey as **Unlocked** if it was already in config mode when the app connected.
:::

## Related pages {#related}

- [Post-quantum keys](/pqc)
- [age with OnlyKey](/age)
- [SSH/GPG agent](/onlykey-agent)
- [OnlyKey web app](/webcrypt)
