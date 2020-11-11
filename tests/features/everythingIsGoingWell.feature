Feature: everything is going well
  Ce scénario débute avec l'enregistrement d'une nouvelle mission et se déroule bien jusqu"à la fin

  Scenario: enregistrement d'une nouvelle mission par Gwynne
    Given un client Francis et son adresse mail francis@gmail.com et une nouvelle fusée SPACE001 enrégistré dans notre BD
    Given un satellite au nom de CATACOMBE
    Given la position finale de ce satellite est 20
    When Gwynne enregistre cette nouvelle mission
    Then On voit qu'une fusée disponible a été affecté à la mission
    Then la fusée disponible est SPACE001

  Scenario: lancement de la fusée dans une zone à risque dans notre cas Toulouse
    Given Toulouse un site où la pression du vent actuellement est au dessus de notre seuil de sécurité
    Given la fusée SPACE001 qui est affecté à la mise en orbite du satellite CATACOMBE
    When  richard décide de démarrer le poll pour l'envoi de la fusée
    Then On voit que Elon donne son GO car la fusée est en état
    Then On voit que la réponse de Tory est NOGO car Toulouse est une zone à risque
    Then et que la réponse de Richard est donc NOGO

  Scenario: lancement de la fusée dans une zone sans risque dans notre cas Paris
    Given Paris un site où la pression du vent actuellement est normale
    When  richard décide de démarrer son poll
    Then On voit que Elon donne son GO car la fusée est dans un bon état
    Then On voit que la réponse de Tory est GO car les conditions atmosphériques de Paris sont aussi bonnes
    Then et que la réponse de Richard est alors GO

  Scenario: etapes de lancement
    Then Rocket Preparation
    Then Rocket on internal power
    Then Startup
    Then Main engine start
    Then Liftoff/Launch
    Then Max Q
    Then Main engine cut-off
    Then Stage separation
    Then Second engine start
    Then Fairing separation
    Then Second engine cut-off
    Then Payload separation/deploy

  Scenario: atterissage de la fusée
    Then Flip maneuver
    Then Entry burn
    Then Guidance
    Then Landing burn
    Then Landing legs deployed
    Then Landing

  Scenario: verification des statuts de la mission
    When Quand on verifie la disponibilité de la fusée attribué à la mission
    Then elle est bien à True
    When Quand on verifie le statut Past de la mission
    Then il est aussi à True
    When Quand on verifie le succès de la mission
    Then il est bien à True
