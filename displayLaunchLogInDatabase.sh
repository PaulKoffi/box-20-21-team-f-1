echo "Execution d'un script qui affiche les logs stockés dans la BD"
cd logs
python printLogIndatabase.py
read -n 1 -s -r -p "Press any key to quit"