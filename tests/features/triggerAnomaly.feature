Feature: trigger Anomaly
  Ce scénario met oeuvre la destruction de la fusée par le système de gestions d'incidents
  Les données prévisionnelles ont été saisies # de celles qui seront envoyés par les serveurs télémetriques
  Le système de gestion d'incidents va donc activer automatiquement détruire la rocket

  Scenario: lancement de la fusée dans une zone sans risque dans notre cas Marseille
    Given Marseille un site où la pression du vent est actuellement normale
    When richard démarre le poll de lancement
    Then Elon donne son GO pour le lancement
    Then Tory donne son GO pour le lancement
    Then la réponse de Richard est GO pour le lancement

  Scenario: etapes de lancement
    Then step - Rocket Preparation
    Then step - Rocket on internal power
    Then step - Startup
    Then step - Main engine start
    Then step - Liftoff/Launch
    Then step - Max Q
    Then step - Main engine cut-off
    Then step - Stage separation
    Then step - Second engine start
    Then le système d'anomalie provoque la destruction de la fusée
    Then on voit que la fusée est bien détruite ensuite

  Scenario: verification des statuts de la mission
    When Quand on verifie alors le statut Past de notre mission
    Then il est alors à True indiquant que la mission s'est donc déja dérouler
    When Quand on vérifie ensuite le succès de la mission
    Then il est aussi à False car le satellite a été détruit
