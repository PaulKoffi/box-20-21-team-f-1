Feature: scenario1
  Ce scénario débute avec l'enregistrement d'une nouvelle mission et se déroule jusq'à ce que Richard lance un STOP

  Scenario: enregistrement d'une nouvelle mission par Gwynne
    Given un client ayant comme Nom Francis et adresse mail francis@gmail.com
    Given un satellite au nom de PERSEUS
    Given la position finale de ce satellite ayant comme valeur 12
    When Gwynne enregistre cette nouvelle mission
    Then On voit qu'une fusée disponible a été affecté à la mission et qu'elle a été bien crée
    Then la fusée disponible est SOUL-9000

  Scenario: lancement de la fusée dans une zone sans risque dans notre cas Paris
    Given Paris un site où la pression du vent actuellement est au dessus de notre seuil de sécurité
    When  richard décide de démarrer le poll
    Then On voit que Elon donne son GO car la fusée est en état de décoller
    Then On voit que la réponse de Tory est GO car les conditions atmosphériques de Paris sont bonnes
    Then et que la réponse de Richard est donc GO

  Scenario: consultation details de la fusée avant le lancement
    Given le GO de Richard
    When  on consulte le statut du lancement de la fusée
    Then  on voit qu'il est bien à True
    Then  la fusée est toujours indisponible pour une autre mission pour le moment

  Scenario: simulation de lancement (Les données télemetriques ont été préEnregistrées en prenant en compte que le satellite arrive en bonne position)
    Given le GO de Richard accordé à Elon
    When Elon donne l'ordre de lancement de la fusée
    When  on consulte le statut success du Payload auquel est affectée la fusée SOUL-9000
    Then  on voit qu'il est à False et que l'attribut Past qui indique que la mission est terminée est aussi à False
    When  Richard décide de stopper la mission
    Then  On voit que Success est à False et Past aussi : La mission est passé et ça a été un échec
    When  On consulte le statut disponible de la fusée
    Then  Elle est indisponible car elle a été détruite



