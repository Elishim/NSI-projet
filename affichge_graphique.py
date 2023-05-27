'''
E F 1A
Projet NSI
TSP
'''

import matplotlib.pyplot as plt

Liste_test=[('Tokyo',1,2),('Paris',4,6),('New-York',9,-3),('Malaga',6,-8)]

def plotting_ville(Liste):
    '''
    Parametre : Un liste de tuples sous la forme : (Nom de la ville , X , Y )
    exemple de liste : [('Tokyo',1,2),('Paris',4,6),('New-York',9,-3),('Malaga',6,-8)]
    Renvoie : None , affiche dans un plan les villes via la bibliotheque matplotlib .
    '''
    Liste.append(Liste[0])
    for i in range(len(Liste)-1):
        plt.scatter(Liste[i][1],Liste[i][2], color='black')
        plt.text(Liste[i][1],Liste[i][2],Liste[i][0], color='black', fontsize=12)
        plt.plot([Liste[i][1],Liste[i+1][1]],[Liste[i][2],Liste[i+1][2]], color='blue')
    plt.title("Carte des villes")
    plt.show()
    return None

plotting_ville(Liste_test)
