# Openterface QT für Win & Linux

Dieses Dokument bietet einen Überblick über eine plattformübergreifende KVM-Software (Tastatur, Video, Maus), die mit Qt entwickelt wurde und mit den Betriebssystemen Linux und Windows kompatibel ist. Die Software ermöglicht die Steuerung eines Zielgeräts von einem Hostsystem aus und bietet eine Vielzahl von Funktionen, die über die Menüleiste und zusätzliche Funktionen zugänglich sind.

## Hauptmenüleistenfunktionen

### Einstellungen

Das Einstellungsmenü ermöglicht es den Benutzern, die Einstellungen über einen Dialog mit vier Seiten anzupassen:<br>
![Einstellungen Allgemein](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   **Allgemein** Diese Seite konfiguriert den Filter für Debug-Protokolle und ob der Bildschirmschoner während der Ausführung der Anwendung deaktiviert werden soll oder nicht. Die Protokollkategorien umfassen:

    -   Kern
    -   Seriell
    -   Benutzeroberfläche
    -   Host

    Benutzer können wählen, ob sie Protokolle in einer .txt-Datei speichern und den Bildschirmschoner deaktivieren möchten oder nicht.<br>

![Einstellungen Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   **Video** Diese Seite ermöglicht es den Benutzern:

    -   Auszuwählen, welche Kameradaten erfasst werden sollen.
    -   Die Auflösung festzulegen.
    -   Das Video-Stream-Format auszuwählen.

-   **Audio** Diese Seite befindet sich derzeit in der Entwicklung.<br>

![Einstellungen Zielsteuerung](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   **Zielsteuerung** Diese Seite bietet Optionen zur Konfiguration der Steuerungsmodi für das Zielgerät:

    -   **Steuermodi:**

        -   **Tastatur + Maus + USB HID-Gerät**
        -   **USB-Tastatur**
        -   **Tastatur + Maus**
        -   **USB HID-Gerät**

    -   **Setzen Sie die Vendor ID (VID) und die Product ID (PID), die vom Ziel gelesen werden.**
    -   **Definieren Sie den USB-Descriptor für das Ziel.**

### Bearbeiten

-   **Einfügen:** Sowohl die Einfügeoption im Bearbeitungsmenü als auch die Einfügetaste in der oberen linken Ecke ermöglichen es den Benutzern, Text aus der Zwischenablage des Hosts in das Zielgerät einzufügen.

### Steuerung

Dieses Menü bietet Optionen zum:<br>

-   Festlegen der Mausbewegungsmodi: Absolut oder Relativ. **Steuerung >> Mausmodus >> Absolut oder Relativ.**
-   Umschalten der Sichtbarkeit des Mauszeigers des Hosts. **Steuerung >> Maus Sichtbarkeit >> Automatisch Ausblenden oder Immer Anzeigen.**
-   Umschalten eines USB-Ports an der Hardware zwischen Ziel- und Hostnutzung. **Steuerung >> Umschaltbarer USB >> ZU Ziel oder Zu Host.**
-   Anpassen der Baudrate für die Chipübertragung. **Steuerung >> Baudrate >> 9600, 115200.**

### Erweitert

Das Erweitert-Menü umfasst die folgenden Optionen:<br>
![Erweitert Menü](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   **Umgebungsprüfung:** Überprüft, ob die erforderlichen Treiber für die Software installiert sind.
-   **Seriellen Port zurücksetzen:** Startet den seriellen Port neu.
-   **Tastatur und Maus zurücksetzen:** Setzt die Einstellungen für Tastatur und Maus zurück.
-   **Werkseinstellung für HID-Chip:** Stellt den HID-Chip auf die Werkseinstellungen zurück.<br>
    ![Erweitert Serielles Konsolen](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   **Serielle Konsole:** Öffnet ein neues Fenster, um alle Nachrichten zu überwachen, die an den seriellen Port gesendet werden, mit Filtern für gesendete/empfangene Nachrichten.<br>
    ![Erweitert Skriptwerkzeug](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   **Skriptwerkzeug:** Führt AutoHotkey (AHK)-Skripte aus. Diese Funktion ahmt AutoHotkey nach, unterstützt jedoch nur eine Teilmenge von Maus-/Tastaturfunktionen und Screenshot-Funktionen. Skripte wirken sich auf das Zielgerät aus.
-   **TCP-Server:** Empfängt AutoHotkey-Befehle über TCP, um sie auf dem Zielgerät auszuführen.
-   **Firmware-Update:** Holt die neueste Firmware von einem Remote-Server, sodass die Benutzer wählen können, ob sie sie auf das Gerät flashen möchten.

### Sprachen

Die Schnittstellensprache kann auf Folgendes eingestellt werden:

-   Dänisch
-   Englisch
-   Deutsch
-   Französisch
-   Japanisch
-   Schwedisch

### Hilfe

Das Hilfemenü bietet: <br>
![Hilfe Menü](https://assets.openterface.com/images/qt/menuHelp.webp)

-   Links zur offiziellen Website und Feedback-Formulare für Software-/Hardwareprobleme.
-   Informationen zum Kauf von Hardware.
-   Eine Beschreibung der Umgebung der Software.
-   Über: Details zur Organisation.
-   Update: Überprüft auf Software-Updates.

## Funktionen der Menüleiste (von links nach rechts)

Die Menüleiste umfasst von links nach rechts die folgenden Funktionen:<br>

![Menüleiste](https://assets.openterface.com/images/qt/menubar.webp)

-   Auswahl der Tastaturbelegung: Wählen Sie die Tastaturbelegung aus.
-   Zoom-Steuerungen: Hineinzoomen, herauszoomen oder die Anzeige des erfassten Video-Streams zurücksetzen.
-   Virtuelle Tastatur: Enthält Funktionstasten und voreingestellte Tastenkombinationen.
-   Screenshot: Erfasst den gesamten Zielbildschirm und speichert ihn in einem Standardordner.
-   Vollbildmodus: Schaltet die Vollbildanzeige um.
-   Einfügen: Fügt Text aus der Zwischenablage des Hosts in das Ziel ein.
-   Mausbewegung: Lässt die Maus vordefinierte Bewegungen ausführen.
-   USB-Geräteanzeige: Zeigt an, ob ein USB-Gerät dem Ziel oder dem Host zugewiesen ist.

In der Zwischenzeit können Sie gerne unser Open-Source-**GitHub-Repository** erkunden: [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) für den neuesten Code, Updates, Beispiele und um Probleme zu melden.

Sie können auch unserer [Discord-Community](/discord) beitreten, um sich mit unserem Entwicklerteam und anderen großartigen Nutzern auszutauschen und über KVM-bezogene Themen zu diskutieren.

Für direkten Support können Sie uns gerne eine E-Mail an [support@openterface.com](mailto:support@openterface.com) senden.

---

**Haben Sie Feedback zu dieser Seite?** [Lassen Sie es uns hier wissen.](https://forms.gle/wmxoR2C1VdG36mT69)
