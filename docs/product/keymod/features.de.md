---
title: "Funktionen & Spezifikationen"
description: "KeyMod-Funktionen: Bluetooth-HID-Tastatur und -Maus, USB + Bluetooth Dual-Verbindung, benutzerdefinierte Profile, Makros, Gamepad-Modi. Open-Source-Mobil-App für Android und iPadOS."
keywords: "KeyMod-Funktionen, HID-Emulator, Bluetooth-Tastatur, USB-Tastatur, programmierbare Tasten, Gamepad, Makro, Open Source, CH9329"
---

# **Funktionen & Spezifikationen** | Openterface KeyMod

## Pre-Launch-Status

KeyMod befindet sich derzeit in der Pre-Launch-Entwicklung. Wir verfeinern die Hardware und Software. Abonnieren Sie die [Produktseite](/product/keymod/), um über Fortschritte und Launch-Benachrichtigungen informiert zu bleiben.

> **Hinweis:** Funktionen, Spezifikationen und Design können sich während der Entwicklung noch ändern.

## Produktvarianten

- **2-in-1-Stecker-Version** — Kombinierter USB-A- und USB-C-Stecker für breite Kompatibilität mit Laptops, Tablets und Smartphones
- **USB-C-Version** — Dedizierter USB-C-Stecker für moderne Geräte und übersichtliche Kabelverwaltung

## Kernfunktionen

### **Smartphone als Tastatur und Trackpad**

KeyMod verwandelt Ihr Smartphone in eine tragbare Tastatur- und Trackpad-Konsole. Verwenden Sie es, wenn eine vollständige Tastatur und Maus nicht verfügbar sind, oder wenn Sie einen schnelleren Workflow als beim Gerätewechsel wünschen. Ideal für Außendisplays, LED-Schilder-Player, Kioske, Smart-TVs und Set-Top-Boxen.

### **Dual-Verbindung: USB + Bluetooth**

- **USB** — Plug-and-Play-Kabelverbindung für zuverlässige, latenzarme Eingabe
- **Bluetooth** — Kabellose Einrichtung, wenn das Szenario es zulässt; halten Sie Ihr Setup leicht und tragbar

KeyMod ist für praktische tägliche lokale Gerätesteuerung konzipiert, nicht als Ersatz für Remote-Desktop.

### **Open-Source-Mobil-App**

Mit unserer Open-Source-Mobil-App können Sie:

- Benutzerdefinierte Eingabeprofile erstellen
- Makros starten und Hotkeys konfigurieren
- Erweiterte Modi nutzen: Tastenfeld und Gamepad
- Workflow-Verknüpfungen erstellen

Die KeyMod-Controller-App konzentriert sich auf **Android und iPadOS**. Wir erweitern auch die Desktop-Steuerung mit **Windows- und macOS-Software** in unserem breiteren Openterface-Ökosystem.

### **Virtueller Game-Controller**

KeyMod kann als virtueller Game-Controller mit vertrauten Layouts fungieren:

- **Xbox-Layout**
- **PlayStation-Layout**
- **NES-Layout**

### **Programmierbare Hardware-Tasten**

KeyMod enthält programmierbare Hardware-Tasten für On-Device-Aktionen wie Schnellauslöser und einfache Makro-Workflows. Diese Funktion ist noch experimentell und wird durch Prototyping, Tests und Community-Feedback verfeinert.

### **Echte Hardware-HID**

Basiert auf dem bewährten HID-Kern von Openterface Mini-KVM. Hardwarebasierte Tastatur- und Mausemulation—keine Softwareinstallation auf dem Zielgerät erforderlich.

### **Open Source**

KeyMod ist Open-Hardware und Open-Source-Software. Wir werden Schaltpläne, PCB-Dateien, Firmware, Software und BOM veröffentlichen, während das Projekt sich weiterentwickelt. [Treten Sie unserer Community bei](/discord), um beizutragen und auf dem Laufenden zu bleiben.

## Technische Spezifikationen

### **Konnektivität**

- **USB**: USB-C-Anschluss (2-in-1-Variante: USB A + USB C kombinierter Stecker)
- **Bluetooth**: HID-Tastatur und -Maus
- **Zielgerät**: Keine Softwareinstallation erforderlich

### **Wichtige Hardware**

- CH9329 HID-Emulator-Chip
- Bluetooth-Modul
- USB-C-Anschluss
- MCU
- Programmierbare(r) Taste(n)

### **Eingabefunktionen**

- Vollständige Tastatur- und Mausemulation (HID)
- Benutzerdefinierte Eingabeprofile
- Makros und Hotkeys
- Tastenfeld- und Gamepad-Modi
- Virtuelle Game-Controller-Layouts (Xbox, PlayStation, NES)
