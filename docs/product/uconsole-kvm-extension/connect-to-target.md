---
title: "Connect to Target Device"
description: "Learn how to connect your target device to the Openterface KVM Extension for uConsole. Complete guide for USB control and video input setup after hardware installation and software setup."
keywords: "KVM connection setup, target device connection, USB control setup, HDMI input setup, uConsole KVM extension connection"
---

# **Connect to Target Device** | Openterface KVM Extension for uConsole

## Connection Overview

![extension-use-case-1a](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1a.webp){:style="height:480px"}

## Prerequisites

Before connecting your target device, ensure you have completed:

1. [Hardware Installation](/product/uconsole-kvm-extension/hardware-installation/) - Physical installation of the KVM Extension board
2. [Software Setup](/product/uconsole-kvm-extension/software-setup/) - Installation of the Openterface App

## Connection Steps

### **USB Control**
Connect the Type-C female port to the target device's USB port to emulate keyboard and mouse signals.

### **Video Input**
Connect target device's video output to the HDMI port on the KVM Extension:

- Use standard HDMI cable for HDMI output devices
- Use VGA-to-HDMI converter cable for VGA output devices. 
    - *Note*: Ensure the converter is powered via its USB connector for proper operation.
- Use other appropriate adapters for different video signal types

## Testing the Connection

1. Turn on power and boot the uConsole
2. Run the Openterface QT app
3. Test HDMI, audio, and USB HID functionality to confirm proper operation