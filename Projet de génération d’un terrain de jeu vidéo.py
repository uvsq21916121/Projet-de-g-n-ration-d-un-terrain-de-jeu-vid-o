#IN200: projet de génération d’un terrain de jeu vidéo

##################################################################################

#Stalin SIVASANGAR 21916121
#Ali GOUMANE
#Elive DIPOKO
#Marie PHILIBERT
#Pierre RATCLIFFE
#MPCI TD5
#https://github.com/uvsq21916121/Projet_de_generation_de_terrain_de_jeu_video.git

##################################################################################
# Import des modules

import tkinter as tk
import random as rd


##################################################################################
# constantes du programme

Largeur = 1000
Hauteur = 1000
COTE = 20
Nombre_de_colonne = Largeur // COTE
Nombre_de_ligne = Hauteur // COTE
a = 1
 




####################################################################################
# Les valeurs pour les paramètres de l’automate

p=0.5
n=4
T=5
k=1

##################################################################################
# Fonctions

def liste ():
    "Crée une grille de 60*60"
    l = list(range(50))
    for i in l :
        l[i]=list(range(50))
        for j in range (50) :
            l[i][j]=0
    return l 


def proba(p) :
    for j in range(50):
        for i in range(50):
            global x 
            x = rd.randint(0,10)
            if x <= (p*10 ):
                etat[i][j]=Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="blue")
                etat[i][j]=1
            else :
               etat[i][j]=Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="saddlebrown")
               etat[i][j]=0


def terrain_de_jeu():

    proba(p)

    "Dessine un quadrillage formé de carrés de côté COTE"
    x = 0
    while x <= Largeur:
        Canvas.create_line(x, 0, x, Hauteur, fill="white")
        x += COTE

    y = 0
    while y <= Hauteur:
        Canvas.create_line(0, y, Largeur, y, fill="white")
        y += COTE


            

def xy_to_ij(x, y):
    "Renvoie les coordonnées de la case du tableau correspondant au pixel de coordonnées (x, y)"
    return x // COTE, y // COTE


def personnage (event):
    "crée un personnage sur une zone de terre a l'aide d'un clic"
    global perso, a
    if a:
        i, j = xy_to_ij(event.x, event.y)
        if  etat[i][j]==0:
            #si la case est de la terre
            etat[i][j] = 2
            x, y = i * COTE, j * COTE
            perso = Canvas.create_rectangle((x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")  
            a = 1 - a
    else :
        i, j = xy_to_ij(event.x, event.y)
        if  etat[i][j]==2:
            etat[i][j] = 0
            Canvas.delete(perso)
            a = 1 - a


def deplacement(event):
    global perso
    touche = event.keysym
    i, j = xy_to_ij(event.x, event.y)
    x, y = i*COTE ,j*COTE
    if etat[i][j]==0:
        if touche == "Up" :
            #déplacement vers le haut
            y -= COTE
            Canvas.move(perso, 0, y)
            
        if touche == "Down" :
            #déplacement vers le bas
            y += COTE
            Canvas.coords(perso,(x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
            Canvas.delete(perso)
        if touche == "d" :
            x += COTE
            Canvas.coords(perso,(x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
            Canvas.delete(perso)
            #déplacement vers la droite
        if touche =="g" :
            #déplacement vers la gauche
            x -= COTE
            Canvas.coords(perso,(x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
            Canvas.delete(perso)






def cel_eau (i,j):
    "Convertit une cellule en case d'eau"
    l[i][j] = 1
    Canvas.delete(etat[i][j])
    Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="blue")

def cel_terre(i,j):
    "Convertit une cellule en case de terre"
    l[i][j] = 0
    Canvas.delete(etat[i][j])
    Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="brown")



def genere_terrain():
    "Redessine un nouveau terrain a partir de la liste c"
    for i in range (len(l)):
        for j in range (len(l[i])):
            if l[i][j]==0 and c[i][j]==3:
                cel_eau(i,j)
            elif (l[i][j]==1 and c[i][j]<2) or (l[i][j]==1 and c[i][j]>3):
                cel_terre(i,j)





def sauvegarder():

    """Sauvegarde le tableau dans le fichier sauvegarde.txt"""

    fic = open("sauvegarde.txt", "w")

    for i in range(Nombre_de_colonne):

        for j in range(Nombre_de_ligne):

            fic.write(str(etat[i][j]) + "\n")

    fic.close()

        




        



##################################################################################
# Programme principal

# Création de la fenêtre principale 
fen_princ = tk.Tk()
fen_princ.title("Projet de génération d’un terrain de jeu vidéo")
Canvas = tk.Canvas(fen_princ, width= Largeur, height= Hauteur, bg='black')
Canvas.bind("<Button-1>",personnage)
Canvas.bind('<Key>',deplacement)
Canvas.grid()


etat=liste()#memorise toute les cellules
l=liste() #memorise l'etat de toutes les cellules
c=liste() #memorise le nombre de case d'eau autour d'une case d'eau


# Création des boutons
bouton_de_sauvegarde = tk.Button(fen_princ, text="Sauvegarder", command=sauvegarder)

# Position des boutons
bouton_de_sauvegarde.grid(column=1, row=0)


liste()
terrain_de_jeu()



fen_princ.mainloop()
