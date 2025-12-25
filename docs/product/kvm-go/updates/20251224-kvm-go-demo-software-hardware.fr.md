---
draft: false
date: 2025-12-24
title: "Nouvelle vidéo de démo, progression logicielle et ce qui se trouve à l'intérieur du KVM-GO"
description: "Regardez la nouvelle vidéo de démo KVM-GO montrant les versions HDMI/DP/VGA en action. Découvrez la mise à jour logicielle unifiée pour Mini-KVM et KVM-GO, les améliorations matérielles incluant le processeur vidéo MS2130S 4K@60Hz et le microcontrôleur CH32V208, ainsi que les fonctionnalités à venir comme le support EDID personnalisé. Mise à jour de campagne : 72k $ avec plus de 220 soutiens."
keywords: "vidéo de démo KVM-GO, mise à jour logicielle KVM-GO, amélioration matérielle KVM-GO, processeur vidéo MS2130S, microcontrôleur CH32V208, KVM 4K@60Hz, comparaison KVM-GO vs Mini-KVM, application unifiée Openterface, performance clavier/souris KVM-GO, support EDID personnalisé, contrôle script KVM-GO, certification OSHWA, crowdfunding KVM-GO, Crowd Supply KVM-GO, Openterface KVM-GO, TechxArtisan, comparaison matérielle KVM-over-USB"
author: "TechxArtisan Studio"
category: "Mises à jour du produit"
tags: ["KVM-GO", "Mises à jour du produit", "Logiciel", "Matériel", "Vidéo de démo", "Crowdfunding", "Analyse technique"]
featured: true
social:
  image: "https://assets.openterface.com/images/blog/Gemini_Generated_Image_kvm-go.webp"
  title: "Nouvelle vidéo de démo, progression logicielle et ce qui se trouve à l'intérieur du KVM-GO"
  description: "Découvrez le KVM-GO en action, apprenez sur les mises à jour logicielles unifiées et découvrez les améliorations matérielles qui alimentent notre dispositif KVM-over-USB de nouvelle génération."
---

# Nouvelle vidéo de démo, progression logicielle et ce qui se trouve à l'intérieur du KVM-GO

