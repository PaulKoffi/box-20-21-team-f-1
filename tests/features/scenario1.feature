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



