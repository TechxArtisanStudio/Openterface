# Openterface Android

## Übersicht

Openterface Mini-KVM ist eine Open-Source-Hardware- und Softwarelösung, die grundlegende KVM (Tastatur, Video, Maus)-Funktionalität bietet, um Geräte über eine Android-basierte Schnittstelle zu steuern. Dieses Repository enthält den Quellcode der Android-Anwendung, Build-Konfigurationen und unterstützende Skripte, um das Projekt einzurichten und bereitzustellen.

Wir setzen uns für offene Hardware und Open-Source-Software ein, lizenziert unter der [GNU Affero General Public License v3](LICENSE).

## Funktionsmodule

### 1. Videoanzeige

#### Hauptfunktionalität

-   Streamt Videoausgaben vom angeschlossenen Zielgerät in Echtzeit auf den Android-Bildschirm.
-   Unterstützt Bildanpassungen für optimale Anzeige.

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### Beschreibung der Benutzeroberfläche

-   Der Hauptbildschirm zeigt den Video-Feed des Zielgeräts an, der den größten Teil der Benutzeroberfläche einnimmt.
-   Eine Symbolleiste an der Seite bietet Anpassungssteuerungen (Helligkeit, Kontrast, Farbton).

#### Betriebsablauf

1. Schließen Sie die Mini-KVM-Hardware über HDMI und USB an das Zielgerät an.
2. Stecken Sie die Mini-KVM über USB-C in Ihr Android-Gerät.
3. Starten Sie die App; der Video-Feed erscheint automatisch.
4. Verwenden Sie die Schieberegler in der Symbolleiste, um Helligkeit, Kontrast oder Farbton nach Bedarf anzupassen.

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### Besondere Merkmale

-   Die Zoomfunktion mit zwei Fingern verbessert die Anzeige

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. Maussteuerung

#### Hauptfunktionalität

-   Bietet absolute und relative Maussteuerung, um mit der Benutzeroberfläche des Zielgeräts zu interagieren.
-   Unterstützt Links- und Rechtsklicks.
-   Wählen Sie den Modus im rechten Menü aus.

#### Beschreibung der Benutzeroberfläche

-   Der Video-Feed dient auch als Touchpad für die Maussteuerung.
-   Eine schwebende Aktionsschaltfläche (FAB) wechselt zwischen Maus- und Tastaturmodi.

#### Betriebsablauf

1. Stellen Sie sicher, dass das Gerät erfolgreich verbunden ist.
2. Tippen Sie auf den Bildschirm, um den Mauszeiger an diese Position zu bewegen (absolute Steuerung).
3. Doppeltippen mit einem Finger für einen Links-Klick, Zwei-Finger-Klick für einen Rechts-Klick.
4. Der Ziehmodus besteht darin, die linke Taste gedrückt zu halten, ohne sie loszulassen.

#### Besondere Merkmale

-   Relative Maussteuerung (in Entwicklung, Umschaltung über Einstellungen, wenn verfügbar).

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. Tastatureingabe

#### Hauptfunktionalität

-   Geben Sie Text in das Gerät ein, indem Sie auf die Tasten der Tastatur klicken.

#### Beschreibung der Benutzeroberfläche

-   Das Tastatursymbol befindet sich in der unteren rechten Ecke.
-   Die Tastatur umfasst Tastenkombinationen, Systemtasten, Standardtasten und Funktionstasten (F1-F12).

#### Betriebsablauf

1. Klicken Sie auf das Tastatursymbol in der unteren rechten Ecke, um die Tastatur aufzurufen.
2. Geben Sie Text ein oder drücken Sie die Funktionstasten nach Bedarf.

#### Besondere Merkmale oder Tastenkombinationen

-   **Tastenkombinationen**: Ctrl+C, Ctrl+V, Ctrl+Z, Ctrl+X, Ctrl+A, Ctrl+S,
    Win+Tab, Win+S, Win+E, Win+R, Win+D, Win+L, Alt+F4, Ctrl+Alt+Del, Alt+PrtScr.
-   **Funktionstasten**: F1-F12, Symboltasten.
-   **Standardtasten**: 0-9, A-Z, Enter, Leertaste, Löschen.

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

In der Zwischenzeit können Sie unser Open-Source-**GitHub-Repository** erkunden: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) für den neuesten Code, Updates, Beispiele und um Probleme zu melden.

Sie können auch unserer [Discord-Community](/discord) beitreten, um sich mit unserem Entwicklerteam und anderen großartigen Benutzern auszutauschen, um über KVM-bezogene Themen zu diskutieren.

Für direkte Unterstützung können Sie uns gerne eine E-Mail an [support@openterface.com](mailto:support@openterface.com) senden.

---

**Haben Sie Feedback zu dieser Seite?** [Lassen Sie es uns hier wissen.](https://forms.gle/wmxoR2C1VdG36mT69)