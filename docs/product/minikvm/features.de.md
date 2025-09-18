---
title: "Funktionen und Spezifikationen"
description: "Vollständige Übersicht über Openterface Mini-KVM: Leistungsstarke Funktionen einschließlich BIOS-Level-Zugriff, 4K-Video-Unterstützung, plattformübergreifende Kompatibilität, USB-Sharing und detaillierte technische Spezifikationen. Alles, was Sie über diese Headless-Computer-Steuerungslösung wissen müssen."
keywords: "Mini-KVM Funktionen, KVM Spezifikationen, BIOS Zugriff, Headless Steuerung, 4K KVM, USB Sharing, plattformübergreifendes KVM, Textübertragung, Plug and Play KVM, Open Source KVM, technische Spezifikationen"
---

# **Funktionen und Spezifikationen** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## Kernfunktionen

### **BIOS-Level-Zugriff**

Direkter Zugriff auf BIOS, Firmware und Startverwaltung des Zielgeräts ohne Netzwerkabhängigkeiten.

### **Netzwerkunabhängigkeit**

Stabile Headless-Steuerung mit HDMI-Video-Capture und emulierten Tastatur/Maus-Eingaben (HID). Keine Netzwerkverbindung erforderlich.

### **Hochleistungs-Video**

- **Eingang**: Bis zu 4K (3840×2160) @ 30Hz über HDMI
- **Ausgang**: Full HD (1920×1080) @ 30Hz mit unter 140ms Latenz
- **Kompression**: YUV und MJPEG Unterstützung
- **Kompatibilität**: VGA, DVI, Micro HDMI über Adapter

### **Umschaltbarer USB-Port**

USB-Zugriff zwischen Host- und Zielgeräten umschalten für nahtloses USB-Laufwerk-Sharing. Mehr erfahren auf der [Umschaltbarer USB-Port](../usb-switch) Seite.

### **Plattformübergreifende Unterstützung**

[Host-Apps](/app) kompatibel mit macOS, Windows, Linux und Android für universelle Integration.

### **Textübertragung**

Text mühelos übertragen durch Simulation von Tastenanschlägen—perfekt für Benutzernamen, Passwörter und Code-Snippets. Unterstützt ASCII-Zeichen einschließlich Symbole und Interpunktion.

!!! warning "Textübertragungs-Limitierungen" - **Keine Zwischenablage-Integration**: Emuliert nur Tippen, keine Bild- oder Dokumentübertragung - **Nur ASCII**: Begrenzt auf ASCII-Zeichen (keine chinesische, japanische, koreanische Unterstützung) - **Längen-Überlegungen**: Am besten für kurzen Text; große Blöcke können Leistungsprobleme verursachen

### **Plug-and-Play-Komfort**

Keine Software-Installation auf dem Zielgerät erforderlich. Steuerung beginnt sofort bei Verbindung ohne zurückgelassene Software-Spuren.

### **Audio-Integration**

HDMI-eingebetteter Audio-Durchgang für vollständige Multimedia-Erfahrung.

### **Erweiterungs-Pins**

[Erweiterungs-Pins](../extension-pins) ermöglichen erweiterte Entwicklung und Anpassung für spezifische Bedürfnisse.

### **Open-Source**

[Vollständig open-source](/compliance) Hardware und Software für Transparenz und [Community-Innovation](/discord).

## Technische Spezifikationen

### **Physikalische Abmessungen**

- **Größe**: 61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 Zoll)
- **Gewicht**: ~48g
- **Material**: Aluminiumlegierung, PLA-Gehäuse

### **Konnektivität und Stromversorgung**

- **Stromversorgung**: USB-C versorgt (keine externe Versorgung erforderlich)
- **USB-Geschwindigkeit**: 12Mbps Vollgeschwindigkeits-Übertragung
- **Host-Kompatibilität**: Windows, macOS, Linux, Android
- **Ziel**: Keine Software-Installation erforderlich

### **Video und Audio**

- **Max Eingang**: 3840×2160@30Hz (HDMI)
- **Max Ausgang**: 1920×1080@30Hz
- **Latenz**: Unter 140ms
- **Audio**: HDMI-eingebetteter Audio-Durchgang

### **Eingabefunktionen**

- Vollständige Tastatur- und Maus-Emulation (absolut & relativ)
- Multimedia-Tasten-Unterstützung
- Benutzerdefinierte HID-Funktionalität
- Computer-Weckfunktion

### **Umgebungsbedingungen**

- **Betrieb**: 0°C bis 40°C
- **Lagerung**: -10°C bis 50°C
- **Luftfeuchtigkeit**: 80% RH

## Produktmodelle

- **Basic**: OP-MINIKVM-BASIC
- **Toolkit**: OP-MINIKVM-TOOLKIT

## Dokumentation Downloads

- **[Schnellstart-Anleitung](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[Datenblatt (Englisch)](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
