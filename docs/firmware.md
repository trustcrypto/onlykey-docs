---
title: OnlyKey Firmware
description: The OnlyKey firmware runs on the OnlyKey itself and provides the core functionality of OnlyKey.
slug: firmware
last_updated: Nov, 25, 2026
keywords: OnlyKey, Firmware
---

# OnlyKey Firmware

This is the official firmware for **OnlyKey**

OnlyKey can be purchased here: [OnlyKey order](https://onlykey.io/)

## Getting Started

Just getting started with OnlyKey?

[Start here](https://onlykey.io/start)

## About

The firmware is the software that runs on the OnlyKey itself. In order to load firmware follow the instructions in the [User's Guide here](/usersguide#loading-onlykey-firmware)

## Current release {#current-release}

The current firmware is **3.1.0**. It adds [post-quantum keys](/pqc), [age](/age) file encryption with derived keys, the [Password Vault](/vault), separate [user input modes](/user-input-modes) and Webcrypt Access, and an encrypted, authenticated connection to the [web app](/webcrypt) at apps.onlykey.io, along with security improvements. OnlyKey and OnlyKey DUO use the same firmware file, and there is one edition.

- [Upgrade Guide](/upgradeguide) - back up first, then load 3.1.0
- [Release notes](https://github.com/trustcrypto/OnlyKey-Firmware/releases/tag/v3.1.0-prod)
- [Version compatibility](/compatibility)

## Development

OnlyKey firmware is open source and new features are added with each firmware release. A list of of supported features are available [here](/features)

## Loading OnlyKey Firmware

Follow the upgrade guide [here](/upgradeguide#loading-onlykey-firmware) to update OnlyKey firmware 

## Support

Check out the [OnlyKey Support Forum](https://forum.onlykey.io)

Check out the [OnlyKey Documentation](https://docs.onlykey.io)

## Libraries

OnlyKey firmware uses additional libraries that are available [here](https://github.com/trustcrypto/libraries).

# Legal things
## Cryptography Notice

This distribution includes cryptographic software. The country in which you currently reside may have restrictions on the import, possession, use, and/or re-export to another country, of encryption software.
BEFORE using any encryption software, please check your country's laws, regulations and policies concerning the import, possession, or use, and re-export of encryption software, to see if this is permitted.
See <http://www.wassenaar.org/> for more information.

The U.S. Government Department of Commerce, Bureau of Industry and Security (BIS), has classified this software as Export Commodity Control Number (ECCN) 5D002.C.1, which includes information security software using or performing cryptographic functions with asymmetric algorithms.
The form and manner of this distribution makes it eligible for export under the License Exception ENC Technology Software Unrestricted (TSU) exception (see the BIS Export Administration Regulations, Section 740.13) for both object code and source code.

The following cryptographic software is included in this distribution:

                      "MBED TLS PROJECT" - https://github.com/ARMmbed/mbedtls
                      "MICRO-ECC PROJECT" - https://github.com/kmackay/micro-ecc
                      "ARDUINOLIBS PROJECT" - https://rweather.github.io/arduinolibs/crypto.html
                      "YUBICO-C PROJECT" - https://github.com/Yubico/yubico-c
                      "MLKEM-NATIVE" - https://github.com/pq-code-package/mlkem-native
                      "MLDSA-NATIVE" - https://github.com/pq-code-package/mldsa-native

For more information on export restrictions see: http://www.apache.org/licenses/exports/

## Source

[OnlyKey Firmware on Github](https://github.com/trustcrypto/OnlyKey-Firmware)

