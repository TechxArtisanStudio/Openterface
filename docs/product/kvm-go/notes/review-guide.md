# Openterface KVM-Go — Review Guide (Engineering Prototype)

## Overview

Thank you for taking the time to test our upcoming product **[Openterface KVM-Go](https://openterface.com/product/kvm-go/)**.

This unit is an **engineering prototype**, and both our firmware and software are evolving quickly. Your feedback will directly help us improve the product before mass production.

If you run into any issues during testing, please contact us directly. **We will provide immediate support to help you resolve them before you record your video.**

## Important Notes

### Prototype Disclaimer

This device is an **engineering prototype**. The firmware and software may still contain bugs or incomplete features. If you encounter instability or anything that blocks your workflow, please let us know. We will fix issues before the production version ships.

### Use the Latest Software

For the best performance and compatibility, please use the **latest version** of the [Openterface software](https://openterface.com/app/overview/) from our GitHub Releases page. We update frequently, and older versions may not match your prototype’s firmware.

## Known Issues and Explanations

> **Note:** All issues listed below will be addressed before the production release.

### Surface Temperature

The device may feel warm or even hot during use. This is expected because the prototype uses higher-performance chips.

Please note:

* All temperatures remain within the safe operating range
* Built-in **temperature sensors** report real-time thermal status in the software
* Multi-day stress tests show no stability problems

We will continue to refine thermal performance before mass production.

### Software Distribution

We currently support multiple platforms:

* **macOS and Windows**
  These are the most stable platforms and recommended for full-feature testing.

* **Linux**
  Please use the **AppImage** version.
  The `.deb` and `.rpm` packages may have dependency issues depending on the distribution. We are improving these installers.

* **Android**
  A working version is available on **Google Play** for basic control and monitoring.
  You are welcome to try it if you want to explore mobile workflows.

* **iPadOS**
  Available through **TestFlight**.
  If you would like to test it, please send me your **Apple ID**, and I will add you to the tester list.

### Copy and Paste Functionality

The firmware on your unit may not include our latest clipboard fixes. These issues have already been resolved in the newest firmware. You can update using the [Firmware Upgrade Guide](firmware-upgrade.md) if you would like to test the latest version.

### Teardown (Optional)

If you enjoy teardowns, you are welcome to take the unit apart.

Your prototype includes the following components:

* **MS2130S** — Video capture chip
* **WCH CH32V208** — USB keyboard and mouse emulation MCU
* **Standard silicone thermal paste** — applied on this prototype

We are currently testing an upgraded thermal solution using **aluminum components** and **higher-performance thermal grease**. These improvements have passed internal testing, but because of limited prototype stock, they are **not included** in the review units yet.

Your unit still uses **silicone paste**, but thermal performance remains within safe limits.

### Advanced Features (Supported in Mini-KVM, Coming Soon to KVM-Go)

KVM-Go follows the same design philosophy as Openterface Mini-KVM. Several advanced features are under active development but **not available yet** in the current prototype:

* **Custom EDID**
  Mini-KVM allows loading or modifying EDID through our QT application to solve compatibility issues.
  We are bringing this feature to KVM-Go as well.

* **Software-based SD Card Switching**
  Mini-KVM supports switching its USB-A port between the host and PC through software.
  For KVM-Go, we are developing similar software-based switching for the micro-SD slot, but it is not enabled in your firmware yet.

We want you to be aware of these upcoming features even though they are not yet active on your unit.

### Open-Source Commitment

Yes, KVM-Go will remain fully open-source. Once the hardware design is finalized for mass production, we will apply for OSHWA certification (Open Source Hardware Association). All hardware design files and STL models will be uploaded to our GitHub repository at [https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware](https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware).

## Further Reading

* [KVM-Go Firmware Upgrade](firmware-upgrade.md) — Step-by-step guide for updating your device