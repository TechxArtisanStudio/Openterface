---
title: "Installation matérielle"
description: "Guide d'installation matérielle étape par étape pour l'Openterface KVM Extension for uConsole. Apprenez comment installer correctement la carte d'extension dans le slot d'expansion de votre uConsole avec des directives de sécurité détaillées."
keywords: "installation extension KVM, configuration matérielle uConsole, installation carte d'expansion, slot d'expansion uConsole, guide matériel KVM, installation physique"
---

# **Installation matérielle** | Openterface KVM Extension for uConsole

## Aperçu
L'Extension KVM remplace le module 4G/LTE dans le slot d'expansion du uConsole, ajoutant une entrée HDMI directe et un contrôle USB HID.

## Ce dont vous avez besoin
- Vérifiez votre [Contenu de l'emballage](whats-in-the-box.md) avant l'installation  
- Carte Openterface KVM Extension  
- **Rondelles** fournies (pour assurer un montage stable et une pression uniforme)  
- Tournevis hexagonal (pour les vis de montage)  
- Protection ESD (bracelet ou surface mise à la terre) — recommandé  

## Étapes d'installation

### **1. Mise hors tension**
Éteignez le uConsole et débranchez toute alimentation et tous câbles.

### **2. Retirer le module existant**
Utilisez un tournevis hexagonal pour retirer les deux vis.  
Soulevez la carte **tout droit** pour éviter de plier les contacts à ressort.

### **3. Installer l'Extension KVM**
- Placez la **rondelle** sur le poteau de vis.  
- Insérez fermement l'Extension KVM dans le slot d'expansion.  
- La rondelle compense le PCB légèrement plus fin (1,0 mm vs 1,2 mm), maintenant une pression de contact à ressort appropriée.

??? note "Vérifier l'ajustement avant l'installation finale"
    Vous pouvez d'abord insérer la carte **sans la rondelle** pour tester l'ajustement. Si la carte semble lâche ou si les contacts sont inégaux, ajoutez la rondelle et réinsérez la carte. L'Openterface KVM Extension fait 1,0 mm d'épaisseur, légèrement plus fine que le module LTE original (1,2 mm). L'utilisation de la rondelle fournie assure un montage stable et un contact à ressort fiable.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="height:220px"}

### **4. Fixer la carte**
Réinsérez les vis et serrez **doucement** — **ne serrez pas trop fort**, car cela pourrait endommager la carte ou dénuder les filets.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="height:220px"}

### **5. Vérifier l'installation**
La carte doit être **plate et stable**, avec un contact à ressort uniforme sur tous les pads. Il ne devrait y avoir aucun mouvement ou balancement notable.

### **6. Installer le couvercle du slot d'expansion**
Réinstallez le couvercle du slot d'expansion pour protéger la carte Extension KVM et maintenir l'apparence originale du uConsole.

??? note "Orientation du texte sur le couvercle du slot d'expansion"
    Le texte sur le couvercle du slot d'expansion peut paraître "à l'envers" lorsqu'on le regarde sous certains angles. C'est un design intentionnel - le texte est orienté pour être lisible lorsque vous tenez le uConsole et regardez les ports de haut en bas, ce qui est la position de vision naturelle lors de l'utilisation de l'appareil.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="height:220px"}

---

**Prochaines étapes**

1. Allez à [Configuration logicielle](/product/uconsole-kvm-extension/software-setup/) pour installer l'App Openterface.  
2. Allez à [Se connecter à l'appareil cible](/product/uconsole-kvm-extension/connect-to-target/) pour connecter votre appareil cible.  
3. Consultez [Fonctionnalités et spécifications](/product/uconsole-kvm-extension/features/) pour les spécifications techniques détaillées.
