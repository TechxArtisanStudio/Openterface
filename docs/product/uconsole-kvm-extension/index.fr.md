# Extension KVM Openterface pour uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## Aperçu

Transformez votre uConsole en **console KVM (Clavier, Vidéo, Souris) portable** avec cette carte d'extension plug-and-play.

L'**Extension KVM Openterface** remplace le modem 4G/LTE original dans l'emplacement d'expansion de votre uConsole et fournit une **entrée HDMI directe et un contrôle USB HID**, vous permettant de gérer des appareils headless en déplacement—sans besoin d'écrans externes, claviers ou configuration réseau.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## Caractéristiques

- **Facteur de Forme Parfait**  
    Correspond à la taille 37×77 mm du module 4G/LTE pour une intégration matérielle transparente.

- **HDMI Direct + USB HID**  
    Permet un contrôle réactif des appareils connectés en utilisant l'entrée et l'écran intégrés de l'uConsole.

- **Faible Latence**  
    Adapté pour le dépannage au niveau BIOS et l'interaction en temps réel.

- **Vraiment Portable**  
    Fait de l'uConsole un outil mobile pour les développeurs, ingénieurs et techniciens.

- **Convivial Open-Source**  
    Construit sur la plateforme [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt). Les contributions de la communauté sont les bienvenues.


## Cas d'Usage

- **Administration Système**  
    Accédez et dépannagez des serveurs ou appareils embarqués sans un commutateur KVM encombrant.

- **Développement Matériel**  
    Testez et déboguez Raspberry Pi, SBC ou microcontrôleurs directement.

- **Déploiement sur le Terrain**  
    Effectuez la maintenance ou la configuration dans les centres de données ou emplacements distants.


## Installation Matérielle

Suivez ces étapes d'installation matérielle pour remplacer le module 4G/LTE dans votre uConsole par la carte Extension KVM Openterface et assurer un montage sécurisé.

### Ce dont Vous Aurez Besoin

- Votre carte d'extension KVM Openterface
- Le joint fourni (cales en plastique) 
- Un tournevis hexagonal (pour les vis de montage de la carte)
- Précautions ESD (bracelet ou surface mise à la terre) — recommandé

### Installation de la Carte d'Extension

1. Arrêt et Déconnexion

    Arrêtez l'uConsole et déconnectez toute l'alimentation et les câbles.

2. Retrait du Module Existant

    Utilisez un tournevis hexagonal pour retirer les deux vis qui maintiennent le module 4G/LTE ou la carte d'extension existante.

    Soulevez soigneusement la carte droit vers le haut pour éviter de plier les contacteurs à ressort.

3. Installation de la Carte d'Extension KVM

    - La carte d'Extension KVM Openterface fait 1.0 mm d'épaisseur (plus fine que l'original 4G/LTE 1.2 mm). Pour cette raison, nous recommandons de placer le joint fourni sur les poteaux de vis (entre le PCB et les entretoises de montage) pour que le joint s'assoie sous les poteaux de vis avant de placer la carte. Cela compense le PCB plus fin et aide à assurer une pression adéquate du contacteur à ressort.
    - Si vous préférez vérifier d'abord, placez la carte sans le joint et vérifiez le contact uniforme du ressort; si le contact est inégal ou la carte s'assoit lâchement, ajoutez le joint et replacez la carte.

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. Réinsertion des Vis

    Réinsérez les deux vis et serrez avec le tournevis hexagonal. Serré est suffisant — ne serrez pas trop.

5. Vérification du Montage

    La carte devrait s'asseoir à plat sans mouvement notable. Vérifiez que les contacteurs à ressort font un contact uniforme à travers les coussinets.

6. Test du Matériel

    Reconnectez l'alimentation, démarrez le système et testez les appareils HDMI, audio et USB HID pour confirmer le fonctionnement correct.

## Guide de Configuration Logicielle

Pour utiliser l'Extension KVM, installez l'**App Openterface** sur votre uConsole.

Option 1 - Utiliser la version Flatpak d'Openterface
- 📖 Suivez notre [Guide d'Installation Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) pour les étapes de configuration détaillées.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

Option 2 - Installer la version communautaire de Rex

Si vous voulez la build communautaire maintenue par Rex, ajoutez son dépôt et installez le paquet avec les commandes ci-dessous.

1. Ajouter la clé GPG du dépôt et le dépôt

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. Mettre à jour et installer

```bash
sudo apt update
sudo apt install openterfaceqt
```

Notes: ces commandes nécessitent sudo. Le dépôt cible les paquets arm64 Bookworm; vérifiez la compatibilité avec votre appareil avant d'installer.

## Statut Pré-Lancement

- 📦 Premier lot actuellement en préparation  
- ⏳ Expédition estimée commence **début août 2024**  
- 🛒 Quantité limitée – [Pré-commandez maintenant](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) pour réserver votre unité

> **Avis de Pré-Commande**  
> Cet article est actuellement en pré-commande avec un délai d'exécution estimé d'**environ 2 mois**.  
> Si vous avez besoin d'autres articles plus tôt, veuillez passer une **commande séparée**. Les commandes combinées seront expédiées quand ce produit sera prêt.

## Communauté et Support

- 🗨️ Rejoignez la discussion: [Serveur Discord](https://discord.gg/ruAD9kcYbq)  
- 📧 Support email: [info@openterface.com](mailto:info@openterface.com)


## FAQ

**Q: Comment fonctionne la Carte d'Extension KVM?**  
Elle capture la sortie HDMI d'un appareil cible et l'affiche sur l'uConsole. En même temps, le clavier et le trackball de l'uConsole sont utilisés pour contrôler l'appareil cible via l'émulation USB HID.

**Q: Puis-je utiliser ceci avec le module 4G/LTE installé?**  
Non. Cette carte occupe le même emplacement d'expansion. Vous devrez choisir entre la connectivité cellulaire ou la fonctionnalité KVM.

**Q: Le logiciel est-il open source?**  
Oui! Nos Apps **Openterface Connect** sont entièrement open source et disponibles dans notre [dépôt GitHub](https://github.com/TechxArtisanStudio/Openterface_QT).
