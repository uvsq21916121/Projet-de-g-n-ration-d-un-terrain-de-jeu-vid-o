IN200: projet de génération d’un terrain de jeu vidéo

#######################################################

#Stalin SIVASANGAR 21916121

#Ali GOUMANE

#Elive DIPOKO

#Marie PHILIBERT

#Pierre RATCLIFFE

#MPCI TD5
# https://github.com/uvsq21916121/Projet_de_generation_de_terrain_de_jeu_video.git

######################################################

Les terrains de jeu sont des composants importants de plusieurs types de jeux vidéos.

 Nous avons mis tous les explications pour les fonctions et programme principal dans le programme.



Appuyer sur le bouton Nouveau Terrain permet de generer un  nouveau terrain
il ne peut y avoir qu'un seul personnage sur le terrain un clic sur le personnage permet l'utlisateur de l'effacer et de repositionner son personnage sur le terrain
les touches de direction permet de deplacer le personnage sur le terrain(fontion qui bug) 
la touche sauvegarder permet de sauvegarder son terrain avec ou sans personnage s'il avait été sauvegarder avec ou sans personnage 



les fonctions
1.-les fonctions associées au terrain
terrain_de_jeu() : permet de d'effacer le terrain s'il en avait deja un et de creer un espace vide 
proba(p) : Attribue une valeur a chaque case en fontion de la probabilité p et lui tribute une valeur 0 si c'est une case d'eau et la valeur 1 si c'est une cause de terre
Moore(n, k) : en faisant a appel a la fonction change_var pour chaque cellule la liste cell_eau cette fonction va affecter la valeur 0 si cette cellule contient de l'eau et crée une cellule d'eau et dans le cas contaire affecte la valeur 1 et crée une cellule de terre
change_var(i,j,k) : converti en cellule d'eau ou de terre en fonction du voisinage
si les valeurs minimales de ses coordonnées  sont inferieures a 0 elle lui affecte la valeur 0 et si les valeurs maximales de ses coordonnées sont superieures a la valeur de la cellule lui attribue la valeur de la cellule ainsi le nombre de voisin est superieur a T la cellule est convertie en ou reste une cellule d'eau si cette valeur est inferieure la cellule est convertie en ou reste une
nouveau_terrain() : fonction qui crée un espace vide et crée un nouvau terrain a partir des automates cellules sans personnage

2.- les fonctions associées au personnage
def personnage(event):cette fonction crée a l'aide d'un click sur le canvas un personnage si le click se fait sur une cellule de terre et ne cree rien si le click s'est fait sur une cellule d'eau

def deplacement(event): devrait deplacer le personnage sur les cellules de terre a l'aide des fleches de direction sur le clavier





Pour le projet nous avons été que 2 a le faire
ils nous a été tres difficile de trouver les réponses seuls


