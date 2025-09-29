---
title: "Hardware-Installation"
description: "Schritt-für-Schritt Hardware-Installationsanleitung für Openterface KVM Extension for uConsole. Lernen Sie, wie Sie die Erweiterungskarte ordnungsgemäß im Erweiterungsslot Ihres uConsole installieren, mit detaillierten Sicherheitsrichtlinien."
keywords: "KVM-Erweiterung Installation, uConsole Hardware-Setup, Erweiterungskarte Installation, uConsole Erweiterungsslot, KVM Hardware-Anleitung, physische Installation"
---

# **Hardware-Installation** | Openterface KVM Extension for uConsole

## Übersicht
Die KVM Extension ersetzt das 4G/LTE-Modul im Erweiterungsslot des uConsole und fügt direkten HDMI-Eingang und USB HID-Steuerung hinzu.

## Was Sie benötigen
- Überprüfen Sie Ihren [Paketinhalt](whats-in-the-box.md) vor der Installation  
- Openterface KVM Extension Board  
- Mitgelieferte **Unterlegscheiben** (für stabile Montage und gleichmäßigen Druck)  
- Sechskantschraubendreher (für Montageschrauben)  
- ESD-Schutz (Handgelenkband oder geerdete Oberfläche) — empfohlen  

## Installationsschritte

### **1. Strom ausschalten**
Fahren Sie den uConsole herunter und trennen Sie alle Stromversorgungen und Kabel.

### **2. Vorhandenes Modul entfernen**
Verwenden Sie einen Sechskantschraubendreher, um die beiden Schrauben zu entfernen.  
Heben Sie das Board **gerade nach oben**, um die Federkontakte nicht zu verbiegen.

### **3. KVM Extension installieren**
- Platzieren Sie die **Unterlegscheibe** auf dem Schraubenpfosten.  
- Setzen Sie die KVM Extension fest in den Erweiterungsslot ein.  
- Die Unterlegscheibe kompensiert die etwas dünnere PCB (1,0 mm vs 1,2 mm) und hält den angemessenen Federkontaktdruck aufrecht.

??? note "Passung vor der finalen Installation prüfen"
    Sie können das Board zunächst **ohne die Unterlegscheibe** einsetzen, um die Passung zu testen. Wenn das Board lose wirkt oder die Kontakte ungleichmäßig sind, fügen Sie die Unterlegscheibe hinzu und setzen Sie das Board erneut ein. Die Openterface KVM Extension ist 1,0 mm dick, etwas dünner als das ursprüngliche LTE-Modul (1,2 mm). Die Verwendung der mitgelieferten Unterlegscheibe gewährleistet eine stabile Montage und zuverlässigen Federkontakt.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="max-height:220px"}

### **4. Board befestigen**
Setzen Sie die Schrauben wieder ein und ziehen Sie sie **sanft** an — **nicht überdrehen**, da dies das Board beschädigen oder die Gewinde beschädigen könnte.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="max-height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="max-height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="max-height:220px"}

### **5. Installation überprüfen**
Das Board sollte **flach und stabil** sitzen, mit gleichmäßigem Federkontakt über alle Pads. Es sollte keine merkliche Wackelbewegung oder Bewegung geben.

### **6. Erweiterungsslot-Abdeckung installieren**
Installieren Sie die Erweiterungsslot-Abdeckung wieder, um das KVM Extension Board zu schützen und das ursprüngliche Aussehen des uConsole zu erhalten.

??? note "Textausrichtung auf der Erweiterungsslot-Abdeckung"
    Der Text auf der Erweiterungsslot-Abdeckung kann aus bestimmten Blickwinkeln "auf dem Kopf" erscheinen. Dies ist ein absichtliches Design - der Text ist so ausgerichtet, dass er lesbar ist, wenn Sie den uConsole halten und die Ports von oben nach unten betrachten, was die natürliche Betrachtungsposition bei der Verwendung des Geräts ist.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="max-height:220px"}

---

**Nächste Schritte**

1. Gehen Sie zu [Software-Setup](/product/uconsole-kvm-extension/software-setup/), um die Openterface App zu installieren.  
2. Gehen Sie zu [Mit Zielgerät verbinden](/product/uconsole-kvm-extension/connect-to-target/), um Ihr Zielgerät zu verbinden.  
3. Überprüfen Sie [Funktionen & Spezifikationen](/product/uconsole-kvm-extension/features/) für detaillierte technische Spezifikationen.
