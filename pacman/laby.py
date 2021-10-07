from numpy.random import randint
import matplotlib.pyplot as plt
import copy
from TAD import Pile, File


class Labyrinthe :
    '''Labyrinthe de dimension l,h
    parametres -> l, h : largeur, hauteur du labyrinthe
    '''
    def __init__(self, l, h) :
        self.__table = self.__constructeur_table({'N': None, 'S': None, 'E': None, 'O': None}, (l,h))
    
    def __constructeur_table(self, val, dim) :
        ''' Createur d'un dictionnaire ayant pour cle chaque case du labyrinthe. La valeur est entrée en parametre
        val : valeur à affecter à chaque nom de cellule
        dim : dimension du labyrinthe (tuple (l,h))
        retour : dictionnaire
        '''
        table = {}
        l, h = dim    
        for i in range(l) :
            for j in range(h) :
                if type(val) == type({}) or type(val) == type([]) or type(val) == type(()) :
                    table[self.__nom(i,j)] = copy.deepcopy(val)
                else :
                    table[self.__nom(i,j)] = val
        return table
    
    def lire_graphe(self) :
        '''accesseur à la liste des successeurs'''
        return self.__table
    
    def __nom(self, i,j) :
        '''Convertir les coordonnées i,j en str
        Exemple : self.__nom(3,2) retourne '3_2'
        '''
        return str(i)+'_'+str(j)

    def __taille(self) :
        ''' Retourne la dimension du labyrinthe'''
        l,h = 0,0
        for elem in self.__table.keys() :
            elem = elem.split('_')
            if int(elem[0]) > l : l = int(elem[0])
            if int(elem[1]) > h : h = int(elem[1])
        return (l+1,h+1)

    def creer(self) :
        '''Creation d'un labyrinthe parfait'''
        etat = {}
        pile = Pile()

        l, h = self.__taille()
        etat = self.__constructeur_table(False,(l,h))

        i, j = randint(l), randint(h)
        pile.empile((i,j))
        etat[self.__nom(i,j)] = True
        while not pile.vide() :
            i, j = pile.depile()
            # Recherche des cases voisines disponibles
            voisins = []
            if j < h-1 and not etat[self.__nom(i,j+1)] :
                voisins.append('N')
            if i > 0 and not etat[self.__nom(i-1,j)] :
                voisins.append('O')
            if j > 0 and not etat[self.__nom(i,j-1)] :
                voisins.append('S')
            if i < l-1 and not etat[self.__nom(i+1,j)] :
                voisins.append('E')
            if len(voisins) > 1 :
                pile.empile((i,j))
            if len(voisins) > 0 :
                direction = voisins[randint(len(voisins))]
                if direction == 'N':
                    self.__table[self.__nom(i,j)]['N'] = self.__nom(i,j+1)
                    self.__table[self.__nom(i,j+1)]['S'] = self.__nom(i,j)
                    etat[self.__nom(i,j+1)] = True
                    pile.empile((i,j+1))
                elif direction == 'O':
                    self.__table[self.__nom(i,j)]['O'] = self.__nom(i-1,j)
                    self.__table[self.__nom(i-1,j)]['E'] = self.__nom(i,j)
                    etat[self.__nom(i-1,j)] = True
                    pile.empile((i-1,j))
                elif direction == 'S':
                    self.__table[self.__nom(i,j)]['S'] = self.__nom(i,j-1)
                    self.__table[self.__nom(i,j-1)]['N'] = self.__nom(i,j)
                    etat[self.__nom(i,j-1)] = True
                    pile.empile((i,j-1))
                elif direction == 'E':
                    self.__table[self.__nom(i,j)]['E'] = self.__nom(i+1,j)
                    self.__table[self.__nom(i+1,j)]['O'] = self.__nom(i,j)
                    etat[self.__nom(i+1,j)] = True
                    pile.empile((i+1,j))
                else : raise IndexError('index orientation inconnu')
        
        return 

    def afficher(self):
        '''Affiche le labyrinthe'''      
        l,h = self.__taille()
        plt.plot([0, 0, l, l, 0], [0, h, h, 0, 0], linewidth=2)
        for i in range(l-1):
            for j in range(h):
                if self.__table[self.__nom(i,j)]['E'] == None:
                    plt.plot([i+1, i+1], [j, j+1], 'b')
        for j in range(h-1):
            for i in range(l):
                if self.__table[self.__nom(i,j)]['N'] == None:
                    plt.plot([i, i+1], [j+1, j+1], 'b')
        plt.axis([-1, l+1, -1, h+1])
        plt.show()
    
  
