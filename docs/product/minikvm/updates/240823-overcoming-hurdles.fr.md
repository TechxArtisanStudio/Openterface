---
draft: false
date: 2024-08-22
description: "Mise à jour importante Openterface Mini-KVM : certification CE terminée, production en cours, nouvelle ETA mi-janvier. Matériel V1.9 finalisé avec broches d'extension, développement d'app Android, emballage amélioré et manuel multilingue en cours."
keywords: "Openterface Mini-KVM, certification CE, matériel V1.9, mise à jour production, calendrier expédition, développement app Android, broches extension, KVM-over-IP, contrôle qualité, emballage produit, manuel multilingue, USB KVM, fabrication tech, matériel open source, mise à jour livraison"
---

# Surmonter les obstacles : Mise à jour des progrès et nouveau calendrier

Salut tout le monde,

J'espère que vous allez tous bien. Cela fait un moment depuis notre dernière mise à jour. J'aimerais pouvoir dire que tout s'est bien passé pour Openterface, mais nous avons rencontré quelques obstacles qui retarderont notre calendrier de livraison. Bien que ce ne soit pas ce que nous attendions, nous relevons ces défis de front et faisons des progrès constants avec beaucoup de bonnes nouvelles à partager. Ce post est une **lecture de 7 minutes**, alors plongeons dans les détails pour que vous sachiez exactement où en sont les choses et ce qui vient ensuite.

## Réglementation, production et qualité

