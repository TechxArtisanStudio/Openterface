---
title: "Verbindungsanleitung"
description: "Schritt-für-Schritt-Anleitung zur Einrichtung des Openterface KVM-Go. Erfahren Sie, wie Sie Ihren Host-Computer und Ihr Zielgerät mithilfe integrierter Videoanschlüsse für ein ultra-einfaches, direktes Plug-in-Erlebnis verbinden."
keywords: "KVM-Go Einrichtung, ultrakompakte KVM Einrichtung, integrierte HDMI-Verbindung, KVM Installationsanleitung, Schlüsselanhänger KVM Einrichtung, USB KVM Verbindung, Headless Computer Setup, tragbare KVM Einrichtung"
---

# **Verbindungsanleitung** | Setup-Anleitung | Openterface KVM-Go

## **Übersicht der Verbindungen**

![KVM-Go Verbindungsübersicht](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

Die obigen Bilder zeigen alle Verbindungen zwischen dem [**KVM-Go**](/product/kvm-go), dem Host-Computer und dem Zielgerät.

- **Host-Computer**: Erfordert die Installation der [Openterface App](/app).  
- **Zielgerät**: Keine Software und Vorkonfiguration erforderlich.
- **Video**: Der integrierte Anschluss wird direkt in das Zielgerät eingesteckt, sodass Sie keine zusätzlichen Videokabel tragen oder verwalten müssen.

## **Was Sie für die Verbindungen benötigen**

![KVM-Go alle Teile](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

Zur Einrichtung Ihres **KVM-Go** benötigen Sie folgende Komponenten:

- **KVM-Go (HDMI / DP / VGA)** — verbindet sich mit dem **Zielgerät** (für Videoaufnahme)  
- **Schwarzes kurzes USB-C-Kabel** — verbindet sich mit dem **Zielgerät** (für Tastatur- und Mausemulation)
- **Oranges langes USB-C-Kabel** — verbindet sich mit dem **Host-Computer** (der die [Openterface App](/app) ausführt)

!!! note "Hinweis zur Kabellänge"
    Die genauen Kabellängen im **offiziellen KVM-Go-Paket** sind **noch nicht finalisiert** und können leicht von den hier gezeigten abweichen.  
    Die in dieser Anleitung gezeigten Kabel stammen aus dem *klassischen Mini-KVM Toolkit* und dienen nur zur Veranschaulichung.

!!! warning "Verwendung eigener Kabel"
    Wenn Sie sich für eigene Kabel entscheiden, stellen Sie sicher, dass es sich um **hochwertige, datenübertragungsfähige USB-Kabel** handelt. Kabel minderer Qualität oder reine Ladekabel können zu folgenden Problemen führen:
    
    - Schwarzbildprobleme
    - Nicht reagierende Tastatur- oder Mauseingaben
    - Zeitweilige Verbindungsabbrüche
    - Flackernde oder instabile Bildschirmausgabe

## **Schritt-für-Schritt-Einrichtung**

### **Schritt 1 — USB-Kabel an KVM-Go anschließen**
![USB-Kabel einstecken](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **Schwarzes USB-C-Kabel** → In den Port mit der Kennzeichnung ![Ziel-Symbol](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![Ziel-Symbol](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** am KVM-Go-Gehäuse einstecken.  
- **Oranges USB-C-Kabel** → In den Port mit der Kennzeichnung ![Host-Symbol](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![Host-Symbol](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host** einstecken.

!!! warning
    Beide USB-C-Ports sind physisch identisch.  
    Überprüfen Sie immer **die Beschriftungen** auf der Gehäuseoberfläche, um Verwechslungen zu vermeiden.

### **Schritt 2 — Video mit Ziel verbinden**
![HDMI-Anschluss einstecken](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

Stecken Sie den **integrierten männlichen Videoanschluss** direkt in den Videoausgang des Zielgeräts.

### **Schritt 3 — Ziel-USB-Port verbinden**
Verbinden Sie das **schwarze USB-Kabel** mit dem Zielgerät für HID-Steuerung.

- **Option A:** Direkt in einen USB-A-Port  
  ![Ziel USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **Option B:** Verwendung eines USB-C-Adapters  
  ![Ziel USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "USB-C-Verbindungsprüfung"
    Einige USB-C-Ports bieten möglicherweise keine sichere Verbindung. Wenn Sie zeitweilige Tastatur-/Mausprobleme haben, wackeln Sie vorsichtig an der Adapterverbindung, um sicherzustellen, dass sie richtig sitzt und Kontakt hat.


### **Schritt 4 — Host-USB-Port verbinden**
Verbinden Sie das **orange USB-Kabel** mit dem Host-Computer.

- Direkt an einen USB-C-Port **ODER** über einen USB-C-zu-USB-A-Adapter.  
  ![Host-USB einstecken](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

