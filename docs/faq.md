---
title: OnlyKey FAQ
description: Frequently Asked Questions
slug: faq
last_updated: Oct, 18 2020
keywords: frequently asked questions, FAQ, question and answer
---

## How do I get started with OnlyKey?

Just getting started with OnlyKey? [Start here](https://onlykey.io/start). Just getting started with OnlyKey DUO? [Start here](https://onlykey.io/duo).

## Where do I go for OnlyKey support?

Check out the [OnlyKey Documentation](https://docs.onlykey.io) and if that does not answer your question reach out on the [OnlyKey Support Forum](https://forum.onlykey.io).

## Is OnlyKey Waterproof and Durable?

OnlyKey is protected with a tamper-resistant and chemical-resistant compound that provides:

1. **Durability** - OnlyKey is crush and impact resistant, it stands up to abuse. You can carry it on your keychain, in your pocket, etc.
2. **Waterproof** - Accidentally leave your OnlyKey in your pocket and it goes through the washing machine? No problem.
3. **Tamper-evident / Tamper-resistant** - Attempts by an adversary to access the electronics inside of OnlyKey will create visible damage.
4. **Transparency** - The protective compound is clear so that it is possible to visually verify the electronic components (verify no hardware backdoor).

## How Does OnlyKey Keep My Information From Getting Hacked?

First it is important to understand how accounts are hacked as there are several ways and OnlyKey has unique features that prevent each type.

**1) The site you use is breached (i.e. Yahoo, LinkedIn, Target, Anthem, Sony etc.)**

If the site you use is breached the attacker may be able to get your password in a couple of ways.

a) They get a dump of all passwords in clear text. This is less likely to occur as it usually requires that the service used very bad security practices. If it does occur then it does not matter how long or complex the password is, the password has been compromised.

b) They get a hashed dump of all passwords. If this occurs the attacker has to crack the passwords and only the weak passwords would be compromised.

OnlyKey addresses b) by allowing users to set strong, up to 56 character long passwords which cannot be cracked by any available methods. These strong passwords are also more usable since you don't have to remember them, they are stored on your OnlyKey and typed out for you.

OnlyKey addresses a) by making multi-factor authentication (MFA) compatible with the largest number of sites. If MFA is used and an attacker has your password they still can't access your account as they do not have your second factor.

**2) The computer you use is hacked (you click on a malicious website or download malware accidentally)**

If the computer you use is hacked and you use a cloud based software password manager like LastPass, Dashlane, or even a local password manager like KeePass then the attacker may be able to extract your passwords. As the hacker has access to your computer they essentially have access to everything you have access to on that computer.

If the computer you use is compromised the attacker may be able to get your passwords in a couple of ways.

a) They log all of your keyboard input (Keylogger) or clipboard if using a software password manager.

b) They wait until you unlock your software password manager like LastPass and download the entire database of passwords or access them one-by-one.

OnlyKey addresses b) by storing everything offline (cold storage). Essentially OnlyKey is secure by design so that you can only ever write or wipe passwords stored on the OnlyKey. If an attacker gains access to your computer there are no passwords stored there to steal. Even if your OnlyKey is plugged in and unlocked there is no way to download or copy information from the OnlyKey.

OnlyKey addresses a) by making MFA usable for users and compatible with the largest number of sites. If a MFA method such as TOTP is used then even if an attacker captures your password they still can't access your account without obtaining your one-time password. One time passwords used by Yubikey OTP are only valid once and Google Authenticator TOTPs are only valid once and for a short period of time, usually 30 seconds.

**3) Your cloud based password manager was compromised.**

In this scenario you have chosen the convenience of having passwords accessible anywhere you go with the security trade off being that they are being stored online in the cloud. The provider assures you that the accounts will never be hacked but they missed something and now an attacker has access to every account you own. With OnlyKey you can store your most important accounts offline so that they are never susceptible to this type of attack.

## What if I lose my OnlyKey?

The data stored on OnlyKey is encrypted with military grade encryption (AES-256-GCM) and cannot be extracted from device. Additionally, with a PIN set on OnlyKey that PIN must be known to use the device.

If an attacker tries to guess the PIN it will wipe all data after 10 failed attempts.

What about getting my accounts back? This is where the secure encrypted backup anywhere feature comes in. You can create encrypted backups anywhere by just holding the #1 button down on the OnlyKey. This means that only a physical person can initiate a backup (not malware) and it types out the encrypted file so you can save it anywhere in a local text file, email, etc.

