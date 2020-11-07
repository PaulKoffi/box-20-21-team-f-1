Feature: scenario1
  Ce scénario débute avec l'enregistrement d'une nouvelle mission et se déroule jusq'à l'aboutissement de la mission


  Scenario: lancement de la fusée à Paris
    Given Paris un site sécurisé de lancement
    Given la fusée RIKIKI qui est affecté à la mise en orbite du satellite APOLLON
    When  richar décide de démarrer le poll pour l'envoi de la fusée
    Then On voit Elon donne son GO
    Then On voit la réponse de Tory est GO
    Then et que Richard donne son GO
