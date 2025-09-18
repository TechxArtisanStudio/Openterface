---
title: "Comment se connecter"
description: "Guide étape par étape pour configurer Openterface Mini-KVM. Apprenez à connecter votre ordinateur hôte et votre appareil cible avec des instructions détaillées pour les connexions USB-C, HDMI et périphériques. Inclut les descriptions d'interface et les conseils de configuration importants."
keywords: "Configuration Mini-KVM, guide de connexion KVM, configuration KVM USB-C, connexion KVM HDMI, guide d'installation KVM, configuration périphériques ordinateur, connexion appareil USB, guide interface KVM, configuration ordinateur headless, configuration KVM"
---

# **Comment se connecter** | Guide de configuration | Openterface Mini-KVM

## Configuration rapide

![to-host](https://assets.openterface.com/images/product/to-host.svg#only-light){:style="height:200px"} ![to-host](https://assets.openterface.com/images/product/to-host_1.svg#only-dark){:style="height:200px"}
![to-target](https://assets.openterface.com/images/product/to-target.svg#only-light){:style="height:200px"} ![to-target](https://assets.openterface.com/images/product/to-target_1.svg#only-dark){:style="height:200px"}

**Configuration en 4 étapes simples :**

1. **Connexion hôte** (côté orange) : Connecter l'ordinateur hôte avec un câble Type-C de 1,5m
2. **Connexion cible** (côté noir) : Connecter l'appareil cible avec un câble Type-C de 0,3m
3. **Connexion vidéo** (côté noir) : Connecter la sortie vidéo de la cible au port HDMI
4. **Appareil USB** (optionnel) : Connecter au port USB-A après avoir terminé les étapes 1-3

!!! note "Exigences" - **Hôte** : Nécessite l'installation de [Openterface App](/app) - **Cible** : Aucune app nécessaire - prend en charge Windows, macOS, Linux, Android, iOS - **Vidéo** : Utiliser le câble HDMI fourni ou le convertisseur VGA-to-HDMI

## Guide des ports

![host-side](https://assets.openterface.com/images/product/host-htc.svg#only-light){:style="width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc.svg#only-light){:style="width:300px"}
![host-side](https://assets.openterface.com/images/product/host-htc_1.svg#only-dark){:style="width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc_1.svg#only-dark){:style="width:300px"}

- ① **USB-C hôte** : Transfert de données vers l'ordinateur hôte
- ② **USB-C cible** : Sortie de contrôle clavier/souris
- ③ **Entrée HDMI** : Entrée vidéo depuis l'appareil cible
- ④ **Port USB-A** : Commutable entre hôte/cible

!!! warning "Notes importantes" - **Alimentation** : Les appareils USB ne doivent pas dépasser 1,5W de consommation - **Verrou USB-A** : Nécessite une force supplémentaire pour insérer/retirer (éviter les petits appareils) - **Hub USB** : Utiliser uniquement des hubs alimentés externes ; éviter les arbres USB profonds - **Commutation** : Voir [Guide de commutation du port USB](../usb-switch) pour plus de détails

⑤ ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} **Interrupteur à bascule** : Basculer le port USB-A entre hôte/cible

⑥ ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins.svg#only-light){:style="height:15px"} ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins_1.svg#only-dark){:style="height:15px"} **Broches d'extension** : Accès développeur (voir [Broches d'extension](../extension-pins))
