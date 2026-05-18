---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19 : Refonte de l'application, mode Compose KM Pro, support multi-langue et guides interactifs par mode"
description: "KeyCmd 0.19 apporte un changement majeur de nom de KeyMod à KeyCmd, le nouveau mode Compose KM Pro avec envoi HID Unicode, une interface multi-langue (coréen, italien, russe, pt-BR), des guides interactifs par mode et des dizaines d'améliorations UX."
keywords: "KeyCmd 0.19, sortie KeyCmd, changement de nom application, mode Compose, envoi HID Unicode, multi-langue, guides interactifs, mise à jour Openterface KeyCmd, émulateur HID, clavier virtuel, application clavier Android"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "Sortie de KeyCmd 0.19 — Mode Compose, refonte de l'application, multi-langue, guides interactifs"
  description: "KeyCmd 0.19 apporte le nouveau mode Compose, le changement de nom en KeyCmd, 4 nouvelles langues, des guides interactifs et d'importantes améliorations UX."
---

# KeyCmd 0.19 : Refonte de l'application, mode Compose KM Pro, support multi-langue et guides interactifs par mode

KeyCmd **0.19** (`versionCode` **19**) est une mise à jour majeure qui apporte le **changement de nom** de KeyMod à KeyCmd, le tout nouveau **mode Compose KM Pro** avec envoi HID compatible Unicode, une **interface multi-langue étendue** (incluant le coréen, l'italien, le russe et le portugais brésilien), des **guides interactifs par mode**, et des dizaines d'améliorations UX dans les modes clavier, gamepad et présentation.

## Refonte de l'application : KeyMod → KeyCmd

Le nom affiché de l'application est désormais **KeyCmd** sur tous les points d'entrée. Ce changement de marque clarifie la distinction entre le **matériel KeyMod** et son **application compagnon KeyCmd**.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="Écran d'accueil KeyCmd" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### Ce qui a changé

- **Nom affiché de l'application** : L'icône du lanceur et l'interface système affichent maintenant « KeyCmd »
- **Flux de bienvenue** : Signature et texte mis à jour de KeyMod à KeyCmd
- **Artéfacts CI et noms de fichiers APK** : Utilisent le préfixe **KeyCmd**
- `applicationId` reste **`com.openterface.keymod`** pour des mises à jour sur place sans interruption

Utilisateurs existants : vos paramètres, profils et appareils jumelés sont conservés. La mise à jour est transparente.

## Clavier et souris : expérience plein écran

KeyCmd offre une expérience plein écran de clavier, pavé tactile et pavé numérique — optimisée pour les orientations portrait et paysage.

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-fr" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="Clavier plein écran paysage" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="Pavé numérique paysage" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="Pavé numérique portrait" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="Clavier et pavé tactile portrait" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="Pavé tactile paysage" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="Codage à distance avec KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="Écran des paramètres KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-fr', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-fr', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-fr', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-fr', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-fr', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-fr', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-fr', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-fr', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-fr', 1)">❯</button>
  </div>
</div>

## KM Pro : mode Compose & Send

La plus grande nouveauté de la version 0.19 est le **mode Compose** dans KM Pro — un éditeur de texte dédié qui vous permet de taper de longs passages et de les envoyer en tant que frappes HID vers la machine cible.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Exécution de script en mode Compose" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">


### Éditeur Compose

- **Barre de raccourcis supérieure + ligne d'action de composition** avec contrôles **Effacer** et **Annuler/Effacer**
- **Conservation du brouillon** : votre texte est conservé lors des changements de sous-mode et même après un envoi réussi
- **Intégration IME** : tapez avec le clavier de votre téléphone, envoyez en tant que frappes HID propres
- **Progression d'envoi déterminée** : une barre de progression visible pour les longs tampons HID afin de savoir exactement où en est l'envoi

### Envoi HID compatible Unicode

- **Révision des risques en double mode** : avant d'envoyer du texte non-ASCII, une boîte de dialogue avertit de la compatibilité Unicode et fournit des actions d'inspection et de prévisualisation
- **Flux hexadécimal Unicode macOS** : sur les hôtes macOS, l'application utilise la méthode de saisie Option+code hexadécimal pour les caractères étendus
- **Boîtes de dialogue d'envoi plus sûres** : l'écran de révision adapte son contenu selon que le tampon est en ASCII pur ou contient des caractères Unicode
- **Outils d'inspection de caractères** : la boîte de dialogue de risque d'envoi fournit des actions **Vérifier** et **Aperçu**, et les hôtes macOS incluent une entrée dédiée **d'audit de chemin hexadécimal Unicode**

### Portée de KM Basic

Dans la version 0.19, **Compose & Send reste une fonctionnalité de Clavier et Souris Pro**. KM Basic se concentre sur les workflows de clavier plein écran, pavé tactile et pavé numérique.

## Support multi-langue

KeyCmd prend désormais en charge **11 langues d'interface**. Cette version ajoute quatre nouvelles traductions :

- **Coréen (ko)** : traduction complète de l'interface
- **Italien (it)** : traduction complète de l'interface
- **Russe (ru)** : traduction complète de l'interface
- **Portugais brésilien (pt-BR)** : traduction complète de l'interface

Combiné avec l'anglais, le chinois simplifié, le chinois traditionnel, le japonais, le français, l'allemand et l'espagnol existants, KeyCmd couvre désormais la grande majorité de notre base d'utilisateurs mondiale.

### Ce qui a changé

- **Sélecteur de langue** dans les Paramètres avec les noms canoniques des langues
- **En-têtes Bluetooth** et **aperçu de frappe** traduits
- **Correctifs lint de version** pour les onglets d'avertissement de composition dans toutes les langues

## Guides interactifs par mode

Chaque mode dispose désormais d'un **guide interactif intégré** qui vous accompagne pas à pas dans ses fonctionnalités.

### Guides disponibles

- **Guide Shortcut Hub** : ouvre le profil par défaut et couvre l'interface de détail, les onglets de catégories et la gestion des raccourcis
- **Guide Gamepad** : explique la disposition du gamepad, la gestion des modules et le système de préréglages
- **Guide KM Pro** : couvre le mode Compose, le panneau de raccourcis et les fonctionnalités Pro
- **Guide KM Basic** : explique le clavier plein écran, le geste de maintien-glissé des modificateurs et le pavé numérique

### Fonctionnalités des guides

- **Guides par mode** : chaque mode a son propre guide personnalisé
- **Feuille de rejeu** : revisitez n'importe quel guide à tout moment via le bouton **Guide de mode** (icône à gauche de la section de connexion)
- **Support i18n** : le contenu des guides est traduit dans toutes les langues de l'application
- **Optimisé paysage** : les feuilles inférieures s'adaptent correctement en orientation paysage

## Améliorations UX

### Clavier

- **Aperçu de frappe** : voyez exactement ce qui sera envoyé avant de taper. Activable via les Paramètres. Activé par défaut.
- **Correction HID de frappe rapide** : amélioration du timing de relâchement des frappes et fusion des événements de relâchement pour une saisie plus rapide
- **Gestion tactile des caractères alternatifs** : un appui long sur la touche `a` affiche maintenant les alternatives ¥ (haut), £ (gauche), € (droite) avec un retour visuel amélioré
- **Geste de maintien-glissé des modificateurs** : dans les guides KM Basic/Pro, une nouvelle étape enseigne le geste de maintien-glissé pour un accès rapide aux modificateurs

### Gamepad

- **Barre de session d'édition supprimée** : interface gamepad plus épurée sans l'ancienne barre d'outils de session d'édition
- **Interface et guide gamepad** : nouveau poli visuel et guide interactif intégré
- **Icône de guide de mode** : placée à gauche de la section de connexion pour un accès facile

### Présentation

- **Verrouillage portrait** : le mode Présentation est limité aux orientations portrait et portrait inversé pour un contrôle présentateur stable

### Interface et thème

- **Nuances d'accent** : remplacement du sélecteur de famille de couleurs de thème par des nuances visuelles pour une sélection plus facile
- **Alignement des accents UI** : tous les accents UI suivent maintenant la famille de couleurs de thème (et non la couleur primaire héritée)
- **Cluster droit de l'en-tête** : dimensions améliorées pour les icônes de connexion dans l'application principale et l'interface KM Basic
- **Style du bouton d'envoi Compose** : apparence du bouton d'envoi non-ASCII alignée en mode clair

### Paramètres

- **Réorganisation des paramètres** : noms canoniques des langues ; scripts d'installation d'émulateur renommés pour plus de clarté
- **Scripts d'aide au développement** : renommés pour une identification plus claire des appareils et des actions
- **Documentation FAQ** : mise à jour de `docs/FAQ.md` avec le comportement actuel de l'application

## Cas d'utilisation réels

### Codage à distance

KeyCmd n'est pas seulement pour la gestion de serveurs. Les développeurs l'utilisent pour des **sessions de codage à distance** — contrôle d'une machine de développement headless depuis un téléphone ou une tablette, avec clavier, pavé tactile et pavé numérique complets.

## Ce qui est inchangé

**Clavier et Souris Pro** (mode composite avec barres Shortcut Hub, dispositions divisées et comportement IME riche) reste l'expérience complète qu'il était auparavant. Tous les profils, préréglages et appareils jumelés existants sont conservés.

## Obtenir la mise à jour

**Cette version (0.19) :** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Note Beta :** L'application Android KeyCmd est toujours en phase bêta active. Le dépôt source n'est pas encore public — nous prévoyons de l'open-sourcer après une campagne de financement participatif réussie. Si vous êtes un testeur bêta et avez besoin du dernier APK, contactez-nous sur Discord et nous vous enverrons la version.

Les installations existantes se mettent à jour sur place.

## Compatible avec Mini-KVM et KVM-Go

L'application KeyCmd ne se limite pas au matériel KeyMod. Les utilisateurs Openterface existants peuvent également l'essayer :

- **KVM-Go** : connexion via **Bluetooth** ou **USB**
- **Mini-KVM** : connexion via **USB**

## Notes de mise à niveau

- **Changement de marque** : le nom de l'application passe de KeyMod à KeyCmd. Vos données sont conservées.
- **Mode Compose** : nouveau pour Clavier et Souris Pro.
- **Guides interactifs** : appuyez sur l'icône de guide (à gauche de la section de connexion) dans n'importe quel mode pour lancer le guide interactif.
- **Langues** : rendez-vous dans les Paramètres pour changer la langue de l'application. KeyCmd prend désormais en charge 11 langues d'interface.

Cordialement,

Openterface Team | TechxArtisan
