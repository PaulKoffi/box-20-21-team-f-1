Feature: supplier In Fuel
  Ce scénario met oeuvre le ravitaillement en carburant d'un satellite par une autre capsule

  Scenario: lancement de la capsule alors que le satellite n'est pas en orbite
    Given CORSAIRE un satellite dont le lancement a échoué
    When  Richard donne l'ordre de ravitaillement
    Then  Il reçoit une erreur car le système après consultation s'est rendu compte que le satellite n'était pas en orbite

  Scenario: Ravitaillement d'un satellite en orbite
    Given APOLLON un satellite en Orbite
    When  Richard donne l'ordre de ravitaillement du satellite
    Then  La capsule se met en route
    Then  La capsule envoit une notification dès qu'il commence le ravitaillement du satellite en Orbite
    Then  La capsule envoit de nouveau une notification quand il atterit sur terre