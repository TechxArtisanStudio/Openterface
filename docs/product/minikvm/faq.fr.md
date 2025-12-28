---
title: FAQ pour Openterface Mini-KVM
description: Questions fréquemment posées sur le Mini-KVM, couvrant les fonctionnalités, la compatibilité, le dépannage et les plans futurs.
keywords: Mini-KVM, Openterface, commutateur KVM, open-source, dépannage, capture vidéo, USB, compatibilité
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

**:material-chat-question:{ .faq } Problèmes de hub USB**

Utilisez un **hub alimenté** pour éviter les chutes de tension causant l'instabilité.

**:material-chat-question:{ .faq } L'app ne montre pas de vidéo ou le contrôle ne répond pas**

Déconnectez tous les câbles, attendez, reconnectez.  
Si non résolu, vérifiez le firmware ou mettez à jour l'app hôte.

**:material-chat-question:{ .faq } Résolutions étranges comme 43184x24228@44Hz**

Le firmware de capture a probablement été réinitialisé à l'usine.  
Re-flashez le firmware via les [releases GitHub](https://github.com/TechxArtisanStudio/Openterface_QT/releases).

**:material-chat-question:{ .faq } Re-flashé mais toujours cassé ?**

-   Vérifiez la bonne énumération USB (`USB Tree Viewer` ou `lsusb -v`)
-   Confirmez la dernière app hôte
-   Si toujours en échec, contactez le support pour diagnostic/remplacement.
