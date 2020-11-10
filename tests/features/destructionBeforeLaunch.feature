Feature: destruction before separation
  Ce scénario met en oeuvre la destruction du satellite avant séparation
  La mission échoue car le premier stage , le second et le payload sont détruits

  Scenario: lancement de la fusée dans une zone sans risque dans notre cas Nice
    Given Nice un site où la pression du vent est actuellement normale
    When  richard décide de démarrer le poll
    Then On voit que Elon donne son GO
    Then On voit que la réponse de Tory est GO
    Then et que la réponse de Richard est GO

  Scenario: etapes de lancement
    Then Rocket Preparation step
    Then Rocket on internal power step
    Then Startup step
    Then Main engine start step
    Then Liftoff/Launch step
    When Richard lance la destruction de la fusée
    Then On voit que la fusée est bien détruite

  Scenario: verification des statuts de la mission
    When Quand on verifie le statut Past de cette mission
    Then il est alors à True
    When Quand on verifie le succès de cette mission
    Then il est quand à lui à False


