---
title: FAQ Openterface KeyMod Series
description: Questions fréquentes sur KeyMod Series : fonctionnalités, compatibilité, plateformes et informations de pré-lancement.
keywords: KeyMod, Openterface, émulateur HID, clavier Bluetooth, clavier téléphone, open source, pré-lancement, Android, iPadOS
---

# FAQ Openterface KeyMod

Bienvenue sur la FAQ **Openterface KeyMod**.  
Si vous ne trouvez pas ce dont vous avez besoin, **envoyez-nous un e-mail à [info@openterface.com](mailto:info@openterface.com)** ou **rejoignez notre communauté** sur [Discord](/discord) ou [Reddit](/reddit).

⚠️ **Note** : KeyMod est actuellement en développement pré-lancement. Les fonctionnalités, spécifications et design peuvent être modifiés lors de la finalisation du produit.

---

## :material-clipboard-list: Navigation rapide

- [FAQ Openterface KeyMod](#faq-openterface-keymod)
  - [:material-clipboard-list: Navigation rapide](#material-clipboard-list-navigation-rapide)
  - [Général](#général)
  - [Connectivité](#connectivité)
  - [Fonctionnalités](#fonctionnalités)
  - [Pré-lancement](#pré-lancement)

---

## Général

**:material-chat-question:{ .faq } Qu'est-ce que KeyMod ?**

KeyMod est un émulateur HID (clavier et souris) compact USB + Bluetooth qui transforme votre téléphone en clavier et pavé tactile portables. Utilisez-le pour contrôler les appareils nécessitant une entrée clavier/souris—bornes, téléviseurs intelligents, décodeurs, affichages extérieurs—sans transporter un clavier complet.

**:material-chat-question:{ .faq } Quelles plateformes l'application KeyMod prend-elle en charge ?**

L'application contrôleur KeyMod Series se concentre sur **Android**, **iOS** et **iPadOS**. Nous développons également le contrôle desktop avec des logiciels **Windows et macOS** dans notre écosystème Openterface plus large.

**:material-chat-question:{ .faq } L'appareil cible a-t-il besoin de logiciels ?**

Non. KeyMod émule un clavier et une souris USB standard. L'appareil cible le reconnaît comme matériel HID plug-and-play—aucun pilote ou installation logicielle requis.

**:material-chat-question:{ .faq } KeyMod est-il open source ?**

Oui. KeyMod est un matériel et logiciel ouverts. Nous publierons les schémas, fichiers PCB, firmware, logiciels et BOM au fur et à mesure de l'évolution du projet.

---

## Connectivité

**:material-chat-question:{ .faq } USB ou Bluetooth—lequel utiliser ?**

- **USB** : Plus fiable, latence plus faible. À utiliser lorsque vous voulez la connexion la plus stable.
- **Bluetooth** : Sans fil. À utiliser lorsque vous voulez une configuration plus légère et que le scénario le permet.

**:material-chat-question:{ .faq } Quelles variantes matérielles sont prévues ?**

1. **Connecteur 2-en-1** — Prise USB A + USB C combinée pour une large compatibilité
2. **Version USB C** — Prise USB C dédiée pour les appareils modernes

---

## Fonctionnalités

**:material-chat-question:{ .faq } Puis-je créer des profils et macros personnalisés ?**

Oui. L'application mobile open source prend en charge les profils d'entrée personnalisés, macros, raccourcis clavier et raccourcis de flux de travail. Vous pouvez également utiliser le pavé numérique.

---

## Pré-lancement

**:material-chat-question:{ .faq } Quand KeyMod sera-t-il lancé ?**

KeyMod est en développement pré-lancement. Abonnez-vous sur la [page produit](/product/keymod/) pour les notifications de lancement et les mises à jour.

**:material-chat-question:{ .faq } Comment KeyMod est-il lié à Mini-KVM et KVM-Go ?**

KeyMod utilise le noyau HID éprouvé d'Openterface Mini-KVM. Il partage la même approche d'émulation clavier et souris basée sur le matériel, mais est conçu pour un cas d'utilisation différent : transformer votre téléphone en clavier/pavé tactile portable pour le contrôle local d'appareils, plutôt que la capture vidéo KVM-over-USB.
