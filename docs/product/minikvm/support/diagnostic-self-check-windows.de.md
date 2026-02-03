---
title: "Openterface Mini-KVM (Windows) - Hardware-Diagnose Selbsttest Anleitung"
description: "Schritt-für-Schritt-Anleitung zur Durchführung des Hardware-Diagnose Selbsttests in der Windows Openterface-App. Erfahren Sie, wie Sie USB-Verbindungen testen, Probleme erkennen und Diagnoseberichte an den Support senden."
keywords: "Openterface Mini-KVM, Windows, Hardware-Diagnose, Diagnose Selbsttest, KVM-Problembehandlung, USB-KVM-Diagnose, Mini-KVM-Support, KVM-Gerät-Test, Windows KVM, KVM-Defektbericht, Mini-KVM-Problemlösungshandbuch"
---

# Openterface Mini-KVM (Windows) — Hardware-Diagnose Selbsttest Anleitung

Diese Anleitung erklärt, wie Sie den **Hardware-Diagnose** Selbsttest in der **Windows**-Version der Openterface-App ausführen und wie Sie den Diagnosebericht an den Support senden, wenn ein Problem erkannt wird.

---

## Vor dem Start

- Verbinden Sie Mini-KVM mit **Host** und **Ziel**.
- Halten Sie das Zielgerät während des Tests im Leerlauf (besonders während des Stresstests).

> **Wichtig (Windows):** Die Diagnose **schreitet nicht automatisch fort**.  
> Um zwischen Tests zu wechseln, verwenden Sie **Weiter** (untere Leiste) **oder** klicken Sie auf einen Testpunkt im **linken Bereich**.  
> Jeder Test wird durch Klicken auf **Jetzt prüfen** ausgeführt.

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## Funktionierendes Gerät (BESTANDEN)

### Schritt 1 — Hardware-Diagnose öffnen (Windows)
In der Windows Openterface-App öffnen Sie: **Erweitert → Hardware-Diagnose**.  

### Schritt 2 — Selbsttest ausführen
Klicken Sie im Hardware-Diagnose-Fenster auf **Jetzt prüfen**, um den aktuellen Diagnoseschritt auszuführen.  

### Schritt 3 — Ziel Plug & Play (Anweisungen folgen)
Wenn **Ziel Plug & Play** Sie auffordert, das Zielkabel neu zu verbinden, folgen Sie den Anweisungen auf dem Bildschirm.  
Bei einigen Konfigurationen kann es erforderlich sein, **mehr als einmal** aus- und wieder einzustecken (z. B. zweimal).  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### Schritt 4 — Host Plug & Play (Anweisungen folgen)
Folgen Sie den Anweisungen auf dem Bildschirm für die Hostseite.  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### Schritt 5 — Stresstest (Hände weg vom Ziel)
Während des **Stresstests** kann die Zielmaus automatisch zur Erkennung bewegt werden.  
**Operieren Sie nicht am Zielgerät**, während der Test läuft.  

> **Hinweis:** Die Maus kann sich schnell bewegen — berühren Sie das Ziel nicht.

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### Schritt 6 — BESTANDEN bestätigen
Fahren Sie fort, bis der Selbsttest abgeschlossen ist. Wenn alles normal ist, zeigen die Ergebnisse **BESTANDEN / Alle Tests bestanden**.  

---

## Problem erkannt (Tastatur/Maus Beispiel)

Wenn ein Problem erkannt wird, können ein oder mehrere Punkte **FEHLER** anzeigen.

### Schritt 1 — Dieselbe Hardware-Diagnose ausführen
Öffnen Sie **Erweitert → Hardware-Diagnose**, dann klicken Sie auf **Jetzt prüfen** zum Starten.  

### Schritt 2 — Durch die Prüfungen fortfahren
Fahren Sie mit den verbleibenden Tests fort, bis die Diagnose abgeschlossen ist.  

### Schritt 3 — Support-E-Mail öffnet sich automatisch
Wenn die Diagnose mit einem Problem abgeschlossen wird, öffnet sich automatisch ein **Support-E-Mail**-Fenster.  

---

## Logs an den Support senden (Windows)

### Schritt 4 — Bestellnummer + Name anwenden
Geben Sie Ihre **Bestellnummer** und **Name** ein und klicken Sie auf **Übernehmen**, um sie in den E-Mail-Entwurf einzufügen. 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### Schritt 5 — E-Mail-Adresse und Entwurf kopieren
- Klicken Sie auf **E-Mail kopieren**, um die Support-E-Mail-Adresse zu kopieren.
- Klicken Sie auf **Entwurf kopieren**, um den vorgefüllten E-Mail-Inhalt (einschließlich Bestellnummer + Name) zu kopieren.  
Fügen Sie beides in Ihren E-Mail-Client (Gmail/Outlook usw.) ein.  

![copy](https://assets2.openterface.com/images/copy.webp)

### Schritt 6 — Die richtigen Logdateien anhängen
Klicken Sie auf **Dateiordner öffnen**. Das Tool zeigt an, welche Dateien angehängt werden sollen.  
**Hängen Sie nur die angeforderten Protokolldateien an** (der Ordner kann viele andere Protokolle enthalten).  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### Schritt 7 — Außerdem ein Aufstellungsphoto anhängen
Fügen Sie derselben E-Mail ein klares **Aufstellungsphoto** bei, das zeigt:
- das Mini-KVM-Gerät,
- beide **Host-** und **Ziel-**Verbindungen,
- Anschlüsse und Kabel deutlich sichtbar.  

### Schritt 8 — E-Mail senden
Senden Sie die E-Mail an den Support (Entwurfstext + angeforderte Protokolle + Aufstellungsphoto angehängt).  

---

## Was bei der Kontaktaufnahme mit dem Support anzugeben ist

- **Bestellnummer**
- **Angeforderte Diagnose-Protokolldateien**
- **Aufstellungsphoto** (Mini-KVM + Host/Ziel-Verkabelung)
