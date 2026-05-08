---
title: "KeyMod Tutorial - Gamepad"
description: "Use KeyMod as a virtual game controller with customizable layouts for gaming, retro emulation, and game testing."
keywords: "KeyMod gamepad, virtual controller, game controller, WASD mapping, analog stick"
---

# 8. Gamepad

Transform your phone into a virtual game controller for gaming, retro emulation, and game testing.

## The Layout

The gamepad provides a full controller layout with D-pad, action buttons, shoulder buttons, analog sticks, and Start/Select.

| Control | How |
|---|---|
| D-pad | Tap the directional arrows |
| Action buttons (A, B, X, Y) | Tap them |
| Shoulder buttons | Tap L1, L2, R1, R2 at the top |
| Analog sticks | Touch and drag the stick circles |
| Start / Select | Tap the buttons |

## Preset System (v7)

KeyMod 0.15 introduced a **preset-based gamepad system**. Instead of fixed built-in layouts, gamepad configurations are now saved as **presets** that you can cycle through, import, and export.

### Managing presets

- **Tap the Preset chip** in the toolbar to cycle through available layouts
- **Long-press the Preset chip** for the full preset list with import, add module, and export options
- The bundled **emu-6** layout ships as the starter preset (`preset_default`)
- Presets are shareable JSON files using layout **schema v7**

### Adding modules

From the preset menu, you can add new modules to any layout:

- **D-Pad / Stick** — adds a left-thumb module (`stick_left`, `stick_left_2`, etc.)
- **Touchpad** — adds a touchpad (`touchpad_1`, `touchpad_2`, etc.) with bundled L/M/R mouse buttons
- **Buttons** — add face buttons, shoulder buttons, or triggers

## Customizing

- **Configure any module** — tap a module to open its configuration dialog and adjust behavior
- **Analog vs Key mode** — sticks can be configured as `STICK_KEY` (digital direction keys) or `STICK_MOUSE` (relative pointer/mouse movement)
- **WASD mapping** — assign WASD keys to the left stick for PC gaming
- **Button/stick size scaling** — adjust sizes for your preferred touch area
- **Background image** — customize the gamepad background (embeds in shared presets as base64, up to 6 MiB)
- **Haptic feedback** — vibration on button press (face buttons only, not mouse clicks)
- **Gyro** — enable device gyroscope to move the host pointer while the gamepad screen is active

### Module model

Each on-screen control is a **module** with three layers:

| Layer | What it defines |
|---|---|
| **Slot / identity** | Which control on the canvas (e.g. `stick_left`, `stick_right`, `touchpad_1`) |
| **Behavior (type)** | What the host receives: `STICK_KEY`, `STICK_MOUSE`, `DPAD`, `BUTTON`, `TOUCHPAD` |
| **Parameters** | Tuning on the same module: `dpadVariant`, `stickMouseSensitivity`, `stickVisualVariant`, size, color |

### Analog Sticks

- **Left stick → Keyboard keys:** Maps to arrow keys with diagonal support. Configurable to WASD in the module configuration.
- **Right stick → Mouse movement:** `STICK_MOUSE` mode with configurable sensitivity (`stickMouseSensitivity`), dead zone to prevent drift.
- **Hysteresis:** Activation (0.6) and deactivation (0.4) thresholds prevent key chatter at the boundary.

### Touchpad

- **Multi-touchpad support**: add multiple touchpads to a single layout (`touchpad_1`, `touchpad_2`, etc.)
- **Square footprint** by default with long-press resize
- **Bundled mouse buttons** (L/M/R) shared across all touchpads
- **Mouse button sizing**: long-press a touchpad to adjust **Mouse button size**, or long-press an individual mouse button for **This button size**

> **Note:** Gamepad HID protocol is under active development. Basic button support works; analog stick precision may vary.

## Troubleshooting

### Analog Stick Not Responding

| Symptom | Solution |
|---|---|
| **Stick not producing action** | Check the module configuration. Verify the stick isn't stuck in the dead zone (center area). Check hysteresis thresholds — the stick needs to move past 0.6 activation to trigger. |
| **Buttons sending wrong keys** | Open the module configuration and check the button's key assignment. Tap the button to open the configuration popup and correct the mapping. |
| **Touchpad mouse buttons not clicking** | Ensure bundled L/M/R buttons are present in the preset. Adding a touchpad automatically adds shared mouse buttons. Check the module configuration for the assigned HID key. |

## Next Steps

- **[← AI Integration](07-ai.md)** — AI-assisted text refinement and command assistant
- **[Numpad →](09-numpad.md)** — Numeric keypad for data entry
