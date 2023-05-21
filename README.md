# Proposition de protocols server/robot

## Description des fichiers

### `dispatcher.py`

Décrit l'API du serveur central.
C'est lui qui fait l'interface entre les Rasptanks et les clients.

### `robot.py`

Décrit l'API du serveur qui tourne sur chaque Rasptank.
La logique s'implémente dans la fonction `control_robot` si vous décidez d'utiliser
Python et FastAPI (ce que je recommande, c'est un standard pour les API modernes).

## Choix dans le design

Le principal paramètre pris en compte dans la conception de ce protocole est
la simplicité:
- pour une implémentation + simple, car tous les groupes doivent implémenter
  leur propre dispatcher
- pour limiter les ressources utilisées, car nous travaillons sur des Raspberry Pi

## Limitations actuelles

- Pas de streaming de données (problématique pour gérer les contrôles en temps réel)
- L'authentification est vulnérable aux écoutes passives
  si le serveur ne chiffre pas les communications.

Pour déclarer de nouvelles limitations, ouvrez une issue sur le repo.
