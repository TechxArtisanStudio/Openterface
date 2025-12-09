# Openterface KVM-Go — Review Guide (Engineering Prototype)

## Overview

Thank you for taking the time to test our upcoming product **Openterface KVM-Go**.

This unit is an **engineering prototype**, and both our firmware and software are still evolving rapidly. Your feedback will directly help us improve the product before mass production.

If you encounter any issues during testing, please contact us directly — **we will provide immediate support to help you resolve them before you record your video**.

## Important Notes

### Prototype Disclaimer

This device is an **engineering prototype**. Firmware and software may contain bugs or incomplete features. If you experience instability or anything that blocks your workflow, please notify us — we will fix issues before shipping the production version.

### Use the Latest Software

For best performance and compatibility, please use the **latest version** of the Openterface software from our GitHub Releases page. We update frequently, and older versions may not match your firmware.

## Known Issues & Explanations

> **Note:** All issues listed below will be addressed before production release.

### Surface Temperature

The device may feel warm or hot during use. This is expected because we are using higher-performance chips.

Please note:

- All temperatures are within the safe operating range
- Built-in **temperature sensors** monitor real-time thermal status in software
- Multi-day stress tests show no stability issues

We will continue adjusting thermal performance before mass production.

### Software Distribution

We currently support multiple platforms:

- **macOS & Windows**

    - These are the most stable and recommended for full-feature testing

- **Linux**

    - Please use the **AppImage** version
    - `.deb` and `.rpm` packages may cause dependency issues depending on the distribution, and we are actively improving this

- **Android**

    - A working version is available on **Google Play** for basic control and monitoring
    - You can try it if you want to explore mobile workflows

- **iPadOS**

    - Available through **TestFlight**
    - If you want to test it, please send me your **Apple ID**, and I will add you to the tester list

### Copy & Paste Functionality

The firmware on your unit may not include our latest clipboard fixes. We have resolved these issues in the newest firmware. See the [Firmware Upgrade Guide](firmware-upgrade.md) if you would like to test the updated version.

### Teardown (Optional)

If you enjoy teardowns, you are welcome to take the unit apart.

Inside the prototype you received, we are using:

- **MS2130S** — Video capture chip
- **WCH CH32V208** — USB keyboard & mouse emulation MCU
- **Standard silicone thermal paste** — used on your prototype

We are currently testing an upgrade to **aluminum thermal components** with **higher-performance thermal grease**. These improved materials have passed internal testing, but because of limited prototype quantity, they are **not included** in the review units yet.

Your version still uses **silicone paste**, but thermal performance remains within safe limits.

### Advanced Features (Supported in Mini-KVM, Coming Soon to KVM-Go)

KVM-Go shares the same design philosophy as Openterface Mini-KVM, and several advanced features are in active development but **not ready yet** on your prototype:

- **Custom EDID**

    - In Mini-KVM you can load or modify EDID to solve compatibility issues
    - We are adding this capability to KVM-Go

- **Software-based SD Card Switching**

    - Mini-KVM supports switching the SD card between host and PC through software
    - This feature is under development for KVM-Go but not yet enabled

We want you to be aware of these upcoming features, even though they are unavailable in the current prototype firmware.

### Open-Source Commitment

Yes — KVM-Go will remain fully open-source.

- **Software** is already on GitHub
- **Hardware design** will be released once the production version is finalized
- **3D-printable case files** are already online, and you can print or customize your own cover

## Further Reading

- [KVM-Go Firmware Upgrade](firmware-upgrade.md) — Step-by-step guide for upgrading firmware on your KVM-Go device

