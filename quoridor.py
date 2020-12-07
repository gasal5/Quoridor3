'''Module quoridor'''
from copy import deepcopy
import random
import quorigraphe as qg

class Quoridor():
    '''classe Quoridor'''
    CHAINE = 1
    DICTIO = 2
    AVANCER = 3
    gesErr = GestionErreur()

    def setetatpartie(self, datapartie):
        '''setetatpartie'''
        self.etatpartie = deepcopy({'joueurs': [
            {'nom': datapartie[0], 'murs': datapartie[2], 'pos': datapartie[4],},
            {'nom': datapartie[1], 'murs': datapartie[3], 'pos': datapartie[5],},
            ],
                                    'murs': {
                                        'horizontaux': datapartie[6],
                                        'verticaux': datapartie[7],
                                    }
                                    })

def __init__(self, joueurs, murs=None):
        '''__init__'''
        self.vrai = True
        self.prochain_coup = None
        if Quoridor.gesErr.tester('init', (joueurs, murs)) == Quoridor.CHAINE:
            data = joueurs[0], joueurs[1]
            data += 10, 10
            data += (5, 1), (5, 9)
            data += [], []
            self.setetatpartie(data)
        else:
            data = joueurs[0]['nom'], joueurs[1]['nom']
            data += joueurs[0]['murs'], joueurs[1]['murs']
            data += joueurs[0]['pos'], joueurs[1]['pos']
            data += murs['horizontaux'], murs['verticaux']
            self.setetatpartie(data)
            Quoridor.gesErr.tester('_joueur_enferme', self.etatpartie)
