---
draft: false
date: 2026-05-09
title: "KeyMod 0.15: Gamepad-Preset-Pipeline, Tastatur & Maus (Basic)-Tier, Multi-Touchpad-Layouts"
description: "KeyMod 0.15 liefert die Gamepad-Preset-Pipeline mit Schema v7, Multi-Touchpad-Layouts, ein dediziertes Tastatur & Maus (Basic)-Tier mit Vollbild-Tastatur und KeyMod-Branding in der gesamten App. Ein wichtiger Schritt hin zu einer polierten Eingabe-Erfahrung."
keywords: "KeyMod 0.15, KeyMod Release, Gamepad-Preset, Multi-Touchpad, Tastatur Maus Basic, KeyMod Branding, Openterface KeyMod Update, HID-Emulator, virtuelles Gamepad, Android Tastatur-App"
author: "TechxArtisan Studio"
category: "Produkt-Updates"
tags: ["KeyMod", "Produkt-Updates", "Release", "Gamepad", "Tastatur", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 Release — Gamepad-Presets, Basic-Tier, Multi-Touchpad"
  description: "KeyMod 0.15 bringt die Gamepad-Preset-Pipeline v7, ein dediziertes Tastatur & Maus (Basic)-Tier, Multi-Touchpad-Layouts und frisches KeyMod-Branding."
---

# KeyMod 0.15: Gamepad-Preset-Pipeline, Tastatur & Maus (Basic)-Tier, Multi-Touchpad-Layouts

KeyMod **0.15** (`versionCode` **15**) ist ein Meilenstein-Release mit drei Hauptfunktionen: der **Gamepad-Preset-Pipeline** mit Layout-Schema **v6-v7**, dem dedizierten **Tastatur & Maus (Basic)**-Tier und **Multi-Touchpad**-Layouts. Dieses Update bringt außerdem vollständiges **KeyMod**-Branding im Willkommens-Flow und in den Build-Artefakten.

## Gamepad: Preset-Pipeline v7

Das Gamepad nutzt nun ein echtes **Preset-System**, mit dem ihr benutzerdefinierte Controller-Layouts speichern, laden, importieren und exportieren könnt.

### Was sich geändert hat

- **Preset-Store v7** ersetzt die alten eingebauten Layouts. Die klassischen Factory-Presets (`preset_classic_*`) und **Two Buttons** (`preset_two_buttons`) wurden von der Festplatte entfernt. Nur **`preset_default`** bleibt als löschgeschütztes Factory-Layout.
- **Schema v7** macht **`stick_left`** optional. Ein Layout kann nun überhaupt kein Linker-Thumb-Modul haben. Das **Add Module**-Menü fügt **`stick_left`**, **`stick_left_2`**, **`stick_left_3`** usw. ein.
- **Multi-Touchpad-Unterstützung**: Presets können mehrere Touchpads enthalten (`touchpad_1`, `touchpad_2`). Hinzufügen eines Touchpads belegt die nächste verfügbare ID mit leicht versetztem Anker. Gebündelte L/M/R-Maustasten werden über alle Touchpads hinweg geteilt.
- **Touchpad-Maustastengröße**: Maustasten verwenden nun einen größeren Standard-Zeichenradius. Größe anpassen per Long-Press **Mouse button size** auf dem Touchpad oder **This button size** auf einzelnen Mausmodulen.
- **Aux-Stick-Defaults**: **`stick_left_2+`** standardmäßig auf D-Pad-Kreuz + WASD-Mapping.

### Preset-Verwaltung

- **Tippt** den Preset-Chip in der Toolbar, um durch verfügbare Layouts zu schalten
- **Long-Press** für die vollständige Preset-Liste mit Import-, Add Module- und Export-Optionen
- Das mitgelieferte **emu-6**-Layout ist das Starter-Preset
- Der Export-Creator unterstützt i18n zum Teilen von Presets über Sprachen hinweg

## Tastatur & Maus (Basic)

Ein dediziertes Vollbild-Tastatur-Tier für konzentriertes Tippen ohne den App-Header.

### Was ihr bekommt

- **Vollbild-Tastatur** ohne Haupt-App-Header für mehr Bildschirmfläche
- **Porträt- und Landschafts-Numpad**: 5x8-Raster im Porträt (PrtSc / ScrLk / Pause / Home / End), 8x5-Raster in Landschaft mit hohem +, Enter und 00
- **IME ASCII-only Send-Gate**: Längeren Text im Compose-Modus eingeben, als saubere HID-Tastendrücke senden
- **Long-Press-Repeat**: Zeichen- oder Funktionstasten gedrückt halten für Auto-Repeat (~400 ms Verzögerung, ~50 ms Wiederholung)
- **Key-Preview**: Schwebende Blase zeigt das effektive Label über der gedrückten Taste
- **Haptisches Feedback** und **themengesteuerte** Tastenflächen

### Sticky vs Chord-Modifikatoren

Einstellungen ermöglichen die Wahl zwischen **sticky Modifiers** (Tippen zum Einrasten) und **momentary + Long-Press Chord** (Standard) für die Basic-Tastatur.

## Branding

- Der App-Anzeigename ist jetzt **KeyMod**
- Der Begrüßungsbildschirm zeigt die **KeyMod**-Wortmarke
- CI-Artefakte und APK-Dateinamen verwenden das **KeyMod**-Präfix
- `applicationId` bleibt **`com.openterface.keymod`** für In-Place-Upgrades

## Was unverändert bleibt

**Tastatur & Maus Pro** (Composite-Modus mit Shortcut-Hub-Strips, geteilten Layouts und reichem IME-Verhalten) bleibt die voll ausgestattete Erfahrung wie bisher.

## Update herunterladen

**Diese Version (0.15):** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

> **Beta-Hinweis:** Die KeyMod Android-App befindet sich noch in der aktiven Beta-Phase. Das Repo ist noch nicht öffentlich — wir planen, es nach einer erfolgreichen Crowdfunding-Kampagne zu open-sourcen. Wenn du Beta-Tester bist und den neuesten APK brauchst, meld dich bei uns auf Discord und wir schicken dir den Build.

> **Bekannte Probleme:** Dieses Release führt erhebliche Änderungen am Gamepad-Preset-System und dem Basic-Tastatur-Tier ein. Unser Dev-Team testet noch intern, es können also noch Bugs auftreten. Falls du auf etwas Unerwartetes stößt, melde es bitte auf Discord — dein Feedback hilft uns, schneller zu stabilisieren.

Bestehende Installationen werden vor Ort aktualisiert.

## Funktioniert mit Mini-KVM und KVM-Go

Die KeyMod-App ist nicht auf KeyMod-Hardware beschränkt. Bestehende Openterface-Nutzer können sie ebenfalls ausprobieren:

- **KVM-Go**: Verbindung über **Bluetooth** oder **USB**
- **Mini-KVM**: Verbindung über **USB**

## Upgrade-Hinweise

- **Gamepad**: Eure bisherige Zwei-Tasten-Präferenz aktiviert beim ersten Start automatisch das **Two Buttons**-Preset. Verwendet **Preset** (Tippen zum Schalten, Long-Press für die Liste) anstelle der alten 1 Button / 2 Buttons Steuerung.
- **Tastatur & Maus (Basic)**: Öffnet Basic, um die Vollbild-Tastatur zu erleben. Der Pro-Modus ist über das Navigations-Drawer für das komplette Shortcut-Hub-Erlebnis verfügbar.

Beste Grüße,

Openterface Team | TechxArtisan
