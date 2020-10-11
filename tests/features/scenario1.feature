Feature: scenario1
  Ce scénario débute avec l'enregistrement d'une nouvelle mission et se déroule jusq'à l'aboutissement de la mission

  Scenario: enregistrement d'une nouvelle mission par Gwynne
    Given un client ayant comme Nom Francis et adresse mail francis@gmail.com
    Given un satellite au nom de CORSAIRE
    Given la position finale de ce satellite ayant comme valeur 12
    When Gwynne enregistre cette nouvelle mission
    Then On voit qu'une fusée disponible a été affecté à la mission et qu'elle a été bien crée
    Then la fusée disponible est VEGA-4000

  Scenario: lancement de la fusée dans une zone à risque dans notre cas Toulouse
    Given Toulouse un site où la pression du vent actuellement est au dessus de notre seuil de sécurité
    Given la fusée VEGA-4000 qui est affecté à la mise en orbite du satellite CORSAIRE
    When  richard décide de démarrer le poll pour l'envoi de la fusée
    Then On voit que Elon donne son GO car la fusée est en état
    Then On voit que la réponse de Tory est NOGO car Toulouse est une zone à risque
    Then et que la réponse de Richard est donc NOGO

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
    When  on consulte le statut success du Payload auquel est affectée la fusée VEGA-4000
    Then  on voit qu'il est à False et que l'attribut Past qui indique que la mission est terminée est aussi à False
    Then  le statut pour passer au detachement de la fusée est à False
    When  On consulte la vitesse de la fusée actuellement
    Then  Sa vitesse est 10
    When  Après 27 secondes on consulte le statut qui indique le detachement en 2 de la fusées
    Then  il est maintenant à True et donc le satellite sera bientôt en Orbite
    When  On consulte maintenant les détails du Payload après 20s
    Then  On voit que Success est à True et Past toujours à False : L'orbite est en place mais la fusée n'a pas encore atteri sur terre
    When  On consulte la vitesse actuelle de la fusée après 10s
    Then  Elle est à 9 et donc la fusée est au MaxQ
    When  On consulte après 20s à nouveau le statut Past et la disponibilité de la rocket VEGA-4000
    Then  La fusée est à nouveau disponible et Past à True indique que la mission est terminée



