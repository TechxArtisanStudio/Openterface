---
title: "Features & Specifications"
description: "Complete overview of Openterface KVM-Go Series: ultra-compact design with built-in video connectors, 4K/60Hz support, MicroSD slot, and detailed technical specifications. Keychain-sized KVM-over-USB solution for IT professionals."
keywords: "KVM-Go features, ultra-compact KVM, built-in HDMI, 4K KVM, MicroSD KVM, keychain KVM, KVM specifications, headless control, portable KVM, IT tools, server management"
---

# **Features & Specifications** | Openterface KVM-Go Series

## Pre-Launch Status

The KVM-Go Series is currently in pre-launch development. We're refining the PCB and case designs. Join our [waiting list]({{ config.extra.kvmgo_purchase_link }}) to stay updated on progress and get early access.

> **Note:** Features, specifications, and design are still subject to change as development continues.

## Product Models
- **KVM-Go HDMI Male** — Direct HDMI connection
- **KVM-Go DisplayPort Male** — High-performance DisplayPort
- **KVM-Go VGA Male** — Legacy system support (in development)

## Core Features

### **Ultra-Compact Design**
Keychain-sized form factor that fits in your pocket. No more carrying bulky KVM devices or searching for video cables.

### **Built-in Video Connectors**
Direct plug-in capability with built-in male connectors:

- **HDMI Male** — Modern device compatibility
- **DisplayPort Male** — High-performance support
- **VGA Male** — Legacy system support (coming soon)

### **BIOS-Level Access**
Direct access to target device BIOS, firmware, and startup management without network dependencies.

### **Network Independence & Lightning-Fast Response**
Stable headless control using built-in video capture and emulated keyboard/mouse (HID) input. No network connection required. Hardware startup time is less than 1 second, ensuring immediate troubleshooting without workflow delays.

### **Upgraded Video Performance**
Massive upgrade from Mini-KVM's 1080p@30Hz:

- **Input**: 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Output**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Default**: 1080p@60Hz for optimal stability and performance
- **4K Mode**: Available as experimental feature*
- **Compression**: YUV420, YUV444, and MJPEG support

*Note: 4K mode generates additional heat; device surface may become quite hot during extended operation

### **MicroSD Slot**
File transfer between host and target devices

### **Cross-Platform Support**
[Host apps](/app) compatible with macOS, Windows, Linux, Android, and Chrome web app for universal integration.

### **Text Transfer**
Effortlessly transmit text by simulating keystrokes—perfect for usernames, passwords, and code snippets. Supports ASCII characters including symbols and punctuation.

- **Host → Target**: Send text via emulated keyboard strokes
- **Target → Host**: Copy text from target's screen to host via OCR (macOS only)

!!! warning "Text Transfer Limitations"
    - **No Clipboard Integration**: Only emulates typing, no image or document transfer
    - **ASCII Only**: Limited to ASCII characters (no Chinese, Japanese, Korean, etc. support)
    - **Length Considerations**: Best for short text; large blocks may cause performance issues
    - **OCR Feature**: Target → Host text transfer currently only available on macOS

### **Plug-and-Play Convenience**
No software installation required on target device. Control begins immediately upon connection with no software traces left behind.

### **Audio Integration**
HDMI embedded audio passthrough for complete multimedia experience. (Not supported on KVM-Go VGA; pending confirmation for KVM-Go DP.)

### **Bluetooth Capability**
Built-in Bluetooth support enables native iPadOS app functionality (coming soon), making KVM-GO one of the few KVMs that works natively with iPads.

### **Open-Source**
[Fully open-source](/compliance) hardware and software for transparency and [community innovation](/discord).

## Technical Specifications

### **Physical Dimensions** *(subject to change before fulfillment)*
- **Size**: 18 × 18 × 55 mm (0.71 × 0.71 × 2.17 inches)
- **Weight**: ~25 g (0.9 oz)
- **Material**: Aluminum alloy casing with 3D-printed caps

### **Connectivity & Power**
- **Power**: USB-C powered (no external supply needed)
- **USB Speed**: USB 3.0 for HDMI/DP versions; USB 2.0 for VGA version;
- **Host Compatibility**: Windows, macOS, Linux, Android, Chrome
- **Target**: No software installation required

### **Video & Audio**
- **Max Input**: 4096×2160@60Hz (YUV420), 4096×2160@30Hz (YUV444)
- **Max Output**: 4096×2160@60Hz (MJPEG), 3840×2160@30Hz (YUV420)
- **Audio**: HDMI embedded audio passthrough

### **Input Features**
- Full keyboard and mouse emulation (absolute & relative)
- Multimedia key support
- Custom HID functionality
- Computer wake-up function

### **Storage**
- **MicroSD Slot**: File transfers via MicroSD between host and target