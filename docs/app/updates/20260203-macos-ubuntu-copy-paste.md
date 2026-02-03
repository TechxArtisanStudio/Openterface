---
title: Ubuntu Copy/Paste Tip (macOS → Ubuntu)
description: Fix paste shortcuts when controlling Ubuntu from macOS with Openterface. Use Windows Mode for reliable Ctrl-style paste, or Edit → Paste as a workaround in Mac Mode.
keywords: Openterface, macOS, Ubuntu, copy paste, keyboard mode, Windows Mode, Mac Mode, KVM, remote desktop
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Ubuntu Copy/Paste Tip (macOS → Ubuntu)

When controlling **Ubuntu** from **macOS** using **Openterface**, shortcut paste may not work reliably in **Mac Mode**. This guide shows the recommended fix and a simple workaround.

![setting](https://assets2.openterface.com/images/setting.webp)

---

## Quick Fix (Recommended for Ubuntu/Linux)

1. Open **Openterface** on macOS.
2. Go to **Settings**.
3. Find **Target device keyboard layout mode**.
4. Select **Windows Mode**.

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ Result: Paste shortcuts behave as expected on Ubuntu (Ctrl-style behavior).

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## Workaround (If you want to stay in Mac Mode)

If you prefer to keep **Mac Mode**, you can still paste reliably using the menu:

- **Edit → Paste**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ Result: Pasting works even if shortcut paste is inconsistent in Mac Mode.

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## Why this happens

Most Ubuntu apps use **Ctrl-based** shortcuts for paste. In some setups, **Mac Mode** shortcut mapping may not trigger paste consistently, while **Edit → Paste** works reliably.

---

## Quick Summary

- **Best experience on Ubuntu/Linux:** use **Windows Mode**
- **If you stay in Mac Mode:** use **Edit → Paste**

---

## Need help identifying the right mode for your setup?

If you're not sure which mode to use, here's a quick rule of thumb:

- If your target OS is **Ubuntu/Linux**, start with **Windows Mode** (most consistent for common shortcuts).
- If you mainly control **macOS targets** and want Mac-style shortcuts, use **Mac Mode**.

If you're switching between different target OSes often, consider keeping this page bookmarked. It's usually a one-click fix.

---

## FAQ

**Does Windows Mode change my Mac shortcuts?**  
It changes how Openterface sends shortcuts to the **target device**, so Ubuntu receives the expected **Ctrl-style** behavior.

**Can I use menu paste in any mode?**  
Yes — **Edit → Paste** is a reliable option in both modes.

**Does this affect Raspberry Pi OS too?**  
Often less affected, but if you see similar behavior, the same fix applies.
