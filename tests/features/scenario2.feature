Feature: scenario2
  Ce scénario débute avec l'enregistrement d'une nouvelle mission et se déroule jusq'à ce que Richard lance un STOP

  Scenario: enregistrement d'une nouvelle mission par Gwynne
    Given un client Francis et son adresse mail francis@gmail.com et une nouvelle fusée SOUL-9000 enrégistré dans notre BD
    Given un satellite au nom de PERSEUS
    Given la position finale de ce satellite ayant est 12
    When Gwynne enregistre cette nouvelle mission dans sa CLI
    Then On voit qu'une fusée disponible a été affecté à la mission
    Then la fusée disponible est SOUL-9000

  Scenario: lancement de la fusée dans une zone sans risque dans notre cas Paris
    Given Paris un site où la pression du vent actuellement est normale
    When  richard décide de démarrer son poll
    Then On voit que Elon donne son GO car la fusée est dans un bon état
    Then On voit que la réponse de Tory est GO car les conditions atmosphériques de Paris sont aussi bonnes
    Then et que la réponse de Richard est alors GO

  Scenario: consultation details de la fusée avant le lancement
    Given le GO accordé par Richard
    When  on consulte le statut du lancement de la fusée SOUL-9000
    Then  on voit qu'il est bien à True donc la fusée a ordre de décoller
    Then  la fusée est toujours indisponible pour une autre mission pour le moment quand on consulte son statut

  Scenario: simulation de lancement (Les données télemetriques ont été préEnregistrées en prenant en compte que le satellite arrive en bonne position)
    Given le GO de Richard accordé à Elon pour lancer la fusée
    When Elon donne l'ordre de lancement de la fusée SOUL-9000
    When  on consulte le statut success du Payload auquel est affectée la fusée SOUL-9000
    Then  on voit qu'il est à False et que l'attribut Past qui indique que la mission est terminée est toujours aussi à False
    When  Richard décide de stopper la mission
    Then  On voit que Success est à False et Past aussi : La mission est passé et ça a été un échec
    When  On consulte le statut disponible de la fusée SOUL-9000
    Then  Elle est indisponible car elle a été détruite



