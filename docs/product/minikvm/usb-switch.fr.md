---
title: "Port USB Commutable"
description: "Découvrez le système de commutation USB double matériel-logiciel dans Openterface Mini-KVM. Comprenez les quatre états opérationnels, les directives de sécurité et les capacités futures d'accès à distance."
keywords: "commutation USB, commutateur KVM, commutateur matériel, commutateur logiciel, contrôle de port USB, KVM over USB, KVM over IP, accès à distance, gestion d'appareils USB, périphériques informatiques, gestion d'alimentation USB"
---

# **Guide de Commutation du Port USB** | Openterface Mini-KVM

Le dispositif mini-KVM possède un seul port USB-A 2.0 qui peut **se connecter soit** à l'ordinateur hôte soit à l'ordinateur cible, mais **jamais aux deux en même temps**.

Le contrôle provient de deux commutateurs :

- **Commutateur Matériel** : Un commutateur physique à deux positions sur l'appareil ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="max-height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="max-height:20px"} (vers l'intérieur = hôte, vers l'extérieur = cible).
- **Commutateur Logiciel** : Un bouton de basculement dans l'application hôte qui redirige instantanément le port USB vers l'hôte ou la cible.

## États Opérationnels

La connexion du port USB-A dépend des positions du **Commutateur Matériel** et du **Commutateur Logiciel**. Le tableau suivant résume les quatre états possibles :

| **État** | **Commutateur Matériel** | **Commutateur Logiciel** | **Port Connecté À** | **Statut de Synchronisation** |
| -------- | ------------------------ | ------------------------ | ------------------- | ----------------------------- |
| 1        | Host                     | Host                     | Host                | Synced                        |
| 2        | Target                   | Target                   | Target              | Synced                        |
| 3        | Target                   | Host                     | Host                | Out of Sync (→ Host)          |
| 4        | Host                     | Target                   | Target              | Out of Sync (→ Target)        |

- **Synced** signifie que les paramètres matériel et logiciel correspondent.
- **Out of Sync** signifie que le logiciel remplace temporairement le commutateur matériel jusqu'à ce que le commutateur matériel soit déplacé à nouveau.

Tout mouvement manuel du commutateur matériel mettra à jour l'affichage logiciel et retournera à un état synchronisé.

Au démarrage, l'appareil se connecte par défaut à l'hôte. Le logiciel détecte la position du commutateur matériel et se synchronise en conséquence.

!!! warning "N'oubliez pas d'éjecter la clé USB avant de basculer le commutateur"
Si le port USB est utilisé par une clé USB, assurez-vous d'éjecter la clé USB avant de basculer le commutateur pour transférer l'utilisation du port à un autre ordinateur.

??? note "Comment partager une clé/disque USB entre les appareils Hôte et Cible ?"
Les fichiers peuvent être transférés entre l'hôte et la cible en suivant ces étapes :

    1. Montez une clé USB sur l'hôte lorsque le petit commutateur noir est réglé du côté du port Type-C de l'hôte.
    2. Copiez les fichiers sur ce disque monté.
    3. Après la copie, démontez le disque sans le débrancher physiquement.
    4. Retournez le petit commutateur noir de l'autre côté. Cette action commute la connexion du port USB-A vers la cible.
    5. Montez la clé USB sur l'appareil cible et copiez/déplacez les fichiers du disque, complétant le processus de transfert de fichiers de l'hôte vers la cible.

    Cette méthode peut également être utilisée dans la direction opposée.

!!! Note "Guide Utilisateur" - **Priorité du Commutateur Logiciel** : Quelle que soit la position du commutateur matériel, cliquer sur le commutateur logiciel changera immédiatement la direction du circuit.

    - **Synchronisation du Commutateur Matériel** : Tout basculement manuel du Commutateur Matériel alignera son état avec le Commutateur Logiciel, passant de l'État 3 ou 4 non synchronisé à l'État 1 ou 2. Cependant, cette synchronisation ne modifie pas nécessairement la connexion de circuit réelle.

    - **Surveillance du Commutateur Matériel** : Le Commutateur Matériel, bien qu'étant physique, est surveillé par le logiciel et ne contrôle pas directement la direction du circuit. Au lieu de cela, le logiciel interprète la position du commutateur et gère la commutation de circuit réelle.
