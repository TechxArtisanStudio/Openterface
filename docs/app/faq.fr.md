# FAQ pour les Applications

Bienvenue dans la FAQ de nos applications. Si vous ne trouvez pas la réponse dont vous avez besoin, **envoyez-nous un email à [info@openterface.com](mailto:info@openterface.com)** ou **rejoignez notre communauté** sur [Discord](/discord) ou [Reddit](/reddit) pour vous connecter avec notre équipe de développement et d'autres utilisateurs.

⚠️ *Les FAQ peuvent devenir obsolètes — merci de nous faire savoir si vous repérez quelque chose qui a besoin d'être mis à jour !*

### :material-clipboard-list: Liste des Questions

- [Où puis-je télécharger les applications hôtes ?](#host-app-download)
- [Pourquoi les fonctionnalités diffèrent-elles entre les différentes applications hôtes ?](#host-app-differences)
- [Quelle application hôte offre actuellement la meilleure expérience ?](#best-host-app)
- [Y a-t-il une application hôte supportant ChromeOS ?](#host-app-chromeos)
- [Y a-t-il une application hôte supportant les appareils mobiles d'Apple ?](#host-app-ios)
- [Que faire si F11 ne fonctionne pas sur les applications macOS ?](#f11-macos-issue)

#### :material-chat-question:{ .faq } Où puis-je télécharger les applications hôtes ? {: #host-app-download }

Visitez notre [page d'installation d'application hôte](/quick-start/#install-host-application) pour les téléchargements officiels supportant **MacOS, Windows, Linux et Android**.

??? warning "Confidentialité et Sécurité : Soyez prudent lors de l'utilisation d'applications hôtes tierces"
    Comme notre projet est open source, vous pourriez trouver des versions alternatives d'applications hôtes compatibles avec notre Mini-KVM développées par d'autres. Bien qu'elles puissent offrir des fonctionnalités supplémentaires, assurez-vous de vérifier leurs pratiques de sécurité et de confidentialité. **L'équipe Openterface ne peut garantir ou être responsable de la sécurité des applications tierces**.

#### :material-chat-question:{ .faq } Pourquoi les fonctionnalités diffèrent-elles entre les différentes applications hôtes ? {: #host-app-differences }

Notre équipe de développement maintient activement les applications hôtes pour macOS, Linux, Windows et Android, mais en raison des défis spécifiques à chaque plateforme et de ressources limitées, les progrès de développement varient. Cela signifie que certaines fonctionnalités pourraient apparaître d'abord sur une plateforme et prendre plus de temps à arriver sur d'autres.

Nous faisons de notre mieux pour synchroniser le développement des fonctionnalités sur toutes les plateformes, mais c'est un travail en cours.

Vos commentaires jouent un rôle important dans la formation de notre feuille de route de développement — que ce soit par notre [communauté](/community/) ou notre [dépôt GitHub](/app/). Chaque suggestion nous aide à prioriser ce qui compte le plus pour vous !

Si vous êtes développeur, vos contributions sont incroyablement précieuses — et nous aimerions votre aide pour accélérer le processus !

#### :material-chat-question:{ .faq } Quelle application hôte offre actuellement la meilleure expérience ? {: #best-host-app }

En mars 2025, les applications hôtes basées sur Qt pour Windows et Linux offrent l'ensemble de fonctionnalités le plus complet dans l'ensemble. La version macOS se distingue par son expérience utilisateur la plus fluide et raffinée, grâce à une intégration système plus profonde et des améliorations d'interface utilisateur. L'application Android est une option pratique en déplacement, avec plus de fonctionnalités qui rattrapent régulièrement.

#### :material-chat-question:{ .faq } Y a-t-il une application web que je peux utiliser sur Chrome ou d'autres plateformes ? {: #host-app-chromeos }

Oui ! Un de nos membres de communauté géniaux, [Kashall](https://github.com/kashalls/openterface-viewer/), a construit **une application web open source légère** que vous pouvez utiliser directement dans votre navigateur : [openterface-viewer.pages.dev](https://openterface-viewer.pages.dev). Ce n'est pas encore partie de notre documentation officielle, mais notre équipe de développement l'a testée et l'a trouvée solide, facile à utiliser et super pratique — surtout sur Chrome ou quand vous voulez quelque chose de rapide et basé sur navigateur. Essayez-la !

#### :material-chat-question:{ .faq } Y a-t-il une application hôte supportant les appareils mobiles d'Apple ? {: #host-app-ios }

Nous explorons actuellement la compatibilité avec les systèmes mobiles d'Apple, tels qu'iOS et iPadOS. En raison des contrôles stricts d'Apple, ces plateformes pourraient ne pas supporter les connexions filaires avec des appareils tiers. Cependant, la situation pourrait changer, ou il pourrait y avoir des solutions de contournement potentielles. Si vous avez des idées ou des suggestions, nous vous invitons à rejoindre notre communauté pour en discuter avec nous. Nous nous engageons à améliorer la commodité de notre appareil en supportant autant de systèmes que possible. Si vous êtes désireux d'aider avec notre développement, venez passer du temps avec nous dans la communauté ou envoyez-nous un email !

#### :material-chat-question:{ .faq } Que faire si F11 ne fonctionne pas sur les applications macOS ? {: #f11-macos-issue }

Sur macOS, appuyer sur F11 affiche le bureau macOS au lieu de passer la touche F11 à l'application et à l'ordinateur cible. Pour corriger cela, vous pouvez dissocier F11 de la fonction "Afficher le bureau".

???+ info "Correction du problème de la touche F11 sur macOS"
    1. Allez dans **Réglages Système**.
    2. Sélectionnez **Bureau et Dock**.
    3. Faites défiler vers le bas et cliquez sur le bouton **"Raccourcis…"**.
    4. Trouvez **"Afficher le bureau"** et définissez-le sur le trait d'union **(-)** en bas de la liste déroulante.
    5. Ce changement permettra à la touche F11 de passer à votre application sur l'ordinateur cible.
