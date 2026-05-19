---
draft: false
date: 2026-05-21
title: "KVM-GO Update: Steuern Sie Ihr Zielgerät vom Handy aus mit KeyCmd 0.19"
description: "Nutzen Sie KeyCmd 0.19 mit KVM-GO über USB oder Bluetooth: KM Basic und Pro Tastaturen, Compose-Modus, Gamepad-Presets, Shortcut Hub und Präsentationssteuerung – kein Video-Dongle für HID-Eingabe erforderlich."
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, KVM-GO Android App, KVM-over-USB Handy-Steuerung, Openterface KeyCmd, virtuelle Tastatur KVM, KVM-GO Bluetooth USB, KM Pro Compose Modus, KVM-GO HDMI DP VGA, Openterface KVM App, portable KVM Eingabe"
author: "Openterface Team | TechxArtisan"
category: "Produkt-Updates"
tags: ["KVM-GO", "KeyCmd", "Produkt-Updates", "Android", "USB", "Bluetooth", "Tastatur", "Gamepad", "Release"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 — Steuern Sie Ihr Zielgerät vom Handy aus"
  description: "KeyCmd 0.19 koppelt sich mit KVM-GO über USB oder Bluetooth für Tastatur, Maus, Gamepad, Shortcuts und Compose – während Openterface KVM das Video übernimmt, wenn Sie es brauchen."
---

# KVM-GO Update: Steuern Sie Ihr Zielgerät vom Handy aus mit KeyCmd 0.19

Hallo zusammen,

vielen Dank für Ihre Unterstützung von **KVM-GO** und für Ihre Geduld, während die Geräte produziert und versendet werden. Wir wissen, dass viele von Ihnen noch auf ihre Hardware warten, und wir möchten, dass sich Ihr Setup vom ersten Tag an komplett anfühlt.

Neben der **Openterface KVM** App (Video und volle KVM-Steuerung auf Ihrem Handy oder Tablet) haben wir **KeyCmd** verbessert, unsere Begleit-App für Tastatur-, Maus-, Gamepad- und Shortcut-Eingaben. **KeyCmd 0.19** ist die Version, die wir heute für die Nutzung mit KVM-GO empfehlen. Die Kopplung erfolgt über **USB** oder **Bluetooth**. Sie können sie einfach über jede vorherige Version installieren; Ihre Einstellungen, Profile und gekoppelten Geräte bleiben erhalten.

![KVM-GO an einem Laptop mit KeyCmd-Tastatur auf einem Handy](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp)

Im Folgenden erfahren Sie, was KeyCmd mit KVM-GO leistet, welchen Modus Sie für welche Aufgabe öffnen sollten und wie Sie das Beste daraus an einem echten Zielgerät herausholen.

![KeyCmd Willkommensbildschirm](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp)

## Modi und ihre Verwendung

### Tastatur & Maus (Basic)

Öffnen Sie diesen Modus, wenn Sie eine **einfache Vollbild-Tastatur** möchten und nichts anderes im Weg sein soll.

**Ideal für:** BIOS-Passwörter, kurze Shell-Befehle, Eingaben über den Ziffernblock oder Maussteuerung mit einem großen Touchpad, während KVM-GO Ihnen den Bildschirm zeigt.

**So verwenden Sie es:**

- Öffnen Sie **KM Basic** über das Navigationsmenü.
- Verwenden Sie die Bildschirmtastatur, den **Ziffernblock** (Hoch- oder Querformat) oder den **Touchpad**-Tab nach Bedarf.
- In den **Einstellungen** können Sie zwischen **Sticky Modifiers** (Tippen zum Einrasten von Shift/Strg) oder **Chord-Style** Modifikatoren wählen, wenn Sie Tastenkombinationen bevorzugen.

**Vorteile:** Mehr Platz auf dem Bildschirm für die Tasten, weniger Benutzeroberfläche, schneller, wenn Sie nur Eingaben und keine Shortcuts benötigen.

![KM Basic Vollbild-Tastatur](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp)

![KeyCmd Ziffernblock im Querformat](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp)

### Tastatur & Maus (Pro)

![KM Pro geteilte Tastatur im Querformat](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp)

![KeyCmd Tastatur und Touchpad im Hochformat](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp)

Öffnen Sie diesen Modus für die **tägliche Steuerungsarbeit** an Geräten hinter KVM-GO: geteilte Tastaturen, IME, Shortcut Hub Leisten und der **Compose**-Editor.

**Ideal für:** längeres Tippen, Makros und Shortcuts, das Senden von Textblöcken oder Skripten an den Host, während Sie das Ergebnis in der KVM-Ansicht beobachten.

![Compose-Modus beim Senden eines Skripts](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp)

**Compose** ist einen Versuch wert, wenn Sie häufig Befehle oder Skripte einfügen: Schreiben Sie auf Ihrem Handy, überprüfen Sie den Text und senden Sie ihn dann als Tastenanschläge an den Host. Eine [kurze Demo auf YouTube](https://www.youtube.com/watch?v=_rJF-hTF3_E) zeigt den Ablauf von Anfang bis Ende.

**So verwenden Sie es:**

- Öffnen Sie **KM Pro** über das Navigationsmenü.
- Verwenden Sie Tastatur und Touchpad wie in der Basic-Version, plus **Shortcut Hub** Kategorien am oberen Rand für Ein-Klick-Aktionen, die Sie in Profilen eingerichtet haben.
- Öffnen Sie **Compose**, um längere Texte auf Ihrem Handy zu entwerfen, zu überprüfen und dann als HID-Tastenanschläge zu **senden**. Bei langen Sendevorgängen wird ein Fortschrittsbalken angezeigt. Wenn Ihr Text Nicht-ASCII-Zeichen enthält, warnt die App Sie vor dem Senden, damit Sie die Host-Kompatibilität prüfen können (besonders hilfreich unter macOS).

**Vorteile:** Ein Ort für Texteingabe, Maussteuerung, Shortcuts und paste-ähnliche Workflows, ohne eine physische Tastatur zum Zielgerät mitführen zu müssen.

### Gamepad

Öffnen Sie diesen Modus, wenn Sie ein **virtuelles Controller-Layout** auf dem Bildschirm wünschen, das für Spiele oder Apps optimiert ist, die ein Gamepad erwarten.

**Ideal für:** Emulatoren, Gelegenheitsspiele oder eine kompakte Steuerfläche mit Sticks und Tasten, während KVM-GO die Anzeige übernimmt.

**So verwenden Sie es:**

- Wechseln Sie in den **Gamepad**-Modus.
- Tippen Sie auf **Preset** in der Toolbar, um durch gespeicherte Layouts zu **blättern**. **Halten Sie Preset gedrückt**, um die vollständige Liste zu öffnen, Layouts zu **importieren/exportieren** oder **Module hinzuzufügen** (Sticks, Tasten, Touchpads).
- Starten Sie mit dem mitgelieferten **emu-6** Preset und bearbeiten Sie es nach Ihren Wünschen. Sie können **mehrere Touchpads** und zusätzliche Stick-Module in einem Layout hinzufügen.

**Vorteile:** Sie sind nicht auf ein festes Layout beschränkt; speichern Sie Layouts pro Spiel oder pro Maschine und teilen Sie Presets mit anderen.

![Gamepad Preset Layout](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp)

![Gamepad Preset genutzt in Minecraft](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp)

*Angepasstes Preset für Minecraft.*

### Shortcut Hub

Dies ist die Zentrale für **Profile und Shortcuts** innerhalb von KM Pro: Kategorien, Detail-Panels und die Shortcuts, die Sie den Leisten zuweisen.

**Ideal für:** wiederkehrende Aufgaben auf dem Zielgerät (Terminal öffnen, Befehlskette einfügen, Einstellungen umschalten), während KVM-GO für das Video verbunden bleibt.

**So verwenden Sie es:**

- Arbeiten Sie in KM Pro im **Default**-Profil (oder Ihrem eigenen).
- Nutzen Sie Kategorie-Tabs und die Detail-UI, um Shortcuts zu verwalten.
- Starten Sie die **Shortcut Hub Tour**, wenn Sie neu in der Organisation von Profilen sind.

### Präsentation

Eine einfachere Steuerung im **Presenter-Stil**, die im **Hochformat** gehalten ist, damit die Tasten nicht springen, wenn Sie das Handy drehen.

**Ideal für:** das Durchblättern von Folien oder einfache Präsentationssteuerungen am Zielgerät.

![Präsentationsmodus zur Steuerung von Google Slides](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp)

---

## Sprachen

Die App-Benutzeroberfläche ist in **11 Sprachen** verfügbar. Neu hinzugekommen sind: Koreanisch, Italienisch, Russisch und Brasilianisches Portugiesisch.

Öffnen Sie **Settings** → **App language**, um die Sprache zu ändern.

---

## KeyCmd 0.19 herunterladen und mit KVM-GO verbinden

**Download:** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

Installieren Sie die Version über Ihre bestehende App, falls vorhanden. Ein Löschen der Daten ist nicht erforderlich.

**Verbindung mit KVM-GO (Video-Port kann ausgesteckt bleiben):**

Bei **allen drei KVM-GO Varianten** (HDMI, VGA und DP) müssen Sie den **Videoanschluss am Dongle** für die KeyCmd-Eingabe nirgendwo einstecken. Der HDMI-, VGA- oder DP-Port kann leer bleiben. Wählen Sie eines der folgenden Setups.

**Option A — Bluetooth (Zielgerät versorgt KVM-GO mit Strom)**

1. Stecken Sie das **kurze schwarze USB-Kabel** in den **Target**-Port des KVM-GO und in das Gerät, das Sie steuern möchten. Diese Verbindung allein **versorgt** KVM-GO mit Strom.
2. Öffnen Sie auf Ihrem Handy **KeyCmd** und suchen Sie KVM-GO über **Bluetooth**.

**Option B — USB zu Ihrem Android-Handy (Host-Port)**

1. Verbinden Sie das **lange orangefarbene Kabel** vom **Host**-Port des KVM-GO mit Ihrem Android-Handy.
2. Öffnen Sie **KeyCmd** und verbinden Sie sich in der App über **USB**.

![KVM-GO Target-Port verbunden mit einem Laptop über das kurze schwarze USB-Kabel](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp)

Für Vollbild-Video plus Eingabe verwenden Sie **Openterface KVM** für die Anzeige des Zielgeräts und **KeyCmd** für Tastatur, Maus und Shortcuts. KeyCmd allein reicht aus, wenn das Zielgerät bereits einen eigenen Bildschirm hat und Sie nur die Eingabe benötigen.

**Funktioniert auch mit Mini-KVM** über USB, falls Sie beide Geräte nutzen.

> **Noch Beta.** Gamepad-Presets und Compose-Sendevorgänge können sich je nach Host-Betriebssystem unterschiedlich verhalten. Wenn etwas Ungewöhnliches mit KVM-GO passiert, kontaktieren Sie uns auf **Discord** mit einem Screenshot, Ihrer KVM-GO Variante (HDMI / DP / VGA) und dem, was Sie erwartet haben.

> **Quellcode:** Noch nicht öffentlich. Wir planen, ihn nach Erreichen von Crowdfunding-Meilensteinen für verwandte Projekte als Open Source zu veröffentlichen. Fragen Sie auf Discord nach, wenn Sie Hilfe beim Finden der APK benötigen.

---

## Über KeyMod (optional, separat von KVM-GO)

Wir entwickeln auch **[KeyMod](https://openterface.com/product/keymod/)**, einen dedizierten USB- und Bluetooth-HID-Dongle für dieselbe KeyCmd-App. KVM-GO Unterstützer benötigen KeyMod für die oben genannten Workflows nicht; KeyCmd über KVM-GO ist der Weg, den wir Ihnen jetzt empfehlen.

Wenn Sie neugierig auf einen eigenständigen Dongle für Nicht-KVM-Setups sind, können Sie die [KeyMod-Kampagne auf Crowd Supply](https://www.crowdsupply.com/techxartisan/openterface-keymod) verfolgen. Dies ist unabhängig von der KVM-GO Auslieferung.

---

## Wir freuen uns auf Ihr Feedback

Wenn Sie ein paar Minuten Zeit haben, installieren Sie **KeyCmd 0.19**, verbinden Sie es mit Ihrem KVM-GO (oder Mini-KVM) und sagen Sie uns, was sich noch unpraktisch anfühlt. Berichte aus Crash-Cart- und Homelab-Szenarien fließen direkt in unsere nächsten Releases ein.

Praktische Wege, das KVM-GO Projekt zu unterstützen:

- **Teilen Sie, was funktioniert**, auf Discord oder in Ihrer Community (BIOS-Tipps, Bluetooth-Kopplung, Lieblingsmodi)
- **Empfehlen Sie uns einem Kollegen**, der Headless-Systeme betreibt und ein KVM für die Hosentasche gebrauchen könnte
- **Senden Sie uns weiterhin ehrliches Feedback**, besonders zu Ecken und Kanten. Das prägt das Produkt mehr als reine Begeisterung

Vielen Dank nochmals für Ihre Unterstützung von KVM-GO und dafür, dass Sie uns helfen, portable KVM-over-USB Lösungen für alle besser zu machen.

Beste Grüße,

**Openterface Team | TechxArtisan**
