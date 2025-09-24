---
title: "Configuration logicielle"
description: "Guide complet de configuration logicielle pour Openterface KVM Extension for uConsole. Apprenez comment installer et configurer l'App Openterface sur votre uConsole pour une fonctionnalité KVM transparente."
keywords: "installation app Openterface, configuration logicielle uConsole, configuration app KVM, configuration app uConsole, guide installation logicielle"
---

# **Configuration logicielle** | Openterface KVM Extension for uConsole

## Aperçu de l'installation

L'App Openterface permet à votre uConsole de fonctionner comme une interface KVM, vous permettant de contrôler les appareils cibles via l'écran intégré, le clavier et le trackball.

!!! note "Exigences"
    - **uConsole** : Nécessite l'installation de l'App Openterface
    - **Cible** : Aucune app nécessaire - prend en charge Windows, macOS, Linux, Android, iOS
    - **Vidéo** : Utilisez un câble HDMI standard. Utilisez un câble HDMI standard. Avec un convertisseur HDMI alimenté, il prend également en charge d'autres formats tels que **VGA**, **DP**, et plus. *Astuce : Assurez-vous que le convertisseur est correctement alimenté ; sinon, vous pourriez rencontrer un écran noir.*

## Méthodes d'installation

### **Option 1 : Installation Flatpak**

Suivez notre [Guide d'installation Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) pour les étapes de configuration détaillées.

### **Option 2 : Dépôt communautaire (Recommandé)**

Si vous préférez la build communautaire maintenue par Rex :

1. **Ajouter le dépôt** :
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **Installer le paquet** :
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "Notes du dépôt"
    Ces commandes nécessitent sudo. Le dépôt cible les paquets arm64 Bookworm ; vérifiez la compatibilité avec votre appareil avant l'installation.

## Instructions d'utilisation

### **Démarrer la session KVM**
1. Lancez l'App Openterface sur votre uConsole
2. L'app détectera automatiquement la carte Extension KVM
3. Connectez votre appareil cible via HDMI
4. Utilisez le clavier et trackball intégrés du uConsole pour contrôler l'appareil cible

### **Fonctionnalités de contrôle**
- **Clavier** : Émulation complète du clavier incluant les touches multimédias
- **Souris** : Positionnement absolu et relatif de la souris
- **Audio** : Pass-through audio HDMI vers les haut-parleurs uConsole

### **Fonctionnalités avancées**
- **Transfert de texte** : Transmettez rapidement du texte en simulant des frappes—idéal pour les noms d'utilisateur, mots de passe et extraits de code
- **USB commutateur** : Basculez facilement l'accès USB entre le uConsole et l'appareil cible en utilisant l'app hôte
