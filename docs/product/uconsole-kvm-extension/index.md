# Openterface KVM Extension for uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## Overview

Transform your uConsole into a **portable KVM (Keyboard, Video, Mouse) console** with this plug-and-play extension board.

The **Openterface KVM Extension** replaces the original 4G/LTE modem in your uConsole’s expansion slot and provides direct **HDMI input and USB HID control**, allowing you to manage headless devices on the go—without the need for external monitors, keyboards, or network configuration.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## Features

- **Perfect Form Factor**  
    Matches the 37×77 mm size of the 4G/LTE module for seamless hardware integration.

- **Direct HDMI + USB HID**  
    Enables responsive control of connected devices using uConsole's built-in input and screen.

- **Low Latency**  
    Suitable for BIOS-level troubleshooting and real-time interaction.

- **Truly Portable**  
    Makes the uConsole a mobile tool for developers, engineers, and technicians.

- **Open-Source Friendly**  
    Built on the [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt) platform. Community contributions welcome.


## Use Cases

- **System Administration**  
    Access and troubleshoot servers or embedded devices without a bulky KVM switch.

- **Hardware Development**  
    Test and debug Raspberry Pi, SBCs, or microcontrollers directly.

- **Field Deployment**  
    Perform maintenance or configuration in data centres or remote locations.


## Hardware Installation

Follow these hardware installation steps to replace the 4G/LTE module in your uConsole with the Openterface KVM Extension board and ensure a secure fit.

### What You’ll Need

- Your Openterface KVM extension board
- The provided gasket (plastic shim) 
- A Hex screwdriver (for the board’s mounting screws)
- ESD precautions (wrist strap or grounded surface) — recommended

### Installing the Extension Board

1. Power Off and Disconnect

    Shut down the uConsole and disconnect all power and cables.

2. Remove the Existing Module

    Use a hex screwdriver to remove the two screws holding the 4G/LTE module or existing extension board.

    Carefully lift the board straight up to avoid bending the spring contactors.

3. Install the KVM Extension Board

    - The Openterface KVM Extension board is 1.0 mm thick (thinner than the original 4G/LTE 1.2 mm). Because of this, we recommend placing the provided gasket on the screw posts (between the PCB and the mounting standoffs) so the gasket sits under the screw posts before seating the board. This compensates for the thinner PCB and helps ensure proper spring contactor pressure.
    - If you prefer to check first, seat the board without the gasket and verify even spring contact; if contact is uneven or the board sits loosely, add the gasket and reseat the board.

![Installing KVM Extension into uConsole](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp)

4. Reinsert Screws

    Reinsert the two screws and tighten with the hex screwdriver. Snug is sufficient — do not overtighten.

5. Verify Fit

    The board should sit flat with no noticeable movement. Verify spring contactors are making even contact across the pads.

6. Test the Hardware

    Reconnect power, boot the system, and test HDMI, audio, and USB HID devices to confirm proper operation.

## Software Setup Guide

To use the KVM Extension, install the **Openterface App** on your uConsole.

Option 1 - Use Flatpak version Openterface
- 📖 Follow our [Flatpak Installation Guide](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) for detailed setup steps.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp)

Option 2 - Install community version from Rex

If you want the community build maintained by Rex, add his repository and install the package with the commands below.

1. Add the repository GPG key and repository

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. Update and install

```bash
sudo apt update
sudo apt install openterfaceqt
```

Notes: these commands require sudo. The repository targets arm64 Bookworm packages; verify compatibility with your device before installing.

## Pre-Launch Status

- 📦 First batch currently in preparation  
- ⏳ Estimated shipping begins in **early August 2024**  
- 🛒 Limited quantity – [Pre-order now](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) to reserve your unit

> **Pre-Order Notice**  
> This item is currently in pre-order with an estimated lead time of **approximately 2 months**.  
> If you require other items sooner, please place a **separate order**. Combined orders will ship when this product is ready.

## Community & Support

- 🗨️ Join the discussion: [Discord Server](https://discord.gg/ruAD9kcYbq)  
- 📧 Email support: [info@openterface.com](mailto:info@openterface.com)


## FAQs

**Q: How does the KVM Extension Board work?**  
It captures HDMI output from a target device and displays it on the uConsole. At the same time, the uConsole’s keyboard and trackball are used to control the target device via USB HID emulation.

**Q: Can I use this with the 4G/LTE module installed?**  
No. This board occupies the same expansion slot. You’ll need to choose between cellular connectivity or KVM functionality.

**Q: Is the software open source?**  
Yes! Our **Openterface Connect** Apps are fully open-source and available on our [GitHub repository](https://github.com/TechxArtisanStudio/Openterface_QT).