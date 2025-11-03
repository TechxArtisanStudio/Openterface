---
title: "Fonctionnalités et spécifications"
description: "Présentation complète de la série Openterface KVM-Go : conception ultra-compacte avec connecteurs vidéo intégrés, prise en charge 4K/60Hz, slot MicroSD et spécifications techniques détaillées. Solution KVM-over-USB de la taille d'un porte-clés pour les professionnels de l'informatique."
keywords: "fonctionnalités KVM-Go, KVM ultra-compact, HDMI intégré, KVM 4K, KVM MicroSD, KVM porte-clés, spécifications KVM, contrôle headless, KVM portable, outils informatiques, gestion de serveurs"
---

# **Fonctionnalités et spécifications** | Série Openterface KVM-Go

## Statut pré-lancement

La série KVM-Go est actuellement en développement pré-lancement. Nous peaufinons les conceptions PCB et du boîtier. Rejoignez notre [liste d'attente]({{ config.extra.kvmgo_purchase_link }}) pour rester informé des progrès et obtenir un accès anticipé.

> **Remarque :** Les fonctionnalités, spécifications et design sont encore susceptibles de changer au fur et à mesure du développement.

## Modèles de produits
- **KVM-Go HDMI Male** — Connexion HDMI directe
- **KVM-Go DisplayPort Male** — DisplayPort haute performance
- **KVM-Go VGA Male** — Support des systèmes hérités (en développement)

## Fonctionnalités principales

### **Design ultra-compact**
Format de la taille d'un porte-clés qui tient dans votre poche. Fini les appareils KVM encombrants ou la recherche de câbles vidéo.

### **Connecteurs vidéo intégrés**
Capacité de branchement direct avec connecteurs mâles intégrés :

- **HDMI Male** — Compatibilité avec les appareils modernes
- **DisplayPort Male** — Support haute performance
- **VGA Male** — Support des systèmes hérités (bientôt disponible)

### **Accès au niveau BIOS**
Accès direct au BIOS, firmware et gestion de démarrage de l'appareil cible sans dépendance réseau.

### **Indépendance réseau et réponse ultra-rapide**
Contrôle headless stable utilisant la capture vidéo intégrée et l'entrée clavier/souris émulée (HID). Aucune connexion réseau requise. Le temps de démarrage du matériel est inférieur à 1 seconde, garantissant un dépannage immédiat sans délais dans votre flux de travail.

### **Performance vidéo améliorée**
Amélioration massive par rapport au 1080p@30Hz du Mini-KVM :

- **Entrée** : 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Sortie** : 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Par défaut** : 1080p@60Hz pour une stabilité et des performances optimales
- **Mode 4K** : Disponible en tant que fonctionnalité expérimentale*
- **Compression** : Support YUV420, YUV444 et MJPEG

*Remarque : Le mode 4K génère de la chaleur supplémentaire ; la surface de l'appareil peut devenir très chaude pendant un fonctionnement prolongé

### **Slot MicroSD**
Transfert de fichiers entre appareils hôte et cible

### **Support multiplateforme**
[Applications hôtes](/app) compatibles avec macOS, Windows, Linux, Android et application web Chrome pour une intégration universelle.

### **Transfert de texte**
Transmettez facilement du texte en simulant des frappes au clavier — parfait pour les noms d'utilisateur, mots de passe et extraits de code. Prend en charge les caractères ASCII y compris symboles et ponctuation.

- **Hôte → Cible** : Envoyer du texte via des frappes clavier émulées
- **Cible → Hôte** : Copier du texte de l'écran de la cible vers l'hôte via OCR (macOS uniquement)

!!! warning "Limitations du transfert de texte"
    - **Pas d'intégration du presse-papiers** : Émule uniquement la saisie, pas de transfert d'image ou de document
    - **ASCII uniquement** : Limité aux caractères ASCII (pas de support chinois, japonais, coréen, etc.)
    - **Considérations de longueur** : Idéal pour les textes courts ; les gros blocs peuvent causer des problèmes de performance
    - **Fonction OCR** : Le transfert de texte Cible → Hôte est actuellement disponible uniquement sur macOS

### **Commodité plug-and-play**
Aucune installation logicielle requise sur l'appareil cible. Le contrôle commence immédiatement après la connexion sans laisser de traces logicielles.

### **Intégration audio**
Audio intégré HDMI pour une expérience multimédia complète. (Non pris en charge sur KVM-Go VGA ; confirmation en attente pour KVM-Go DP.)

### **Capacité Bluetooth**
Le support Bluetooth intégré permet la fonctionnalité de l'application native iPadOS (à venir), faisant du KVM-GO l'un des rares KVM fonctionnant nativement avec les iPads.

### **Open-source**
Matériel et logiciel [entièrement open-source](/compliance) pour la transparence et [l'innovation communautaire](/discord).

## Spécifications techniques

### **Dimensions physiques** *(susceptibles de changer avant livraison)*
- **Taille** : 18 × 18 × 55 mm (0,71 × 0,71 × 2,17 pouces)
- **Poids** : ~25 g (0,9 oz)
- **Matériau** : Boîtier en alliage d'aluminium avec capuchons imprimés en 3D

### **Connectivité et alimentation**
- **Alimentation** : Alimenté par USB-C (aucune alimentation externe nécessaire)
- **Vitesse USB** : USB 3.0 pour les versions HDMI/DP ; USB 2.0 pour la version VGA
- **Compatibilité hôte** : Windows, macOS, Linux, Android, Chrome
- **Cible** : Aucune installation logicielle requise

### **Vidéo et audio**
- **Entrée max** : 4096×2160@60Hz (YUV420), 4096×2160@30Hz (YUV444)
- **Sortie max** : 4096×2160@60Hz (MJPEG), 3840×2160@30Hz (YUV420)
- **Audio** : Audio intégré HDMI

### **Fonctionnalités d'entrée**
- Émulation complète clavier et souris (absolue et relative)
- Support des touches multimédia
- Fonctionnalité HID personnalisée
- Fonction de réveil de l'ordinateur

### **Stockage**
- **Slot MicroSD** : Transferts de fichiers via MicroSD entre hôte et cible

