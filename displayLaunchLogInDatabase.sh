echo "Execution d'un script qui affiche les logs stockés dans la BD"
cd logs
pip3 install pymongo
pip3 install dnspython
python3 printLogIndatabase.py
read -n 1 -s -r -p "Press any key to quit"