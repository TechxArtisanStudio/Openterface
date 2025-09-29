---
title: "Erweiterungs-Pins"
description: "Entdecken Sie das Potenzial der Erweiterungs-Pins des Openterface Mini-KVM für kundenspezifische Hardwareentwicklung und Open-Source-Projekte."
keywords: "Mini-KVM Erweiterungs-Pins, kundenspezifische Entwicklung, Hardware-Modifikation, Open-Source KVM"
---

# **Erweiterungs-Pins** | Entwicklermodus | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="max-height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:300px"}

Der Openterface Mini-KVM verfügt über Erweiterungs-Pins für fortgeschrittene Entwicklung und Experimente mit [Open Software](/app). Diese Pins sind in der Standard-Gehäusekonfiguration nicht freiliegt.

## Zugriff auf die Pins

1. Gerät zerlegen.
2. Die originale Gehäuseabdeckung durch eine spezielle Extension Pin Cap ersetzen.
3. Das [3D-Modell](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) für die Extension Pin Cap herunterladen.
4. Unser [Hardware-GitHub-Repository](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware) ansehen.

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="max-height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="max-height:300px"}

!!! warning "Garantie erlischt"
    Das Entfernen des Originalgehäuses kann die Produktgarantie ungültig machen. Alle Modifikationen oder Demontagen erfolgen auf eigenes Risiko des Nutzers.

!!! note "Experimentelle Funktionen"
    Mit diesen Pins entwickelte Funktionen sind experimentell und nicht vollständig getestet. Openterface haftet nicht für Schäden, Verletzungen oder Fehlfunktionen, die aus Modifikationen, dem Freilegen der Erweiterungs-Pins oder anderen Änderungen am Gerät entstehen.

## Pin-Konfiguration

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="max-height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="max-height:200px"}

Die Erweiterungs-Pins bieten folgende Verbindungen:

1. USB-5V-Stromversorgung für externe Komponenten
2. Daten-Plus zum USB-Hub des Hosts
3. Daten-Minus zum USB-Hub des Hosts
4. Daten-Plus zum USB-Hub des Targets
5. Daten-Minus zum USB-Hub des Targets
6. Masse (GND)

!!! danger "Falsche Verbindungen verursachen Schäden"
    Eine Verwechslung von VCC und GND kann zu schweren Schäden am Gerät und an angeschlossenen Komponenten führen. Überprüfen Sie die Pin-Verbindungen vor dem Einschalten stets sorgfältig.

## Extension Pin Cap

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:360px"}

Diese 3D-gedruckte Extension Pin Cap ersetzt die originale Abdeckung des Openterface Mini-KVM und ermöglicht fortgeschrittenen Nutzern, die Erweiterungs-Pins für kundenspezifische Entwicklungen freizulegen und zu nutzen. Sie können die 3D-Modell-Dateien aus unserem GitHub-Repository herunterladen und die Kappe selbst drucken.

- **Verwendung**: Ermöglicht den Zugriff auf Erweiterungs-Pins für fortgeschrittene Hardware-Entwicklung.
- **Download**: [3D-Modelldateien](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## An der Entwicklung mitwirken

Während wir weiterentwickeln und experimentieren, werden wir diesen Abschnitt mit weiteren Informationen darüber aktualisieren, was diese Pins leisten können und wie sie kreativ eingesetzt werden können. Ihre Kreativität und Expertise kann die Grenzen des Möglichen mit dem Openterface Mini-KVM erweitern. Bitte machen Sie mit:

1. **Ideen teilen**: Haben Sie ein cooles Konzept zur Nutzung dieser Pins? Wir freuen uns darauf!
2. **DIY-Projekte beitragen**: Wenn Sie etwas Interessantes erstellt haben, teilen Sie es gerne in unserer [Discord Openterface](/discord)-Community.
3. **An der Diskussion teilnehmen**: Vernetzen Sie sich mit anderen Entwicklern und Enthusiasten, um zu brainstormen und zusammenzuarbeiten.

Lassen Sie uns gemeinsam bauen und innovieren!
