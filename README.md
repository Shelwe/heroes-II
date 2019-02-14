# heroes-II
Bienvenue sur le projet d'implémentation du système de jeu du Reboot du jdr Heroes. 

Le projet est libre, tout le code est accessible comme on aime, meme si il sera dégueu. Mais bon, je peux pas vraiment critiquer. La suite est plus claire et synthétique, promis.

---------------------------------------------------
**USUAL DISCLAIMER**
- L'ensemble des codes soumis se doivent de pouvoir être interprétés et avoir été testé avec au moins un exemple. C'est une très bonne pratique pour éviter beaucoup de temps de debug.
- Tout peut être rediscuter, même les paradigmes généraux. Il suffit de le dire, d'énoncer l'interêt du changement et il sera probablement appliqué.
- Privilégiez un découpage systématique des codes en fonction dans des fichiers séparés.
---------------------------------------------------

Découpage principal :

La structure, qui sera amenée à être refragmentée, est naturellement divisée selon les étapes de jeu :

- Création de perso :
	+ Définition d'un classe personnage
	+ Fonctions sur cette classe
	+ Formatage des entrées et sorties de ces fonctions (WARNING : on n'aura pas accès au stdout)
	+ BONUS: Calcul de token intégrés en fonction des attributes du personnage, et compatibilité de la valeur avec les fichiers d'affichage
- Combat :
	+ Ecriture du gameplay
	+ Implémentation des fonctions associées
	+ Gestion d'un tour à tour par rapport à des variables d'un autre fichier
	+ Gestion d'un tour à tour par des entrées de différentes machines
- Affichage: (WARNING: Domaine technique, demande de se renseigner de façon conséquente sur les lib utilisées)
	+ Création d'une interface utilisateur comprenant son profil, ses items et ses possibilités
	+ Création d'un board de schématisation des combats, avec les sorties de Combat (On ne demande pas de dessiner, la majeure partie du travail sera fait par la description de votre MJ)
	+ Création d'un interface MJ suceptible d'avoir accès à toutes les informations contenues dans le programme, y compris le code lui même, sans interrompre le processus
	+ Transformer les input des joueurs en informations utilisables
- RCP: (WARNING: Domaine technique, demande de se renseigner de façon conséquente sur les lib utilisées)  
	+ Assurer la sécurité et l'intégriter des transferts de paquets
	+ Minimiser les informations et développer un protocole efficace de transfert d'information
	+ Coordonner les échanges pour limiter les temps d'attente
- Mémoire:
	+ Structurer l'ensemble des items, mobs, spells et effets du jeu. Trouver des structures de données adaptées a chaque chose
	+ BONUS: Permettre des inventaires partiels et fournir des descriptions en fonction de l'indentité et du profil de l'utilisateur qui fait la requête
	+ BONUS: Encoder la mémoire et les protocoles de lecture pour éviter la triche
