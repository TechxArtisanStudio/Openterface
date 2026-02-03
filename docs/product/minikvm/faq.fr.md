---
title: FAQ pour Openterface Mini-KVM
description: Questions fréquemment posées sur le Mini-KVM, couvrant les fonctionnalités, la compatibilité, le dépannage et les plans futurs.
keywords: Mini-KVM, Openterface, commutateur KVM, open-source, dépannage, capture vidéo, USB, compatibilité, auto-vérification diagnostique, contrôle clavier souris, diagnostic matériel, support
---

# FAQ pour Openterface Mini-KVM

Bienvenue dans la FAQ de notre produit phare **Openterface Mini-KVM**.  
Si vous ne trouvez pas ce dont vous avez besoin, **envoyez-nous un email à [info@openterface.com](mailto:info@openterface.com)** ou **rejoignez notre communauté** sur [Discord](/discord) ou [Reddit](/reddit).

⚠️ _Les FAQ peuvent être obsolètes — merci de nous faire savoir si vous voyez quelque chose qui nécessite une mise à jour._

---

## :material-clipboard-list: Navigation rapide

-   [Port USB et transfert de fichiers](#port-usb-et-transfert-de-fichiers)
-   [Technique](#technique)
-   [Contrôle](#contrôle)
-   [Vidéo](#vidéo)
-   [Dépannage](#dépannage)
-   [Plus](#plus)

---

## Port USB et transfert de fichiers

**:material-chat-question:{ .faq } Peut-il transférer des fichiers ?**

Oui — via le port USB-A commutateur partagé entre l'hôte et la cible.

**:material-chat-question:{ .faq } Puis-je basculer le port USB en logiciel ?**

Oui, sur la version matérielle **v1.9+**.

**:material-chat-question:{ .faq } Pourquoi USB 2.0 au lieu de 3.0 ?**

USB 2.0 est suffisant pour la vidéo 1080p@30Hz + HID + transfert de fichiers à vitesse standard tout en restant compact, plus frais et plus abordable.  
USB 3.0 pourrait apparaître dans les futurs modèles pro.

---

## Technique

**:material-chat-question:{ .faq } Open-source ?**

Oui — certifié par [OSHWA](https://certification.oshwa.org/cn000015.html). Le matériel et le logiciel sont sur [GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

**:material-chat-question:{ .faq } Accès BIOS**

La connexion USB directe permet un contrôle complet au niveau BIOS, contrairement aux outils uniquement distants (VNC, TeamViewer).  
Les machines plus anciennes peuvent avoir des problèmes BIOS pour reconnaître notre hub USB — merci de signaler les cas.

**:material-chat-question:{ .faq } Transmission vidéo/données**

La vidéo est capturée via HDMI et envoyée via USB 2.0.  
Le port USB commutateur vous permet de partager des disques ou d'autres appareils.

**:material-chat-question:{ .faq } Gestion de l'alimentation**

Le Mini-KVM peut tirer l'alimentation de **chaque côté** (hôte ou cible). Le côté avec le **câble le plus court** devient généralement la source d'alimentation principale.  
Pour les cibles à faible consommation (ex. Raspberry Pi), utilisez une alimentation dédiée au lieu d'alimenter en retour via Mini-KVM.

**:material-chat-question:{ .faq } Limites de longueur de câble**

-   Gardez le **câble USB-C hôte orange ≤1.5m**.
-   Pour des câbles plus longs, injectez l'alimentation via :
    -   Câble USB-A mâle-mâle
    -   [Broches d'extension](/product/minikvm/extension-pins/)
    -   Séparateur USB-C Y
-   La même règle s'applique au **câble cible noir**.

---

## Contrôle

**:material-chat-question:{ .faq } Le clavier et la souris ne peuvent pas contrôler l'ordinateur cible**

Si vous voyez le bureau cible mais que les entrées clavier/souris ne répondent pas, cela signifie généralement que la communication HID n'est pas établie. Essayez ces étapes :

1. **Vérifier les connexions des câbles** — Assurez-vous que le câble Type-C cible est connecté à l'ordinateur cible ; le câble hôte à votre ordinateur de contrôle.
2. **Éviter les hubs USB non alimentés** — Utilisez une connexion directe ou un hub alimenté.
3. **Réinitialiser la puce HID** — Si l'appareil semble « gelé », utilisez **Menu Avancé → Réinitialisation usine puce HID** (OpenterfaceQt) ou **Outil de réinitialisation série** (macOS).
4. **Essayer un autre port USB ou redémarrer** — L'OS hôte peut désactiver un port après des erreurs USB.
5. **Réduire le débit en bauds** — Dans les environnements bruyants, passez à 9600 bps pour une communication plus fiable.

Pour plus de détails, voir [Dépannage du contrôle clavier et souris](/product/minikvm/support/keyboard-mouse-control/).

**:material-chat-question:{ .faq } Version sans fil ou Ethernet ?**

Pas intégré. Utilisez un ordinateur sans tête (ex. Raspberry Pi) + bureau distant pour le contrôle distant.

**:material-chat-question:{ .faq } Compatibilité PS/2 ?**

Non — le support PS/2 pourrait être exploré dans les futures versions.

**:material-chat-question:{ .faq } Plusieurs Mini-KVM sur un ordinateur ?**

Oui, fonctionnalité expérimentale dans l'app QT (Windows/Linux).

**:material-chat-question:{ .faq } Contrôle marche/arrêt ?**

Pas directement, mais les [broches d'extension](/product/minikvm/extension-pins/) permettent de futurs modules de contrôle ATX.

---

## Vidéo

**:material-chat-question:{ .faq } Latence et résolution**

-   Capture à **1080p@30Hz**
-   Latence sous **140ms** → contrôle fluide

**:material-chat-question:{ .faq } Résolution d'entrée vs capture**

-   Accepte l'entrée jusqu'à **4K@30Hz**
-   Capture à **1080p**, les entrées plus élevées sont sous-échantillonnées (peuvent paraître légèrement floues).
-   Meilleure pratique : **Réglez la cible à 1080p**.

**:material-chat-question:{ .faq } Aptitude au jeu**

Pas pour les jeux AAA. Fonctionne bien pour les jeux plus légers comme Minecraft ou les émulateurs.

**:material-chat-question:{ .faq } Contrôle distant sur internet**

Pas intégré, mais associez le Mini-KVM avec un logiciel de bureau distant sur l'hôte.

**:material-chat-question:{ .faq } Autres formats vidéo**

Utilisez des adaptateurs pour VGA, DVI, DisplayPort, etc.

---

## Dépannage

**:material-chat-question:{ .faq } Comment exécuter les diagnostics pour vérifier si mon Mini-KVM fonctionne ?**

Exécutez l'auto-vérification diagnostique intégrée pour vérifier les connexions USB et détecter les problèmes matériels :

- **macOS :** [Guide d'auto-vérification diagnostique (macOS)](/product/minikvm/support/diagnostic-self-check/) — Paramètres → Avancé & Débogage → Ouvrir l'outil de diagnostic
- **Windows :** [Guide d'auto-vérification diagnostique (Windows)](/product/minikvm/support/diagnostic-self-check-windows/) — Avancé → Diagnostic matériel

Les diagnostics testent Target/Host Plug & Play, test de stress, etc. Si tous les tests passent, votre appareil fonctionne correctement.

**:material-chat-question:{ .faq } Comment signaler un problème matériel au support ?**

Si l'auto-vérification diagnostique affiche **ÉCHEC** sur un ou plusieurs tests :

1. Complétez les étapes de diagnostic restantes (l'outil vous guidera).
2. Lorsqu'un problème est détecté, une fenêtre **E-mail de support** ou **Rapport de défaut** s'ouvre.
3. Entrez votre **Numéro de commande** et **Nom**, puis copiez l'adresse e-mail et le brouillon.
4. Joignez les **fichiers de journaux demandés** (l'outil indique lesquels) et une **photo de la configuration** (Mini-KVM + connexions hôte/cible clairement visibles).
5. Envoyez l'e-mail au support.

Instructions étape par étape : [Guide d'auto-vérification diagnostique (macOS)](/product/minikvm/support/diagnostic-self-check/) ou [Guide d'auto-vérification diagnostique (Windows)](/product/minikvm/support/diagnostic-self-check-windows/).

**:material-chat-question:{ .faq } Problèmes de hub USB**

Utilisez un **hub alimenté** pour éviter les chutes de tension. Les hubs non alimentés peuvent entraîner une alimentation insuffisante et un comportement erratique du HID (clavier/souris). Voir [Dépannage du contrôle clavier et souris](/product/minikvm/support/keyboard-mouse-control/).

**:material-chat-question:{ .faq } L'app ne montre pas de vidéo ou le contrôle ne répond pas**

1. Déconnectez tous les câbles, attendez quelques secondes, reconnectez.
2. Consultez [Dépannage du contrôle clavier et souris](/product/minikvm/support/keyboard-mouse-control/) pour les problèmes HID (câbles, hubs, réinitialisation HID).
3. Exécutez l'[auto-vérification diagnostique](/product/minikvm/support/diagnostic-self-check/) (macOS) ou le [Diagnostic matériel](/product/minikvm/support/diagnostic-self-check-windows/) (Windows) pour vérifier l'appareil.
4. Si non résolu, vérifiez le firmware ou mettez à jour l'app hôte.

**:material-chat-question:{ .faq } Résolutions étranges comme 43184x24228@44Hz**

Le firmware de capture a probablement été réinitialisé à l'usine.  
Re-flashez le firmware via les [releases GitHub](https://github.com/TechxArtisanStudio/Openterface_QT/releases).

**:material-chat-question:{ .faq } Re-flashé mais toujours cassé ?**

-   Vérifiez la bonne énumération USB (`USB Tree Viewer` ou `lsusb -v`)
-   Confirmez la dernière app hôte
-   Exécutez l'[auto-vérification diagnostique](/product/minikvm/support/diagnostic-self-check/) pour capturer les journaux
-   Si toujours en échec, contactez le support avec votre Numéro de commande, journaux de diagnostic et photo de configuration — voir [Comment signaler un problème matériel au support ?](#comment-signaler-un-problème-matériel-au-support)