Avant de pouvoir lancer la production, nous devions passer les tests de qualité nécessaires selon les réglementations, en particulier la certification CE. Comme notre version toolkit inclut non seulement le Mini-KVM mais aussi plusieurs accessoires, chaque partie devait subir des tests CE. Ces tests ont pris plus de temps que prévu (il s'avère que les câbles peuvent être assez difficiles), mais la bonne nouvelle est que **nous avons réussi la certification CE pour notre Mini-KVM et tous ses composants !** Voici un aperçu des certifications pour toutes nos pièces : Mini-KVM, câble HDMI, câble Type-C orange, câble Type-C court noir et câble VGA2HDMI. Avec la certification en main, notre calendrier de production est maintenant certain, et nos fabricants **produisent actuellement toutes les pièces** au moment où je parle.

![240823-0](https://www.crowdsupply.com/img/fcb5/db59e179-2413-4d57-8462-2285c007fcb5/openterface-240823-0_jpg_gallery-lg.jpg)
*Les exigences UKCA et CE sont les mêmes pour nos produits électroniques, avec CE couvrant également la conformité RoHS.*

Il y a deux semaines, nous avons visité l'un de nos fabricants pour former leurs responsables de ligne sur le contrôle qualité des câbles orange avant qu'ils ne nous les expédient. Maintenant, TOUS les câbles orange ont été produits et sont assis dans un coin de notre studio.
![240823-1](https://www.crowdsupply.com/img/28dc/34844b54-0e02-414d-b58b-d40e8abe28dc/openterface-240823-1_jpg_gallery-lg.jpg)
*Kevin et Shawn expliquaient les méthodes de test pour s'assurer que le câble orange fonctionne correctement avec notre Openterface Mini-KVM.*

Nous ferons la même tâche cette semaine pour former l'QA en première ligne de production pour les autres pièces également. Voici des échantillons de câbles supplémentaires.
![240823-2](https://www.crowdsupply.com/img/e703/abb8ffa5-eb85-4eb9-b5f8-d8a3d349e703/openterface-240823-2_jpg_md-xl.jpg)
*Fierté marqués avec notre logo TechxArtisan, ce sont des échantillons du câble HDMI, du câble Type-C court et du câble VGA-to-HDMI.*

Nous nous attendons à ce que les autres pièces et Mini-KVM arrivent bientôt de nos fabricants, moment auquel nous vérifierons la qualité de chaque composant et les emballerons correctement dans notre studio avant l'expédition. En d'autres termes, **notre équipe assurera personnellement la qualité** avant qu'elle n'atteigne vos mains.

## Expédition, retards potentiels et nouvelle ETA

**L'incertitude actuelle réside dans le processus d'expédition**. Après avoir enquêté sur plusieurs compagnies d'expédition, nous avons découvert que l'expédition prendra du temps supplémentaire car nous transférerons probablement les colis par un entrepôt avant d'atteindre l'entrepôt de Crowd Supply. Nous débattons encore du choix entre le transport maritime ou aérien—veuillez nous supporter encore quelques jours pendant que nous réglons les arrangements.

Le dédouanement est un autre obstacle potentiel qui pourrait causer des retards inattendus. Une fois que nos produits arrivent à l'entrepôt de Crowd Supply aux États-Unis, ils prendront une à deux semaines pour être expédiés mondialement selon chaque commande. Pour les soutiens en dehors des États-Unis, les colis individuels devront encore passer par l'expédition mondiale et le dédouanement dans le pays de destination.

Compte tenu de la situation actuelle et en ajoutant un peu de temps tampon, je reste prudemment optimiste que nous terminerons la livraison avant la fin de cette année, avec **une nouvelle ETA de mi-janvier**. Je suis vraiment désolé pour l'inconvénient et j'apprécie votre soutien et votre patience pendant ce changement.

## Matériel V1.9 finalisé

Comme vous le savez peut-être de notre précédent [post Reddit](https://www.reddit.com/r/Openterface_miniKVM/comments/1e25pco/openterface_minikvm_v19_with_pins_for_more/), nous avons décidé de **mettre à niveau notre matériel vers V1.9**, incluant un ensemble de broches d'extension hackables. Ce n'était pas partie du plan original pour la campagne de crowdfunding, mais nous croyons que cela améliore significativement le **potentiel d'utilisation plus large** du matériel.

![240823-3](https://www.crowdsupply.com/img/77d7/09a9d0e5-3065-4f3e-8b61-bae66b5c77d7/openterface-240823-3_jpg_md-xl.jpg)
*Les broches VCC, GND, Target D+, Target D-, Host D+ et Host D-—où 'D' signifie données USB.*

Une motivation clé était d'**permettre au commutateur USB d'être basculé au niveau logiciel**. Pourquoi est-ce important ? Sur notre feuille de route, nous **visons à supporter une solution KVM-over-IP**, comme VNC, à l'avenir. L'idée est de faire correspondre le contrôle KVM local avec le protocole VNC, permettant aux utilisateurs de contrôler à distance l'ordinateur cible via l'ordinateur hôte. Dans un tel scénario distant, la capacité pour les utilisateurs de basculer le port USB est essentielle, surtout quand des transferts de fichiers entre l'hôte et la cible sont requis.

**Les broches d'extension ouvrent aussi des possibilités pour plus**, comme l'intégration avec iPadOS, le contrôle ATX, le pontage réseau et le contournement audio. Bien que je ne plonge pas dans tous les détails ici, je vous encourage à rejoindre notre communauté Openterface pour discuter avec nous davantage.

Cette mise à niveau matérielle pourrait potentiellement étendre notre solution Openterface pour fonctionner sur IP et inclure des fonctionnalités plus avancées tout en maintenant sa force centrale comme outil KVM-over-USB plug-and-play—parfait pour les pros IT naviguant dans des environnements IT incertains, comme des centres de données non familiers.

Je suis heureux de rapporter que V1.9 a passé nos tests internes de base et sera finalisé comme la version officielle pour tous nos soutiens. Cependant, cette mise à niveau matérielle nécessitera des tests supplémentaires, et tout développement basé sur ces broches d'extension sera expérimental et susceptible d'avoir des bugs. C'est là où vous pouvez contribuer. Nous comptons sur la communauté open-source pour nous aider à améliorer Openterface ensemble.

## Plus de mises à jour logicielles

Sur le front logiciel, nous faisons des progrès excitants. Nous plongeons maintenant dans **l'app Openterface Android** ! Consultez ce [tweet](https://x.com/TechxArtisan/status/1825460088922071398) pour une démo précoce montrant un contrôle KVM fluide, le mouvement de la souris et les clics en action. Plus de fonctionnalités sont en route, et comme toujours, une fois que nous aurons poli le code un peu plus, **cette app sera aussi open-sourcée** sur notre repo GitHub [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android).
![240823-4](https://www.crowdsupply.com/img/7007/b192f260-1e1f-4dab-905b-fb0a6d927007/openterface-240823-4_jpg_md-xl.jpg)
*Utilisant juste nos bouts de doigts pour contrôler KVM un ordinateur Linux depuis une tablette Android. Sympa !*

Notre version QT vient de recevoir une mise à jour pratique—vous pouvez maintenant [transférer du texte de l'hôte vers la cible](https://x.com/TechxArtisan/status/1825919721960780131) ! Donc maintenant cette fonctionnalité est supportée sur les apps hôtes macOS, Windows et Linux.

De plus, nous planifions aussi d'ajouter une fonctionnalité amusante—[un mouvement automatique de souris pour empêcher votre ordinateur cible de dormir](https://x.com/TechxArtisan/status/1825471186668847241). Devrions-nous opter pour la balle de ping-pong rebondissant autour de l'écran ou l'effet classique de l'économiseur d'écran DVD ? Votez et commentez le [tweet](https://x.com/TechxArtisan/status/1825470086800691459) 😃

## Design d'emballage, étiquetage et manuel

Nous avons [expérimenté avec diverses maquettes et designs d'emballage](https://www.reddit.com/r/Openterface_miniKVM/comments/1elm4vq/almost_ready_to_finalize_our_package_design/) pour trouver l'équilibre parfait entre plusieurs facteurs clés :

- Sélectionner des matériaux assez robustes pour protéger le produit et ses pièces pendant l'expédition,
- Créer un étiquetage informatif qui aide les utilisateurs à comprendre le produit d'un coup d'œil,
- Assurer la conformité aux réglementations,
- Rendre l'emballage visuellement attrayant,
- Et être écologique en minimisant l'utilisation de plastique partout où possible.

De plus, nous avons fait plusieurs améliorations à l'ancien sac toolkit, incluant :

- Un espace de stockage plus large,
- Une fermeture éclair orange stylée,
- Des matériaux extérieurs et intérieurs améliorés,
- Et une poche maillée super extensible.

Nous avons choisi ce matériau car il frappe l'équilibre idéal entre être économique, agréable au toucher et assez durable pour protéger les articles à l'intérieur. **Nous sommes confiants que vous l'aimerez**.

![240823-5](https://www.crowdsupply.com/img/099a/75e16f52-bd0c-4652-af27-08caf448099a/openterface-240823-5_jpg_md-xl.jpg)

Nous mettons aussi à jour les étiquettes sur le boîtier en aluminium pour les rendre aussi informatives et visuellement attrayantes que possible. Nous espérons que ces améliorations amélioreront votre expérience utilisateur et rendront plus facile de commencer avec Openterface.

![240823-6](https://www.crowdsupply.com/img/94d8/441a5757-2d6a-4c79-885b-7b5b3a7094d8/openterface-240823-6_jpg_md-xl.jpg)

Nous finalisons le manuel Openterface, qui sera disponible en anglais, allemand, français, japonais et chinois. Désolé si nous avons manqué votre langue—notre boîte n'est pas de taille TARDIS (la boîte de police du Doctor Who) ! Mais nous ferons de notre mieux pour ajouter plus de traductions sur notre site web.

![240823-7](https://www.crowdsupply.com/img/e2d9/2e5a2086-20f0-47ec-a27b-288d10d0e2d9/openterface-240823-7_jpg_md-xl.jpg)

## Révision linguistique communautaire

J'ai utilisé ChatGPT pour aider avec les traductions, mais il peut parfois manquer la cible avec la phraséologie et le choix des mots. Si ce n'est pas trop de problème, j'apprécierais grandement toute aide pour réviser le contenu dans d'autres langues, surtout pour les matériaux imprimés que nous sommes sur le point de finaliser. J'ai mis à jour tout le contenu textuel pour l'emballage dans notre dossier GitHub [product-printed-materials](https://github.com/TechxArtisanStudio/Openterface/tree/main/product-printed-materials), où vous pouvez réviser et soumettre toute amélioration. Vous pouvez aussi me DM directement. Merci !

## Remarques finales et progrès en cours

Nous nous excusons encore pour les retards et le changement dans l'ETA de notre produit. Merci pour votre patience et de rester avec nous—nous travaillons dur pour vous l'apporter dès que possible ! Je vous mettrai à jour immédiatement une fois que notre expédition sera arrangée. Plus de mises à jour sont en route, alors rejoignez notre communauté Openterface et restez à l'écoute !

Salut,

Billy Wang  
Gestionnaire de produit  
Équipe Openterface | TechxArtisan
