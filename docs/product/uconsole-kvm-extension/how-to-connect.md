---
title: "How to Connect"
description: "Step-by-step guide for setting up Openterface KVM Extension for uConsole. Learn how to connect your target device with detailed instructions for HDMI and USB connections."
keywords: "KVM extension setup, uConsole KVM connection, HDMI KVM setup, KVM installation guide, uConsole expansion, KVM interface guide, headless computer setup"
---

# **How to Connect** | Setup Guide | Openterface KVM Extension for uConsole

> **✅ Now Available** - Get your KVM Extension from [TechxArtisan Shop](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) and follow this guide to get started

## Quick Setup

**Setup in 3 simple steps:**

1. **Hardware Installation**: Install the KVM Extension board in your uConsole's expansion slot
2. **HDMI Connection**: Connect target device's video output to the extension board's HDMI port
3. **Software Setup**: Install and launch the Openterface App on your uConsole

!!! note "Requirements"
    - **uConsole**: Requires [Openterface App](/app) installed
    - **Target**: No app needed - supports Windows, macOS, Linux, Android, iOS
    - **Video**: Use standard HDMI cable

## Hardware Installation

### **Step 1: Power Off and Disconnect**
Shut down the uConsole and disconnect all power and cables.

### **Step 2: Remove Existing Module**
Use a hex screwdriver to remove the two screws holding the 4G/LTE module or existing extension board. Carefully lift the board straight up to avoid bending the spring contactors.

### **Step 3: Install KVM Extension Board**
- Place the provided gasket on the screw posts (between the PCB and mounting standoffs)
- Seat the KVM Extension board in the expansion slot
- The gasket compensates for the thinner PCB (1.0mm vs 1.2mm) and ensures proper spring contactor pressure

### **Step 4: Secure Installation**
Reinsert the two screws and tighten with the hex screwdriver. Snug is sufficient — do not overtighten.

### **Step 5: Verify Installation**
The board should sit flat with no noticeable movement. Verify spring contactors are making even contact across the pads.

## Connection Guide

### **HDMI Input Connection**
- **Port**: HDMI input on the KVM Extension board
- **Cable**: Standard HDMI cable (not included)
- **Source**: Connect to target device's HDMI output
- **Audio**: HDMI embedded audio is supported

### **Target Device Connection**
- **Compatibility**: Works with any device that has HDMI output
- **No Software Required**: Target device needs no special software
- **Power**: Target device should be powered independently

## Software Setup

### **Option 1: Flatpak Installation (Recommended)**
Follow our [Flatpak Installation Guide](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) for detailed setup steps.

### **Option 2: Community Repository**
If you prefer the community build maintained by Rex:

1. **Add Repository**:
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **Install Package**:
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "Repository Notes"
    These commands require sudo. The repository targets arm64 Bookworm packages; verify compatibility with your device before installing.

## Usage Instructions

### **Starting the KVM Session**
1. Launch the Openterface App on your uConsole
2. The app will automatically detect the KVM Extension board
3. Connect your target device via HDMI
4. Use uConsole's built-in keyboard and trackball to control the target device

### **Control Features**
- **Keyboard**: Full keyboard emulation including multimedia keys
- **Mouse**: Absolute and relative mouse positioning
- **Audio**: HDMI audio passthrough to uConsole speakers
- **Wake-up**: Can wake target devices from sleep

## Troubleshooting

### **No Video Signal**
- Check HDMI cable connection
- Verify target device is powered on
- Ensure target device is set to output via HDMI

### **Control Not Working**
- Restart the Openterface App
- Check that the KVM Extension board is properly seated
- Verify spring contactors are making good contact

### **Installation Issues**
- Ensure gasket is properly positioned
- Check that screws are not overtightened
- Verify board sits flat without movement

## Safety Guidelines

!!! warning "ESD Precautions"
    Use ESD precautions (wrist strap or grounded surface) when handling the extension board to prevent static damage.

!!! note "Power Management"
    Always power off the uConsole before installing or removing the extension board.

!!! tip "Cable Management"
    Keep HDMI cables away from sharp edges and avoid excessive bending to prevent damage.
