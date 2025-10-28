---
title: "Guide de commutation de carte MicroSD"
description: "Apprenez à utiliser le système de commutation MicroSD double matériel-logiciel dans l'Openterface KVM-Go. Comprenez les quatre états de fonctionnement, les indicateurs LED, les directives de sécurité et les capacités de transfert de fichiers."
keywords: "commutation MicroSD, commutateur KVM, commutateur matériel, commutateur logiciel, contrôle carte MicroSD, KVM over USB, transfert de fichiers, gestion périphérique USB, périphériques informatiques, gestion alimentation MicroSD, indicateurs LED"
---

# **Guide de commutation de carte MicroSD** | Openterface KVM-Go

L'**Openterface KVM-Go** comprend un seul emplacement de carte MicroSD qui peut être partagé entre l'ordinateur hôte et l'appareil cible, mais jamais les deux en même temps.

Cette conception vous permet de basculer rapidement entre les appareils pour le **transfert de fichiers**, sans retirer physiquement la carte, rendant votre flux de travail plus rapide et plus efficace. Il peut également servir de **lecteur de carte MicroSD classique**.

## **Installer la carte MicroSD**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "Installation correcte de la carte MicroSD"
    Insérez fermement la carte MicroSD jusqu'à ce que vous entendiez un **clic**, indiquant qu'elle est solidement installée et verrouillée en place.

## **Méthodes de contrôle**

KVM-Go offre deux façons de basculer la carte MicroSD entre l'hôte et la cible :

- **Bouton matériel** — Un bouton physique sur l'appareil pour un contrôle manuel.  
- **Commutateur logiciel** — Un bouton à bascule dans l'application hôte pour une commutation instantanée.


## **Bouton de commutation et indicateurs LED** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

Les **indicateurs LED bicolores** affichent l'état actuel de la connexion MicroSD *(Remarque : En développement / Sujet à changement)* :

- **🔵 LED bleue allumée** — La carte MicroSD est montée sur l'**appareil cible**  
- **🟢 LED verte allumée** — La carte MicroSD est montée sur l'**ordinateur hôte**  
- **LED éteinte** — Aucune carte MicroSD insérée ou appareil hors tension  
- **LED clignotante** — Transfert de données en cours (activité de lecture/écriture)

!!! note "Fonction de montage automatique (Expérimental)"
    Par défaut, la carte MicroSD se monte sur l'**hôte** lors de la première mise sous tension de l'appareil.  
    Une fonctionnalité expérimentale à venir permettra le **montage automatique** du côté (hôte ou cible) qui se connecte en premier, rendant l'expérience encore plus fluide.


