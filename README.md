# NSI-projet-TSP

Nous avons décidé d’écrire un programme qui résout le problème du voyageur de commerce, ou qui en donne en tout cas une solution rapidement.
On va faire plusieurs programmes (3 ou 4) qui utilisent des approches différentes afin de les comparer. Chaque programme devra lire en entrée le nombre de villes (pas plus de 100 ou 200) puis les coordonnées ces villes et leurs noms. Il devra ensuite afficher en sortie un cycle passant par toutes les villes, dont la longueur totale doit être la plus faible possible. Le programme affichera aussi un graphique, représentant dans le plan ce cycle et les villes avec leur nom.

On vous renverra aussi un programme qui permet de générer des exemples aléatoires en écrivant dans un fichier, et les fichiers tests qu’on a utilisés pour tester nos programmes. ( Les fichiers testes seront des fichiers CSV ? )

Voici les différents algorithmes qu’on essaiera d’utiliser :
- Un algorithme bourrin qui essaie tous les cycles possibles (s’il y a au plus 10 villes) en parcourant tous les cycles en calculant la distance totale pour chaque cycle
- Un algorithme glouton qui construit une solution au fur et à mesure en minimisant à chaque étape la longueur totale : on part d’une ville, et on ajoute la ville la plus proche parmi les villes restantes tant qu’il reste des villes à visiter
- Un algorithme qui part d’un cycle et le change légèrement (par exemple en échangeant deux villes, ou en retournant une partie du chemin) si ça diminue la distance totale, et ce tant que c’est possible
- Un algorithme qui part aussi d’un cycle, mais essaie cette fois toutes les façons possibles d’échanger deux villes, et retient celle qui minimise la distance totale pour se diriger vers elle, puis qui recommence tant que la longueur du chemin diminue

et une ou deux autres méthodes si on arrive.

On essaiera aussi de faire un programme affichant un graphique comparant les résultats des différents programmes, à partir de fichiers contenant ces résultats.

