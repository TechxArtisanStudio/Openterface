---
title: FAQs for Openterface KeyMod
description: Frequently asked questions about KeyMod, covering features, compatibility, platforms, and pre-launch information.
keywords: KeyMod, Openterface, HID emulator, Bluetooth keyboard, phone keyboard, open-source, pre-launch, Android, iPadOS
---

# FAQs for Openterface KeyMod

Welcome to the FAQ for **Openterface KeyMod**.  
If you don't find what you need, **email us at [info@openterface.com](mailto:info@openterface.com)** or **join our community** on [Discord](/discord) or [Reddit](/reddit).

⚠️ **Note**: KeyMod is currently in pre-launch development. Features, specifications, and design are subject to change as we finalize the product.

---

## :material-clipboard-list: Quick Navigation

- [FAQs for Openterface KeyMod](#faqs-for-openterface-keymod)
  - [:material-clipboard-list: Quick Navigation](#material-clipboard-list-quick-navigation)
  - [General](#general)
  - [Connectivity](#connectivity)
  - [Features](#features)
  - [Pre-Launch](#pre-launch)

---

## General

**:material-chat-question:{ .faq } What is KeyMod?**

KeyMod is a compact USB + Bluetooth HID (keyboard and mouse) emulator that turns your phone into a portable keyboard and trackpad. Use it to control devices that need keyboard/mouse input—kiosks, smart TVs, set top boxes, outdoor displays—without carrying a full keyboard.

**:material-chat-question:{ .faq } What platforms does the KeyMod app support?**

The KeyMod controller app focuses on **Android** and **iPadOS**. We are also expanding desktop control with **Windows and macOS** software in our broader Openterface ecosystem.

**:material-chat-question:{ .faq } Does the target device need any software?**

No. KeyMod emulates a standard USB keyboard and mouse. The target device recognizes it as plug-and-play HID hardware—no drivers or software installation required.

**:material-chat-question:{ .faq } Is KeyMod open source?**

Yes. KeyMod is open hardware and open software. We will publish schematics, PCB files, firmware, software, and BOM as the project evolves.

---

## Connectivity

**:material-chat-question:{ .faq } USB vs Bluetooth—which should I use?**

- **USB**: More reliable, lower latency. Use when you want the most stable connection.
- **Bluetooth**: Cable-free. Use when you want a lighter setup and the scenario allows wireless.

**:material-chat-question:{ .faq } What hardware variants are planned?**

1. **2-in-1 Connector** — Combined USB A + USB C plug for broad compatibility
2. **USB C Version** — Dedicated USB C plug for modern devices

---

## Features

**:material-chat-question:{ .faq } What gamepad layouts are supported?**

KeyMod can act as a virtual game controller with **Xbox layout**, **PlayStation layout**, and **NES layout**.

**:material-chat-question:{ .faq } Can I create custom profiles and macros?**

Yes. The open source mobile app supports custom input profiles, macros, hotkeys, and workflow shortcuts. You can also use keypad and gamepad modes.

**:material-chat-question:{ .faq } What are the programmable hardware buttons?**

KeyMod includes programmable hardware buttons for on-device actions like quick triggers and simple macro-style workflows. This capability is still experimental and will be refined through community feedback.

---

## Pre-Launch

**:material-chat-question:{ .faq } When will KeyMod launch?**

KeyMod is in pre-launch development. Subscribe on the [product page](/product/keymod/) for launch notifications and updates.

**:material-chat-question:{ .faq } How is KeyMod related to Mini-KVM and KVM-Go?**

KeyMod uses the proven HID core from Openterface Mini-KVM. It shares the same hardware-based keyboard and mouse emulation approach but is designed for a different use case: turning your phone into a portable keyboard/trackpad for local device control, rather than KVM-over-USB video capture.
