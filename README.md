# blue-origin-x-20-21-soa-20-21-f
* Auteurs: **Team F**
    * AINADOU Florian
    * DJEKINOU Paul-Marie
    * KOFFI Paul
    * NABAGOU Djotiham
  * Version actuelle: en développement (MVP - Sprint 1)
  * Releases :
    * À venir...
  * Statuts d'Intégration continue : 
    * Weather service : 
    * Rocket service : [![Build Status](https://travis-ci.com/pns-si5-soa/blue-origin-x-20-21-soa-20-21-f-rocketRest.svg?token=A689phqWFprpuzVyuqDk&branch=develop)](https://travis-ci.com/pns-si5-soa/blue-origin-x-20-21-soa-20-21-f-rocketRest)
    * Poll Creator RPC :
    * Elon CLI :
    * Richard CLI :
    * Tory CLI :
  
# Vue d'ensemble
 Cette étude de cas est utilisée pour illustrer les différentes technologies impliquées dans le cours d'Architecture Orienté Services (SOA) donné à Polytech Nice - Sophia Antipolis en 5e année. Ce code de démonstration nécessite les logiciels suivants pour fonctionner correctement :
 
   * Environnement de Build & de configuration Npm : Npm 6.14.8        
   * Environnement de déploiement : Docker 2.2.0.5 (Stable)
   * Langage d'implémentation Javascript : Node JS v12.14.1
   * Langage d'implémentation Python : Python 3
   
  ## Vision du produit
  Le produit à mettre en oeuvre est décrit 👉[ici](./docs/scope_1.pdf)👈. 
    
  L'architecture logicielle à développer dans ce projet s'appuiera sur la pile suivante :
  <p align="center">
      <img src="./docs/archi.png"/>
  </p>
  
  ## Comment utiliser ce repository
  * La branche `master` (la branche par défaut) représente la dernière version stable du système.
  * La branche `develop` représente le système en cours de développement.
  * Les issues peuvent être créés en utilisant le [système de ticket de Github](https://github.com/pns-si5-soa/blue-origin-x-20-21-soa-20-21-f/issues)
  * La suite des fonctionnalités à implémenter peuvent être consultées dans le [backlog](https://github.com/pns-si5-soa/blue-origin-x-20-21-soa-20-21-f/milestone/2)
  
  ### Récupération du projet
  Ce projet contient des sous-modules github et nécessite de ce fait de suivre les instructions suivantes pour effectuer une récupération complète du projet.
  1. Effectuer un clone classique du projet en faisant ```git clone url_du_repo``` ou en récupérant le zip depuis cette page.
  2. PS: Exécuter un seul fichier
     - Pour une version en développement (branche develop, test, no-release, no-tag), lancer le script [gitUpdateAllSubmodules.sh](./gitUpdateAllSubmodules.sh) se trouvant dans à la racine de ce projet.
     - Pour une version stable (branche master, release, tag spécifique), lancer le script [gitUpdateAllSubmodules(master).sh](./gitUpdateAllSubmodules(master).sh) se trouvant dans à la racine de ce projet.
    
  ### Compilation
  
  ### Exécution
  
  ## Pile technologique
  
  <p align="center">
    <img src="./docs/stack.jpg"/>
  </p>
