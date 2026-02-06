---
title: "Openterface Mini-KVM (Windows) - Guide d'auto-vérification diagnostique matériel"
description: "Guide étape par étape pour exécuter l'auto-vérification diagnostique matériel dans l'application Openterface pour Windows. Découvrez comment tester les connexions USB, détecter des problèmes et envoyer des rapports de diagnostic au support."
keywords: "Openterface Mini-KVM, Windows, diagnostic matériel, auto-vérification diagnostique, dépannage KVM, diagnostics USB KVM, support Mini-KVM, test appareil KVM, Windows KVM, rapport de défaut KVM, guide dépannage Mini-KVM"
---

# Openterface Mini-KVM (Windows) — Guide d'auto-vérification diagnostique matériel

Ce guide explique comment exécuter l'auto-vérification **Diagnostic matériel** dans la version **Windows** de l'application Openterface, et comment envoyer le rapport de diagnostic au support si un problème est détecté.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uSq3BDc_SBU?si=rREugsUxX1FzDGqm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Avant de commencer

- **Mettre à jour l'application :** Assurez-vous d'avoir la dernière version de [l'application Openterface pour Windows](/app) installée avant d'exécuter les diagnostics. Vérifiez le menu de l'application pour les mises à jour.
- Connectez Mini-KVM à **Hôte** et **Cible**.
- Gardez l'appareil cible inactif pendant les tests (surtout pendant le test de stress).

> **Important (Windows) :** Les diagnostics **n'avancent pas automatiquement**.  
> Pour passer d'un test à l'autre, utilisez **Suivant** (barre inférieure) **ou** cliquez sur un élément de test dans le **panneau de gauche**.  
> Chaque test s'exécute en cliquant sur **Vérifier maintenant**.

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## Unité fonctionnelle (PASS)

### Étape 1 — Ouvrir Diagnostic matériel (Windows)
Dans l'application Openterface pour Windows, ouvrez : **Avancé → Diagnostic matériel**.  

### Étape 2 — Exécuter l'auto-vérification
Dans la fenêtre Diagnostic matériel, cliquez sur **Vérifier maintenant** pour exécuter l'étape de diagnostic actuelle.  

### Étape 3 — Plug & Play cible (suivre les instructions)
Lorsque **Plug & Play cible** vous demande de reconnecter le câble cible, suivez les instructions à l'écran.  
Certaines configurations peuvent demander de **débrancher/rebrancher plus d'une fois** (par ex. deux fois).  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### Étape 4 — Plug & Play hôte (suivre les instructions)
Suivez les instructions à l'écran pour le côté hôte.  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### Étape 5 — Test de stress (ne pas toucher la cible)
Pendant le **test de stress**, la souris cible peut se déplacer automatiquement pour la détection.  
**Ne touchez pas la cible** pendant que le test s'exécute.  

> **Note :** La souris peut bouger rapidement — ne touchez pas la cible.

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### Étape 6 — Confirmer PASS
Continuez jusqu'à ce que l'auto-vérification soit terminée. Si tout est normal, les résultats afficheront **PASS / Tous les tests réussis**.  

---

## Problème détecté (Exemple clavier/souris)

Si un problème est détecté, un ou plusieurs éléments peuvent afficher **ÉCHEC**.

### Étape 1 — Exécuter le même Diagnostic matériel
Ouvrez **Avancé → Diagnostic matériel**, puis cliquez sur **Vérifier maintenant** pour démarrer.  

### Étape 2 — Continuer les vérifications
Continuez les tests restants jusqu'à ce que les diagnostics soient terminés.  

### Étape 3 — L'e-mail de support s'ouvre automatiquement
Lorsque les diagnostics se terminent avec un problème, une fenêtre **E-mail de support** s'ouvre automatiquement.  

---

## Envoyer les journaux au support (Windows)

### Étape 4 — Appliquer Numéro de commande + Nom
Entrez votre **Numéro de commande** et **Nom**, puis cliquez sur **Appliquer** pour les insérer dans le brouillon d'e-mail. 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### Étape 5 — Copier l'adresse e-mail et le brouillon
- Cliquez sur **Copier l'e-mail** pour copier l'adresse e-mail du support.
- Cliquez sur **Copier le brouillon** pour copier le contenu de l'e-mail prérempli (y compris Numéro de commande + Nom).  
Collez les deux dans votre client e-mail (Gmail/Outlook/etc.).  

![copy](https://assets2.openterface.com/images/copy.webp)

### Étape 6 — Joindre les fichiers de journaux corrects
Cliquez sur **Ouvrir le dossier des fichiers**. L'outil indiquera quels fichiers joindre.  
**Joignez uniquement les fichiers de journaux demandés** (le dossier peut contenir de nombreux autres journaux).  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### Étape 7 — Joindre également une photo de la configuration
Dans le même e-mail, joignez une **photo claire de la configuration** montrant :
- l'appareil Mini-KVM,
- les connexions **Hôte** et **Cible**,
- les ports et câbles clairement visibles.  

### Étape 8 — Envoyer l'e-mail
Envoyez l'e-mail au support (texte du brouillon + journaux demandés + photo de configuration joints).  

---

## Ce qu'il faut inclure lors de la prise de contact avec le support

- **Numéro de commande**
- **Fichiers de journaux de diagnostic demandés**
- **Photo de la configuration** (Mini-KVM + câblage hôte/cible)
