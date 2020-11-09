Feature: destruction before separation
  Ce scénario met en oeuvre la destruction du satellite après séparation du premier et du second stage
  La mission réussit car seul le premier stage sera impacté par la destruction

  Scenario: lancement de la fusée dans une zone sans risque dans notre cas Rennes
    Given Rennes un site où la pression du vent est actuellement normale
    When richard décide de démarrer le poll de lancement
    Then Elon donne son GO
    Then Tory donne son GO
    Then la réponse de Richard est GO

  Scenario: etapes de lancement
    Then step Rocket Preparation
    Then step Rocket on internal power
    Then step Startup
    Then step Main engine start
    Then step Liftoff/Launch
    Then step Max Q
    Then step Main engine cut-off
    Then step Stage separation
    Then step Second engine start
    When Richard lance l'ordre de destruction de la fusée
    Then On voit que le first stage est bien détruit

  Scenario: verification des statuts de la mission
    When Quand on verifie alors le statut Past de cette mission
    Then il est alors à True indiquant que la mission s'est déja déroulée
    When Quand on vérifie alors le succès de la mission
    Then il est quand à lui à True car après séparation seul le first stage a été détruit par l'ordre de destruction
