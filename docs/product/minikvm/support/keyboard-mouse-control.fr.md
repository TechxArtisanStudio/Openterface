# **Dépannage des problèmes de clavier et souris ne pouvant pas contrôler l'ordinateur cible**

Occasionnellement, les utilisateurs peuvent rencontrer des situations où les fonctions de clavier et de souris du dispositif Openterface ne fonctionnent pas comme prévu. Ce document décrit les causes les plus courantes et comment les résoudre ou les prévenir.

**Retour du logiciel :** Lorsque Openterface ne peut pas établir une communication HID en raison d'une connexion de cible manquante ou incorrecte, l'interface met en évidence l'état pour que vous puissiez agir rapidement.

- Sur **macOS**, l'icône de clavier et de souris dans le coin supérieur droit de l'utilitaire Openterface devient **orange**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_macos.webp" alt="Inactive keyboard and mouse (macOS)" width="200" />

- Sur **Windows/Linux**, l'icône correspondant en bas de la fenêtre devient **rouge**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_windows.webp" alt="Inactive keyboard and mouse (Windows)" width="200" />

La vidéo apparaît toujours dans Openterface mais le clavier et la souris ne réagissent pas — vous pouvez voir le bureau cible mais ne pas le contrôler. Cela signifie généralement que la communication HID n'est pas établie (par exemple, mauvais câble cible, hub sans alimentation ou puce HID défectueuse) ; consultez la liste de contrôle et les sections ci-dessous. Le logiciel bloque également les connexions clavier/souris supplémentaires jusqu'à ce que le câblage/problème soit résolu.

---

## **1. Connexion de câble incorrecte**

**Problème :**  
Étonnamment courant : les utilisateurs oublient de connecter le port Openterface Target Type-C à l'ordinateur cible.

**Solution :**  
✅ Vérifiez toujours :
- Le **câble Type-C cible** est solidement connecté du **port cible** Openterface à l'**ordinateur cible** que vous souhaitez contrôler.
- Le **câble USB-A/USB-C hôte** est connecté à votre **ordinateur hôte/contrôleur** (où OpenterfaceQt ou le logiciel de contrôle s'exécute).

> **Conseil :** Étiquetez les câbles pour éviter toute confusion dans les configurations complexes.
- Connectez le câble noir au côté noir du connecteur cible.
- Connectez le câble orange au côté recouvert d'orange du connecteur cible.


## **2. Utilisation de hubs USB sans alimentation**

**Problème :**  
La connexion d'Openterface via un hub USB sans alimentation peut entraîner une **alimentation insuffisante** (chute de tension VBUS). Cela peut causer un fonctionnement erratique du dispositif ou l'impossibilité d'initialiser les fonctions HID (clavier/souris).

**Solution :**  
✅ **Évitez les hubs USB sans alimentation** entre Openterface et l'ordinateur cible.  
✅ Si un hub est nécessaire, utilisez un **hub USB de haute qualité alimenté en externe** capable de fournir une alimentation 5V stable.

> **Remarque :** L'alimentation USB est essentielle au fonctionnement fiable de la puce HID. Les baisses de tension peuvent déclencher des défauts internes.

---

## **3. La puce HID entre en « état zombie »**

**Problème :**  
Dans certaines conditions — comme des rafales de commandes rapides combinées à une alimentation marginale — la puce HID interne (par exemple, CH9329) peut entrer dans un **« état zombie »**. Dans cet état :
- La puce HID se verrouille et arrête l'envoi de données de réponse en série à l'ordinateur hôte.
- Elle conserve un état d'erreur interne qui empêche la réinitialisation normale par le logiciel hôte.
- Le dispositif peut sembler connecté (vidéo présente) alors que les entrées restent non réactives.
- Le logiciel hôte (par exemple, OpenterfaceQt) ne peut pas réinitialiser correctement le dispositif.
- La reconnexion de tous les câbles ou le cycle d'alimentation de la connexion USB n'effacent généralement pas cette erreur interne ; une réinitialisation usine de la puce HID est nécessaire.

**Solution :**  
Effectuez une **réinitialisation usine de la puce HID** :

- Sur **macOS** : Utilisez l'**outil de réinitialisation en série** disponible dans le **menu Avancé** de l'utilitaire macOS.  

    <img src="https://assets.openterface.com/images/software/MacOS_FactoryResetHID.webp" alt="Serial Reset Tool (macOS)" width="150" />

- Dans **OpenterfaceQt** (application de bureau) : Allez à **Menu Avancé → Réinitialisation usine de la puce HID**.

    <img src="https://assets.openterface.com/images/software/OpenterfaceQT_FactoryResetHID.webp" alt="Factory Reset HID Chip (OpenterfaceQt)" width="150" />

> Cela efface l'état interne de la puce et restaure le fonctionnement normal.

---

## **4. Sensibilité du débit en baud dans les environnements bruyants**

**Problème :**  
Openterface utilise par défaut une vitesse en baud de **115200 bps** pour une transmission de données souris plus rapide. Cependant, dans les environnements électriquement bruyants (par exemple, alimentations à découpage ou câbles longs/mal blindés), ce débit élevé peut entraîner des **erreurs de communication en série**, provoquant la perte ou la corruption de commandes HID.

**Solution :**  
Basculez vers un débit en baud de **9600 bps** :
- Cela améliore considérablement la **fiabilité de la communication** dans les configurations bruyantes.
- L'impact sur la latence est **négligeable** dans une utilisation typique (par exemple, capture vidéo 30 FPS et contrôle).

> **Recommandation :** Si vous rencontrez des défauts d'entrée intermittents sans problèmes d'alimentation ou de connexion, essayez d'abaisser le débit en baud dans la configuration d'Openterface.

---

## **Liste de contrôle récapitulative**

Si le clavier/souris ne fonctionne pas :

1. ✅ Confirmez que le **câble Type-C cible** correct est connecté à l'**ordinateur cible**.
2. ✅ Évitez les hubs USB sans alimentation — utilisez une connexion directe ou un **hub alimenté**.
3. ✅ Si le dispositif semble « figé », **réinitialisez la puce HID** via le logiciel.
4. ✅ Dans les environnements instables, **réduisez le débit en baud à 9600** pour une communication plus robuste.
5. ✅ Si les tentatives ci-dessus n'aident pas, essayez un port USB différent sur l'hôte ou redémarrez l'ordinateur hôte — le système d'exploitation peut désactiver un port ou le hub après avoir reçu trop de paquets d'erreur USB. Le changement de port ou le redémarrage de l'hôte restaure généralement la connexion.

---

En abordant ces quatre domaines, la plupart des problèmes HID intermittents peuvent être évités ou rapidement résolus. Pour les problèmes persistants, veuillez contacter le support (support@openterface.com) avec les détails de votre configuration et les journaux.
