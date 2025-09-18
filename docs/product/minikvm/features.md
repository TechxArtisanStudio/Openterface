---
title: "Features & Specifications"
description: "Complete overview of Openterface Mini-KVM: powerful features including BIOS-level access, 4K video support, cross-platform compatibility, USB sharing, and detailed technical specifications. Everything you need to know about this headless computer control solution."
keywords: "Mini-KVM features, KVM specifications, BIOS access, headless control, 4K KVM, USB sharing, cross-platform KVM, text transfer, plug and play KVM, open source KVM, technical specs"
---

# **Features & Specifications** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## Core Features

### **BIOS-Level Access**
Direct access to target device BIOS, firmware, and startup management without network dependencies.

### **Network Independence**
Stable headless control using HDMI video capture and emulated keyboard/mouse (HID) input. No network connection required.

### **High-Performance Video**
- **Input**: Up to 4K (3840×2160) @ 30Hz via HDMI
- **Output**: Full HD (1920×1080) @ 30Hz with under 140ms latency
- **Compression**: YUV and MJPEG support
- **Compatibility**: VGA, DVI, Micro HDMI via adapters

### **Switchable USB Port**
Toggle USB access between host and target devices for seamless USB drive sharing. Learn more on the [Switchable USB Port](../usb-switch) page.

### **Cross-Platform Support**
[Host apps](/app) compatible with macOS, Windows, Linux, and Android for universal integration.

### **Text Transfer**
Effortlessly transmit text by simulating keystrokes—perfect for usernames, passwords, and code snippets. Supports ASCII characters including symbols and punctuation.

!!! warning "Text Transfer Limitations"
    - **No Clipboard Integration**: Only emulates typing, no image or document transfer
    - **ASCII Only**: Limited to ASCII characters (no Chinese, Japanese, Korean support)
    - **Length Considerations**: Best for short text; large blocks may cause performance issues

### **Plug-and-Play Convenience**
No software installation required on target device. Control begins immediately upon connection with no software traces left behind.

### **Audio Integration**
HDMI embedded audio passthrough for complete multimedia experience.

### **Extension Pins**
[Extension pins](../extension-pins) enable advanced development and customization for specific needs.

### **Open-Source**
[Fully open-source](/compliance) hardware and software for transparency and [community innovation](/discord).

## Technical Specifications

### **Physical Dimensions**
- **Size**: 61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 inches)
- **Weight**: ~48g
- **Material**: Aluminum alloy, PLA casing

### **Connectivity & Power**
- **Power**: USB-C powered (no external supply needed)
- **USB Speed**: 12Mbps full-speed transmission
- **Host Compatibility**: Windows, macOS, Linux, Android
- **Target**: No software installation required

### **Video & Audio**
- **Max Input**: 3840×2160@30Hz (HDMI)
- **Max Output**: 1920×1080@30Hz
- **Latency**: Under 140ms
- **Audio**: HDMI embedded audio passthrough

### **Input Features**
- Full keyboard and mouse emulation (absolute & relative)
- Multimedia key support
- Custom HID functionality
- Computer wake-up function

### **Environmental**
- **Operating**: 0°C to 40°C
- **Storage**: -10°C to 50°C
- **Humidity**: 80% RH

## Product Models
- **Basic**: OP-MINIKVM-BASIC
- **Toolkit**: OP-MINIKVM-TOOLKIT

## Docs Downloads
- **[Quick Start Guide](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[Datasheet (English)](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}