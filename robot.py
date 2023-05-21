"""
Décrit l'API du robot.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Command(BaseModel):
    """
    Représente une commande envoyée au robot.

    Parameters
    ----------
    payload : dict
        Le payload de la commande.
        L'implémentation est propre à chaque robot.
    auth : str
        Une chaîne de caractères permettant au robot d'identifier
        l'authenticité de l'auteur de la commande.
        L'implémentation est propre à chaque paire client/robot.
    """
    payload: dict
    auth: str


@app.get("/robot/ping")
def ping():
    """
    Vérifie que le robot est bien connecté.
    Utilisé lors de l'enregistrement du joueur.

    Raises
    ------
    200
        Requête valide.
    500
        Erreur interne au robot.
    """
    return {"pong": True}


@app.post("/robot/control")
def control_robot(command: Command):
    """
    Transmet une commande au robot d'un joueur.

    Parameters
    ----------
    command : Command
        La commande à exécuter.

    Raises
    ------
    200
        Requête valide: la commande a été exécutée.
    403
        L'authentification a échoué.
    422
        Erreur de validation du schéma.
    500
        Erreur interne au robot.
    501
        Le robot n'a pas implémenté la commande.
    """
    return 200
