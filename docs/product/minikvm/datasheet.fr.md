---
title: "Fiche technique de l'Openterface Mini-KVM | Spécifications techniques & détails du produit"
description: "Fiche technique complète de l'Openterface Mini-KVM. Consultez les spécifications, dimensions, capacités vidéo/audio, exigences d'alimentation, accessoires et options de connectivité pour cette solution KVM-over-USB."
keywords: "Fiche technique Mini-KVM, spécifications Mini-KVM, spécifications techniques KVM over USB, dimensions Mini-KVM, accessoires Mini-KVM, spécifications HDMI KVM, détails techniques USB KVM, spécifications de contrôle d'ordinateur sans écran, spécifications du commutateur KVM, outils de gestion serveur"
---

# Fiche technique de l'Openterface Mini-KVM

## Aperçu

L'Openterface™ Mini-KVM est un appareil riche en fonctionnalités, de production, open source et communautaire. Il propose une solution légère et rapide KVM-over-USB, vous permettant de contrôler un ordinateur sans écran (appelé l'ordinateur cible) directement depuis votre propre ordinateur portable ou de bureau (appelé l'ordinateur hôte), via une simple connexion USB et HDMI. Cette approche compacte élimine le besoin de claviers supplémentaires, de souris, d'écrans ou de toute configuration réseau, simplifiant votre installation et améliorant l'efficacité.

## Spécifications

### Général

| Paramètre | Caractéristiques |
|-----------|----------------|
| Nom du produit | Openterface Mini-KVM |
| Fabricant | TechxArtisan Limited |

### Variantes du produit

#### Mini-KVM Basic (392-OP-MINIKVM-BASIC)

**Contenu :**

- Openterface Mini-KVM
- Guide de démarrage rapide

#### Mini-KVM Toolkit (392-OPMINIKVMTOOLKIT)

**Contenu :**

- Openterface Mini-KVM
- Guide de démarrage rapide
- Sac d'outils (165 x 110 x 50 mm)
- Bouchon de prolongation
- Câble HDMI mâle-mâle (0,3 m)
- Câble Type-C mâle vers USB-A mâle (0,3 m) avec adaptateur USB-A femelle vers Type-C mâle
- Câble Type-C mâle-mâle (1,5 m) avec adaptateur USB-C femelle vers USB-A mâle

### Alimentation

| Paramètre | Caractéristiques |
|-----------|----------------|
| Type de connexion | Alimentation via USB-C. Aucune alimentation externe requise. |

### Vidéo

| Paramètre | Caractéristiques |
|-----------|----------------|
| Entrée vidéo maximale | Jusqu'à 3840x2160@30Hz, via HDMI<br>(Note : Avec l'utilisation d'un adaptateur, il peut également supporter VGA, Micro HDMI, DVI et autres sources d'entrée vidéo) |
| Résolutions vidéo prises en charge | Jusqu'à 1920x1080@30Hz |
| Méthodes de compression vidéo | YUV, MJPEG |
| Latence | Moins de 140 millisecondes |

### Audio

| Paramètre | Caractéristiques |
|-----------|----------------|
| Mode de capture audio | Audio embarqué HDMI |

### Environnement

| Paramètre | Caractéristiques |
|-----------|----------------|
| Température d'exploitation | 0°C à 40°C |
| Température de stockage | -10°C à 50°C |
| Humidité | 80 % RH |

### Dimensions et poids

| Paramètre | Caractéristiques |
|-----------|----------------|
| Longueur x Largeur x Hauteur | 61 x 13,5 x 53 mm |
| Poids | 48 g |

## Accessoires du kit

| Article | Numéro de modèle | Description |
|------|--------------|-------------|
| Câble HDMI mâle-mâle | OP-03-CABLE30-HDMI | Longueur : 0,3 m / ~12"<br>Couleur : Noir<br>Utilisation : Transmission vidéo HD HDMI |
| Câble Type-C vers USB-A avec adaptateur | OP-04-CABLE30-C2A | Longueur : 0,3 m / ~12"<br>Couleur : Noir<br>Adaptateur : USB-A femelle vers Type-C mâle<br>Utilisation : Transfert de données / contrôle KVM |
| Câble Type-C en nylon avec adaptateur | OP-05-CABLE150-C2C | Longueur : 1,5 m / 4' 11"<br>Couleur : Orange<br>Adaptateur : USB-C vers USB-A<br>Vitesse de transfert des données : Jusqu'à 10 Gbps<br>Puissance d'alimentation : 240 W |

## Connexions

### Connectivité / Interfaces

1. **Port USB-C (femelle)** ⓵  
   En tant que port d'appareil USB, se connecte à l'ordinateur hôte pour le transfert de données via un hub USB intégré

2. **Port USB-C (femelle)** ②  
   En tant que port d'appareil USB, se connecte à l'ordinateur hôte pour simuler la sortie HID clavier et souris via un hub USB intégré

3. **Port d'entrée HDMI (femelle)** ③  
   Source HDMI d'entrée depuis l'ordinateur cible

4. **Port USB-A 2.0 (femelle) bascule** ④  
   En tant que port d'hôte USB, utilisé soit par l'ordinateur hôte soit par l'ordinateur cible à tout moment, mais pas en même temps

5. **Interrupteur bascule** ⑤  
   Pour basculer la connexion du port USB-A 2.0 entre l'ordinateur hôte et l'ordinateur cible

6. **Pins de prolongation** ⑥  
   Pour plus d'informations, veuillez consulter les pins de prolongation pour l'utilisation par les développeurs.

## Applications

L'Openterface Mini-KVM est le compagnon idéal pour une large gamme d'utilisateurs et de scénarios :

- Professionnels de l'informatique dépannant des serveurs
- Techniciens intervenant sur des distributeurs automatiques, terminaux de vente et kiosques
- Développeurs gérant des appareils de calcul en périphérie
- Enthusiastes technologiques expérimentant avec des ordinateurs à circuit imprimé
- Professionnels nécessitant des opérations locales sécurisées sur la séparation réseau, tels que ceux gérant des actifs de cryptomonnaie
- Tout utilisateur ayant besoin d'écoulements de travail fréquemment intégrés entre ordinateurs personnels et professionnels.

## Logiciels pour l'ordinateur hôte

Pour mettre ce dispositif en service sur macOS, Windows, Linux ou Android, installez l'un de nos applications disponibles sur les plateformes d'applications correspondantes ou construisez-le à partir de la source en utilisant nos dépôts GitHub.

## Open Source & Conformité

Les applications Openterface sont licenciées AGPL-3.0, développées activement par TechxArtisan. L'appareil est certifié OSHWA (UID CN000015), garantissant un accès ouvert à toutes les schémas et codes sources sur GitHub : [Openterface_Mini-KVM_Hardware](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

## Restez informé

Visitez [openterface.com](https://openterface.com) et rejoignez notre communauté Discord pour rester informé, obtenir un support et collaborer avec d'autres utilisateurs.