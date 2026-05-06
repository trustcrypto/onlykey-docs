---
title: Using OnlyKey with Windows Subsystem for Linux
description: How to use OnlyKey with Windows Subsystem for Linux (WSL 2)
slug: wsl
last_updated: Jun, 15, 2022
keywords: OnlyKey, WSL, WLS2, onlykey-agent
---

## Windows Subsystem for Linux (WSL 2) Support

OnlyKey is supported on WSL2 by following the steps described in the Microsoft article [here](https://docs.microsoft.com/en-us/windows/wsl/connect-usb). As WSL 2 does not have access to USB devices by default the USB/IP open-source project is used to connect devices. 

### Step 1. Install WSL 2 and Dependencies on Windows

**Automatic Setup**
- Run the Powsershell script <a href="https://raw.githubusercontent.com/trustcrypto/trustcrypto.github.io/pages/InstallWSL-Step1.ps1" target="_blank" download="InstallWSL-Step1.ps1">here</a> to install WSL 2 and Dependencies on Windows


**Manual Setup**
- Powershell command to install WSL 2 and the default Ubuntu VM
```
> Start-Process powershell -Verb RunAs -ArgumentList 'wsl --install' -Wait  
```
- Powershell command to install USB/IP
```
> Start-Process "winget.exe" -ArgumentList "install",  "--silent",  "--exact dorssel.usbipd-win"
```
- Powershell commands to install WSL USB GUI (optional but recommended)
```
> Invoke-RestMethod "https://gitlab.com/api/v4/projects/35133362/packages/generic/wsl-usb-gui/3.2/WSL-USB-3.2-g4a21d53.msi" -OutFile $env:USERPROFILE\Downloads\WSL-USB-3.2-g4a21d53.msi
> Start-Process "msiexec.exe"  -ArgumentList "/I", "$env:USERPROFILE\Downloads\WSL-USB-3.2-g4a21d53.msi /quiet" -Wait
```

### Step 2. Reboot and Install OnlyKey-Agent

- Reboot system, on reboot Windows will prompt to complete WSL installation once WSL is installed complete steps below:

**Automatic Setup**

- Run the Powsershell script <a href="https://raw.githubusercontent.com/trustcrypto/trustcrypto.github.io/pages/InstallOnlyKeyAgent-Step2.ps1" target="_blank" download="InstallOnlyKeyAgent-Step2.ps1">here</a> to install the OnlyKey CLI and OnlyKey-Agent in WSL

**Manual Setup**

- Powershell commands to update Ubuntu and install OnlyKey dependencies
```
> Start-Process bash -ArgumentList '-c "sudo apt update && sudo apt upgrade -y"' -Wait 
> Start-Process bash -ArgumentList '-c "sudo apt install python3-pip python3-tk libusb-1.0-0-dev libudev-dev linux-tools-5.4.0-77-generic hwdata -y && pip3 install onlykey-agent && wget https://raw.githubusercontent.com/trustcrypto/trustcrypto.github.io/pages/49-onlykey.rules && sudo cp 49-onlykey.rules /etc/udev/rules.d"' -Wait
> Start-Process bash -ArgumentList '-c "sudo update-alternatives --install /usr/local/bin/usbip usbip /usr/lib/linux-tools/5.4.0-77-generic/usbip 20"' -Wait
```

### Step 3. Using OnlyKey in WSL

- Attach OnlyKey to WSL using WSL USB Manager GUI or with command
```
usbipd wsl attach --hardware-id=1d50:60fc
```
- Run any [onlykey cli](/command-line) or [onlykey-agent](/onlykey-agent) commands as described in [documententation](/index#apps)


{% include links.html %}
