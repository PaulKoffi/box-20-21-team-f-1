# Journal de bord 

* ***24/09/2020*** :
  - Implémentation du serveur rpc en python
  - Implémentation de la fonction `getResponsePoll` qui prend en paramètres `le nom du site` et `le nom de la fusée`.

  Cette fonction effectue des requêtes aux services `REST` s'occupant de la météo et de l'état de la fusée. Puis anlayse ces réponses et en fonction de l'état de ces derniers, la fonction renvoie un string  contenant la réponse de chacun `Go ou NoGo`
