# Software

Um Ihre Openterface™ KVM-Gadgets zum Laufen zu bringen, müssen Sie eine der unten aufgeführten Apps auf Ihrem Host-Computer installieren. Sie können diese Apps von verschiedenen App-Plattformen herunterladen oder einfach auf die bereitgestellten Links klicken. Wenn Sie sich abenteuerlustig fühlen, können Sie sie auch aus dem Quellcode mit unseren GitHub-Repositories erstellen!

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## Download & Installation

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } **Windows**

    ***

    Download oder Build aus dem Quellcode für **Openterface QT Win**:

    [:octicons-download-24: {{qt_version}} Installer herunterladen](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.windows.amd64.installer.exe) <br>
    [:octicons-download-24: {{qt_version}} Portable EXE herunterladen](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT-portable.exe) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Demo ansehen](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } **macOS**

    ***

    Download oder Build aus dem Quellcode für **Openterface MacOS**:

    [:octicons-arrow-right-24: Aus dem App Store installieren](/appstore) <br>
    [:octicons-download-24: Portable DMG herunterladen](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: Demo ansehen](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } **Linux**

    ***

    Download oder Build aus dem Quellcode für **Openterface QT Linux**:

    [:octicons-download-24: {{qt_stable}} AMD64 DEB herunterladen](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.amd64.deb) <br>
    [:octicons-download-24: {{qt_stable}} AMD64 RPM herunterladen](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.amd64.rpm) <br>
    [:octicons-download-24: {{qt_stable}} AMD64 AppImage herunterladen](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.amd64.AppImage) <br>
    [:octicons-download-24: {{qt_stable}} ARM64 DEB herunterladen](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.arm64.deb) <br>
    [:octicons-download-24: {{qt_stable}} ARM64 RPM herunterladen](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.arm64.rpm) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Demo ansehen](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } **Android**

    ***

    Download oder Build aus dem Quellcode für **Android APK**:

    [:octicons-download-24: {{android_version}} herunterladen](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk) <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) <br>
    [:octicons-play-24: Demo ansehen](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "Achtung: Datenschutz & Sicherheit bei Drittanbieter-Apps prüfen"
Da alle unsere Apps Open Source sind, könnten Sie auf alternative Versionen von Host-Anwendungen für Openterface-Geräte stoßen, die von anderen erstellt wurden. Sie können ziemlich cool sein und zusätzliche Funktionen bieten, aber hier ist eine freundliche Erinnerung: Überprüfen Sie ihre Sicherheits- und Datenschutzpraktiken sorgfältig—besonders weil KVM-Kontrolle Ereignisse von Ihrem Bildschirm, Tastatur und Maus beinhaltet. Das Openterface-Team kann nicht für die Sicherheit dieser Drittanbieter-Apps bürgen, also gehen Sie vorsichtig vor!

## Grundlegende Host-App-Steuerungen

### 💻 Kompatibilität

-   **Host-Software**: Installieren Sie unsere Host-App für macOS, Windows oder Linux.
-   **Zielgeräte**: Keine Einrichtung erforderlich—verbinden Sie einfach jedes Gerät mit Videoausgabe (HDMI, VGA, etc.) und einem USB-Port für Tastatur/Maus-Steuerung. Funktioniert mit Windows, macOS, Linux, Android und iOS.

### 🖱 Maus-Modi

-   **Absoluter Modus**: Host-Maus mappt direkt auf die Zielbildschirmposition.
-   **Relativer Modus**: Bewegt den Zielcursor relativ zur aktuellen Position. Mit einer Tastenkombination beenden.

### ⌨️ Tastatur

Tastenanschläge vom Host werden direkt an das Ziel gesendet, wenn die App fokussiert ist.

### ⚙️ BIOS-Zugriff

Steuern Sie das Ziel-BIOS direkt.  
Häufige Tasten: F2 (Dell/Lenovo/ASUS), F10 (HP), Del (ASUS/Gigabyte/MSI), ⌥ (Apple).

### 🔊 Audio

Ziel-Audio streamt über HDMI und spielt auf Ihrem Host-Computer.

### 🎥 Video

Betrachten Sie Ihren Zielbildschirm direkt in der App.

-   **Aktuelle Modelle**: Bis zu **1080p 30Hz** Anzeige in der App, mit Unterstützung für **4K 30Hz Eingang** über HDMI.
-   **Andere Eingänge**: Kompatibel mit VGA, DVI, Micro HDMI und mehr bei Verwendung geeigneter Adapter.
-   **Zukünftige Modelle**: Höhere Auflösungen und Bildwiederholraten werden unterstützt, wenn neue Hardware-Versionen veröffentlicht werden.

### 🔄 Umschaltbare Ports

Einige Openterface-Geräte enthalten Ports, die **zwischen Host und Ziel umgeschaltet** werden können, wie USB 2.0-Ports oder micro-SD-Kartensteckplätze (auf kommenden Modellen).

-   **Einzelnutzung**: Nur eine Seite (Host oder Ziel) kann gleichzeitig auf den Port zugreifen.
-   **Umschaltmethoden**:
    -   **Hardware-Umschalter** — physischer Schalter am Gerät
    -   **Software-Button** — Steuerung über die Host-App
-   **Wichtig**:
    -   Entfernen Sie Speichergeräte (USB-Laufwerke oder micro-SD-Karten) sicher vor dem Umschalten.
    -   Vermeiden Sie das Anschließen von Hochleistungsgeräten, um Instabilität oder Schäden zu verhindern.
    -   Siehe den [Umschaltbare Ports Guide](/usb-switch) für Details und Logikdiagramme.
