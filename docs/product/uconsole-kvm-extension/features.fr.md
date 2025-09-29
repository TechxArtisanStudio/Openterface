---
title: "Fonctionnalités et spécifications"
description: "Aperçu complet de l'Openterface KVM Extension for uConsole : fonctionnalités puissantes incluant l'entrée HDMI directe, le contrôle USB HID, un facteur de forme parfait, et des spécifications techniques détaillées. Tout ce que vous devez savoir sur cette solution KVM portable."
keywords: "fonctionnalités extension KVM, uConsole KVM, HDMI KVM, contrôle USB HID, KVM portable, contrôle headless, remplacement 4G LTE, spécifications techniques, expansion uConsole"
---

# **Fonctionnalités et spécifications** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="max-height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="max-height:320px"}

## Fonctionnalités principales

- **HDMI direct + USB HID** : Exploitez l'écran et les contrôles intégrés du uConsole avec une entrée HDMI directe et une émulation USB HID.
- **Plug-and-Play** : Contrôle instantané sans installation de logiciel ou traces résiduelles sur l'appareil cible.
- **Faible latence** : Optimisé pour le dépannage au niveau BIOS et les interactions en temps réel.
- **Portable** : Outil mobile tout-en-un—pas besoin de moniteurs supplémentaires, claviers ou configuration réseau.
- **Sans réseau** : Contrôle headless stable via capture HDMI et entrée HID, aucun réseau requis.
- **Transfert de texte** : Transmettez rapidement du texte en simulant des frappes—idéal pour les noms d'utilisateur, mots de passe et extraits de code. Prend en charge ASCII complet, y compris les symboles et la ponctuation. [Consultez notre app](/app) pour plus de détails.
- **Open Source** : Construit sur [Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt) avec un support communautaire actif.

## Spécifications techniques

### Dimensions physiques

- **Taille :** 37 × 77 mm (correspond au module 4G/LTE)
- **Épaisseur :** 1,0 mm (plus fin que le module 4G/LTE original à 1,2 mm)
- **Matériau :** PCB de haute qualité avec contacts à ressort

### Émulation complète clavier et souris

- **USB HID :** Positionnement absolu et relatif de la souris, support complet du clavier, touches multimédias.
- **Connexion :** Lien USB vers la cible via le port femelle Type-C de la carte d'extension.

### Vidéo et audio

- **Entrée :** Jusqu'à 4K (3840×2160) @ 30Hz via HDMI
- **Sortie :** Full HD (1920×1080) @ 30Hz avec une latence inférieure à 140ms
- **Affichage :** Utilise l'écran intégré du uConsole
- **Compression :** Support YUV et MJPEG
- **Compatibilité :** VGA, DVI, Micro HDMI (via adaptateurs)
- **Audio :** Pass-through audio intégré HDMI

### Port USB 2.0 commutateur

- **Port partagé** : Basculez facilement l'accès USB entre le uConsole et l'appareil cible (ex. : clés USB) en utilisant l'app hôte.
- **Vitesse USB :** Transmission à pleine vitesse 12Mbps

### Connectivité et alimentation

- **Alimentation :** Tire l'alimentation directement du slot d'expansion du uConsole (aucune alimentation externe nécessaire)
- **Compatibilité cible :** Windows, macOS, Linux, Android, iOS
- **Logiciel cible :** Aucune installation requise
