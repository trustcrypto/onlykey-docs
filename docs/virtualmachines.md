---
title: Using OnlyKey with Virtual Machines
description: How to use OnlyKey with VMware and Virtualbox
slug: virtualmachines
last_updated: Feb, 27, 2020
keywords: OnlyKey, vm, vmware, virtualbox, virtual
---

## Virtual Machine Support

OnlyKey is supported on Virtual Machines in the same way as USB keyboards (USB HID).

### VMware Workstation or VMware Fusion Support

- With the VM shut down, open the .vmx file in a text editor
- Add this line to the .vmx file and save
```
usb.generic.allowHID = "TRUE"
usb.generic.allowLastHID = "TRUE"
```
- Restart the VM and now you will be able to connect OnlyKey to the VM

:::note
MacOS CATALINA (10.15+) requires additional security setting to access USB HID devices in VMware Fusion. Click on Apple logo on the top left of the Mac screen -> System Preferences -> Security and Privacy -> Privacy -> Input Monitoring. Select the + button and add VMware Fusion.
:::

### VirtualBox Support

- Go to Devices -> USB
- Select "CRYPTOTRUST ONLYKEY"

Or to have OnlyKey automatically connect to the VM whenever the VM is powered on

- Go to Devices -> USB -> USB Settings
- Select the add button (Green Plus)
- Select "CRYPTOTRUST ONLYKEY"
- Remove and reinsert OnlyKey to connect it to the VM

