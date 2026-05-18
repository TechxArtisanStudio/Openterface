---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19: App-Rebranding, KM Pro Compose-Modus, Mehrsprachige Unterstützung und Modus-führungen"
description: "KeyCmd 0.19 bringt ein wichtiges Rebranding von KeyMod zu KeyCmd, den neuen KM Pro Compose-Modus mit Unicode-HID-Senden, mehrsprachige UI (Koreanisch, Italienisch, Russisch, pt-BR), interaktive Modus-führungen und Dutzende UX-Verbesserungen."
keywords: "KeyCmd 0.19, KeyCmd Release, App-Rebranding, Compose-Modus, Unicode-HID-Senden, mehrsprachig, interaktive Modus-führungen, Openterface KeyCmd Update, HID-Emulator, virtuelle Tastatur, Android Tastatur-App"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "KeyCmd 0.19 Release — Compose-Modus, Rebranding, Mehrsprachigkeit, Modus-führungen"
  description: "KeyCmd 0.19 bringt den neuen Compose-Modus, App-Rebranding zu KeyCmd, 4 neue Sprachen, interaktive Modus-führungen und erhebliche UX-Verbesserungen."
---

# KeyCmd 0.19: App-Rebranding, KM Pro Compose-Modus, Mehrsprachige Unterstützung und Modus-führungen

KeyCmd **0.19** (`versionCode` **19**) ist ein großes Update, das das **App-Rebranding** von KeyMod zu KeyCmd, den brandneuen **KM Pro Compose-Modus** mit Unicode-fähigem HID-Senden, eine erweiterte **mehrsprachige UI** (einschließlich Koreanisch, Italienisch, Russisch und brasilianischem Portugiesisch), **interaktive Modus-führungen** und Dutzende von UX-Verbesserungen in Tastatur-, Gamepad- und Präsentationsmodi bringt.

## App-Rebranding: KeyMod → KeyCmd

Der App-Anzeigename ist jetzt an allen Einstiegspunkten **KeyCmd**. Dieses Rebranding verdeutlicht die Unterscheidung zwischen der **KeyMod-Hardware** und ihrer begleitenden **KeyCmd-App**.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="KeyCmd Willkommensbildschirm" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### Was sich geändert hat

- **App-Anzeigename**: Launcher-Symbol und System-UI zeigen jetzt „KeyCmd"
- **Willkommensablauf**: Wortmarke und Texte von KeyMod zu KeyCmd aktualisiert
- **CI-Artefakte und APK-Dateinamen**: Verwenden das **KeyCmd**-Präfix
- `applicationId` bleibt **`com.openterface.keymod`** für nahtlose Inplace-Upgrades

Bestehende Benutzer: Eure Einstellungen, Profile und gekoppelten Geräte werden beibehalten. Das Upgrade ist nahtlos.

## Tastatur & Maus: Vollbild-Erfahrung

KeyCmd bietet eine Vollbild-Tastatur-, Touchpad- und Ziffernblock-Erfahrung — optimiert für sowohl Porträt- als auch Landschaftsorientierung.

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-de" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="Vollbildtastatur Landschaft" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="Ziffernblock Landschaft" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="Ziffernblock Porträt" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="Tastatur und Touchpad Porträt" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="Touchpad Landschaft" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="Remote-Coding mit KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="KeyCmd Einstellungsbildschirm" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-de', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-de', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-de', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-de', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-de', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-de', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-de', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-de', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-de', 1)">❯</button>
  </div>
</div>

## KM Pro: Compose & Send-Modus

Das größte neue Feature in 0.19 ist der **Compose-Modus** in KM Pro — ein dedizierter Texteditor, der es euch ermöglicht, lange Texte einzugeben und als HID-Tastendrücke an das Zielgerät zu senden.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Skriptausführung im Compose-Modus" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">


### Compose-Editor

- **Obere Shortcut-Leiste + Composer-Aktionszeile** mit **Löschen**- und **Rückgängig/Löschen**-Steuerungen
- **Entwurfserhaltung**: Euer Text wird beim Wechseln von Submodi und sogar nach einem erfolgreichen Senden beibehalten
- **IME-Integration**: Tippt mit der Telefon-Tastatur, sendet als saubere HID-Tastendrücke
- **Determinierter Sende-Fortschritt**: Eine sichtbare Fortschrittsleiste für lange HID-Puffer, sodass ihr genau wisst, wie weit der Sende-Vorgang fortgeschritten ist

