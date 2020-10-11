# blue-origin-x-20-21-soa-20-21-f
* Auteurs: **Team F**
    * AINADOU Florian
    * DJEKINOU Paul-Marie
    * KOFFI Paul
    * NABAGOU Djotiham
* Version actuelle : en développement (MVP - Sprint 1)
* Releases :
    * [Sprint 1](https://github.com/pns-si5-soa/box-20-21-team-f/releases/tag/sprint1) : Semaine 1 de dev
* Statuts d'Intégration continue : [![Build Status](https://travis-ci.com/pns-si5-soa/box-20-21-team-f.svg?token=A689phqWFprpuzVyuqDk&branch=master)](https://travis-ci.com/pns-si5-soa/box-20-21-team-f)
  
# Vue d'ensemble
 Cette étude de cas est utilisée pour illustrer les différentes technologies impliquées dans le cours d'Architecture Orienté Services (SOA) donné à Polytech Nice - Sophia Antipolis en 5e année. Ce code de démonstration nécessite les logiciels suivants pour fonctionner correctement :
 
   * Environnement de Build & de configuration Npm : Npm 6.14.8        
   * Environnement de déploiement : Docker 2.2.0.5 (Stable)
   * Langage d'implémentation Javascript : Node JS v12.14.1
   * Langage d'implémentation Python : Python 3
   
   * ##### PS : Exclusivement pour les systèmes linux ou Unix : GNOME Terminal 3.36.2 using VTE 0.60.3 +BIDI +GNUTLS +ICU +SYSTEMD
   
  ## Vision du produit
  Le produit à mettre en oeuvre évolue itérativement sur plusieurs semaines :   
   👉 [Version 1](./docs/scope_1.pdf)   
   👉 [Version 2](./docs/scope_2.pdf)   
   👉 [Version 3](./docs/scope_3.pdf) 
    
  L'architecture logicielle à développer dans ce projet est également incrémentale et se présente comme suit :
  
  👉 Version 1 :
  <p align="center">
      <img src="./docs/archi_scope_1.png"/>
  </p>
  
  👉 Version 2 :
    <p align="center">
        <img src="./docs/archi_scope_2.png"/>
    </p>
  
  👉 Version 3 :
    <p align="center">
        <img src="./docs/archi_scope_3.png"/>
    </p>
  
  ## Comment utiliser ce repository
  * La branche `master` (la branche par défaut) représente la dernière version stable du système.
  * La branche `develop` représente le système en cours de développement.
  * Les issues peuvent être créés en utilisant le [système de ticket de Github](https://github.com/pns-si5-soa/blue-origin-x-20-21-soa-20-21-f/issues)
  * La suite des fonctionnalités à implémenter peuvent être consultées dans le [backlog](https://github.com/pns-si5-soa/blue-origin-x-20-21-soa-20-21-f/milestone/2)
  
  ### Récupération du projet
  Effectuer un clone classique du projet en faisant ```git clone https://github.com/pns-si5-soa/box-20-21-team-f.git``` ou en récupérant le zip depuis cette page.
  
  ## Compilation & Exécution  
  La compilation et l'exécution s'effectuent via des conteneurs *Docker* correspondants aux différents micro-services et autres acteurs du système.
  Le lancement et démarrage de ces conteneurs est automatisé grace à l'exécution de scripts.
  
  Ainsi, il est possible d'exécuter les actions suivantes : 
     
  - *Compilation & Exécution :* Exécuter le fichier [prepare.sh](./prepare.sh) à la racine du projet afin de compiler et exécuter toutes les images docker.
  - *Compilation :* Exécuter le fichier [build.sh](./build.sh) à la racine du projet afin de compiler toutes les images docker.
  - *Exécution :* Exécuter le fichier [launch.sh](./launch.sh) à la racine du projet afin d'exécuter toutes les images docker grâce à un [docker-compose.yml](./docker/docker-compose.yml) configuré à cet effet.
  - *Client Tory :* Exécuter le fichier [tory.sh](./tory.sh) à la racine du projet afin d'accéder à la cli dockerisée de Tory et exécuter les [commandes](./CLIs/tory/README.md) souhaitées.
  - *Client Elon :* Exécuter le fichier [elon.sh](./elon.sh) à la racine du projet afin d'accéder à la cli dockerisée de Elon et exécuter les [commandes](./CLIs/elon/README.md) souhaitées.
  - *Client Richard :* Exécuter le fichier [richard.sh](./richard.sh) à la racine du projet afin d'accéder à la cli dockerisée de Richard et exécuter les [commandes](./CLIs/richard/README.md) souhaitées.
  - *Arrêt :* Exécuter le fichier [stop.sh](./stop.sh) à la racine du projet afin d'arrêter puis supprimer tous les conteneurs docker en cours d'exécution et ainsi stopper la simulation.
  - *Suppression :* Exécuter le fichier [clean.sh](./clean.sh) à la racine du projet afin de supprimer toutes les images docker créées pendant l'exécution de la simulation.
  
  PS : 
  - La première fois, la compilation et exécution peut prendre un peu de temps à terminer.
  - Sur linux, l'exécution du prepare.sh se termine en ouvrant deux fenêtres qui sont des dashboards de logs nécessaires à la compréhension du scénario.
  - Sur windows, l'exécution du prepare.sh se termine sans ouvrir de fenêtres car tous les logs sont consultables depuis docker desktop en choisissant le conteneur approprié.
  - Une fois l'exécution du prepare.sh terminé, il faut exécuter de suite le run.sh pour visionner les logs. 
  
  
  ## Pile technologique
  
  <p align="center">
    <img src="./docs/stack.jpg"/>
  </p>
