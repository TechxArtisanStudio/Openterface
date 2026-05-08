---
title: "KeyMod Tutorial - Keyboard & Mouse"
description: "Learn how to use the KeyMod keyboard and touchpad to type, send shortcuts, and control your target computer's mouse from your phone."
keywords: "KeyMod keyboard, KeyMod mouse, touchpad, modifier keys, keyboard shortcuts"
---

# 2. Keyboard & Mouse

The Keyboard & Mouse mode is the most frequently used mode. It provides a virtual keyboard and touchpad for controlling the target computer from your phone.

## Two Tiers: Basic and Pro

KeyMod offers two keyboard experiences:

| Tier | Mode name | Best for |
|---|---|---|
| **Basic** | Keyboard & Mouse | Quick typing with a full-screen keyboard, no header distraction |
| **Pro** | Keyboard & Mouse Pro | Full composite layout with Shortcut Hub strips, split keyboard, and rich IME |

### Keyboard & Mouse (Basic)

The **Basic** tier gives you a **dedicated full-screen keyboard** without the app's top header. All controls live on the keyboard's own top row:

- Menu, mode switching (Touchpad / Compose & Send / Num pad)
- Target OS selector
- Connection status

**Features unique to Basic:**

- **Long-press repeat**: hold any character or function key for auto-repeat (~400ms delay, ~50ms repeat)
- **Key preview**: a floating bubble shows the effective label above the key when pressed
- **Haptic feedback** and **theme-aware** key surfaces
- **Portrait and landscape numpad**: 5x8 grid (portrait) or 8x5 grid (landscape)
- **IME compose mode**: type long text, send as clean ASCII-only HID keystrokes

> Basic does **not** include Shortcut Hub strip rows. For strip profiles, switch to **Keyboard & Mouse Pro**.

### Keyboard & Mouse Pro

**Pro** is the full composite experience: Shortcut Hub strip rows, split keyboard layouts, and the complete IME workflow. This is what power users expect.

## The Layout

**Portrait mode:**

<div align="center">
  <img src="https://assets2.openterface.com/images/keymod/andorid/demo-keyboard-mouse-portrait-touchpad-gestures.webp" alt="Portrait touchpad gesture help and keyboard" width="300" />
  <p><em>Portrait — touchpad gestures + keyboard layout. Swipe up/down on the touchpad to scroll, drag to move the cursor.</em></p>
</div>

**Landscape — split keyboard + touchpad:**

<div align="center">
  <img src="https://assets2.openterface.com/images/keymod/andorid/demo-keyboard-mouse-landscape-split-keyboard-touchpad.webp" alt="Landscape split keyboard and central touchpad" width="420" />
  <p><em>Landscape — split keyboard halves with touchpad on the left side for comfortable two-thumb typing.</em></p>
</div>

**Landscape — macro row + profiles:**

<div align="center">
  <img src="https://assets2.openterface.com/images/keymod/andorid/demo-keyboard-mouse-landscape-macro-strip.webp" alt="Landscape macro strip and profile selector" width="420" />
  <p><em>Landscape — macro strip above the keyboard and profile selector (e.g. Default, KiCAD).</em></p>
</div>

## Display Modes (Android)

Tap the **toggle handle** (pill-shaped divider between keyboard and touchpad) to cycle through display modes:

| Mode | What you see |
|---|---|
| **Both** (default) | Keyboard + touchpad together |
| **Keyboard only** | Full-width keyboard, touchpad hidden |
| **Touchpad only** (portrait) | Touchpad takes the full screen |
| **Split** (landscape) | Two half-keyboards with touchpad on the left |

## How to Use the Keyboard

| Action | How |
|---|---|
| Type a letter | Tap it |
| Uppercase letter | Tap **Shift** first, then the letter |
| Type a number or symbol | Tap **?123** to switch to the number/symbol layout |
| Type Ctrl+C (copy) | Tap **Ctrl** (it highlights), then tap **C** |
| Type Win+R (Run dialog) | Tap **Win**, then tap **R** |
| Access F1-F12 | Tap **Fn**, then the letter row becomes function keys |
| Multi-modifier (Ctrl+Shift+C) | Tap **Ctrl**, then **Shift** (both held), then **C** |

### Modifier Behavior

