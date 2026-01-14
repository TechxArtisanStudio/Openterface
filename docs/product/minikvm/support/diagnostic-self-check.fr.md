---
title: "Openterface Mini-KVM - Guide d'auto-vérification diagnostique"
description: "Guide étape par étape pour exécuter des tests d'auto-vérification diagnostique sur l'appareil Openterface Mini-KVM. Découvrez comment tester les connexions USB, détecter des problèmes et envoyer des rapports de défauts au support."
keywords: "Openterface Mini-KVM, auto-vérification diagnostique, dépannage KVM, diagnostics USB KVM, support Mini-KVM, test appareil KVM, test connexion USB, rapport de défaut KVM, guide dépannage Mini-KVM, outil diagnostic KVM, diagnostics serveur sans interface, outils dépannage IT"
---

# Openterface Mini-KVM - Guide d'auto-vérification diagnostique

Ce guide fournit des instructions étape par étape pour exécuter des tests d'auto-vérification diagnostique sur l'appareil Openterface Mini-KVM.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Unité fonctionnelle

**Étape 1 :** Dans l'application Openterface, ouvrez Paramètres → Paramètres…

**Étape 2 :** Dans la fenêtre des paramètres, allez dans Avancé & Débogage.

**Étape 3 :** Cliquez sur Ouvrir l'outil de diagnostic.

**Étape 4 :** Lorsqu'on vous le demande, cliquez sur Activer pour activer la journalisation diagnostique.

**Étape 5 :** Cliquez sur Vérifier maintenant pour démarrer l'auto-vérification.

**Étape 6 :** Cliquez sur Démarrer le test, puis débranchez et reconnectez le câble USB-C noir (côté cible) lorsqu'on vous le demande.

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**Étape 7 :** Cliquez sur Démarrer le test, puis débranchez et reconnectez le câble USB-C orange (côté hôte) lorsqu'on vous le demande.

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**Étape 8 :** Cliquez sur Démarrer le test, puis attendez que le test se termine.

**Étape 9 :** Cliquez sur Réinitialiser maintenant, puis attendez qu'il se termine.

**Étape 10 :** Cliquez sur Changer maintenant, puis attendez que le changement de taux de transmission se termine.

**Étape 11 :** Cliquez sur Démarrer le test, puis attendez environ 30 secondes. Ne touchez pas la cible pendant que le test s'exécute.

> **Note :** Le curseur peut bouger rapidement. Ne touchez pas la cible.

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**Étape 12 :** Vérifiez que tous les éléments affichent des marques de vérification vertes et que le processus est terminé.

**Étape 13 :** Cliquez sur ❌ (en haut à droite) pour fermer la fenêtre de diagnostic.

---

## Problème détecté (Exemple clavier/souris)

Suivez d'abord les Étapes 1 à 11 de « Unité fonctionnelle ». Les notes ci-dessous expliquent ce que vous verrez lorsqu'un problème de clavier/souris est détecté.

## Comment ce problème se manifeste

Dans cet exemple, la Connexion globale affiche ÉCHÉC d'abord car un problème de clavier/souris (HID) côté cible affecte la vérification globale. C'est un indicateur précoce, pas un problème distinct. (Vous verrez le statut ÉCHÉC mis en évidence à côté de « Connexion globale » à gauche.)

- **Connexion globale :** ÉCHÉC est affiché ici d'abord en raison du problème côté cible.

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **Plug & Play cible :** Après avoir exécuté cette étape, le résultat peut montrer plus clairement le problème côté cible.

> **Conseil :** Si une étape affiche ÉCHÉC, les diagnostics ne s'arrêteront pas, mais ils peuvent arrêter l'avancement automatique — donc vous devrez continuer manuellement.

## Test final supplémentaire (dépend du type de problème)

**Étape 12 :** Après le test de stress, les diagnostics peuvent afficher un test final supplémentaire selon le problème détecté ; dans cet exemple de clavier/souris, il continue avec la vérification des ports cible.

**Étape 13 :** Cliquez sur « Détecter les appareils » pour démarrer la vérification des ports cible, puis suivez les instructions à l'écran.

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## Ce qui se passe lorsqu'un problème est détecté

**Étape 14 :** Pour continuer, cliquez sur Suivant (barre inférieure) ou sélectionnez le test suivant dans le panneau de gauche.

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## Envoyer les journaux au support

**Étape 15 :** Cliquez sur Envoyer le rapport de défaut au support pour préparer le rapport.

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**Étape 16 :** Dans la fenêtre de rapport de défaut, entrez votre **Numéro de commande** et **Nom**.

**Étape 17 :** Cliquez sur **Ouvrir le dossier des journaux**, puis attachez les fichiers de journaux exportés à votre e-mail.

**Étape 18 :** Copiez l'**adresse e-mail de support**, collez le sujet et corps d'e-mail prémis en place, attachez une photo claire de la configuration (Mini-KVM + connexions hôte/cible), puis envoyez l'e-mail.

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**Étape 19 :** Cliquez sur ❌ (en haut à droite) pour fermer la fenêtre de diagnostic.