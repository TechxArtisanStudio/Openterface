# Openterface KVM-Erweiterung für uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## Übersicht

Verwandeln Sie Ihr uConsole mit dieser Plug-and-Play-Erweiterungskarte in eine **tragbare KVM (Tastatur, Video, Maus) Konsole**.

Die **Openterface KVM-Erweiterung** ersetzt das ursprüngliche 4G/LTE-Modem im Erweiterungsslot Ihres uConsole und bietet direkten **HDMI-Eingang und USB HID-Steuerung**, wodurch Sie Headless-Geräte unterwegs verwalten können—ohne externe Monitore, Tastaturen oder Netzwerkkonfiguration.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## Funktionen

- **Perfektes Formfaktor**  
    Entspricht der 37×77 mm Größe des 4G/LTE-Moduls für nahtlose Hardware-Integration.

- **Direktes HDMI + USB HID**  
    Ermöglicht reaktive Steuerung verbundener Geräte mit der eingebauten Eingabe und dem Bildschirm des uConsole.

- **Niedrige Latenz**  
    Geeignet für BIOS-Level-Fehlerbehebung und Echtzeit-Interaktion.

- **Wahrlich Tragbar**  
    Macht das uConsole zu einem mobilen Werkzeug für Entwickler, Ingenieure und Techniker.

- **Open-Source-Freundlich**  
    Basiert auf der [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt) Plattform. Community-Beiträge willkommen.


## Anwendungsfälle

- **Systemadministration**  
    Zugriff auf und Fehlerbehebung von Servern oder eingebetteten Geräten ohne sperrigen KVM-Switch.

- **Hardware-Entwicklung**  
    Direktes Testen und Debuggen von Raspberry Pi, SBCs oder Mikrocontrollern.

- **Feldeinsatz**  
    Wartung oder Konfiguration in Rechenzentren oder entfernten Standorten durchführen.


## Hardware-Installation

Befolgen Sie diese Hardware-Installationsschritte, um das 4G/LTE-Modul in Ihrem uConsole durch die Openterface KVM-Erweiterungskarte zu ersetzen und einen sicheren Sitz zu gewährleisten.

### Was Sie Benötigen

- Ihre Openterface KVM-Erweiterungskarte
- Die mitgelieferte Dichtung (Kunststoff-Spacer) 
- Ein Sechskantschraubendreher (für die Montageschrauben der Karte)
- ESD-Vorsichtsmaßnahmen (Handgelenkband oder geerdete Oberfläche) — empfohlen

### Installation der Erweiterungskarte

1. Ausschalten und Trennen

    Schalten Sie das uConsole aus und trennen Sie alle Stromversorgung und Kabel.

2. Entfernen des Bestehenden Moduls

    Verwenden Sie einen Sechskantschraubendreher, um die beiden Schrauben zu entfernen, die das 4G/LTE-Modul oder die bestehende Erweiterungskarte halten.

    Heben Sie die Karte vorsichtig gerade nach oben, um die Federkontakte nicht zu verbiegen.

3. Installation der KVM-Erweiterungskarte

    - Die Openterface KVM-Erweiterungskarte ist 1.0 mm dick (dünner als das ursprüngliche 4G/LTE 1.2 mm). Aus diesem Grund empfehlen wir, die mitgelieferte Dichtung auf die Schraubenpfosten (zwischen PCB und Montageabstandshalter) zu legen, damit die Dichtung unter den Schraubenpfosten sitzt, bevor die Karte eingesetzt wird. Dies kompensiert das dünnere PCB und hilft, den angemessenen Federkontakt-Druck zu gewährleisten.
    - Wenn Sie zuerst überprüfen möchten, setzen Sie die Karte ohne Dichtung ein und überprüfen Sie den gleichmäßigen Federkontakt; wenn der Kontakt ungleichmäßig ist oder die Karte lose sitzt, fügen Sie die Dichtung hinzu und setzen Sie die Karte erneut ein.

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. Wiedereinsetzen der Schrauben

    Setzen Sie die beiden Schrauben wieder ein und ziehen Sie sie mit dem Sechskantschraubendreher fest. Festziehen ist ausreichend — nicht überdrehen.

5. Überprüfung des Sitzes

    Die Karte sollte flach sitzen ohne merkliche Bewegung. Überprüfen Sie, dass die Federkontakte gleichmäßigen Kontakt über die Pads haben.

6. Hardware-Test

    Verbinden Sie die Stromversorgung wieder, starten Sie das System und testen Sie HDMI-, Audio- und USB HID-Geräte, um den ordnungsgemäßen Betrieb zu bestätigen.

## Software-Setup-Anleitung

Um die KVM-Erweiterung zu verwenden, installieren Sie die **Openterface App** auf Ihrem uConsole.

Option 1 - Flatpak-Version von Openterface verwenden
- 📖 Folgen Sie unserer [Flatpak-Installationsanleitung](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) für detaillierte Setup-Schritte.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

Option 2 - Community-Version von Rex installieren

Wenn Sie die von Rex gepflegte Community-Build möchten, fügen Sie sein Repository hinzu und installieren Sie das Paket mit den unten stehenden Befehlen.

1. Repository-GPG-Schlüssel und Repository hinzufügen

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. Aktualisieren und installieren

```bash
sudo apt update
sudo apt install openterfaceqt
```

Hinweise: Diese Befehle erfordern sudo. Das Repository zielt auf arm64 Bookworm-Pakete ab; überprüfen Sie die Kompatibilität mit Ihrem Gerät vor der Installation.

## Pre-Launch-Status

- 📦 Erste Charge derzeit in Vorbereitung  
- ⏳ Geschätzte Versand beginnt **Anfang August 2024**  
- 🛒 Begrenzte Menge – [Jetzt vorbestellen](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole), um Ihre Einheit zu reservieren

> **Vorbestellungs-Hinweis**  
> Dieser Artikel ist derzeit zur Vorbestellung mit einer geschätzten Lieferzeit von **etwa 2 Monaten**.  
> Wenn Sie andere Artikel früher benötigen, bitte eine **separate Bestellung** aufgeben. Kombinierte Bestellungen werden versandt, wenn dieses Produkt bereit ist.

## Community & Support

- 🗨️ Diskussion beitreten: [Discord-Server](https://discord.gg/ruAD9kcYbq)  
- 📧 E-Mail-Support: [info@openterface.com](mailto:info@openterface.com)


## FAQs

**F: Wie funktioniert die KVM-Erweiterungskarte?**  
Sie erfasst die HDMI-Ausgabe von einem Zielgerät und zeigt sie auf dem uConsole an. Gleichzeitig werden die Tastatur und das Trackball des uConsole verwendet, um das Zielgerät über USB HID-Emulation zu steuern.

**F: Kann ich dies mit dem installierten 4G/LTE-Modul verwenden?**  
Nein. Diese Karte belegt denselben Erweiterungsslot. Sie müssen zwischen zellularer Konnektivität oder KVM-Funktionalität wählen.

**F: Ist die Software Open Source?**  
Ja! Unsere **Openterface Connect** Apps sind vollständig Open Source und in unserem [GitHub-Repository](https://github.com/TechxArtisanStudio/Openterface_QT) verfügbar.
