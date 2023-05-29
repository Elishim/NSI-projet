import math as m
import matplotlib.pyplot as plt

MAX_NB_VILLES = 80

'''
Petit fichier test fait par mes soins :

26

a 1 1
b 6 8
c -3 -2
d 2 -4
e 4 3
f 8 10
g -3 -3
h -5 5
i -1 7
j 0 0
k 1 9
l 1 -7
m 3 0
n 1 2
o 4 4
p -6 6
q -2 7
r 1 -8
s -2 8
t 3 -1
u -4 1
v 1 -5
w 9 2
x -4 -9
y -8 8
z 8 -8


'''


def litEntree():
    """
    lit le nombre de villes, leur nom et leurs coordonnées
    renvoie le nombre des villes, le tableau de leur coordonnées, un tableau avec les noms des villes, un tableau contenant les distances entre toutes les paires de villes
    """

    dist = [[0 for _ in range(MAX_NB_VILLES)] for _ in range(MAX_NB_VILLES)]
    coord = [[0 for i in range(2)] for _ in range(MAX_NB_VILLES)]
    noms = ["" for _ in range(MAX_NB_VILLES)]

    nbV = int(input("Entrez le nombre de villes : "))
    print("Entrez les noms des villes puis leurs coordonnées (entières, dans le plan) dans l'ordre:\n")
    for i in range(nbV):
        ligne = list(input().split())
        noms[i] =ligne[0]
        coord[i][0] = int(ligne[1])
        coord[i][1] = int(ligne[2])
    
    #précalcule les distances entre les paires de villes
    for i in range(MAX_NB_VILLES):
        for j in range(MAX_NB_VILLES):
            dist[i][j] = m.sqrt((coord[i][0] - coord[j][0])**2 + (coord[j][1] - coord[i][1])**2)
    return nbV, coord, noms, dist

def glouton(nbV, coord, dist):
    """
    construit un ordre des villes avec un algorithme glouton
    renvoie un tuple : un tableau d'entiers (l'ordre des villes sur le chemin) et la distance totale
    """

    tot = 0 #distance totale
    chem = [-1 for _ in range(nbV)]
    chem[0] = 0
    pris = [False for _ in range(nbV)]
    pris[0] = True
    for idV in range(1, nbV):
        prec = chem[idV-1]
        mini = 1000000000
        num = -1
        for prochain in range(nbV):         #trouve la ville la plus proche pas encore choisie
            if (not pris[prochain]):
                if (dist[prec][prochain] < mini):
                    mini = dist[prec][prochain]
                    num = prochain
        pris[num] = True
        chem[idV] = num
        tot += mini
    tot += dist[chem[nbV-1]][chem[0]]
    return chem, tot

def plotting_ville(Liste, dist):
    '''
    Parametre : Un liste de tuples sous la forme : (Nom de la ville , X , Y ) avec x et y des floats et le Nom de la ville un str 
    exemple de liste : [('Tokyo',1,2),('Paris',4,6),('New-York',9,-3),('Malaga',6,-8)]
    Renvoie : None , crée un graphique reliant les villes via la bibliotheque matplotlib .
    '''
    Liste.append(Liste[0])
    for i in range(len(Liste)-1):
        plt.scatter(Liste[i][1],Liste[i][2], color='black')
        plt.text(Liste[i][1],Liste[i][2],Liste[i][0], color='black', fontsize=12)
        plt.plot([Liste[i][1],Liste[i+1][1]],[Liste[i][2],Liste[i+1][2]], color='blue')
    plt.title("Ce chemin reliant toutes les villes mesure " + str(round(dist,3)) + " km.")
    plt.show()
    plt.savefig("algo_glouton")
    return None

def afficheRes(res, noms,coord):
    """
    prend en paramètre un tuple contenant l'ordre des villes et la distace totale, le tableau de noms des villes et le tableau des coordonnées des villes
    affiche le résultat de l'algorithme
    ne renvoie rien
    """
    dist = res[1]
    ordre = res[0]
    itineraire = []
    for elem in ordre:
        itineraire.append((noms[elem], coord[elem][0],coord[elem][1]))
    plotting_ville(itineraire, dist)
    return None

        
def main():
    """
    fonction principale, ne prend pas de paramètre et ne renvoie rien
    """
    nbV, coord, noms, dist = litEntree()
    res = glouton(nbV, coord, dist)
    afficheRes(res,noms,coord)
    return None


main()
