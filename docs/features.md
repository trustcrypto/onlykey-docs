---
title: OnlyKey Features
description: Detailed information on OnlyKey Features
slug: features
last_updated: Dec, 28 2022
keywords: OnlyKey, Features
---

## OnlyKey Product Details
OnlyKey comes in two models:

OnlyKey - Features 6 physical buttons, USB-A interface, and multiple color cases
![](/assets/Infographic.png)

OnlyKey DUO - Features 3 physical buttons, both USB-C & USB-A interface, and small form factor
![](/assets/infographic-duo.jpg)

### UNIVERSAL SUPPORT
Supports Windows, Mac OS, Android, Linux, and Chrome OS. Driverless operation – Recognized by computer as a regular keyboard.

### PORTABLE. DURABLE. WATERPROOF
On-the-go – Easily attach and detach the OnlyKey to your keychain and bring it everywhere you go.

![](/assets/package.jpg)

### PIN PROTECTED
For OnlyKey your PIN code must be typed onto the 6 button keypad of the OnlyKey in order to unlock. For OnlyKey DUO you can use the OnlyKey App to unlock. If you lose OnlyKey no problem, it is PIN protected and can’t be used without the PIN, enter the wrong PIN too many times the data will self destruct. 

### WHERE CONVENIENCE AND SECURITY MEET
OnlyKey is dual use. It functions as a password manager and a two-factor token. You can plug OnlyKey into any computer, press a button, and it types out a username and password the same as if you typed it yourself; but with one big difference, you don’t have to remember passwords! OnlyKey does that for you. This allows using very complex and secure passwords that cannot be cracked by any available methods.

### SECURE BY DESIGN
Information can only be written to the OnlyKey or wiped. This protects your data even if the connected computer has been compromised. Unlike smartcards that are vulnerable to keylogger attacks, the PIN used to unlock OnlyKey is entered on the OnlyKey itself.

## Key Features

### HARDWARE PASSWORD MANAGER
Instead of having to remember all of your passwords you can just remember one 7 - 10 digit PIN. OnlyKey stores up to 24 unique accounts in offline storage and can be used to secure an unlimited number of accounts if used in conjunction with a software password manager. You can set up each of the 24 accounts using strong and random (up to 56 character) passwords along with the login page URLs, usernames, and/or two-factor authentication. This way whenever you need to log in you just detach the OnlyKey from your keyring and enter your PIN to unlock your passwords. The Onlykey automatically types them into the login fields for you with the press of a button.
![](/assets/mobile.gif)


### UNIVERSAL 2-FACTOR TOKEN
Supports FIDO2 and FIDO Universal 2nd Factor Authentication (U2F), OATH TOTP, and Yubikey® compatible OTP. Chances are that if the website supports two-factor authentication, OnlyKey is compatible.
![](/assets/fido2.gif)

