---
title: KeepassXC Upgrade Guide
description: Follow this guide to upgrade OnlyKey firmware and configure KeepassXC challenge-response
slug: keepassxc-upgrade
last_updated: Oct, 29, 2020
keywords: OnlyKey, Firmware, Upgrade
---

With OnlyKey firmware 2.1.0 support for challenge-response is now compatible with Yubikey devices. This permits OnlyKey and Yubikey to be used interchangeably for challenge-response with KeePassXC. A KeePassXC database can be unlocked with OnlyKey, Yubikey, or both if they share the same HMAC key. OnlyKey comes with a random key already set, however a custom key may be set following the guide [here](/usersguide#challenge-response).

Additionally, OnlyKey now supports customizable "HMAC User Input Mode" which allows the user to select if button press is required for challenge-response.
![](/assets/prefs.png)

## Before OnlyKey Upgrade

Before upgrading OnlyKey firmware challenge-response must be removed from KeePassXC databases by completing these steps:

- With your KeePassXC password database open go to Database -> Database Security
- Select Remove YubiKey Challenge-Response

![](/assets/keepassxcstep1.png)

- Close KeePassXC

## Upgrade OnlyKey Firmware

Proceed to upgrade OnlyKey firmware following the upgrade guide steps [here]()

## After OnlyKey Upgrade

Re-enable KeePassXC challenge-response:

- With your KeePassXC password database open go to Database -> Database Security
- Select Add Additional Protection
![](/assets/keepassxcstep2.png)
- Select OnlyKey slot 1 or slot 2
![](/assets/keepassxcstep3.png)
- Click OK
- OnlyKey will flash yellow, press button to enable challenge-response
- Close KeePassXC

{% include links.html %}