Salut à tous ! Désolé pour cette période calme. Nous avons travaillé intensivement à polir à la fois le matériel et le logiciel pour [KVM-GO](https://openterface.com/product/kvm-go/), et le temps a filé. À la fin de décembre, nous avons atteint **72k $ avec plus de 220 soutiens**, ce qui est incroyable. Si vous pouvez nous aider à aller plus loin, veuillez **faire connaître le projet** !

Merci infiniment pour votre patience et votre soutien. Oui, Noël a certainement ajouté au chaos 🙂🎄 Maintenant, rattrapons le temps.

![blog-Gemini_Generated_Image_kvm-go](https://assets.openterface.com/images/blog/Gemini_Generated_Image_kvm-go.webp)
*Image à thème de Noël générée avec Nano Banana, basée sur des photos réelles de nos produits KVM-GO.*

## Nouvelle vidéo de démo : Le KVM-GO en action

Nous venons de publier une [**nouvelle vidéo de démo**](https://www.youtube.com/watch?v=459rWCQbJRE) montrant le KVM-GO en utilisation réelle.


Dans la vidéo, vous verrez :

* Les versions KVM-GO **HDMI / DP / VGA** en action
* Ce qui est inclus **dans la boîte**
* Comment contrôler différents appareils cibles
* Comment le KVM-GO s'intègre dans des workflows réels, de l'accès rapide aux configurations multi-cibles

Si vous êtes curieux d'en savoir plus sur des tests manuels et des usages réels, n'hésitez pas à consulter notre [réseau social](https://openterface.com/about/community/). Nous partageons souvent des extraits bruts de tests et des scénarios pratiques montrant comment le KVM-GO se comporte sur les fronts technologiques réels.

## Progrès logiciels : Une seule application pour Mini-KVM et KVM-GO

Du côté logiciel, nous avons fait un pas solide.

Nos dernières mises à jour permettent à l'**application Openterface d'être utilisée de manière fluide avec à la fois le Mini-KVM et la série KVM-GO**. Pour les utilisateurs, cela signifie :

* Une expérience cohérente à travers les produits
* Moins de fragmentation si vous utilisez plus d'un appareil Openterface

Nous avons également consacré du temps à améliorer **la performance des claviers et souris**, en mettant l'accent sur :

* Une latence globale plus faible
* Un traitement d'entrée plus stable, y compris une meilleure détection de l'état de connexion et de la qualité du signal
* Une réponse plus rapide lors d'interactions rapides ou continues

Bien que le jeu ne soit pas l'utilisation principale ciblée de nos solutions KVM, nous attachons toujours une grande importance à la réactivité des entrées dans les scénarios réels. Si vous êtes intéressé par les détails techniques, notamment sur macOS, nous avons récemment publié une analyse approfondie ici :
👉 **[Vitesse de la souris et performance de jeu du Mini-KVM Openterface sur macOS](https://openterface.com/app/updates/20251218-macos-mouse-speed/)**

Beaucoup des améliorations abordées là-bas sont désormais directement intégrées à notre pile logicielle unifiée pour le Mini-KVM et le KVM-GO.

## Améliorations matérielles clés dans le KVM-GO (par rapport au Mini-KVM)

Pour ceux qui s'intéressent aux détails internes, voici un rapide aperçu des changements matériels clés du Mini-KVM au KVM-GO.

### Amélioration de la chaîne vidéo

| Aspect           | **MS2109 (Mini-KVM)**    | **MS2130S (KVM-GO)** | Amélioration           |
| ---------------- | ------------------------ | -------------------- | --------------------- |
| Entrée HDMI       | 4K @ 30Hz                | 4K @ 60Hz            | Double bande passante d'entrée    |
| Sortie vidéo USB | 1080p @ 30Hz             | 4K @ 60Hz            | Quadruple débit de pixels   |
| Échelle interne | 4K → 1080p               | 4K natif            | Aucune réduction forcée |
| Latence d'image    | Plus élevée (échelle + tampon) | Plus basse (chemin direct)  | Latence réduite       |

### Amélioration de l'émulation clavier et souris USB

| Aspect             | **CH340 + CH9329 (Mini-KVM)** | **CH32V208 (KVM-GO)** | Amélioration     |
| ------------------ | ----------------------------- | --------------------- | --------------- |
| Nombre de puces         | 2 puces                       | MCU unique            | Système plus simple  |
| Gestion USB       | Pont USB–Série                | Périphérique USB natif     | Latence plus basse   |
| Génération HID     | Fonction fixe                | Définie par le firmware      | Contrôle complet    |
| Chemin de données          | USB → UART → HID              | USB → HID             | Un saut en moins |
| Compatibilité BIOS | Mixte                         | Excellente             | Plus fiable   |

## Fonctionnalités avancées en développement actif

Plusieurs fonctionnalités avancées sont planifiées et activement développées pour le firmware final du KVM-GO. Aperçu rapide :

* **Support EDID personnalisé** pour résoudre les problèmes de compatibilité d'affichage
* **Contrôle par script** pour l'automatisation et les workflows avancés

Nous partagerons plus de détails à mesure que ces fonctionnalités mûrissent.

## Engagement open source (comme d'habitude)

Oui, **le KVM-GO restera pleinement open source**.

Une fois que la conception matérielle sera finalisée pour la production de masse, nous déposerons une demande de **certification OSHWA (Open Source Hardware Association)**.

Tous les fichiers de conception matérielle et modèles STL seront publiés ici :
👉 [https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware](https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware)

La transparence et la collaboration communautaire restent au cœur de ce que nous faisons.

## Derniers jours de la campagne : Un rappel amical

Nous sommes maintenant dans les **derniers jours** de la campagne de crowdfunding.

Le crowdfunding est **la meilleure chance d'obtenir le KVM-GO au prix le plus bas**. Une fois que la campagne se terminera et que nous passerons aux commandes post-crowdfunding, le prix augmentera.

Si vous étiez hésitant, c'est maintenant le moment.

👉 **Soutenez la campagne et sécurisez votre unité sur Crowd Supply :**
[https://www.crowdsupply.com/techxartisan/openterface-kvm-go](https://www.crowdsupply.com/techxartisan/openterface-kvm-go)

Merci à nouveau pour votre patience, votre confiance et votre soutien. D'autres mises à jour sont en route bientôt, et nous essaierons de ne plus rester silencieux. Des vœux de joyeuses fêtes de la part de toute l'équipe !

**L'équipe Openterface | TechxArtisan**