**Hold-and-tap:** Tap a modifier to hold it (it highlights), then tap any key. The modifier releases automatically after one key press. For multi-modifier combos, tap each modifier in sequence before tapping the final key.

### Long-Press Alternates

Many letter keys have **hidden symbols** you can access by pressing and holding:

```
Long-press "d" → shows: $  €  ¥  £
Long-press "k" → shows: (  {  [  <
Long-press "/" → shows: \  |
Long-press "m" → shows: +  _
```

Press and hold until a popup appears, then slide your finger toward the symbol you want and release.

### Fn Key Layer

Tap the **Fn** key in the modifier row. The letter keys temporarily become **F1 through F12**:

- Q = F1, W = F2, E = F3, R = F4, T = F5, Y = F6
- U = F7, I = F8, O = F9, P = F10
- A = F11, S = F12

## Quick-Action Buttons

Common shortcut buttons are available for quick access. The app uses the **Target OS** setting to determine the correct modifier:

| Action | macOS | Windows/Linux |
|---|---|---|
| Copy | Cmd+C | Ctrl+C |
| Paste | Cmd+V | Ctrl+V |
| Cut | Cmd+X | Ctrl+X |
| Undo | Cmd+Z | Ctrl+Z |
| Select All | Cmd+A | Ctrl+A |
| Redo | Cmd+Y | Ctrl+Y |
| Find | Cmd+F | Ctrl+F |
| Save | Cmd+S | Ctrl+S |
| New Tab | Cmd+T | Ctrl+T |
| Close Tab | Cmd+W | Ctrl+W |
| Next Tab | Cmd+Tab | Ctrl+Tab |
| Lock Screen | Cmd+L | Win+L |
| Show Desktop | Cmd+D | Win+D |
| Alt+F4 | — | Alt+F4 |
| Ctrl+Alt+Del | — | Ctrl+Alt+Del |

## TouchPad

### Gestures

| Gesture | Action |
|---|---|
| Tap | Left click |
| Two-finger tap | Right click |
| Drag | Move cursor |
| Two-finger swipe up/down | Scroll (natural scrolling) |
| Long-press | Drag mode (locks the cursor for dragging) |
| Double-tap | Double click |

### TouchPad Extras

- **Pop-out touchpad** — Tap the touchpad info icon (?) to open a floating touchpad that stays on top of other modes
- **TouchPad Help overlay** (Android) — Tap the **?** icon to see a full-screen gesture reference guide
- **Haptic feedback** — You'll feel a vibration on clicks and drag toggles

<div align="center">
  <img src="https://assets2.openterface.com/images/keymod/andorid/demo-keyboard-mouse-portrait-touchpad-numpad.webp" alt="Portrait touchpad and keypad grid" width="300" />
  <p><em>Portrait — touchpad with keypad grid on the right for quick number/symbol entry.</em></p>
</div>

## Text Input (IME Compose Mode — Android)

In portrait Keyboard & Mouse mode, you can switch to **IME capture mode** — a text editor below the keyboard where you compose longer text before sending it as HID keystrokes to the target computer.

- Tap the **keyboard/IME toggle** icon in the modifier row to switch between direct key sending and text compose mode
- In compose mode, you get a text editor with a toolbar for copy, paste, clear, undo, and send
- **Collapse/expand** the compose area with the arrow icon

<div align="center">
  <img src="https://assets2.openterface.com/images/keymod/andorid/demo-keyboard-mouse-portrait-long-text-compose.webp" alt="Portrait long text compose and Send" width="300" />
  <p><em>IME compose mode — type or paste long text, then tap Send to deliver it as HID keystrokes to the target.</em></p>
</div>

## Target OS

Set the target OS to match the target computer's key conventions. This affects shortcut labels, Unicode input methods, and modifier key mapping. Change it by tapping the **OS icon** in the header bar.

## Shortcut Strip (Android, Landscape)

In landscape split mode, a **scrollable shortcut strip** appears above the two keyboard halves, providing quick access to common shortcuts (Copy, Paste, Cut, Save, Undo, Select All).

## Next Steps

- **[Target-Specific Keyboard →](03-target-keyboard.md)** — Keyboard layouts and target OS mapping
- **[Troubleshooting →](12-troubleshooting.md)** — Common problems and solutions
