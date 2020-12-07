# -*- coding: utf-8 -*-
import argparse
import api 
#import quoridor as qr

def analyser_commande():
    parser = argparse.ArgumentParser(description='Quoridor - phase 1')
    parser.add_argument('IDUL',metavar='idul', help="IDUL du joueur")
    parser.add_argument('-p', '--parties', metavar='partie', help="Lister les identifiants de vos 20 dernières parties")
  
    return parser.parse_args()

def afficher_damier_ascii(etat):
    print('Légende:')
    j = etat.get('joueurs')
    nom = j[0].get('nom')
    nb = j[0].get('murs')
    #nb = 3
    print('   1=' + nom + ','  + '     '  + 'murs=' + '|'*nb)
    nom = j[1].get('nom')
    nb = j[1].get('murs')
    #nb = 5
    print('   2=' + nom + ','  + '      '  + 'murs=' + '|'*nb)
    print("   "+"-"*35)
    MV = etat["murs"]["verticaux"]
    MH = etat["murs"]["horizontaux"]
    [pCol1, pRang1] = j[0]["pos"]
    [pCol2, pRang2] = j[1]["pos"]
    #pCol1, pRang1 = 1, 9
  
    #MV = [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    #MH = [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]]

    #print(mursV)
    for rang in range(9):
        ligne = str(9 - rang ) + " | "
        ligne2 = [" "]*35
        for col in range(8):
            car =" "
            if ([ col + 2, 9 - rang] in MV) or ([col + 2, 9 - rang - 1 ] in MV):
               car = "|"
            if [col + 2, 9 - rang - 1 ] in MV:
               ligne2[3 + col*4] = "|"
            if ([col + 2, 9 - rang  ] in MH):
              for offset in range(7):
                ligne2[4 + col*4 + offset] ="-"
            if  (pRang1 == 9 - rang) and (pCol1 == col + 1): #position du joueur 1
                ligne += "1 " + car + " "
            elif  (pRang2 == 9 - rang) and (pCol2 == col + 1): #position du joueur 2
                ligne += "2 " + car + " "
            else:
                ligne += ". " + car + " "
        print(ligne  + ". |") 

        if rang < 8:
          print("  |" + "".join(ligne2) + "|")
    print('--|-----------------------------------' )
    print('  | 1   2   3   4   5   6   7   8   9')
    print(etat)

"""
        Type de coup disponible :
        - D : Déplacement
        - MH: Mur Horizontal
        - MV: Mur Vertical

        Choisissez votre type de coup (D, MH ou MV) : D
        Définissez la colonne de votre coup : 5
        Définissez la ligne de votre coup : 2
"""




if __name__ == "__main__":
  ARGS = analyser_commande()
  #print(ARGS)

  if ARGS.parties:
     r =  api.lister_parties(ARGS.IDUL)
     for p in r.get('parties'):
        print(p.get('id'), p.get('état'))
  else:
     etat = api.initialiser_partie(ARGS.IDUL)
     #etat = r.get('état')
     #print(etat)
     while (True):
        afficher_damier_ascii(etat['état'])
        coup = input("Entrez votre coup: ")
        typeCoup, x, y = coup.split(',')
        etat = api.jouer_coup(etat['id'], typeCoup, (x, y))
       # print(etat)
     #print(d, x, y)
