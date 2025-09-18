---
title: "Broches d’extension"
description: "Explorez le potentiel des broches d’extension de l’Openterface Mini-KVM pour le développement matériel personnalisé et les projets open source."
keywords: "Mini-KVM broches d’extension, développement personnalisé, modification matérielle, KVM open source"
---

# **Broches d’extension** | Mode développeur | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:300px"}

Openterface Mini-KVM intègre des broches d’extension pour le développement avancé et l’expérimentation avec [Open Software](/app). Ces broches ne sont pas exposées dans la configuration de boîtier standard.

## Comment accéder aux broches

1. Démontez l’appareil.
2. Remplacez le capot de boîtier d’origine par un capot spécial « Extension Pin Cap ».
3. Téléchargez le [modèle 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) du capot d’extension.
4. Consultez notre [dépôt GitHub matériel](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="height:300px"}

!!! warning "Annulation de la garantie"
    Le retrait du boîtier d’origine peut annuler la garantie du produit. Toute modification ou tout démontage est effectué aux risques et périls de l’utilisateur.

!!! note "Fonctionnalités expérimentales"
    Les fonctionnalités développées à l’aide de ces broches sont expérimentales et n’ont pas été entièrement testées. Openterface n’est pas responsable des dommages, blessures ou dysfonctionnements résultant de modifications, de l’exposition des broches d’extension ou d’autres altérations de l’appareil.

## Configuration des broches

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="height:200px"}

Les broches d’extension offrent les connexions suivantes :

1. Alimentation USB 5 V pour composants externes
2. Données positives vers le hub USB de l’hôte
3. Données négatives vers le hub USB de l’hôte
4. Données positives vers le hub USB de la cible
5. Données négatives vers le hub USB de la cible
6. Masse

!!! danger "Connexions incorrectes = dommages"
    Inverser VCC et GND peut provoquer de graves dommages à l’appareil et aux composants connectés. Vérifiez toujours les connexions des broches avant la mise sous tension.

## Capot de broches d’extension

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:360px"}

Ce capot de broches d’extension imprimé en 3D remplace le capot d’origine de l’Openterface Mini-KVM, permettant aux utilisateurs avancés d’exposer et d’accéder aux broches d’extension pour un développement personnalisé. Vous pouvez télécharger les fichiers du modèle 3D depuis notre dépôt GitHub et imprimer le capot vous‑même.

- **Utilisation** : offre un accès aux broches d’extension pour le développement matériel avancé.
- **Téléchargement** : [Fichiers du modèle 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## Participer au développement

Au fil de nos développements et expérimentations, nous mettrons à jour cette section avec davantage d’informations sur les capacités de ces broches et leurs usages créatifs. Votre créativité et votre expertise peuvent repousser les limites du possible avec l’Openterface Mini-KVM. Participez :

1. **Partagez vos idées** : vous avez un concept intéressant pour utiliser ces broches ? Dites‑nous tout !
2. **Contribuez avec des projets DIY** : si vous avez créé quelque chose d’intéressant, pensez à le partager avec notre communauté [Discord Openterface](/discord).
3. **Rejoignez la discussion** : échangez avec d’autres développeurs et passionnés pour réfléchir et collaborer.

Construisons et innovons ensemble !
