---
title: FAQs für Openterface Mini-KVM
description: Häufig gestellte Fragen zum Mini-KVM, die Funktionen, Kompatibilität, Fehlerbehebung und zukünftige Pläne abdecken.
keywords: Mini-KVM, Openterface, KVM-Switch, Open-Source, Fehlerbehebung, Videoaufnahme, USB, Kompatibilität
---

# FAQs für Openterface Mini-KVM

Willkommen zu den FAQs für unser Flaggschiff **Openterface Mini-KVM**.  
Falls Sie nicht finden, was Sie brauchen, **mailen Sie uns unter [info@openterface.com](mailto:info@openterface.com)** oder **treten Sie unserer Community** auf [Discord](/discord) oder [Reddit](/reddit) bei.

⚠️ _FAQs können veraltet sein — bitte lassen Sie uns wissen, wenn Sie etwas sehen, das aktualisiert werden muss._

---

## :material-clipboard-list: Schnelle Navigation

-   [USB-Port & Dateiübertragung](#usb-port--dateiübertragung)
-   [Technisch](#technisch)
-   [Steuerung](#steuerung)
-   [Video](#video)
-   [Fehlerbehebung](#fehlerbehebung)
-   [Mehr](#mehr)

---

## USB-Port & Dateiübertragung

**:material-chat-question:{ .faq } Kann es Dateien übertragen?**

Ja — über den schaltbaren USB-A-Port, der zwischen Host und Ziel geteilt wird.

**:material-chat-question:{ .faq } Kann ich den USB-Port per Software umschalten?**

Ja, auf Hardware-Version **v1.9+**.

**:material-chat-question:{ .faq } Warum USB 2.0 statt 3.0?**

USB 2.0 ist ausreichend für 1080p@30Hz Video + HID + Standard-Geschwindigkeits-Dateiübertragung und bleibt dabei kompakt, kühler und erschwinglicher.  
USB 3.0 könnte in zukünftigen Pro-Modellen erscheinen.

---

## Technisch

**:material-chat-question:{ .faq } Open-Source?**

Ja — zertifiziert von [OSHWA](https://certification.oshwa.org/cn000015.html). Hardware und Software sind auf [GitHub](/contributing/).

**:material-chat-question:{ .faq } BIOS-Zugriff**

Direkte USB-Verbindung ermöglicht vollständige BIOS-Level-Kontrolle, anders als nur Remote-Tools (VNC, TeamViewer).  
Ältere Maschinen können BIOS-Probleme bei der Erkennung unseres USB-Hubs haben — bitte melden Sie solche Fälle.

**:material-chat-question:{ .faq } Video/Datenübertragung**

Video wird über HDMI erfasst und über USB 2.0 gesendet.  
Der schaltbare USB-Port ermöglicht es Ihnen, Laufwerke oder andere Geräte zu teilen.

**:material-chat-question:{ .faq } Stromversorgung**

Das Mini-KVM kann Strom von **beiden Seiten** (Host oder Ziel) ziehen. Die Seite mit dem **kürzeren Kabel** wird normalerweise zur Hauptstromquelle.  
Für stromsparende Ziele (z.B. Raspberry Pi) verwenden Sie eine dedizierte Stromversorgung statt Rückstromversorgung über Mini-KVM.

**:material-chat-question:{ .faq } Kabellängen-Limits**

-   Halten Sie das **orange Host USB-C-Kabel ≤1.5m**.
-   Für längere Kabel, Strom einspeisen über:
    -   USB-A Stecker-Stecker-Kabel
    -   [Erweiterungs-Pins](/product/minikvm/extension-pins/)
    -   USB-C Y-Splitter
-   Gleiche Regel gilt für das **schwarze Ziel-Kabel**.

---

## Steuerung

**:material-chat-question:{ .faq } Drahtlose oder Ethernet-Version?**

Nicht eingebaut. Verwenden Sie einen Headless-Computer (z.B. Raspberry Pi) + Remote-Desktop für Fernsteuerung.

**:material-chat-question:{ .faq } PS/2-Kompatibilität?**

Nein — PS/2-Unterstützung könnte in zukünftigen Versionen erkundet werden.

**:material-chat-question:{ .faq } Mehrere Mini-KVMs an einem Computer?**

Ja, experimentelle Funktion in der QT-App (Windows/Linux).

**:material-chat-question:{ .faq } Ein-/Ausschalt-Steuerung?**

Nicht direkt, aber [Erweiterungs-Pins](/product/minikvm/extension-pins/) ermöglichen zukünftige ATX-Steuerungsmodule.

---

## Video

**:material-chat-question:{ .faq } Latenz & Auflösung**

-   Erfassung bei **1080p@30Hz**
-   Latenz unter **140ms** → flüssige Steuerung

**:material-chat-question:{ .faq } Eingabe vs. Erfassungsauflösung**

-   Akzeptiert Eingaben bis zu **4K@30Hz**
-   Erfasst bei **1080p**, höhere Eingaben werden heruntergerechnet (können leicht unscharf aussehen).
-   Beste Praxis: **Ziel auf 1080p setzen**.

**:material-chat-question:{ .faq } Gaming-Tauglichkeit**

Nicht für AAA-Gaming. Funktioniert gut für leichtere Spiele wie Minecraft oder Emulatoren.

**:material-chat-question:{ .faq } Fernsteuerung über Internet**

Nicht eingebaut, aber koppeln Sie Mini-KVM mit Remote-Desktop-Software auf dem Host.

**:material-chat-question:{ .faq } Andere Videoformate**

Verwenden Sie Adapter für VGA, DVI, DisplayPort, etc.

---

## Fehlerbehebung

**:material-chat-question:{ .faq } USB-Hub-Probleme**

Verwenden Sie einen **aktiven Hub**, um Spannungsabfälle zu vermeiden, die Instabilität verursachen.

**:material-chat-question:{ .faq } App zeigt kein Video oder Steuerung reagiert nicht**

Trennen Sie alle Kabel, warten Sie, verbinden Sie wieder.  
Wenn nicht gelöst, Firmware prüfen oder Host-App aktualisieren.

**:material-chat-question:{ .faq } Seltsame Auflösungen wie 43184x24228@44Hz**

Erfassungs-Firmware wahrscheinlich auf Werkseinstellungen zurückgesetzt.  
Firmware neu flashen über [GitHub-Releases](https://github.com/TechxArtisanStudio/Openterface_QT/releases).

**:material-chat-question:{ .faq } Neu geflasht aber immer noch kaputt?**

-   Richtige USB-Enumeration verifizieren (`USB Tree Viewer` oder `lsusb -v`)
-   Neueste Host-App bestätigen
-   Wenn immer noch fehlschlagend, Support für Diagnose/Austausch kontaktieren.