### Unicode-fähiges HID-Senden

- **Dual-Modus-Risikoprüfung**: Vor dem Senden von nicht-ASCII-Text warnt ein Dialog über Unicode-Kompatibilität und bietet Inspektions- und Vorschauaktionen
- **macOS Unicode-Hex-Flow**: Auf macOS-Hosts verwendet die App die Option+Hex-Code-Eingabemethode für erweiterte Zeichen
- **Sicherere Sende-Dialoge**: Der Prüfungsbildschirm passt seinen Inhalt basierend darauf an, ob der Puffer reines ASCII oder Unicode-Zeichen enthält
- **Zeicheninspektions-Tools**: Der Sende-Risiko-Dialog bietet **Prüfen**- und **Vorschau**-Aktionen, und macOS-Hosts enthalten einen dedizierten **Unicode-Hex-Pfad-Audit**-Eintrag

### KM Basic-Umfang

In 0.19 bleibt **Compose & Send eine Funktion von Tastatur & Maus Pro**. KM Basic konzentriert sich auf Vollbildtastatur-, Touchpad- und Ziffernblock-Workflows.

## Mehrsprachige Unterstützung

KeyCmd unterstützt jetzt **11 App-UI-Sprachen**. Dieses Release fügt vier neue Lokalisierungen hinzu:

- **Koreanisch (ko)**: vollständige UI-Übersetzung
- **Italienisch (it)**: vollständige UI-Übersetzung
- **Russisch (ru)**: vollständige UI-Übersetzung
- **Brasilianisches Portugiesisch (pt-BR)**: vollständige UI-Übersetzung

Zusammen mit dem bestehenden Englisch, vereinfachtem Chinesisch, traditionellem Chinesisch, Japanisch, Französisch, Deutsch und Spanisch deckt KeyCmd jetzt den Großteil unserer globalen Nutzerbasis ab.

### Was sich geändert hat

- **Sprachauswahl** in den Einstellungen mit kanonischen App-Sprachnamen
- **Bluetooth-Header** und **Tastenvorschau** lokalisiert
- **Release-Lint**-Korrekturen für Compose-Warn-Tabs in allen Sprachen

## Interaktive Modus-führungen

Jeder Modus hat jetzt eine **integrierte interaktive Modus-führung**, die euch Schritt für Schritt durch seine Funktionen führt.

### Verfügbare Modus-führungen

- **Shortcut Hub-Modus-führung**: Öffnet das Standard-Profil und deckt Detail-UI, Kategorie-Tabs und Shortcut-Verwaltung ab
- **Gamepad-Modus-führung**: Erklärt das Gamepad-Layout, Modulverwaltung und Voreinstellungssystem
- **KM Pro-Modus-führung**: Deckt den Compose-Modus, Shortcut-Panel und Pro-spezifische Funktionen ab
- **KM Basic-Modus-führung**: Erklärt die Vollbildtastatur, Modifikator-Halte-Wischgeste und Ziffernblock

### Modus-führungsfunktionen

- **Modus-spezifische Modus-führungen**: Jeder Modus hat seine eigene maßgeschneiderte Modus-führung
- **Wiederholungsblatt**: Jede Modus-führung jederzeit über die **Modus-führung**-Taste (Symbol links neben der Verbindungsleiste) erneut aufrufen
- **i18n-Unterstützung**: Modus-führungsinhalte sind in der gesamten App-Sprachmenge lokalisiert
- **Landschafts-optimiert**: Bottom-Sheet-Layouts passen sich in Landschaftsorientierung korrekt an

## UX-Verbesserungen

### Tastatur

- **Tastenvorschau**: Seht genau, was gesendet wird, bevor ihr tippt. Über Einstellungen aktivierbar. Standardmäßig aktiviert.
- **Schnell-Tipp-HID-Korrektur**: Verbessertes Timing der Tastenfreigabe und zusammengeführte Freigabe-Ereignisse für schnelleres Tippen
- **Alternativen-Tipp-Verarbeitung**: Langes Drücken der Taste `a` zeigt jetzt Alternativen für ¥ (oben), £ (links), € (rechts) mit verbessertem visuellen Feedback
- **Modifikator-Halte-Wischgeste**: In KM Basic/Pro-Modus-führungen lehrt ein neuer Schritt die Halte-Wischgeste für schnellen Modifikatorzugriff

