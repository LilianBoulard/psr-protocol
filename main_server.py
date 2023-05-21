"""
Décrit l'API du serveur principal (auquel sont connectés tous les joueurs).
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
        Note: cette valeur est différente de celle utilisée pour
        enregistrer le joueur auprès du serveur.
    """
    payload: dict
    auth: str


@app.put("/player/{player_name}")
def register_player(player_name: str, robot_address: str,
                    robot_port: int, auth: str):
    """
    Enregistre/met à jour un joueur (robot) auprès du serveur.

    Parameters
    ----------
    player_name : str
        Le nom du joueur.
    robot_address : str
        L'adresse IP du robot.
    robot_port : int
        Le port de l'API Rest du robot.
    auth : str
        Une chaîne de caractères secrète entre le client et le serveur,
        permettant au client de manipuler le joueur (le supprimer ou le mettre
        à jour par exemple).
        Elle est définie lors du premier `put`. Elle est ensuite nécessaire
        pour toute requête `delete` ou `put` ultérieure.

    Raises
    ------
    200
        Requête valide: joueur enregistré/mis à jour.
    403
        L'authentification a échoué (uniquement pour les `put` ultérieurs).
    404
        Le robot n'a pas pu être enregistré car il est injoignable.
    422
        Erreur de validation du schéma.

    """
    return {"player_name": str}


@app.delete("/player/{player_name}")
def delete_player(player_name: str, auth: str):
    """
    Supprime un joueur (robot) du serveur.

    Parameters
    ----------
    player_name : str
        Le nom du joueur.
    auth : str
        La chaîne de caractères secrète entre le client et le serveur, définie
        au moment du premier `put` du joueur.

    Raises
    ------
    200
        Requête valide: joueur supprimé.
        Note: la chaîne de caractères secrète (`auth`) est oubliée.
    403
        L'authentification a échoué.
    404
        Le joueur n'est pas enregistré.
    422
        Erreur de validation du schéma.
    """
    return {"player_name": str}


@app.post("/player/control/{player_name}")
def control_robot(player_name: str, command: Command):
    """
    Transmet une commande au robot d'un joueur.

    Parameters
    ----------
    player_name : str
        Le nom du joueur.
    command : Command
        La commande à transmettre au robot.

    Raises
    ------
    200
        Requête valide.
    403
        L'authentification a échoué.
    404
        Le joueur n'est pas enregistré.
    503
        Le joueur a été enregistré (donc précédemment joignable),
        mais est actuellement injoignable.
    422
        Erreur de validation du schéma.
    500
        Erreur interne au robot.
    """
    return {"player_name": str}


@app.get("/player/{player_name}/bonus")
def get_player_bonus(player_name: str, auth: str):
    """
    Retourne le nombre de bonus du joueur.

    Les bonus permettent de contrer les pénalités.
    Les bonus sont ajoutés par le serveur.

    Parameters
    ----------
    player_name : str
        Le nom du joueur.
    auth : str
        La chaîne de caractères secrète entre le client et le serveur, définie
        au moment de l'enregistrement du joueur.

    Raises
    ------
    200
        Requête valide.
    404
        Le joueur n'est pas enregistré.
    422
        Erreur de validation du schéma.
    """
    return {"bonus": int}


@app.post("/player/{player_name}/penalty")
def sent_player_penalty(player_name: str):
    """
    Inflige une pénalité au joueur.

    Les pénalités peuvent être contrées par les bonus:
    si le joueur a un nombre de bonus >= 1, alors il ne reçoit pas la pénalité,
    et son nombre de bonus est décrémenté de 1.
    Si le joueur n'a pas de bonus, alors il reçoit la pénalité.

    La pénalité est la suivante: pendant 3 secondes à partir du moment
    où le serveur enregistre la pénalité, le robot ne peut pas recevoir
    de commandes.

    Parameters
    ----------
    player_name : str
        Le nom du joueur.

    Raises
    ------
    200
        Requête valide.
    404
        Le joueur n'est pas enregistré.
    422
        Erreur de validation du schéma.
    """
    return {"bonus": int}


@app.get("/player/list")
def get_player_list():
    """
    Retourne la liste des joueurs.

    Raises
    ------
    200
        Requête valide.
    422
        Erreur de validation du schéma.
    """
    return {"player_list": list[str]}
