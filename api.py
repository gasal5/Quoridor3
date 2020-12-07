# -*- coding: utf-8 -*-
import requests
 
BASE_URL = 'https://python.gel.ulaval.ca/quoridor/api/'
 
def lister_parties(idul):
 
    rep = requests.get(f'{BASE_URL}parties/', params = {'idul': idul})
    if rep.status_code == 200:
       rep = rep.json()
       if rep.get('message'):
            raise RuntimeError(rep.get('message'))
    else:
        print(f"Le GET sur {BASE_URL}lister a produit le code d'erreur {rep.status_code}.\n")
 
    return rep
 
def initialiser_partie(idul):
    rep = requests.post(f'{BASE_URL}partie/', data = {'idul': idul})
    rep = rep.json()
    
    return rep
 

def jouer_coup(id_partie, type_c, posi):
    '''Fonction qui permet de jouer un coup.'''
    rep = requests.post(f'{BASE_URL}jouer/', data={'id': id_partie, 'type': type_c, 'pos': posi})
    if rep.status_code == 200:
        rep = rep.json()
        if rep.get('message'):
            raise RuntimeError(rep.get('message'))
        if rep.get('gagnant'):
            raise StopIteration(rep.get('gagnant'))
    else:
        print(f"Le POST sur {BASE_URL}jouer a produit le code d'erreur {rep.status_code}.\n")

    return rep




    
"""
    Joue un coup en effectuant une requête à l'URL cible
    quoridor/api/jouer/
 
    Cette requête est de type PUT, contrairement à lister_parties,
    car elle modifie l'état interne du serveur en modifiant une partie existante.
 
    Elle s'attend à recevoir en entrée trois (3) paramètres associés au PUT:
 
        id: l'identifiant de la partie;
        type: le type de coup du joueur
              'D' pour déplacer le jeton,
              'MH' pour placer un mur horizontal,
              'MV' pour placer un mur vertical;
        pos: la position (x, y) du coup.
 
    En cas de succès (code 200), elle retourne en JSON
    un dictionnaire pouvant contenir les clés suivantes:
 
        état: l'état actuel du jeu;
        gagnant: le nom du joueur gagnant, None s'il n'y a pas encore de gagnant.
 
    En cas d'erreur (code 406), elle retourne en JSON
    un dictionnaire contenant la clé suivante:
 
        message: un message en cas d'erreur.
 
    Args:
        id_partie (str): Identifiant de la partie.
        type_coup (str): Type de coup du joueur :
                            'D' pour déplacer le jeton,
                            'MH' pour placer un mur horizontal,
                            'MV' pour placer un mur vertical;
        position (tuple): La position (x, y) du coup.
 
    Returns:
        dict: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
 
    Raises:
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.
 
    Examples:
        >>> id_partie = 'c1493454-1f7f-446f-9c61-bd7a9d66c92d'
        >>> type_coup = 'D'
        >>> position = (3, 5)
        >>> partie = jouer_coup(id_partie, type_coup, position)
        >>> print(partie)
        ('c1493454-1f7f-446f-9c61-bd7a9d66c92d', { 'joueurs': ..., 'murs': ... })
    """
 
    