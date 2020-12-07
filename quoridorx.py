'''MODULE QUORIDORX'''
import turtle
import quoridor


class QuoridorX(quoridor.Quoridor):
    '''QuoridorX'''
    HEIGHT = 768
    WIDTH = 1024
    INTERCASEH = 20
    INTERCASEV = 20
    TCASE = 50
    OPLATEAU = (50, 50)

    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs)
        self.fen = turtle.Screen()
        self.fen.title("Quoridor Phase 3")
        self.fen.setup(QuoridorX.WIDTH, QuoridorX.HEIGHT)
        self.tortue = turtle.Turtle()
        self.dans_loop = False
        self.floop = None
        self.couleurcase = 'blue'

    def _home(self):
        self._goto_xy((0, 0))

    def _goto_xy(self, pos):
        x, y = pos
        xorigine, yorigine = -QuoridorX.WIDTH//2, QuoridorX.HEIGHT//2
        self.tortue.goto(xorigine + x, yorigine - y)
        return self

    def _afficher_murh(self, pos):
        x, y = pos
        epaisseur_mur = 10
        ox, oy = self.OPLATEAU
        x = ox + (self.TCASE + QuoridorX.INTERCASEH)*(x -1)
        y = oy + (self.TCASE + QuoridorX.INTERCASEV)*(10 - y) + \
            (epaisseur_mur // 2) - QuoridorX.INTERCASEV
        self.tortue.penup()
        self.tortue.color('brown', 'brown')
        self._goto_xy((x, y))
        self.tortue.pendown()
        self.tortue.begin_fill()
        for _ in range(2):
            self.tortue.fd(self.TCASE*2 + QuoridorX.INTERCASEH)
            self.tortue.rt(90)
            self.tortue.fd(epaisseur_mur)
            self.tortue.rt(90)
        self.tortue.end_fill()
        self.tortue.penup()

    def _afficher_murv(self, pos):
        x, y = pos
        epaisseur_mur = 10
        ox, oy = self.OPLATEAU
        x = ox + (self.TCASE + QuoridorX.INTERCASEH)*(x -1)  + \
            (epaisseur_mur // 2) - QuoridorX.INTERCASEH
        y = oy + (self.TCASE + QuoridorX.INTERCASEV)*(8 - y)
        self.tortue.penup()
        self.tortue.color('brown', 'brown')
        self._goto_xy((x, y))
        self.tortue.pendown()
        self.tortue.begin_fill()
        for _ in range(2):
            self.tortue.fd(epaisseur_mur)
            self.tortue.rt(90)
            self.tortue.fd(self.TCASE*2 + QuoridorX.INTERCASEV)
            self.tortue.rt(90)
        self.tortue.end_fill()
        self.tortue.penup()

    def _afficher_jeton(self, args):
        x, y, couleur = args
        rayon = 15
        ox, oy = self.OPLATEAU
        x = ox + (self.TCASE + QuoridorX.INTERCASEH)*(x -1) + self.TCASE // 2
        y = oy + (self.TCASE + QuoridorX.INTERCASEV)*(9 - y) + rayon + self.TCASE // 2
        self.tortue.penup()
        self.tortue.color('black', couleur)
        self._goto_xy((x, y))
        self.tortue.pendown()
        self.tortue.begin_fill()
        self.tortue.circle(rayon)
        self.tortue.end_fill()
        self.tortue.penup()

    def _afficher_cadre(self, pos, taille, ccadre):
        x, y = pos
        self.tortue.penup()
        self.tortue.pencolor(ccadre)
        self._goto_xy((x, y))
        self.tortue.pendown()
        for _ in range(4):
            self.tortue.fd(taille)
            self.tortue.rt(90)
        self.tortue.penup()

    def _afficher_case(self, pos, taille, couleurs):
        cfond, ccadre = couleurs
        self.tortue.color(ccadre, cfond)
        self.tortue.pendown()
        self.tortue.begin_fill()
        self._afficher_cadre(pos, taille, ccadre)
        self.tortue.end_fill()
        self.tortue.penup()

    def _afficher_plateau(self, taille, tcase, couleur):
        nbrcaseh, nbrcasev = taille
        ox, oy = self.OPLATEAU
        for lignes in range(nbrcaseh):
            for col in range(nbrcasev):
                self._afficher_case((ox + (tcase + QuoridorX.INTERCASEH)*col, oy + \
                    (tcase + QuoridorX.INTERCASEV)*lignes), tcase, (couleur, 'black'))

    def afficher(self):
        '''AFFICHER'''
        self.fen.clearscreen()
        self.tortue.ht()
        self.couleurcase = 'blue'
        self.fen.tracer(0, 0)
        self._afficher_plateau((9, 9), self.TCASE, self.couleurcase)
        x, y = self.etatpartie['joueurs'][0]['pos']
        self._afficher_jeton((x, y, 'yellow'))
        x, y = self.etatpartie['joueurs'][1]['pos']
        self._afficher_jeton((x, y, 'red'))
        for mur in self.etatpartie['murs']['horizontaux']:
            self._afficher_murh(mur)
        for mur in self.etatpartie['murs']['verticaux']:
            self._afficher_murv(mur)
        self.tortue.color('black', 'white')
        self._goto_xy((700, 100))
        ch = self.etatpartie['joueurs'][1]['nom'] + ': '
        self.tortue.pendown()
        self.tortue.write(ch, font=(x, 40))
        self.tortue.penup()
        ch = str(self.etatpartie['joueurs'][1]['murs']) + ' murs.'
        self._goto_xy((700, 150))
        self.tortue.pendown()
        self.tortue.write(ch, font=(x, 40))
        self.tortue.penup()
        self._goto_xy((700, 600))
        ch = self.etatpartie['joueurs'][0]['nom'] + ': '
        self.tortue.pendown()
        self.tortue.write(ch, font=(x, 40))
        self.tortue.penup()
        self._goto_xy((700, 650))
        ch = str(self.etatpartie['joueurs'][0]['murs']) + ' murs.'
        self.tortue.pendown()
        self.tortue.write(ch, font=(x, 40))
        self.tortue.penup()
        self.fen.update()
        self.fen.ontimer(self.floop, 100)
        turtle.done()
