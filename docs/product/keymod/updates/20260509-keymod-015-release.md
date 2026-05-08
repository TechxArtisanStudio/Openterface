---
draft: false
date: 2026-05-09
title: "KeyMod 0.15: Gamepad Preset Pipeline, Keyboard & Mouse (Basic) Tier, Multi-Touchpad Layouts"
description: "KeyMod 0.15 ships the gamepad preset pipeline with schema v7, multi-touchpad layouts, Keyboard & Mouse (Basic) tier with full-screen keyboard, and KeyMod branding across the app. A major step toward a polished input experience."
keywords: "KeyMod 0.15, KeyMod release, gamepad preset, multi-touchpad, keyboard mouse basic, KeyMod branding, Openterface KeyMod update, HID emulator, virtual gamepad, Android keyboard app"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyMod", "Product Updates", "Release", "Gamepad", "Keyboard", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 release — gamepad presets, basic tier, multi-touchpad"
  description: "KeyMod 0.15 brings gamepad preset pipeline v7, a dedicated Keyboard & Mouse (Basic) tier, multi-touchpad layouts, and fresh KeyMod branding."
---

# KeyMod 0.15: Gamepad Preset Pipeline, Keyboard & Mouse (Basic) Tier, Multi-Touchpad Layouts

KeyMod **0.15** (`versionCode` **15**) is a milestone release that ships three major features: the **gamepad preset pipeline** with layout schema **v6-v7**, the dedicated **Keyboard & Mouse (Basic)** tier, and **multi-touchpad** layouts. This update also brings full **KeyMod** branding across the welcome flow and build artifacts.

## Gamepad: Preset Pipeline v7

The gamepad now uses a proper **preset system** that lets you save, load, import, and export custom controller layouts.

### What changed

- **Preset store v7** replaces the old built-in layouts. The classic factory presets (`preset_classic_*`) and **Two buttons** (`preset_two_buttons`) have been removed from disk. Only **`preset_default`** remains as the deletion-protected factory layout.
- **Schema v7** makes **`stick_left`** optional. A layout can now have no left-thumb module at all. The **Add module** menu inserts **`stick_left`**, **`stick_left_2`**, **`stick_left_3`**, and so on.
- **Multi-touchpad support**: presets may include multiple touchpads (`touchpad_1`, `touchpad_2`). Adding a touchpad allocates the next available id with a slightly offset anchor. Bundled L/M/R mouse buttons are shared across all touchpads.
- **Touchpad mouse button sizing**: mouse buttons now use a larger default draw radius. You can adjust size via long-press **Mouse button size** on the touchpad, or **This button size** on individual mouse modules.
- **Aux stick defaults**: **`stick_left_2+`** default to D-pad cross + WASD mapping.

### Preset management

- **Tap** the Preset chip in the toolbar to cycle through available layouts
- **Long-press** for the full preset list with import, add module, and export options
- Bundled **emu-6** layout ships as the starter preset
- Export creator supports i18n for sharing presets across languages

## Keyboard & Mouse (Basic)

A dedicated full-screen keyboard tier designed for focused typing without the app header.

### What you get

- **Full-screen keyboard** without the main app header for more screen real estate
- **Portrait and landscape numpad**: 5x8 grid in portrait (PrtSc / ScrLk / Pause / Home / End), 8x5 grid in landscape with tall +, Enter, and 00
- **IME ASCII-only send gate**: type long text in compose mode, send as clean HID keystrokes
- **Long-press repeat**: hold character/function keys for auto-repeat (~400ms delay, ~50ms repeat)
- **Key preview**: floating bubble shows the effective label above the key when pressed
- **Haptic feedback** and **theme-aware** key surfaces

### Sticky vs Chord modifiers

Settings let you choose between **sticky modifiers** (tap to latch) and **momentary + long-press chord** (default) for the Basic keyboard.

## Branding

- App display name is now **KeyMod**
- Welcome screen shows the **KeyMod** wordmark
- CI artifacts and APK filenames use **KeyMod** prefix
- `applicationId` remains **`com.openterface.keymod`** for in-place upgrades

## What is unchanged

**Keyboard & Mouse Pro** (composite mode with Shortcut Hub strips, split layouts, and rich IME behavior) remains the full-featured experience it was before.

## Get the update

Download the latest APK from [GitHub Releases](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android/releases) or [GitHub Actions](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android/actions). Existing installs upgrade in place.

## Upgrade notes

- **Gamepad**: your previous two-button preference automatically activates the **Two buttons** preset on first launch. Use **Preset** (tap to cycle, long-press for the list) instead of the old 1 Button / 2 Buttons control.
- **Keyboard & Mouse (Basic)**: open Basic to experience the full-screen keyboard. Pro mode is available via the navigation drawer for the complete Shortcut Hub experience.

Best regards,

Openterface Team | TechxArtisan
