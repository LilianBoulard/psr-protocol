# Proposition de protocols server/robot

## `main_server.py`

Décrit l'API du serveur central, celui sur lequel tous les Rasptanks et les clients sont connectés

## `robot_server.py`

Décrit l'API du serveur qui tourne sur chaque rasptank.
La logique s'implémente dans control_robot si vous décidez d'utiliser
Python et FastAPI (ce que je recommande, c'est un standard pour les API modernes).
