---
title: "Software-Setup"
description: "Vollständiger Software-Setup-Leitfaden für Openterface KVM Extension for uConsole. Lernen Sie, wie Sie die Openterface App auf Ihrem uConsole installieren und konfigurieren für nahtlose KVM-Funktionalität."
keywords: "Openterface App Installation, uConsole Software Setup, KVM App Setup, uConsole App Konfiguration, Software Installation Guide"
---

# **Software-Setup** | Openterface KVM Extension for uConsole

## Installationsübersicht

Die Openterface App ermöglicht es Ihrem uConsole, als KVM-Interface zu fungieren, sodass Sie Zielgeräte über den eingebauten Bildschirm, die Tastatur und das Trackball steuern können.

!!! note "Anforderungen"
    - **uConsole**: Erfordert Installation der Openterface App
    - **Ziel**: Keine App erforderlich - unterstützt Windows, macOS, Linux, Android, iOS
    - **Video**: Verwenden Sie ein Standard-HDMI-Kabel. Verwenden Sie ein Standard-HDMI-Kabel. Mit einem netzbetriebenen HDMI-Konverter unterstützt es auch andere Formate wie **VGA**, **DP** und mehr. *Tipp: Stellen Sie sicher, dass der Konverter ordnungsgemäß mit Strom versorgt wird; andernfalls können Sie einen schwarzen Bildschirm erleben.*

## Installationsmethoden

### **Option 1: Flatpak-Installation**

Folgen Sie unserem [Flatpak-Installationsleitfaden](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) für detaillierte Setup-Schritte.

### **Option 2: Community-Repository (Empfohlen)**

Wenn Sie die von Rex gepflegte Community-Build bevorzugen:

1. **Repository hinzufügen**:
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **Paket installieren**:
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "Repository-Hinweise"
    Diese Befehle erfordern sudo. Das Repository zielt auf arm64 Bookworm-Pakete ab; überprüfen Sie die Kompatibilität mit Ihrem Gerät vor der Installation.

## Verwendungsanweisungen

### **KVM-Sitzung starten**
1. Starten Sie die Openterface App auf Ihrem uConsole
2. Die App erkennt automatisch die KVM Extension-Karte
3. Verbinden Sie Ihr Zielgerät über HDMI
4. Verwenden Sie die eingebaute Tastatur und das Trackball des uConsole, um das Zielgerät zu steuern

### **Steuerungsfunktionen**
- **Tastatur**: Vollständige Tastaturemulation einschließlich Multimediatasten
- **Maus**: Absolute und relative Mauspositionierung
- **Audio**: HDMI-Audio-Durchgang zu uConsole-Lautsprechern

### **Erweiterte Funktionen**
- **Textübertragung**: Übertragen Sie schnell Text durch Simulation von Tastenanschlägen—ideal für Benutzernamen, Passwörter und Codeschnipsel
- **Umschaltbares USB**: Wechseln Sie einfach den USB-Zugriff zwischen uConsole und Zielgerät über die Host-App
