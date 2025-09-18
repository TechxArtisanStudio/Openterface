# Openterface QT pour Win & Linux

Ce document fournit un aperçu d'un logiciel KVM (Clavier, Vidéo, Souris) multiplateforme développé avec Qt, compatible avec les systèmes d'exploitation Linux et Windows. Le logiciel permet de contrôler un appareil cible depuis un système hôte, offrant diverses fonctionnalités accessibles via sa barre de menu et des fonctionnalités supplémentaires.

## Fonctionnalités de la barre de menu principale

### Préférences

Le menu Préférences permet aux utilisateurs de personnaliser les paramètres via une boîte de dialogue avec quatre pages :<br>
![Preferences Gernal](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   **Général** Cette page configure le filtre des journaux de débogage et l'inhibition ou non de l'économiseur d'écran lorsque l'application est en cours d'exécution. Les catégories de journaux comprennent :

    -   Core
    -   Serial
    -   UserInterface
    -   host

    Les utilisateurs peuvent choisir d'enregistrer les journaux dans un fichier .txt et d'inhiber ou non l'économiseur d'écran.<br>

![Preferences Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   **Vidéo** Cette page permet aux utilisateurs de :

    -   Sélectionner les données de quelle caméra capturer.
    -   Définir la résolution.
    -   Choisir le format du flux vidéo.

-   **Audio** Cette page est actuellement en développement.<br>

![Preferences TargetControl](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   **Contrôle de la cible** Cette page offre des options pour configurer les modes de contrôle de l'appareil cible :

    -   **Modes de contrôle :**

        -   **Clavier + Souris + périphérique USB HID**
        -   **Clavier USB**
        -   **Clavier + Souris**
        -   **Périphérique USB HID**

    -   **Définir l'ID du vendeur (VID) et l'ID du produit (PID) lus depuis la cible.**
    -   **Définir le descripteur USB pour la cible.**

### Édition

-   **Coller :** L'option Coller dans le menu Édition et le bouton coller en haut à gauche permettent aux utilisateurs de coller du texte depuis le presse-papiers de l'hôte vers l'appareil cible.

### Contrôle

Ce menu offre des options pour :<br>

-   Définir les modes de mouvement de la souris : Absolu ou Relatif. **Control >> MouseMode >> Absolute or Relative.**
-   Basculer la visibilité du curseur de la souris de l'hôte. **Control >> Mouse Visibility >> Auto Hide or Always Show.**
-   Basculer un port USB sur le matériel entre l'utilisation cible et hôte. **Control >> Switchable USB >> TO Target or To Host.**
-   Ajuster le débit en bauds pour la transmission de la puce. **Control >> Baudrate >> 9600, 115200.**

### Avancé

Le menu Avancé comprend les options suivantes :<br>
![Advance menu](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   **Vérification de l'environnement :** Vérifie si les pilotes requis pour le logiciel sont installés.
-   **Réinitialiser le port série :** Redémarre le port série.
-   **Réinitialiser le clavier et la souris :** Réinitialise les paramètres du clavier et de la souris.
-   **Réinitialisation d'usine de la puce HID :** Restaure les paramètres d'usine de la puce HID.<br>
    ![Advance SerialConsole](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   **Console série :** Ouvre une nouvelle fenêtre pour surveiller tous les messages envoyés au port série, avec des filtres pour les messages envoyés/reçus.<br>
    ![Advance ScriptTool](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   **Outil de script :** Exécute des scripts AutoHotkey (AHK). Cette fonctionnalité imite AutoHotkey mais ne prend en charge qu'un sous-ensemble de fonctions souris/clavier et de captures d'écran. Les scripts affectent l'appareil cible.
-   **Serveur TCP :** Reçoit des commandes AutoHotkey via TCP pour les exécuter sur l'appareil cible.
-   **Mise à jour du firmware :** Récupère le dernier firmware depuis un serveur distant, permettant aux utilisateurs de choisir de le flasher ou non sur l'appareil.

### Langues

L'interface peut être configurée en :

-   Danois
-   Anglais
-   Allemand
-   Français
-   Japonais
-   Suédois

### Aide

Le menu Aide fournit : <br>
![Help menu](https://assets.openterface.com/images/qt/menuHelp.webp)

-   Des liens vers le site web officiel et les formulaires de retour pour les problèmes logiciels/matériels.
-   Des informations sur l'achat de matériel.
-   Une description de l'environnement du logiciel.
-   À propos : Détails sur l'organisation.
-   Mise à jour : Vérifie les mises à jour du logiciel.

## Fonctions de la barre de menu (de gauche à droite)

La barre de menu, de gauche à droite, comprend les fonctionnalités suivantes :<br>

![MenuBar](https://assets.openterface.com/images/qt/menubar.webp)

-   Sélection de la disposition du clavier : Choisir la disposition du clavier.
-   Contrôles de zoom : Zoom avant, zoom arrière ou réinitialisation de l'affichage du flux vidéo capturé.
-   Clavier virtuel : Inclut les touches de fonction et les combinaisons de raccourcis prédéfinies.
-   Capture d'écran : Capture l'écran cible entier et l'enregistre dans un dossier par défaut.
-   Mode plein écran : Bascule l'affichage en plein écran.
-   Coller : Colle du texte depuis le presse-papiers de l'hôte vers la cible.
-   Danse de la souris : Déclenche des mouvements prédéfinis de la souris.
-   Indicateur de périphérique USB : Affiche si un périphérique USB est assigné à la cible ou à l'hôte.

En attendant, n'hésitez pas à explorer notre **dépôt GitHub** open-source : [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) pour le dernier code, les mises à jour, les exemples et pour signaler des problèmes.

Vous pouvez également rejoindre notre [communauté Discord](/discord) pour vous connecter avec notre équipe de développement et d'autres utilisateurs formidables pour discuter de tous les sujets liés au KVM.

Pour un support direct, n'hésitez pas à nous envoyer un email à [support@openterface.com](mailto:support@openterface.com).

---

**Vous avez des commentaires sur cette page ?** [Faites-le nous savoir ici.](https://forms.gle/wmxoR2C1VdG36mT69)