### Gamepad

- **Bearbeitungs-Sitzungsleiste entfernt**: Saubereres Gamepad-Chrome ohne die alte Bearbeitungs-Sitzungs-Symbolleiste
- **Gamepad-Chrome und Modus-führung**: Neuer visueller Schliff und integrierte Modus-führung
- **Modus-führungssymbol**: Links neben der Verbindungsleiste für einfachen Zugriff platziert

### Präsentation

- **Porträt-Paar-Sperre**: Der Präsentationsmodus ist auf Porträt- und umgekehrte Porträt-Orientierungen für stabile Präsentationssteuerung beschränkt

### UI & Thema

- **Akzent-Farbfelder**: Ersetzt den Themenfarben-Familiendreher durch visuelle Akzent-Farbfelder für einfachere Farbauswahl
- **UI-Akzent-Ausrichtung**: Alle UI-Akzente folgen jetzt der Themenfarbenfamilie (nicht der Legacy-Primärfarbe)
- **Header-Rechts-Cluster**: Verbesserte Dimensionen für Verbindungssymbole sowohl in der Haupt-App als auch im KM Basic-Chrome
- **Compose-Sende-Taste-Styling**: Angeglichene nicht-ASCII-Sende-Tasten-Appearance im Hell-Modus

### Einstellungen

- **Einstellungs-Neuordnung**: Kanonische App-Sprachnamen; Emulator-Installationsskripte für Klarheit umbenannt
- **Dev-Helfer-Skripte**: Für klarere Geräte-Identifikation und Aktionsbenennung umbenannt
- **FAQ-Docs**: `docs/FAQ.md` mit aktuellem App-Verhalten aktualisiert

## Reale Anwendungsfälle

### Remote-Coding

KeyCmd ist nicht nur für die Serververwaltung gedacht. Entwickler verwenden es für **Remote-Coding-Sitzungen** — Steuerung einer Headless-Entwicklungsbox vom Telefon oder Tablet aus, mit vollständiger Tastatur-, Touchpad- und Ziffernblock-Unterstützung.

## Was unverändert bleibt

**Tastatur & Maus Pro** (Composite-Modus mit Shortcut Hub-Leisten, geteilten Layouts und reichem IME-Verhalten) bleibt die voll ausgestattete Erfahrung, die es vorher war. Alle bestehenden Profile, Voreinstellungen und gekoppelten Geräte werden beibehalten.

## Update holen

**Diese Version (0.19):** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Beta-Hinweis:** Die KeyCmd Android-App befindet sich noch in der aktiven Beta-Phase. Das Quellcode-Repo ist noch nicht öffentlich — wir planen, es nach einer erfolgreichen Crowdfunding-Kampagne zu open-sourcen. Wenn ihr ein Beta-Tester seid und die neueste APK benötigt, kontaktiert uns auf Discord und wir schicken euch den Build.

Bestehende Installationen werden vor Ort aktualisiert.

## Funktioniert mit Mini-KVM und KVM-Go

Die KeyCmd-App ist nicht auf KeyMod-Hardware beschränkt. Bestehende Openterface-Nutzer können sie ebenfalls ausprobieren:

- **KVM-Go**: Verbindung über **Bluetooth** oder **USB**
- **Mini-KVM**: Verbindung über **USB**

## Upgrade-Hinweise

- **Rebranding**: Der App-Name ändert sich von KeyMod zu KeyCmd. Eure Daten werden beibehalten.
- **Compose-Modus**: Neu für Tastatur & Maus Pro.
- **Modus-führungen**: Tippt in jedem Modus auf das Modus-führungssymbol (links neben der Verbindungsleiste), um die interaktive Modus-führung zu starten.
- **Sprachen**: Geht zu den Einstellungen, um die App-Sprache zu ändern. KeyCmd unterstützt jetzt 11 App-UI-Sprachen.

Mit freundlichen Grüßen,

Openterface Team | TechxArtisan
