---
title: "KeyMod Tutorial"
description: "Complete guide to using the KeyMod app. Learn how to connect, control your computer from your phone, and use keyboard, mouse, gamepad, macros, and voice input modes."
keywords: "KeyMod tutorial, how to use KeyMod, phone keyboard guide, KeyMod app tutorial"
---

# KeyMod Tutorial

{% include "partials/keymod-tutorial-slideshow.html" %}

This tutorial covers the **Android** version of the KeyMod app. The iOS version is under development.

## What is KeyMod?

KeyMod transforms your phone or tablet into a **universal input device** for any computer. It connects to the **Openterface KeyMod** hardware (a KVM — Keyboard, Video, Mouse switcher), which then sends your phone's keystrokes, mouse movements, and gamepad inputs to a target computer as if they came from a real USB keyboard and mouse.

### How the connection works

```
[ Your Phone ] ──USB/BLE──> [ KeyMod Hardware ] ──USB HID──> [ Target Computer ]
   (KeyMod app)                (CH9329 protocol)              (Windows/macOS/Linux)
```

The app communicates with the KeyMod hardware using the **CH9329 protocol** over a serial connection (USB-C at 115200 baud, 8N1, or Bluetooth BLE). The KeyMod device appears to the target computer as a standard USB keyboard and mouse — no drivers needed.

### Who is this for?

| You are... | KeyMod helps you... |
|---|---|
| **System Administrator** | Manage servers from your phone without carrying a spare keyboard and monitor |
| **Presenter / Speaker** | Control slides from anywhere in the room, no clicker needed |
| **Gamer** | Use your phone as a gamepad for retro gaming or as an extra controller |
| **Content Creator** | Trigger shortcuts, macros, and voice input while recording on another machine |
| **Power User** | Send complex keyboard shortcuts, text snippets, or automation sequences from your phone |
| **Anyone** | Type on your computer from your couch, bed, or across the room |

## Tutorial Sections

| Guide | Description |
|---|---|
| [1. Getting Started](01-getting-started.md) | Install, connect, and pick your first mode (5 minutes) |
| [2. Keyboard & Mouse](02-keyboard-mouse.md) | Typing, modifiers, touchpad, and text input |
| [3. Target OS](03-target-keyboard.md) | Target operating system mapping |
| [4. Shortcut Hub](04-shortcuts.md) | Profile-based keyboard shortcuts for popular apps |
| [5. Macros](05-macros.md) | Automated key sequences with delays |
| [6. Voice Input](06-voice-input.md) | Speech-to-keyboard with Whisper AI |
| [7. AI Integration](07-ai.md) | Text refinement and command assistant |
| [8. Gamepad](08-gamepad.md) | Virtual game controller with customizable layouts |
| [9. Numpad](09-numpad.md) | Numeric keypad for data entry |
| [10. Presentation](10-presentation.md) | Slide remote control and timer |
| [11. Settings](11-settings.md) | App configuration and preferences |
| [12. Troubleshooting](12-troubleshooting.md) | Common problems and solutions |

## Getting Help

- **Bug reports:** [GitHub Issues](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android/issues)
- **Community:** [TechxArtisan Discord](https://discord.gg/techxartisan)
- **Source code:** [Openterface_KeyMod_Android](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android)
