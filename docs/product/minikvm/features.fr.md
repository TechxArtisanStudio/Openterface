---
title: "Fonctionnalités et Spécifications"
description: "Aperçu complet d'Openterface Mini-KVM : fonctionnalités puissantes incluant l'accès au niveau BIOS, support vidéo 4K, compatibilité multiplateforme, partage USB et spécifications techniques détaillées. Tout ce que vous devez savoir sur cette solution de contrôle d'ordinateur headless."
keywords: "fonctionnalités Mini-KVM, spécifications KVM, accès BIOS, contrôle headless, KVM 4K, partage USB, KVM multiplateforme, transfert de texte, KVM plug and play, KVM open source, spécifications techniques"
---

# **Fonctionnalités et Spécifications** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## Fonctionnalités Principales

### **Accès au Niveau BIOS**

Accès direct au BIOS de l'appareil cible, au firmware et à la gestion de démarrage sans dépendances réseau.

### **Indépendance Réseau**

Contrôle headless stable utilisant la capture vidéo HDMI et l'entrée clavier/souris émulée (HID). Aucune connexion réseau requise.

### **Vidéo Haute Performance**

- **Entrée** : Jusqu'à 4K (3840×2160) @ 30Hz via HDMI
- **Sortie** : Full HD (1920×1080) @ 30Hz avec une latence inférieure à 140ms
- **Compression** : Support YUV et MJPEG
- **Compatibilité** : VGA, DVI, Micro HDMI via adaptateurs

### **Port USB Commutable**

Basculer l'accès USB entre les appareils hôte et cible pour un partage de disque USB transparent. En savoir plus sur la page [Port USB Commutable](../usb-switch).

### **Support Multiplateforme**

[Applications hôte](/app) compatibles avec macOS, Windows, Linux et Android pour une intégration universelle.

### **Transfert de Texte**

Transmettre du texte sans effort en simulant les frappes—parfait pour les noms d'utilisateur, mots de passe et extraits de code. Supporte les caractères ASCII incluant les symboles et la ponctuation.

!!! warning "Limitations du Transfert de Texte" - **Pas d'Intégration Presse-papiers** : Émule seulement la frappe, pas de transfert d'image ou de document - **ASCII Uniquement** : Limité aux caractères ASCII (pas de support chinois, japonais, coréen) - **Considérations de Longueur** : Meilleur pour le texte court ; les gros blocs peuvent causer des problèmes de performance

### **Convenience Plug-and-Play**

Aucune installation de logiciel requise sur l'appareil cible. Le contrôle commence immédiatement à la connexion sans traces de logiciel laissées.

### **Intégration Audio**

Passage audio intégré HDMI pour une expérience multimédia complète.

### **Broches d'Extension**

Les [broches d'extension](../extension-pins) permettent un développement avancé et une personnalisation pour des besoins spécifiques.

### **Open-Source**

Matériel et logiciel [entièrement open-source](/compliance) pour la transparence et l'[innovation communautaire](/discord).

## Spécifications Techniques

### **Dimensions Physiques**

- **Taille** : 61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 pouces)
- **Poids** : ~48g
- **Matériau** : Alliage d'aluminium, boîtier PLA

### **Connectivité et Alimentation**

- **Alimentation** : Alimenté par USB-C (pas d'alimentation externe nécessaire)
- **Vitesse USB** : Transmission pleine vitesse 12Mbps
- **Compatibilité Hôte** : Windows, macOS, Linux, Android
- **Cible** : Aucune installation de logiciel requise

### **Vidéo et Audio**

- **Entrée Max** : 3840×2160@30Hz (HDMI)
- **Sortie Max** : 1920×1080@30Hz
- **Latence** : Inférieure à 140ms
- **Audio** : Passage audio intégré HDMI

### **Fonctionnalités d'Entrée**

- Émulation complète clavier et souris (absolue et relative)
- Support des touches multimédia
- Fonctionnalité HID personnalisée
- Fonction de réveil d'ordinateur

### **Environnemental**

- **Fonctionnement** : 0°C à 40°C
- **Stockage** : -10°C à 50°C
- **Humidité** : 80% HR

## Modèles de Produit

- **Basic** : OP-MINIKVM-BASIC
- **Toolkit** : OP-MINIKVM-TOOLKIT

## Téléchargements de Documentation

- **[Guide de Démarrage Rapide](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[Fiche Technique (Anglais)](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
