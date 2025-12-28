# Openterface Android

## Vue d'ensemble

Openterface Mini-KVM est une solution matérielle et logicielle open-source conçue pour fournir des fonctionnalités KVM (Clavier, Vidéo, Souris) de base pour contrôler des appareils via une interface Android. Ce dépôt contient le code source de l'application Android, les configurations de build et les scripts de support pour configurer et déployer le projet.

Nous nous engageons en faveur du matériel ouvert et des logiciels open-source, sous licence [GNU Affero General Public License v3](https://github.com/TechxArtisanStudio/Openterface_Android/blob/main/LICENSE).

## Modules de fonctionnalités

### 1. Affichage vidéo

#### Fonctionnalité principale

-   Diffuse la sortie vidéo de l'appareil cible vers l'écran Android en temps réel.
-   Prend en charge les ajustements d'image pour une visualisation optimale.

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### Description de l'interface utilisateur

-   L'écran principal affiche le flux vidéo de l'appareil cible, occupant la majeure partie de l'interface.
-   Une barre d'outils sur le côté fournit des contrôles d'ajustement (luminosité, contraste, teinte).

#### Flux d'opération

1. Connectez le matériel Mini-KVM à l'appareil cible via HDMI et USB.
2. Branchez le Mini-KVM à votre appareil Android via USB-C.
3. Lancez l'application ; le flux vidéo apparaît automatiquement.
4. Utilisez les curseurs de la barre d'outils pour ajuster la luminosité, le contraste ou la teinte selon vos besoins.

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### Fonctionnalités spéciales

-   Le zoom à deux doigts améliore l'affichage

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. Contrôle de la souris

#### Fonctionnalité principale

-   Fournit un contrôle absolu et relatif de la souris pour interagir avec l'interface de l'appareil cible.
-   Prend en charge les clics gauche et droit.
-   Sélectionnez le mode dans le menu de droite.

#### Description de l'interface utilisateur

-   Le flux vidéo fait également office de pavé tactile pour la saisie de la souris.
-   Un bouton d'action flottant (FAB) permet de basculer entre les modes souris et clavier.

#### Flux d'opération

1. Assurez-vous que l'appareil est connecté avec succès.
2. Tapez sur l'écran pour déplacer le curseur de la souris à cette position (contrôle absolu).
3. Double-cliquez avec un doigt pour un clic gauche, cliquez avec deux doigts pour un clic droit.
4. Le mode glisser consiste à maintenir le bouton gauche enfoncé sans le relâcher.

#### Fonctionnalités spéciales

-   Contrôle relatif de la souris (en développement, à activer via les paramètres lorsque disponible).

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. Saisie au clavier

#### Fonctionnalité principale

-   Tapez sur l'appareil en cliquant sur les touches du clavier.

#### Description de l'interface utilisateur

-   L'icône du clavier se trouve dans le coin inférieur droit.
-   Le clavier comprend des touches de raccourci, des touches système, des touches standard et des touches de fonction (F1-F12).

#### Flux d'opération

1. Cliquez sur l'icône du clavier dans le coin inférieur droit pour faire apparaître le clavier.
2. Tapez du texte ou appuyez sur les touches de fonction selon vos besoins.

#### Fonctionnalités spéciales ou raccourcis

-   **Touches de raccourci** : Ctrl+C、Ctrl+V、Ctrl+Z、Ctrl+X、Ctrl+A、Ctrl+S、
    Win+Tab、Win+S、Win+E、Win+R、Win+D、Win+L、Alt+F4、Ctrl+Alt+Del、Alt+PrtScr.
-   **Touches de fonction** : F1-F12、Touches symboles.
-   **Touches standard** : 0-9、A-Z、Entrée、Espace、Supprimer.

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

En attendant, n'hésitez pas à explorer notre **dépôt GitHub** open-source : [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) pour le dernier code, les mises à jour, les exemples et pour signaler des problèmes.

Vous pouvez également rejoindre notre [communauté Discord](/discord) pour vous connecter avec notre équipe de développement et d'autres utilisateurs formidables pour discuter de tous les sujets liés au KVM.

Pour un support direct, n'hésitez pas à nous envoyer un email à [support@openterface.com](mailto:support@openterface.com).

---

**Vous avez des commentaires sur cette page ?** [Faites-le nous savoir ici.](https://forms.gle/wmxoR2C1VdG36mT69)