*   [FIDO2 and FIDO Universal 2nd Factor Authentication (U2F)](/usersguide#universal-2nd-factor-u2f)
*   [OATH TOTP](/usersguide#google-authenticator-totp)
*   [Yubico® One-Time Password](/usersguide#Yubico-one-time-password)
*   [Challenge-Response](/usersguide#challenge-response)

### SSH AUTHENTICATION
SSH authentication is easy with passwordless login. Your SSH key remains securely stored in hardware and not available to attackers.

*   [OpenSSH Support](/openssh)
*   [OnlyKey Agent SSH](/onlykey-agent)

### OPENPGP SUPPORT
Using OnlyKey makes OpenPGP easier than ever.
![](/assets/agent.gif)

*   [OnlyKey WebCrypt](/webcrypt)
*   [OnlyKey Agent GPG](/onlykey-agent)

Keys are loaded using the OnlyKey App. Step by step directions for generating and loading keys are provided in the User's Guide here:

*   [Generate keys](/importpgp#generating-keys) using Keybase
*   [Load keys](/importpgp#loading-keys) onto OnlyKey

### SELF-DESTRUCT FEATURE
In a pinch and want to wipe your OnlyKey? Enter your self-destruct PIN to wipe EVERYTHING! Plus you can always restore from backup easily.

*   [What does entering the self destruct PIN do?](/faq#what-does-entering-the-self-destruct-pin-do)

### PLAUSIBLE DENIABILITY FEATURE
The first and only hardware solution where only you hold the keys + no proof there even are keys! Travel abroad without having to give up your encryption keys/passwords.

*   [International Travel Edition Guide](/ite)

### ENCRYPTED BACKUP ANYWHERE
OnlyKey types out the encrypted backup so it works anywhere independent of apps. Save the encrypted backup to a file or email it to yourself.

*   For information on setting up and using secure encrypted backup see the user's guide [here](/usersguide#secure-encrypted-backup-anywhere)
*   For security information on secure encrypted backup see the security page [here](/security#how-backup)

## Other Features

### AUTOMATIC LOCK FEATURE
Want your OnlyKey to automatically lock itself after being inactive for 30 minutes? No problem, this is customizable in [OnlyKey preferences](/usersguide#configurable-inactivity-lockout-period).

### USER SELECTABLE TYPE SPEED FEATURE
Want your OnlyKey to type out information faster or slower? No problem, this is customizable in [OnlyKey preferences](/usersguide#configurable-keyboard-type-speed).

### SYSADMIN MODE
Want your OnlyKey to fill any login form or even automate system administration commands? No problem, enable [Sysadmin Mode](/usersguide#sysadmin-mode).

### ADVANCED HARDWARE SECURITY
Once a PIN has been set on your OnlyKey it locks down the hardware so that even if an attacker gains physical access to your OnlyKey, without the correct PIN it will be useless. Read more about [security architecture of OnlyKey](/security).

### INTERNATIONAL KEYBOARD LAYOUTS
OnlyKey is the world's first device to allow changing your keyboard layout on the fly. Supports multiple international keyboard layouts:
- US_ENGLISH (default)
- CANADIAN_FRENCH
- CANADIAN_MULTILINGUAL
- DANISH
- DANISH_MAC
- FINNISH
- FRENCH
- FRENCH_BELGIAN
- FRENCH_SWISS
- GERMAN
- GERMAN_MAC
- GERMAN_SWISS
- ICELANDIC
- IRISH
- ITALIAN
- NORWEGIAN
- PORTUGUESE
- PORTUGUESE_BRAZILIAN
- SPANISH
- SPANISH_LATIN_AMERICA
- SWEDISH
- TURKISH
- UNITED_KINGDOM
- US_INTERNATIONAL
- CZECH
- SERBIAN_LATIN_ONLY
- HUNGARIAN
- DVORAK

### LED DEFINITIONS {#led-definitions-onlykey-color}

*   Steady green light = Unlocked first profile
*   Steady blue light = Unlocked second profile
*   No light = Locked
*   Single yellow flash = Button pressed for PIN entry
*   3 red flashes = Wrong PIN
*   Continuous red flashes = Exceeded PIN tries
*   Continuous green flashes = Backup and restore is complete.
*   Blue blink then green blink = FIDO U2F request
*   Blue blink on/off = FIDO2 request
*   Purple fade in and fade out - Private key signing request (SSH or PGP)
*   Turquoise fade in and fade out - Private key decryption request
*   Yellow fade in and fade out - HMAC challenge request
*   Red fade in and fade out - Device is in [config mode](/security#config-mode)
*   Steady white light - Device is in bootloader mode, use the OnlyKey app to [load firmware](/usersguide#loading-onlykey-firmware).

**ONLYKEY DUO ONLY**

*   Steady green light = Unlocked first profile
*   Steady blue light = Unlocked second profile
*   Steady yellow light = Unlocked third profile
*   Steady purple light = Unlocked fourth profile

### Button Definitions {#button-definitions}

#### Unconfigured OnlyKey {#uninitialized-onlykey}

*   Hold button #3 down for 5+ seconds to start quick setup - See [OnlyKey Quick Setup](/usersguide#quick-setup) for more information.
*   Hold button #1 down for 5+ seconds to start quick setup in manual mode.
*   Hold button #2 down for 5+ seconds to start quick setup in auto mode.

#### Locked OnlyKey {#uninitialized-onlykey}

*   While locked buttons only function to enter PIN code to unlock OnlyKey, 7-10 digits.

**ONLYKEY DUO ONLY**

*   PIN may be entered via OnlyKey App or by physical touch. Touch buttons 1, 2, 3 to enter 1, 2, 3 and hold (for 1 second) buttons 1, 2, 3 to enter 4, 5, 6.

#### Unlocked OnlyKey {#unlocked-onlykey}

*   Tap a button for slot <button #>A (i.e. Press OnlyKey button #1 for less than 1 second to type out account data stored in slot 1a)
*   Hold a button for slot <button #>B (i.e. Press OnlyKey button #1 for more than 1 second to type out account data stored in slot 1b)

***Note: OnlyKey supports multiple profiles for a maximum of 24 accounts.***

*   Hold button #1 for 5+ seconds to backup OnlyKey - See [secure backup feature](/usersguide#secure-encrypted-backup-anywhere) for more information.
*   Hold button #2 for 5+ seconds to type out slot labels - See [OnlyKey on-the-go](/usersguide#otg) for more information.<br>i.e.<br>
1a Google<br>
2a Bank<br>
3a Email<br>
4a VPN<br>
5a School<br>
6a Coinbase<br>
1b Amazon AWS<br>
2b Dropbox<br>
3b KeePassXC<br>
4b Azure<br>
5b Github<br>
6b Lastpass<br>

**ONLYKEY ONLY**

*   Hold button #3 for 5+ seconds to lock OnlyKey.
*   Hold button #6 for 5+ seconds to put OnlyKey in config mode - See [config mode](/security#config-mode) for more information.

**ONLYKEY DUO ONLY**

*   Hold button #3 for 5+ seconds to switch OnlyKey DUO profiles (cycles through green -> blue -> yellow -> purple)
*   Hold button #3 for 10+ seconds to lock OnlyKey DUO.
*   Hold button #1 for 10+ seconds to put OnlyKey DUO in config mode - See [config mode](/security#config-mode) for more information.
*   Hold button #1 for 10+ seconds to put OnlyKey DUO in config mode, then  Hold button #2 for 20+ seconds to restore OnlyKey DUO to factory defaults (also called [self-destruct feature](/features#self-destruct-feature)).

### ONLYKEY AND ONLYKEY DUO DIFFERENCES

- OnlyKey DUO is a small form factor, three button, USB-A and USB-C security key. OnlyKey is a medium form factor, six button, USB-A security key.
- OnlyKey requires on-device PIN, with OnlyKey DUO the PIN is optional.
- OnlyKey and OnlyKey DUO both support the same features, detailed technical description of differences available [here](/security#about-differences-between-onlykey-and-onlykey-duo).


{% include links.html %}
