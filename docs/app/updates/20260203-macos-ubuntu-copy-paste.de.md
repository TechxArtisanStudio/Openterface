---
title: Ubuntu Kopieren/Einfügen-Tipp (macOS → Ubuntu)
description: Beheben Sie Einfügen-Shortcuts beim Steuern von Ubuntu von macOS mit Openterface. Verwenden Sie den Windows-Modus für zuverlässiges Ctrl-Style-Einfügen oder Bearbeiten → Einfügen als Alternative im Mac-Modus.
keywords: Openterface, macOS, Ubuntu, Kopieren Einfügen, Tastaturmodus, Windows-Modus, Mac-Modus, KVM, Remote-Desktop
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Ubuntu Kopieren/Einfügen-Tipp (macOS → Ubuntu)

Beim Steuern von **Ubuntu** von **macOS** mit **Openterface** funktioniert das Einfügen per Shortcut im **Mac-Modus** möglicherweise nicht zuverlässig. Diese Anleitung zeigt die empfohlene Lösung und eine einfache Alternative.

![setting](https://assets2.openterface.com/images/setting.webp)

---

## Schnelle Lösung (empfohlen für Ubuntu/Linux)

1. Öffnen Sie **Openterface** auf macOS.
2. Gehen Sie zu **Einstellungen**.
3. Suchen Sie **Tastaturlayout-Modus des Zielgeräts**.
4. Wählen Sie **Windows-Modus**.

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ Ergebnis: Einfügen-Shortcuts verhalten sich unter Ubuntu wie erwartet (Ctrl-Style-Verhalten).

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## Alternative (wenn Sie im Mac-Modus bleiben möchten)

Wenn Sie den **Mac-Modus** beibehalten möchten, können Sie weiterhin zuverlässig über das Menü einfügen:

- **Bearbeiten → Einfügen**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ Ergebnis: Einfügen funktioniert auch, wenn Shortcut-Einfügen im Mac-Modus inkonsistent ist.

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## Warum passiert das?

Die meisten Ubuntu-Apps verwenden **Ctrl-basierte** Shortcuts zum Einfügen. In einigen Konfigurationen kann die **Mac-Modus**-Shortcut-Zuordnung das Einfügen nicht zuverlässig auslösen, während **Bearbeiten → Einfügen** zuverlässig funktioniert.

---

## Kurz zusammengefasst

- **Beste Erfahrung unter Ubuntu/Linux:** **Windows-Modus** verwenden
- **Bei Mac-Modus:** **Bearbeiten → Einfügen** verwenden

---

## Brauchen Sie Hilfe bei der Auswahl des richtigen Modus?

Wenn Sie unsicher sind, welchen Modus Sie verwenden sollen, hier eine einfache Faustregel:

- Wenn Ihr Ziel-OS **Ubuntu/Linux** ist, beginnen Sie mit dem **Windows-Modus** (am konsistentesten für gängige Shortcuts).
- Wenn Sie hauptsächlich **macOS-Ziele** steuern und Mac-Style-Shortcuts möchten, verwenden Sie den **Mac-Modus**.

Wenn Sie häufig zwischen verschiedenen Ziel-OS wechseln, bookmarken Sie diese Seite. Es ist meist eine Ein-Klick-Lösung.

---

## FAQ

**Ändert der Windows-Modus meine Mac-Shortcuts?**  
Er ändert, wie Openterface Shortcuts an das **Zielgerät** sendet, sodass Ubuntu das erwartete **Ctrl-Style**-Verhalten erhält.

**Kann ich Menü-Einfügen in jedem Modus verwenden?**  
Ja — **Bearbeiten → Einfügen** ist in beiden Modi eine zuverlässige Option.

**Betrifft das auch Raspberry Pi OS?**  
Oft weniger betroffen, aber bei ähnlichem Verhalten gilt dieselbe Lösung.
