---
draft: false
date: 2026-05-21
title: "Mise à jour KVM-GO : contrôlez votre cible depuis votre téléphone avec KeyCmd 0.19"
description: "Utilisez KeyCmd 0.19 avec KVM-GO via USB ou Bluetooth : claviers KM Basic et Pro, mode Compose, préréglages de manette, Shortcut Hub et commandes de présentation—aucun dongle vidéo requis pour l'entrée HID."
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, application KVM-GO Android, contrôle téléphone KVM-over-USB, Openterface KeyCmd, clavier virtuel KVM, KVM-GO Bluetooth USB, mode KM Pro Compose, KVM-GO HDMI DP VGA, application Openterface KVM, entrée KVM portable"
author: "Openterface Team | TechxArtisan"
category: "Mises à jour produits"
tags: ["KVM-GO", "KeyCmd", "Mises à jour produits", "Android", "USB", "Bluetooth", "Clavier", "Manette", "Sortie"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 — contrôlez votre cible depuis votre téléphone"
  description: "KeyCmd 0.19 s'associe au KVM-GO via USB ou Bluetooth pour le clavier, la souris, la manette, les raccourcis et Compose—tandis qu'Openterface KVM gère la vidéo quand vous en avez besoin."
---

# Mise à jour KVM-GO : contrôlez votre cible depuis votre téléphone avec KeyCmd 0.19

Bonjour à tous,

Merci de soutenir **KVM-GO** et pour votre patience pendant que les unités passent par la production et l'expédition. Nous savons que beaucoup d'entre vous attendent encore leur matériel, et nous voulons que votre installation soit complète dès le premier jour.

Parallèlement à l'application **Openterface KVM** (vidéo et contrôle KVM complet sur votre téléphone ou tablette), nous avons amélioré **KeyCmd**, notre application compagnon pour l'entrée clavier, souris, manette et raccourcis. **KeyCmd 0.19** est la version que nous recommandons aujourd'hui si vous utilisez KVM-GO. Associez-la via **USB** ou **Bluetooth**, installez-la par-dessus toute version précédente, et vos paramètres, profils et appareils associés seront conservés.

![KVM-GO sur un ordinateur portable avec le clavier KeyCmd sur un téléphone](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp)

Voici ci-dessous ce que KeyCmd fait avec KVM-GO, quel mode ouvrir pour chaque tâche et comment en tirer le meilleur parti sur une machine cible réelle.

![Écran d'accueil de KeyCmd](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp)

## Les modes et comment les utiliser

### Clavier et souris (Basic)

Ouvrez ce mode lorsque vous voulez un **clavier simple en plein écran** sans que rien d'autre ne vienne vous gêner.

**Idéal pour :** les mots de passe BIOS, les commandes shell courtes, la saisie sur pavé numérique ou le contrôle de la souris avec un grand pavé tactile pendant que KVM-GO vous montre l'écran.

**Comment l'utiliser :**

- Ouvrez **KM Basic** depuis le menu de navigation.
- Utilisez le clavier à l'écran, le **pavé numérique** (portrait ou paysage) ou l'onglet **pavé tactile** selon vos besoins.
- Dans les **Paramètres**, choisissez les **touches rémanentes** (appuyez pour verrouiller Maj/Ctrl) ou les modificateurs **style accord** si vous préférez les combinaisons maintenir-et-appuyer.

**Pourquoi c'est utile :** plus d'espace à l'écran pour les touches, moins d'interface, plus rapide lorsque vous n'avez besoin que de la saisie et non des raccourcis.

![Clavier plein écran KM Basic](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp)

![Pavé numérique KeyCmd en paysage](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp)

### Clavier et souris (Pro)

![Clavier divisé KM Pro en paysage](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp)

![Clavier et pavé tactile KeyCmd en portrait](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp)

Ouvrez ce mode pour le **travail de contrôle quotidien** sur les machines derrière KVM-GO : claviers divisés, IME, barres Shortcut Hub et l'éditeur **Compose**.

**Idéal pour :** les sessions de frappe plus longues, les macros et les raccourcis, l'envoi de blocs de texte ou de scripts à l'hôte pendant que vous observez le résultat sur la vue KVM.

![Mode Compose envoyant un script](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp)

**Compose** vaut la peine d'être essayé si vous collez souvent des commandes ou des scripts : écrivez sur votre téléphone, révisez, puis envoyez comme des frappes de touches à l'hôte. Une [courte démo sur YouTube](https://www.youtube.com/watch?v=_rJF-hTF3_E) montre le flux de bout en bout.

**Comment l'utiliser :**

- Ouvrez **KM Pro** depuis le menu de navigation.
- Utilisez le clavier et le pavé tactile comme dans le mode Basic, plus les catégories **Shortcut Hub** en haut pour des actions en un seul clic que vous configurez dans les profils.
- Ouvrez **Compose** pour rédiger un texte plus long sur votre téléphone, révisez-le, puis cliquez sur **envoyer** en tant que frappes HID. Les envois longs affichent une barre de progression. Si votre texte contient des caractères non-ASCII, l'application vous avertit avant l'envoi afin que vous puissiez vérifier la compatibilité de l'hôte (utile sur macOS en particulier).

**Pourquoi c'est utile :** un seul endroit pour taper, pointer, utiliser des raccourcis et des flux de travail de type collage sans avoir à transporter un clavier complet vers la cible.

### Manette (Gamepad)

Ouvrez ce mode lorsque vous voulez une disposition de **manette virtuelle** à l'écran, réglée pour les jeux ou toute application sur la cible qui attend une manette.

**Idéal pour :** les émulateurs, les jeux occasionnels ou une surface de contrôle compacte avec sticks et boutons pendant que KVM-GO gère l'affichage.

**Comment l'utiliser :**

- Passez en mode **Gamepad**.
- Appuyez sur **Preset** dans la barre d'outils pour faire **défiler** les dispositions enregistrées. **Appuyez longuement sur Preset** pour ouvrir la liste complète, **importer/exporter**, ou **ajouter des modules** (sticks, boutons, pavés tactiles).
- Commencez par le préréglage **emu-6** fourni et éditez-le à partir de là. Vous pouvez ajouter **plusieurs pavés tactiles** et des modules de sticks supplémentaires dans une seule disposition.

**Pourquoi c'est utile :** vous n'êtes pas limité à une seule disposition d'usine ; enregistrez des dispositions par jeu ou par machine et partagez les préréglages avec d'autres.

![Disposition de préréglage de manette](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp)

![Préréglage de manette utilisé dans Minecraft](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp)

*Préréglage personnalisé pour Minecraft.*

### Shortcut Hub

C'est le centre des **profils et raccourcis** à l'intérieur de KM Pro : catégories, panneaux de détails et raccourcis que vous affectez aux barres.

**Idéal pour :** les opérations répétitives sur la cible (ouvrir le terminal, coller une chaîne de commandes, basculer les paramètres) pendant que KVM-GO reste connecté pour la vidéo.

**Comment l'utiliser :**

- Depuis KM Pro, travaillez dans le profil **Default** (ou le vôtre).
- Utilisez les onglets de catégorie et l'interface de détails pour gérer les raccourcis.
- Suivez la **visite guidée du Shortcut Hub** si vous découvrez l'organisation des profils.

### Présentation

Une surface de contrôle de style **télécommande de présentation** plus simple, maintenue en **portrait** pour que les boutons ne bougent pas lorsque vous faites pivoter le téléphone.

**Idéal pour :** faire défiler des diapositives ou des commandes de présentation légères sur la cible.

![Mode Présentation contrôlant Google Slides](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp)

---

## Langues

L'interface de l'application est disponible en **11 langues**. Ajouts récents : coréen, italien, russe et portugais brésilien.

Ouvrez **Settings** → **App language** pour changer de langue.

---

## Obtenez KeyCmd 0.19 et connectez-vous au KVM-GO

**Téléchargement :** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

Installez par-dessus votre application existante si vous en avez déjà une. Pas besoin d'effacer les données.

**Connectez-vous au KVM-GO (le port vidéo peut rester débranché) :**

Pour les **trois variantes de KVM-GO** (HDMI, VGA et DP), vous n'avez pas besoin de brancher le **connecteur vidéo du dongle** à quoi que ce soit pour l'entrée KeyCmd. Le port HDMI, VGA ou DP peut rester vide. Choisissez l'une des configurations ci-dessous.

**Option A — Bluetooth (la cible alimente le KVM-GO)**

1. Branchez le **câble USB noir court** sur le port **Target** du KVM-GO et sur la machine que vous contrôlez. Cette connexion seule **alimente** le KVM-GO.
2. Sur votre téléphone, ouvrez **KeyCmd** et trouvez le KVM-GO via **Bluetooth**.

**Option B — USB vers votre téléphone Android (port Host)**

1. Branchez le **câble orange long** depuis le port **Host** du KVM-GO sur votre téléphone Android.
2. Ouvrez **KeyCmd** et connectez-vous via **USB** dans l'application.

![Port Target du KVM-GO connecté à un ordinateur portable via le câble USB noir court](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp)

Pour une vidéo en plein écran plus l'entrée, utilisez **Openterface KVM** pour l'affichage de la cible et **KeyCmd** pour le clavier, la souris et les raccourcis. KeyCmd seul suffit lorsque la cible possède déjà son propre écran et que vous n'avez besoin que de l'entrée.

**Fonctionne également avec le Mini-KVM** via USB si vous utilisez les deux appareils.

> **Encore en bêta.** Les préréglages de manette et les envois Compose peuvent se comporter différemment selon l'OS de l'hôte. Si quelque chose d'étrange se produit avec le KVM-GO, contactez-nous sur **Discord** avec une capture d'écran, votre variante de KVM-GO (HDMI / DP / VGA) et ce que vous attendiez.

> **Code source :** Pas encore public. Nous prévoyons de passer en open-source après les étapes de financement participatif sur les projets connexes. Demandez sur Discord si vous avez besoin d'aide pour trouver l'APK.

---

## À propos de KeyMod (optionnel, séparé du KVM-GO)

Nous développons également **[KeyMod](https://openterface.com/product/keymod/)**, un dongle HID USB et Bluetooth dédié pour la même application KeyCmd. Les contributeurs du KVM-GO n'ont pas besoin de KeyMod pour les flux de travail ci-dessus ; KeyCmd via KVM-GO est la voie que nous vous recommandons de suivre actuellement.

Si vous êtes curieux au sujet d'un dongle autonome pour des configurations sans KVM, vous pouvez suivre la [campagne KeyMod sur Crowd Supply](https://www.crowdsupply.com/techxartisan/openterface-keymod). C'est indépendant de l'expédition du KVM-GO.

---

## Nous aimerions recevoir vos commentaires

Si vous avez quelques minutes, installez **KeyCmd 0.19**, connectez-le à votre KVM-GO (ou Mini-KVM) et dites-nous ce qui vous semble encore peu pratique. Les rapports provenant de cas d'utilisation sur le terrain (chariots d'urgence) et de laboratoires à domicile (homelab) vont directement dans nos prochaines versions.

Moyens concrets d'aider le projet KVM-GO :

- **Partagez ce qui fonctionne** sur Discord ou dans votre communauté (astuces BIOS, couplage Bluetooth, modes préférés)
- **Parlez-en à un collègue** qui gère des équipements sans écran et qui pourrait utiliser un KVM de poche
- **Continuez à envoyer des commentaires honnêtes**, en particulier sur les points rugueux. Cela façonne le produit plus que les simples encouragements

Merci encore de soutenir KVM-GO et de nous aider à rendre le KVM-over-USB portable meilleur pour tous.

Cordialement,

**L'équipe Openterface | TechxArtisan**
