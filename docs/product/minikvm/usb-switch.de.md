---
title: "Schaltbarer USB-Port"
description: "Erfahren Sie mehr über das duale Hardware-Software USB-Schaltsystem in Openterface Mini-KVM. Verstehen Sie die vier Betriebszustände, Sicherheitsrichtlinien und zukünftige Remote-Zugriffsfunktionen."
keywords: "USB-Schaltung, KVM-Schalter, Hardware-Schalter, Software-Schalter, USB-Port-Steuerung, KVM über USB, KVM über IP, Remote-Zugriff, USB-Geräteverwaltung, Computer-Peripheriegeräte, USB-Stromverwaltung"
---

# **USB-Port-Schaltungsführer** | Openterface Mini-KVM

Das mini-KVM-Gerät hat einen einzelnen USB-A 2.0-Port, der **sowohl** mit dem Host- als auch mit dem Zielcomputer **verbunden werden kann, aber niemals gleichzeitig mit beiden**.

Die Steuerung erfolgt über zwei Schalter:

- **Hardware-Schalter**: Ein physischer Zwei-Positionen-Umschalter am Gerät ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} (nach innen = Host, nach außen = Ziel).
- **Software-Schalter**: Ein Umschaltknopf in der Host-App, der den USB-Port sofort entweder zum Host oder zum Ziel umleitet.

## Betriebszustände

Die Verbindung des USB-A-Ports hängt von den Positionen des **Hardware-Schalters** und des **Software-Schalters** ab. Die folgende Tabelle fasst die vier möglichen Zustände zusammen:

| **Zustand** | **Hardware-Schalter** | **Software-Schalter** | **Port Verbunden Mit** | **Sync-Status**        |
| ----------- | --------------------- | --------------------- | ---------------------- | ---------------------- |
| 1           | Host                  | Host                  | Host                   | Synced                 |
| 2           | Target                | Target                | Target                 | Synced                 |
| 3           | Target                | Host                  | Host                   | Out of Sync (→ Host)   |
| 4           | Host                  | Target                | Target                 | Out of Sync (→ Target) |

- **Synced** bedeutet, dass Hardware- und Software-Einstellungen übereinstimmen.
- **Out of Sync** bedeutet, dass die Software den Hardware-Schalter vorübergehend überschreibt, bis der Hardware-Schalter erneut bewegt wird.

Jede manuelle Bewegung des Hardware-Schalters aktualisiert die Software-Anzeige und kehrt zu einem synchronisierten Zustand zurück.

Beim Start ist das Gerät standardmäßig mit der Host-Verbindung verbunden. Die Software erkennt die Position des Hardware-Schalters und synchronisiert entsprechend.

!!! warning "Denken Sie daran, das Flash-Laufwerk zu entfernen, bevor Sie den Schalter umschalten"
Wenn der USB-Port von einem Flash-Laufwerk verwendet wird, stellen Sie sicher, dass Sie das Flash-Laufwerk entfernen, bevor Sie den Schalter umschalten, um die Port-Nutzung auf einen anderen Computer zu übertragen.

??? note "Wie teilt man einen USB-Stick/Disk zwischen Host- und Zielgeräten?"
Dateien können zwischen Host und Ziel übertragen werden, indem Sie diese Schritte befolgen:

    1. Mounten Sie einen USB-Stick-Laufwerk auf dem Host, wenn der kleine schwarze Schalter auf der Seite des Type-C-Ports des Hosts eingestellt ist.
    2. Kopieren Sie die Dateien auf dieses gemountete Laufwerk.
    3. Nach dem Kopieren mounten Sie das Laufwerk aus, ohne es physisch zu trennen.
    4. Drehen Sie den kleinen schwarzen Schalter auf die andere Seite. Diese Aktion schaltet die Verbindung des USB-A-Ports zum Ziel um.
    5. Mounten Sie den USB-Stick auf dem Zielgerät und kopieren/verschieben Sie Dateien vom Laufwerk, wodurch der Dateiübertragungsprozess vom Host zum Ziel abgeschlossen wird.

    Diese Methode kann auch in entgegengesetzter Richtung verwendet werden.

!!! Note "Benutzerführung" - **Software-Schalter-Priorität**: Unabhängig von der Hardware-Schalter-Position ändert das Klicken auf den Software-Schalter sofort die Schaltungsrichtung.

    - **Hardware-Schalter-Synchronisation**: Jedes manuelle Umschalten des Hardware-Schalters richtet seinen Zustand mit dem Software-Schalter aus und wechselt vom nicht synchronisierten Zustand 3 oder 4 zu Zustand 1 oder 2. Diese Synchronisation ändert jedoch nicht unbedingt die tatsächliche Schaltungsverbindung.

    - **Hardware-Schalter-Überwachung**: Der Hardware-Schalter wird trotz seiner physischen Natur von der Software überwacht und steuert die Schaltungsrichtung nicht direkt. Stattdessen interpretiert die Software die Schalterposition und verwaltet die tatsächliche Schaltungsumschaltung.
