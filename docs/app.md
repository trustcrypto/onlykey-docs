---
title: OnlyKey App
description: The OnlyKey App sets up and configures OnlyKey and OnlyKey DUO - PINs, slots, keys, backups, firmware and preferences. Version 6.0.0 for macOS, Windows and Linux.
slug: app
last_updated: Nov, 25, 2026
keywords: OnlyKey, App, desktop app, install, 6.0.0
---

# OnlyKey App

This is the official app for **OnlyKey** and **OnlyKey DUO**.

OnlyKey can be purchased here: [OnlyKey order](https://onlykey.io/products)

## About

OnlyKey App 6.0.0 is a new desktop app for macOS, Windows and Linux, rebuilt from the ground up with a redesigned interface and light and dark themes. The way it talks to the OnlyKey is unchanged, and it works with older firmware too; the firmware 3.1.0 settings appear only when your OnlyKey has firmware 3.1.0 or later.

The app has eight pages:

| Page | What it is for |
| --- | --- |
| **Setup** | Initial setup: PINs, second profile, self-destruct PIN, backup passphrase or key, and restoring a backup |
| **Slots** | Accounts: usernames, passwords, TOTP and other two-factor settings for each button |
| **Keys** | Loading OpenPGP and OpenSSH private keys (PEM format) into key slots |
| **Backup** | Encrypted backup and restore |
| **Firmware** | Checking for and loading firmware updates |
| **Preferences** | Device settings, including [User Input Modes and Webcrypt Access](/user-input-modes) (firmware 3.1.0) |
| **Advanced** | Raw ECC and HMAC keys, and legacy Yubico OTP settings |
| **Tools** | Links to the [web app](/webcrypt), the [Password Vault](/vault) and OnlyKey Agent, and app updates |

*The app is required on all systems where Google Authenticator (TOTP) is used, because it sets the OnlyKey's clock. You can also set the clock in the [web app](/webcrypt#pages).*

For information on using the app with OnlyKey see the [OnlyKey User's Guide](/usersguide) or the [OnlyKey DUO User's Guide](/duousersguide).

### Install OnlyKey App {#app-desktop}

:::callout
**Step 1.** Download the installer for your computer from the [OnlyKey App 6.0.0 release](https://github.com/trustcrypto/OnlyKey-App/releases/tag/v6.0.0).
:::

::: tabs
== tab macOS
Download **OnlyKey_6.0.0.dmg**. It is a universal app for Apple silicon and Intel Macs, signed and notarized by CryptoTrust LLC.

Open the DMG and drag OnlyKey App to Applications.

:::warning "⚠️ Upgrading on macOS"
If your previous OnlyKey App was set to open at login, the old entry can stay behind and open the app full screen when you log in. After installing 6.0.0, open **System Settings › General › Login Items & Extensions**. Under **Open at Login**, select the old "OnlyKey App" entry and click **–**. To start the new app at login, turn the option on again in the app.
:::
== tab Windows
:::note
The Windows installer for OnlyKey App 6.0.0 will be posted on the release page when it is ready. Until then, use [OnlyKey App 5.3.6 for Windows](https://github.com/trustcrypto/OnlyKey-App/releases/download/v5.3.6/OnlyKey_5.3.6.exe). It cannot change the new firmware 3.1.0 settings; use [onlykey-cli](/command-line) for those.
:::

When you install 6.0.0, setup closes a running OnlyKey App and removes the previous version first.
== tab Linux
Download **OnlyKey_6.0.0_amd64.deb** and its signature, **OnlyKey_6.0.0_amd64.deb.sig**. Verify the signature, then install:

```
$ gpg --verify OnlyKey_6.0.0_amd64.deb.sig OnlyKey_6.0.0_amd64.deb
$ sudo apt install ./OnlyKey_6.0.0_amd64.deb
```

The package is signed by CryptoTrust LLC &lt;admin@cryptotrust.net&gt;, key `A1D6 4A3B 496C B0F3 6E12 B46F 9A9F 520D 44EA 53D1`.

The package installs the OnlyKey udev rule (`/etc/udev/rules.d/49-onlykey.rules`), so you can use the OnlyKey without root. If the app still cannot reach the OnlyKey, it shows a **Linux USB Permissions** message; see the [Linux guide](/linux).
:::

:::callout
**Step 2.** Install and launch the app.
:::

:::tip "💡 Pro Tip"
You can ensure the integrity of your download by checking its SHA-256 checksum:<br>
OnlyKey_6.0.0.dmg: `4a3d6ed88039cc97b7a1b328d1ee3da9ada06832b4b29a69159be29ef7a003f4`<br>
OnlyKey_6.0.0_amd64.deb: `e3b0b6ae44c6a05d666e036fb9ee21e0633333865273c8c148f8808ee0a0926f`
:::

:::tip "💡 Pro Tip"
As you use the OnlyKey app you can hover over icons for tooltips, and click them to open that topic in the documentation.
:::

If you have an OnlyKey to set up, once you have installed the app proceed to [OnlyKey Setup](/usersguide#onlykey-setup).

## Updates {#updates}

The app checks for updates to itself and to the OnlyKey firmware. Every download is checked against its SHA-256 checksum before it is installed, and a package without one is refused.

- **App updates:** on the **Tools** page, turn on **Automatically check for app updates**, or select **Check now**.
- **Firmware updates:** on the **Firmware** page, turn on **Automatically check for firmware updates**, or select **Check now**. The app shows the update in a dialog and loads it for OnlyKey and OnlyKey DUO. Back up first; see the [Upgrade Guide](/upgradeguide).

## Tray and start at login {#tray}

The app keeps an icon in the system tray (the menu bar on macOS). Closing the window hides the app to the tray; quitting it from the tray menu, or with Cmd+Q on a Mac, closes it.

The tray menu has:

- **Show OnlyKey App**
- **Autostart to tray** - start the app minimized when you log in (Windows and macOS)
- **Automatically check for app updates**
- **Automatically check for firmware updates**
- **Hide to system tray when window is closed**
- **Quit OnlyKey App**

On macOS, the first time the app checks for a login item left by an older version, it asks first and macOS then asks to let it control System Events. Choose **Allow**, or **Not now** to skip the check; starting at login works either way.

## Tools {#tools}

The **Tools** page opens the [web app](/webcrypt) at apps.onlykey.io: encrypt and decrypt messages and files, and the [Password Vault](/vault). For an OnlyKey on firmware 3.0.4 or older, use [apps.crp.to](https://apps.crp.to) instead.

It also links to [OnlyKey Agent](/onlykey-agent) for OpenPGP, SSH, Git signing and [age](/age).

## Good to know {#notes}

- Slot text uses the Latin-1 character set. A character the OnlyKey cannot type, such as € or an emoji, is refused with an error instead of being stored as a different character.
- When you edit a slot, the password generator fills in a strong password without going through the clipboard.
- The app wipes its session state when the OnlyKey locks or is unplugged.
- A 50-message history shows what the OnlyKey reported.

## Known issues {#known-issues}

- If the OnlyKey was already in config mode when the app connected, the app shows it as **Unlocked**.
- macOS: the old app's **Open at Login** entry can remain after upgrading; see the macOS install tab above.

## OnlyKey Chrome App {#onlykey-chrome-app}

:::warning "⚠️ No Longer Supported"
The OnlyKey Chrome App is **discontinued**. Google has ended support for Chrome Apps: ChromeOS 138 (July 2025) was the last ChromeOS release that supported user-installed Chrome apps, and Chrome Apps have been removed from desktop Chrome, Chromium, Brave and Edge. Use the desktop app on macOS, Windows or Linux, and the [web app](/webcrypt) on other systems.
:::

## Support

Check out the [OnlyKey Support Forum](https://forum.onlykey.io)

Check out the [OnlyKey Documentation](https://docs.onlykey.io)

## Source

[OnlyKey App on Github](https://github.com/trustcrypto/OnlyKey-App)
