Feature: aborted launch
  Ce scénario met en oeuvre l'annulation de la mission avant le lancement de la fusée

 Scenario: lancement de la fusée dans une zone sans risque dans notre cas Monaco
    Given Monaco un site où la pression du vent est actuellement normale
    When  richard démarre le poll
    Then Elon répond par GO
    Then Tory répond par GO
    Then Richard répond ensuite par GO

  Scenario: etapes de lancement
    Then step : Rocket Preparation step
    When Richard lance l'ordre de destruction
    Then on voit que la mission est bien annulée
