---
title: Astuce Copier/Coller Ubuntu (macOS → Ubuntu)
description: Corrigez les raccourcis de collage lors du contrôle d'Ubuntu depuis macOS avec Openterface. Utilisez le mode Windows pour un collage fiable style Ctrl, ou Édition → Coller comme solution de contournement en mode Mac.
keywords: Openterface, macOS, Ubuntu, copier coller, mode clavier, mode Windows, mode Mac, KVM, bureau à distance
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Astuce Copier/Coller Ubuntu (macOS → Ubuntu)

Lors du contrôle d'**Ubuntu** depuis **macOS** avec **Openterface**, le collage par raccourci peut ne pas fonctionner de manière fiable en **mode Mac**. Ce guide présente la correction recommandée et une solution de contournement simple.

![setting](https://assets2.openterface.com/images/setting.webp)

---

## Correction rapide (recommandé pour Ubuntu/Linux)

1. Ouvrez **Openterface** sur macOS.
2. Allez dans **Réglages**.
3. Trouvez **Mode de disposition du clavier de l'appareil cible**.
4. Sélectionnez **Mode Windows**.

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ Résultat : Les raccourcis de collage se comportent comme prévu sur Ubuntu (comportement style Ctrl).

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## Solution de contournement (si vous souhaitez rester en mode Mac)

Si vous préférez garder le **mode Mac**, vous pouvez toujours coller de manière fiable via le menu :

- **Édition → Coller**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ Résultat : Le collage fonctionne même si le raccourci de collage est incohérent en mode Mac.

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## Pourquoi cela se produit

La plupart des applications Ubuntu utilisent des raccourcis **basés sur Ctrl** pour coller. Dans certaines configurations, le mappage des raccourcis en **mode Mac** peut ne pas déclencher le collage de manière cohérente, tandis que **Édition → Coller** fonctionne de manière fiable.

---

## Résumé rapide

- **Meilleure expérience sur Ubuntu/Linux :** utilisez le **mode Windows**
- **Si vous restez en mode Mac :** utilisez **Édition → Coller**

---

## Besoin d'aide pour identifier le bon mode ?

Si vous n'êtes pas sûr du mode à utiliser, voici une règle simple :

- Si votre OS cible est **Ubuntu/Linux**, commencez par le **mode Windows** (le plus cohérent pour les raccourcis courants).
- Si vous contrôlez principalement des **cibles macOS** et souhaitez des raccourcis style Mac, utilisez le **mode Mac**.

Si vous changez souvent d'OS cible, pensez à mettre cette page en favori. C'est généralement une correction en un clic.

---

## FAQ

**Le mode Windows modifie-t-il mes raccourcis Mac ?**  
Il modifie la façon dont Openterface envoie les raccourcis à l'**appareil cible**, afin qu'Ubuntu reçoive le comportement **style Ctrl** attendu.

**Puis-je utiliser le collage par menu dans n'importe quel mode ?**  
Oui — **Édition → Coller** est une option fiable dans les deux modes.

**Cela affecte-t-il aussi Raspberry Pi OS ?**  
Souvent moins affecté, mais si vous observez un comportement similaire, la même correction s'applique.