To restore your data if you lose your OnlyKey you can restore this backup to a new OnlyKey or if you like to plan ahead then get a secondary OnlyKey and restore your backup so it is ready in case your primary is lost.

Read more about the technical physical hardware security and encrypted backup feature [here](/security#hardware-security).

## How is OnlyKey Better Than a Smart Card?

Smart Cards are commonly used to provide two-factor authentication and decryption/signing for things like email. Unfortunately, if the computer that a smart card is plugged into is compromised by an attacker then the security of the smart card is compromised. All the attacker has to do is capture the keyboard output (keylogging) and they can capture the users smart card PIN. With this PIN they can then authenticate to anything that the user has access to and also decrypt/sign emails as if the user had done so. With OnlyKey your PIN is entered on the 6 digit keypad located on the device itself that does not in any way send this PIN to the connected computer. In this way the PIN entry is offline and inaccessible to an attacker who has compromised the connected computer.

In addition to on-device PIN security OnlyKey has functionality that smart cards do not like password management, SSH login, GPG agent and is universally supported without the need for drivers to be installed. The OnlyKey is detected by the computer as a keyboard and no middleware or special drivers are required. OnlyKey can be plugged in and used on a computer that you have never used before and it works without installing anything. The OnlyKey app is required to make changes on your OnlyKey and that is available on Windows, Mac OS, and Linux.

## How is OnlyKey Better Than Other Tokens?

There are a variety of hardware and software tokens out there. Some support FIDO U2F and others support Yubikey OTP and yet others support Google Authenticator (TOTP). Unfortunately for users not all websites support all of these. There is no standardization of two-factor support among websites so in order to log in using a token you often need multiple tokens and apps. OnlyKey set out to address this issue and make two-factor authentication usable by supporting the methods most commonly used by websites. Additionally, by combining this with password management we can provide users with a secure login with the touch of a button.

## What specifically are the differences between the Standard Edition firmware and the International Travel Edition firmware?

The International Travel Edition firmware is essentially a feature limited version of the OnlyKey. It is a fully functional password manager but does not utilize encryption and may be usable in countries where encryption is banned/restricted. More information [here](/ite).

## What does entering the self destruct PIN do?

Depending on what your wipe mode is set to it either wipes all sensitive data (erases your usernames, passwords, keys etc.) or if you are using full wipe mode it does a complete erase of the OnlyKey including sensitive data and all firmware (this requires reloading firmware).

Use this PIN when you wish to wipe all sensitive data from the OnlyKey and restore it to a factory default state.

## What apps and services are compatible with OnlyKey?

Our team has created several desktop applications for OnlyKey, see details [here](/#apps). OnlyKey can be used with any application that supports passwords entered via a keyboard which means most applications are supported. Additionally, OnlyKey can be used as a security key for any website or app that supports modern two-factor authentication methods like OATH-TOTP (Google Authenticator), FIDO2 (Security Key), and Yubikey OTP. Finally, you can use OnlyKey for developer tools that are compatible with GPG such as GIT and remote access with SSH. Check out the knowledge base for other use cases [here](/#knowledge-base).

## How is the OnlyKey firmware signed and verified?

The firmware is signed and only signed firmware can be loaded onto device. Additionally, firmware integrity is verified every time the device boots. In the event firmware verification fails the device is wiped and signed firmware must be reloaded. More information available [here](/security#security-features-overview).

## How can I be sure my OnlyKey does not have a backdoor or was not tampered with?

We have designed OnlyKey to be as transparent as possible. The firmware and applications are open source and can be reviewed [here](https://github.com/trustcrypto). Here are some of the features that allow you to validate that there is no backdoor or tampering has occurred.

1. **Hardware** - By having a clear coat on the electronics you can actually see the hardware and would be able to see a hardware type of backdoor.
2. **Open Source** - OnlyKey firmware and apps are published on GitHub and are open to review by the security community.
3. **Decentralized** - Secret keys are generated by you and accessible only to you. Unlike our competitors, we believe in a decentralized model where you have the freedom to control and verify everything on the OnlyKey.

## Is OnlyKey Supported on iPhone, Android, and other mobile devices?

Yes, OnlyKey is supported by any device that would support a USB keyboard. A guide to using OnlyKey with mobile devices is available [here](/mobile).
