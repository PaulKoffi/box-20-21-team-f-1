Feature: scenario1
    Ce scénario débute avec l'enregistrement d'une nouvelle mission et se déroule jusq'à l'aboutissement de la mission

    Scenario: enregistrement d'une nouvelle mission par Gwynne
        Given un client ayant comme Nom Francis et adresse mail francis@gmail.com
        Given un satellite au nom de CORSAIRE
        Given la position finale de ce satellite ayant comme valeur 12
        When Gwynne enregistre cette nouvelle mission
        Then On voit qu'une fusée disponible a été affecté à la mission et qu'elle a été bien crée
        Then la fusée disponible est VEGA-4000



