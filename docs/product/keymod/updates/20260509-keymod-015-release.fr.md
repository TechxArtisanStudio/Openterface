---
draft: false
date: 2026-05-09
title: "KeyMod 0.15 : Pipeline de préréglages du gamepad, Clavier et souris (Basic), Dispositions multi-touchpad"
description: "KeyMod 0.15 introduit la pipeline de préréglages du gamepad avec le schéma v7, les dispositions multi-touchpad, le niveau Clavier et souris (Basic) avec clavier plein écran, et le branding KeyMod dans toute l'application. Une avancée majeure vers une expérience de saisie soignée."
keywords: "KeyMod 0.15, KeyMod version, préréglage gamepad, multi-touchpad, clavier souris basic, branding KeyMod, Openterface KeyMod mise à jour, émulateur HID, gamepad virtuel, appli clavier Android"
author: "TechxArtisan Studio"
category: "Mises à jour du produit"
tags: ["KeyMod", "Mises à jour du produit", "Version", "Gamepad", "Clavier", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 — préréglages gamepad, niveau basic, multi-touchpad"
  description: "KeyMod 0.15 apporte la pipeline de préréglages du gamepad v7, un niveau dédié Clavier et souris (Basic), des dispositions multi-touchpad et un nouveau branding KeyMod."
---

# KeyMod 0.15 : Pipeline de préréglages du gamepad, Clavier et souris (Basic), Dispositions multi-touchpad

KeyMod **0.15** (`versionCode` **15**) est une version jalalon qui apporte trois fonctionnalités majeures : la **pipeline de préréglages du gamepad** avec le schéma de disposition **v6-v7**, le niveau dédié **Clavier et souris (Basic)** et les dispositions **multi-touchpad**. Cette mise à jour apporte également le branding **KeyMod** complet dans le flux d'accueil et les artefacts de build.

## Gamepad : Pipeline de préréglages v7

Le gamepad utilise désormais un véritable **système de préréglages** qui permet de sauvegarder, charger, importer et exporter des dispositions de contrôleur personnalisées.

### Ce qui a changé

- **Preset store v7** remplace les anciennes dispositions intégrées. Les préréglages de fabrique classiques (`preset_classic_*`) et **Two buttons** (`preset_two_buttons`) ont été supprimés du disque. Seul **`preset_default`** reste comme disposition de fabrique protégée contre la suppression.
- **Schéma v7** rend **`stick_left`** optionnel. Une disposition peut désormais ne plus avoir aucun module pouce gauche. Le menu **Add module** insère **`stick_left`**, **`stick_left_2`**, **`stick_left_3`**, etc.
- **Support multi-touchpad** : les préréglages peuvent inclure plusieurs touchpads (`touchpad_1`, `touchpad_2`). Ajouter un touchpad alloue le prochain id disponible avec une ancre légèrement décalée. Les boutons de souris L/M/R intégrés sont partagés entre tous les touchpads.
- **Taille des boutons de souris du touchpad** : les boutons de souris utilisent maintenant un rayon de dessin par défaut plus grand. Vous pouvez ajuster la taille via un appui long **Mouse button size** sur le touchpad, ou **This button size** sur des modules de souris individuels.
- **Valeurs par défaut du stick auxiliaire** : **`stick_left_2+`** par défaut sur croix D-pad + mappage WASD.

### Gestion des préréglages

- **Appuyez** sur la puce Preset dans la barre d'outils pour parcourir les dispositions disponibles
- **Appui long** pour la liste complète des préréglages avec options d'importation, ajout de module et exportation
- La disposition **emu-6** fournie sert de préréglage de démarrage
- Le créateur d'exportation prend en charge l'i18n pour partager des préréglages entre langues

## Clavier et souris (Basic)

Un niveau dédié de clavier plein écran conçu pour la saisie concentrée sans l'en-tête de l'application.

### Ce que vous obtenez

- **Clavier plein écran** sans l'en-tête principal de l'app pour plus d'espace d'écran
- **Pavé numérique portrait et paysage** : grille 5x8 en portrait (PrtSc / ScrLk / Pause / Home / End), grille 8x5 en paysage avec + grand, Entrée et 00
- **Portail d'envoi ASCII-only IME** : tapez du texte long en mode compose, envoyez-le en frappes HID propres
- **Répétition par appui long** : maintenez les touches caractère/fonction pour la répétition automatique (~400ms de délai, ~50ms de répétition)
- **Aperçu de touche** : une bulle flottante affiche l'étiquette effective au-dessus de la touche appuyée
- **Retour haptique** et surfaces de touches **adaptées au thème**

### Modificateurs Sticky vs Chord

Les paramètres vous permettent de choisir entre **modificateurs sticky** (appui pour verrouiller) et **momentané + chord par appui long** (par défaut) pour le clavier Basic.

## Branding

- Le nom d'affichage de l'app est maintenant **KeyMod**
- L'écran d'accueil affiche le logotype **KeyMod**
- Les artefacts CI et les noms de fichiers APK utilisent le préfixe **KeyMod**
- `applicationId` reste **`com.openterface.keymod`** pour les mises à jour in-place

## Ce qui ne change pas

**Clavier et souris Pro** (mode composite avec les bandes Shortcut Hub, dispositions divisées et comportement IME riche) reste l'expérience complète qu'il était auparavant.

## Obtenir la mise à jour

**Cette version (0.15) :** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

> **Note beta :** L'app KeyMod pour Android est toujours en phase beta active. Le repo n'est pas encore public — nous prévoyons de l'open-sourcer après une campagne crowdfunding réussie. Si vous êtes beta testeur et avez besoin du dernier APK, contactez-nous sur Discord et nous vous enverrons le build.

> **Problèmes connus :** Cette version introduit des changements importants sur le système de préréglages du gamepad et le niveau clavier Basic. Notre équipe dev effectue encore des tests en interne, des bugs peuvent donc survenir. Si vous rencontrez quelque chose d'inattendu, signalez-le sur Discord — vos retours nous aident à stabiliser plus vite.

Les installations existantes se mettent à jour in-place.

## Compatible avec Mini-KVM et KVM-Go

L'application KeyMod ne se limite pas au matériel KeyMod. Les utilisateurs actuels d'Openterface peuvent également l'essayer :

- **KVM-Go** : connexion via **Bluetooth** ou **USB**
- **Mini-KVM** : connexion via **USB**

## Notes de mise à jour

- **Gamepad** : votre préférence précédente à deux boutons active automatiquement le préréglage **Two buttons** au premier lancement. Utilisez **Preset** (appuyez pour parcourir, appui long pour la liste) au lieu de l'ancien contrôle 1 Button / 2 Buttons.
- **Clavier et souris (Basic)** : ouvrez Basic pour découvrir le clavier plein écran. Le mode Pro est disponible via le tiroir de navigation pour l'expérience complète Shortcut Hub.

Cordialement,

Openterface Team | TechxArtisan
