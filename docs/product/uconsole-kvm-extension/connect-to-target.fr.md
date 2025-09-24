---
title: "Connecter à l'Appareil Cible"
description: "Apprenez comment connecter votre appareil cible à l'Openterface KVM Extension for uConsole. Guide complet pour la configuration du contrôle USB et de l'entrée vidéo après l'installation matérielle et la configuration logicielle."
keywords: "configuration connexion KVM, connexion appareil cible, configuration contrôle USB, configuration entrée HDMI, connexion extension KVM uConsole"
---

# **Connecter à l'Appareil Cible** | Openterface KVM Extension for uConsole

## Aperçu de la Connexion

![extension-use-case-1a](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1a.webp){:style="height:480px"}

## Prérequis

Avant de connecter votre appareil cible, assurez-vous d'avoir terminé :

1. [Installation Matérielle](/product/uconsole-kvm-extension/hardware-installation/) - Installation physique de la carte Extension KVM
2. [Configuration Logicielle](/product/uconsole-kvm-extension/software-setup/) - Installation de l'App Openterface

## Étapes de Connexion

### **Contrôle USB**
Connectez le port femelle Type-C au port USB de l'appareil cible pour émuler les signaux clavier et souris.

### **Entrée Vidéo**
Connectez la sortie vidéo de l'appareil cible au port HDMI sur l'Extension KVM :

- Utilisez un câble HDMI standard pour les appareils à sortie HDMI
- Utilisez un câble convertisseur VGA-to-HDMI pour les appareils à sortie VGA.
    - *Note* : Assurez-vous que le convertisseur est alimenté via son connecteur USB pour un fonctionnement correct.
- Utilisez d'autres adaptateurs appropriés pour différents types de signaux vidéo

## Test de la Connexion

1. Allumez l'alimentation et démarrez l'uConsole
2. Exécutez l'app Openterface QT
3. Testez les fonctionnalités HDMI, audio et USB HID pour confirmer le bon fonctionnement
