---
title: FAQs for Openterface KVM-Go Series
description: Frequently asked questions about the KVM-Go Series, covering features, compatibility, and pre-launch information.
keywords: KVM-Go, Openterface, ultra-compact KVM, built-in HDMI, keychain KVM, open-source, pre-launch, video capture, USB, compatibility, MicroSD
---

# FAQs for Openterface KVM-Go Series

Welcome to the FAQ for our next-generation **Openterface KVM-Go Series**.  
If you don't find what you need, **email us at [info@openterface.com](mailto:info@openterface.com)** or **join our community** on [Discord](/discord) or [Reddit](/reddit).

⚠️ **Note**: KVM-Go is currently in pre-launch development. Features, specifications, and design are subject to change as we finalize the product.

---

## :material-clipboard-list: Quick Navigation

- [FAQs for Openterface KVM-Go Series](#faqs-for-openterface-kvm-go-series)
  - [:material-clipboard-list: Quick Navigation](#material-clipboard-list-quick-navigation)
  - [General](#general)
  - [MicroSD \& File Transfer](#microsd--file-transfer)
  - [Technical](#technical)
  - [Pre-Launch](#pre-launch)

---

## General

**:material-chat-question:{ .faq } What is KVM-Go?**

KVM-Go is our next-generation ultra-compact KVM-over-USB solution. It's keychain-sized with built-in video connectors (HDMI, DisplayPort, or VGA) that eliminate the need for separate cables.

**:material-chat-question:{ .faq } How small is it?**

Ultra-compact dimensions: **18 × 18 × 55 mm** (0.71 × 0.71 × 2.17 inches) — small enough to fit on your keychain. Weight is approximately **25g (0.9 oz)**.

**:material-chat-question:{ .faq } What models are available?**

- **KVM-Go HDMI Male** — Direct HDMI connection for modern devices
- **KVM-Go DisplayPort Male** — High-performance DisplayPort support  
- **KVM-Go VGA Male** — Legacy system compatibility (coming soon)

**:material-chat-question:{ .faq } How does this compare to Mini-KVM?**

Major improvements:

- **Size**: 18×18×55mm vs 61×53×13.5mm (much smaller)
- **Weight**: 25g vs 48g (lighter)
- **Video**: 4K@60Hz vs 1080p@30Hz (better performance)
- **USB**: USB 3.0 vs USB 2.0 (faster)
- **Setup**: Built-in connectors vs separate cables (easier)

---

## MicroSD & File Transfer

**:material-chat-question:{ .faq } Can it transfer files?**

Yes — via the switchable MicroSD slot shared between host and target devices.

**:material-chat-question:{ .faq } How do I switch the MicroSD direction?**

Two ways:
1. **Hardware**: Press the physical button on the device
2. **Software**: Use the toggle in the host app

**:material-chat-question:{ .faq } What do the LED indicators mean?**

- **🔵 Blue LED**: MicroSD card is mounted to the target device
- **🟢 Green LED**: MicroSD card is mounted to the host device
- **LED OFF**: No MicroSD card inserted or device powered off
- **LED FLASHING**: MicroSD card is being read from or written to

---

## Technical

**:material-chat-question:{ .faq } What's the video performance?**

- **Input**: Up to 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Output**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Latency**: Under 140ms for smooth control

**:material-chat-question:{ .faq } Open-source?**

Yes — certified by [OSHWA](https://certification.oshwa.org/cn000015.html). Hardware and software are on [GitHub](/contributing/).

**:material-chat-question:{ .faq } BIOS access**

Direct USB connection allows full BIOS-level control, unlike remote-only tools (VNC, TeamViewer).

**:material-chat-question:{ .faq } Cross-platform support?**

[Host apps](/app) compatible with macOS, Windows, Linux, Android, and Chrome web app for universal integration.

**:material-chat-question:{ .faq } Which video connector should I choose?**

- **HDMI**: Best for modern devices, servers, workstations
- **DisplayPort**: High-resolution displays, professional setups
- **VGA**: Legacy systems, older servers (coming soon)

---

## Pre-Launch

**:material-chat-question:{ .faq } When will KVM-Go be available?**

KVM-Go is currently in pre-launch development. We're refining the PCB and case designs. Join our [waiting list]({{ config.extra.kvmgo_purchase_link }}) to stay updated on progress and get early access.

**:material-chat-question:{ .faq } How much will it cost?**

Pricing will be announced during the official launch campaign. Early supporters will receive special discounts and priority access.

**:material-chat-question:{ .faq } Can I become a beta tester?**

Yes! If you have hardware and software testing experience, you’re welcome to apply for our beta testing program [here](https://forms.gle/yaS1F5E5MSo8DWNZ6).

**:material-chat-question:{ .faq } Are specifications final?**

No, features, specifications, and design are subject to change as we finalize the product during development.
