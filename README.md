# Proposition de protocols server/robot

## `main_server.py`

Décrit l'API du serveur central.
C'est lui qui fait l'interface entre les Rasptanks et les clients.

## `robot_server.py`

Décrit l'API du serveur qui tourne sur chaque Rasptank.
La logique s'implémente dans control_robot si vous décidez d'utiliser
Python et FastAPI (ce que je recommande, c'est un standard pour les API modernes).
