# KVM-GO Beta Schnellstartanleitung

> Mit ❤️ verfasst von [Iker](https://github.com/IkerGarcia) aus der Openterface-Community — vielen Dank, dass du uns hilfst, bessere Dokus zu erstellen!

Willkommen zur [KVM-GO Beta](/product/kvm-go/updates/251007-kvm-go-beta-test-kits-sent-1/)! Nachfolgend findest du eine Kurzversion des Beta-Feedback-Fragebogens. Arbeite jeden Abschnitt durch, halte deine Erkenntnisse fest und reiche alles anschließend über den [Google-Formular-Beta-Feedback-Fragebogen](https://openterface.com/product/kvm-go/beta-questions) ein.

Herzlichen Glückwunsch zur Auswahl als Beta-Tester! Wir freuen uns sehr auf dein Feedback und sind sicher, dass du das Gerät in unterschiedlichen Szenarien gründlich prüfen wirst.

Dieser Test bietet dir viel Flexibilität, dennoch hätten wir gern, dass du dich auf ein paar konkrete Szenarien konzentrierst.

Dein Feedback ist für uns äußerst wertvoll. Du kannst gern weitere Aspekte des Geräts testen, aber besonders interessieren uns die folgenden Schwerpunktbereiche:

1. **Langzeitleerlauf-Test**
   1. Starte die Software und verbinde sie mit einem Target
   2. Lass die Software über einen längeren Zeitraum (mehrere Stunden) ohne Interaktion laufen
   3. Kehre zurück und versuche, Maus- und Tastatursteuerung zu nutzen
   - Haben Maus und Tastatur nach der Leerlaufzeit wieder normal funktioniert?

2. **Hot-Plug-Test**
   - Bitte teste das Ab- und Wiederanschließen des Geräts, während die Software läuft.

3. **BIOS- und Low-Level-Zugriff**

4. **Kopieren & Einfügen (kurze und lange Texte)**

5. **Gerätesimulations-Einstellungen (Windows/Linux)**
   - 5.1. Anzeige-EDID-Konfiguration
   - 5.2. USB-Geräteidentifikation (VID/PID)
   - 5.3. SD-Karten-Funktionalität
     - 5.3.1. Anwendungsfall 1 – Systeminstallation: Wir empfehlen Ventoy – ein Tool, das mehrere ISO-Dateien auf einer SD-Karte ermöglicht und eine Auswahl beim Booten bietet. Hast du versucht, ein Systemabbild auf HOST zu schreiben und anschließend auf TARGET zu wechseln, um die Installation durchzuführen (ohne die Karte zu entfernen)?
     - Anwendungsfall 2 – Dateitransfer: Hast du die SD-Karte verwendet, um Dateien zwischen HOST und TARGET zu übertragen?

Diese Beispiele entsprechen einigen Fragen aus dem Beta-Feedback-Formular und ergänzen allgemeine Informationen zur Konsistenz von Audio/Video/Tastatur/Maus sowie zum Wärmemanagement.

Vielen Dank für deine Unterstützung!

!!! reminder "Nicht vergessen"
    Reiche deine vollständigen Beobachtungen über das Google-Formular ein, damit das Team sie zeitnah prüfen kann.

