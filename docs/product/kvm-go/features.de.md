---
title: "Funktionen & Spezifikationen"
description: "Vollständige Übersicht über die Openterface KVM-Go Serie: ultrakompaktes Design mit integrierten Videoanschlüssen, 4K/60Hz-Unterstützung, MicroSD-Steckplatz und detaillierte technische Spezifikationen. Schlüsselanhängergroße KVM-over-USB-Lösung für IT-Profis."
keywords: "KVM-Go Funktionen, ultrakompakter KVM, integriertes HDMI, 4K KVM, MicroSD KVM, Schlüsselanhänger KVM, KVM Spezifikationen, Headless-Steuerung, tragbarer KVM, IT-Tools, Serververwaltung"
---

# **Funktionen & Spezifikationen** | Openterface KVM-Go Serie

## Pre-Launch-Status

Die KVM-Go Serie befindet sich derzeit in der Pre-Launch-Entwicklung. Wir verfeinern die PCB- und Gehäusedesigns. Treten Sie unserer [Warteliste]({{ config.extra.kvmgo_purchase_link }}) bei, um über Fortschritte auf dem Laufenden zu bleiben und frühen Zugang zu erhalten.

> **Hinweis:** Funktionen, Spezifikationen und Design können sich während der Entwicklung noch ändern.

## Produktmodelle
- **KVM-Go HDMI Male** — Direkte HDMI-Verbindung
- **KVM-Go DisplayPort Male** — Hochleistungs-DisplayPort
- **KVM-Go VGA Male** — Legacy-Systemunterstützung (in Entwicklung)

## Kernfunktionen

### **Ultrakompaktes Design**
Schlüsselanhängergroßer Formfaktor, der in Ihre Tasche passt. Keine sperrigen KVM-Geräte mehr tragen oder nach Videokabeln suchen.

### **Integrierte Videoanschlüsse**
Direkte Plug-in-Fähigkeit mit integrierten männlichen Anschlüssen:

- **HDMI Male** — Moderne Gerätekompatibilität
- **DisplayPort Male** — Hochleistungsunterstützung
- **VGA Male** — Legacy-Systemunterstützung (demnächst)

### **BIOS-Level-Zugriff**
Direkter Zugriff auf BIOS, Firmware und Startverwaltung des Zielgeräts ohne Netzwerkabhängigkeiten.

### **Netzwerkunabhängigkeit & Blitzschnelle Reaktion**
Stabile Headless-Steuerung mit integrierter Videoaufnahme und emulierter Tastatur/Maus (HID)-Eingabe. Keine Netzwerkverbindung erforderlich. Die Hardware-Startzeit beträgt weniger als 1 Sekunde und gewährleistet sofortige Fehlerbehebung ohne Verzögerungen im Arbeitsablauf.

### **Verbesserte Videoleistung**
Massive Verbesserung gegenüber Mini-KVMs 1080p@30Hz:

- **Eingang**: 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Ausgang**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Standard**: 1080p@60Hz für optimale Stabilität und Leistung
- **4K-Modus**: Als experimentelle Funktion verfügbar*
- **Kompression**: YUV420-, YUV444- und MJPEG-Unterstützung

*Hinweis: Der 4K-Modus erzeugt zusätzliche Wärme; die Geräteoberfläche kann während des erweiterten Betriebs sehr heiß werden

### **MicroSD-Steckplatz**
Dateiübertragung zwischen Host- und Zielgeräten

### **Plattformübergreifende Unterstützung**
[Host-Apps](/app) kompatibel mit macOS, Windows, Linux, Android und Chrome-Web-App für universelle Integration.

### **Textübertragung**
Übertragen Sie mühelos Text durch Simulation von Tastenanschlägen — perfekt für Benutzernamen, Passwörter und Code-Snippets. Unterstützt ASCII-Zeichen einschließlich Symbole und Satzzeichen.

- **Host → Ziel**: Text über emulierte Tastenanschläge senden
- **Ziel → Host**: Text vom Bildschirm des Ziels über OCR zum Host kopieren (nur macOS)

!!! warning "Textübertragungsbeschränkungen"
    - **Keine Zwischenablage-Integration**: Nur Tippenemulation, keine Bild- oder Dokumentübertragung
    - **Nur ASCII**: Beschränkt auf ASCII-Zeichen (keine Unterstützung für Chinesisch, Japanisch, Koreanisch usw.)
    - **Längenüberlegungen**: Am besten für kurzen Text; große Blöcke können Leistungsprobleme verursachen
    - **OCR-Funktion**: Ziel → Host Textübertragung derzeit nur auf macOS verfügbar

### **Plug-and-Play-Komfort**
Keine Softwareinstallation auf dem Zielgerät erforderlich. Die Steuerung beginnt sofort nach der Verbindung ohne hinterlassene Softwarespuren.

### **Audio-Integration**
HDMI-eingebetteter Audio-Durchgang für vollständiges Multimedia-Erlebnis. (Nicht unterstützt auf KVM-Go VGA; Bestätigung ausstehend für KVM-Go DP.)

### **Bluetooth-Fähigkeit**
Integrierte Bluetooth-Unterstützung ermöglicht native iPadOS-App-Funktionalität (demnächst verfügbar) und macht KVM-GO zu einem der wenigen KVMs, die nativ mit iPads funktionieren.

### **Open-Source**
[Vollständig Open-Source](/compliance) Hardware und Software für Transparenz und [Community-Innovation](/discord).

## Technische Spezifikationen

### **Physische Abmessungen** *(Änderungen vor Auslieferung vorbehalten)*
- **Größe**: 18 × 18 × 55 mm (0,71 × 0,71 × 2,17 Zoll)
- **Gewicht**: ~25 g (0,9 oz)
- **Material**: Aluminiumlegierungsgehäuse mit 3D-gedruckten Kappen

### **Konnektivität & Stromversorgung**
- **Stromversorgung**: USB-C-betrieben (keine externe Stromversorgung erforderlich)
- **USB-Geschwindigkeit**: USB 3.0 für HDMI/DP-Versionen; USB 2.0 für VGA-Version
- **Host-Kompatibilität**: Windows, macOS, Linux, Android, Chrome
- **Ziel**: Keine Softwareinstallation erforderlich

### **Video & Audio**
- **Max. Eingang**: 4096×2160@60Hz (YUV420), 4096×2160@30Hz (YUV444)
- **Max. Ausgang**: 4096×2160@60Hz (MJPEG), 3840×2160@30Hz (YUV420)
- **Audio**: HDMI-eingebetteter Audio-Durchgang

### **Eingabefunktionen**
- Vollständige Tastatur- und Mausemulation (absolut & relativ)
- Multimedia-Tastenunterstützung
- Benutzerdefinierte HID-Funktionalität
- Computer-Weckfunktion

### **Speicher**
- **MicroSD-Steckplatz**: Dateiübertragungen via MicroSD zwischen Host und Ziel

