# Guide de démarrage rapide KVM-GO Beta

> Rédigé avec ❤️ par [Iker](https://github.com/IkerGarcia) de la communauté Openterface — merci de nous aider à améliorer la documentation !

Bienvenue dans la [version bêta de KVM-GO](/product/kvm-go/updates/251007-kvm-go-beta-test-kits-sent-1/) ! Vous trouverez ci-dessous une version condensée du questionnaire de retour bêta. Suivez chaque section, consignez vos observations et, une fois terminé, envoyez l’ensemble via le [questionnaire de retour bêta sur Google Form](https://openterface.com/product/kvm-go/beta-questions).

Félicitations, vous avez été sélectionné(e) comme testeur bêta ! Nous sommes ravis de recueillir vos impressions ; nous sommes certains que vous pourrez mettre l’appareil à l’épreuve dans de nombreux scénarios.

Ce test reste flexible, mais nous aimerions que vous concentriez vos efforts sur quelques scénarios précis.

Votre retour nous est extrêmement précieux. Vous pouvez explorer d’autres aspects de l’appareil, mais voici les domaines clés qui nous intéressent particulièrement :

1. **Test d’inactivité prolongée**
   1. Lancez le logiciel et connectez-vous à une cible
   2. Laissez le logiciel tourner sans interaction pendant une longue période (plusieurs heures)
   3. Revenez et tentez d’utiliser les contrôles clavier et souris
   - Après cette période d’inactivité, la souris et le clavier fonctionnaient-ils normalement à votre retour ?

2. **Test de connexion à chaud**
   - Veuillez tester la déconnexion puis la reconnexion de l’appareil pendant que le logiciel est en marche.

3. **Accès au BIOS et bas niveau**

4. **Copier-coller (textes courts et longs)**

5. **Paramètres de simulation de périphériques (Windows/Linux)**
   - 5.1. Configuration EDID de l’affichage
   - 5.2. Identification du périphérique USB (VID/PID)
   - 5.3. Fonctionnalité de la carte SD
     - 5.3.1. Cas d’usage 1 - Installation système : nous recommandons d’essayer Ventoy, un outil qui permet de placer plusieurs fichiers ISO sur une seule carte SD et de choisir lequel démarrer. Avez-vous essayé d’écrire une image système sur HOST, puis de passer sur TARGET pour l’installation (sans retirer la carte) ?
     - Cas d’usage 2 - Transfert de fichiers : avez-vous utilisé la carte SD pour transférer des fichiers entre HOST et TARGET ?

Ces exemples reflètent une partie des questions qui figurent dans le formulaire de retour bêta ; nous collectons également des informations générales sur la cohérence audio/vidéo/clavier/souris et la gestion thermique.

Merci pour votre aide !

!!! reminder "À ne pas oublier"
    Soumettez vos observations complètes via Google Form afin que l’équipe puisse les examiner rapidement.

