---
title: "Comment se connecter"
description: "Guide étape par étape pour configurer l'Openterface KVM-Go. Apprenez à connecter votre ordinateur hôte et votre appareil cible en utilisant des connecteurs vidéo intégrés pour une expérience de branchement direct ultra-simple."
keywords: "configuration KVM-Go, configuration KVM ultra-compact, connexion HDMI intégrée, guide d'installation KVM, configuration KVM porte-clés, connexion USB KVM, configuration ordinateur headless, configuration KVM portable"
---

# **Comment se connecter** | Guide de configuration | Openterface KVM-Go

## **Aperçu des connexions**

![Aperçu des connexions KVM-Go](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

Les images ci-dessus montrent toutes les connexions entre le [**KVM-Go**](/product/kvm-go), l'ordinateur hôte et l'appareil cible.

- **Ordinateur hôte** : Nécessite l'installation de [l'application Openterface](/app).  
- **Appareil cible** : Aucun logiciel ni pré-configuration nécessaire.
- **Vidéo** : Le connecteur intégré se branche directement dans l'appareil cible, vous n'avez donc pas besoin de transporter ou de gérer des câbles vidéo supplémentaires.

## **Ce dont vous avez besoin pour les connexions**

![KVM-Go toutes les pièces](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

Pour configurer votre **KVM-Go**, vous aurez besoin des composants suivants :

- **KVM-Go (HDMI / DP / VGA)** — se connecte à **l'appareil cible** (pour la capture vidéo)  
- **Câble USB-C court noir** — se connecte à **l'appareil cible** (pour l'émulation du clavier et de la souris)
- **Câble USB-C long orange** — se connecte à **l'ordinateur hôte** (exécutant [l'application Openterface](/app))

!!! note "Avertissement sur la longueur des câbles"
    Les longueurs exactes des câbles inclus dans le **package officiel KVM-Go** ne sont **pas encore finalisées** et peuvent différer légèrement de celles présentées ici.  
    Les câbles démontrés dans ce guide proviennent du *kit Mini-KVM classique* et sont à titre indicatif uniquement.

!!! warning "Utilisation de vos propres câbles"
    Si vous choisissez d'utiliser vos propres câbles, assurez-vous qu'ils sont **des câbles USB de haute qualité, capables de transférer des données**. Les câbles de mauvaise qualité ou réservés à la charge peuvent entraîner :
    
    - Des problèmes d'écran noir
    - Des entrées clavier ou souris non réactives
    - Des déconnexions intermittentes
    - Une sortie d'affichage scintillante ou instable

## **Configuration étape par étape**

### **Étape 1 — Connecter les câbles USB au KVM-Go**
![Branchement des câbles USB](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **Câble USB-C noir** → Brancher dans le port étiqueté ![Icône cible](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![Icône cible](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** sur le boîtier KVM-Go.  
- **Câble USB-C orange** → Brancher dans le port étiqueté ![Icône hôte](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![Icône hôte](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host**.

!!! warning
    Les deux ports USB-C sont physiquement identiques.  
    Toujours **vérifier deux fois les étiquettes** sur la surface du boîtier pour éviter de les confondre.

### **Étape 2 — Connecter la vidéo à la cible**
![Branchement du connecteur HDMI](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

Brancher le **connecteur vidéo mâle intégré** directement dans le port de sortie vidéo de l'appareil cible.

### **Étape 3 — Connecter le port USB cible**
Connecter le **câble USB noir** à l'appareil cible pour le contrôle HID.

- **Option A :** Directement dans un port USB-A  
  ![Cible USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **Option B :** En utilisant un adaptateur USB-C  
  ![Cible USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "Vérification de la connexion USB-C"
    Certains ports USB-C peuvent ne pas fournir une connexion sécurisée. Si vous rencontrez des problèmes de contrôle intermittent du clavier/souris, secouez doucement la connexion de l'adaptateur pour vous assurer qu'il est correctement inséré et en contact.


### **Étape 4 — Connecter le port USB hôte**
Connecter le **câble USB orange** à l'ordinateur hôte.

- Directement à un port USB-C **OU** via un adaptateur USB-C vers USB-A.  
  ![Branchement USB hôte](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

