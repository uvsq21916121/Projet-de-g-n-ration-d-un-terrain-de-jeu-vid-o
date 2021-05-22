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




def Quadrillage():
    "Dessine un quadrillage formé de carrés de côté COTE"
    x = 0
    while x <= Largeur:
        Canvas.create_line(x, 0, x, Hauteur, fill="white")
        x += COTE

    y = 0
    while y <= Hauteur:
        Canvas.create_line(0, y, Largeur, y, fill="white")
        y += COTE

def proba(p) :
    for j in range(50):
        for i in range(50):
            global x 
            x = rd.randint(0,10)
            if x <= (p*10 ):
                etat[i][j]=Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="blue")
                etat[i][j]=1
            else :
               etat[i][j]=Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="brown")
               etat[i][j]=0
            

def xy_to_ij(x, y):
    "Renvoie les coordonnées de la case du tableau correspondant au pixel de coordonnées (x, y)"
    return x // COTE, y // COTE


def personnage (event):
    "crée un personnage sur une zone de terre a l'aide d'un clic"
    i, j = xy_to_ij(event.x, event.y)
    if  etat[i][j]==0:
        #si la case est de la terre
        x, y = i * COTE, j * COTE
        Canvas.create_rectangle((x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
        



##################################################################################
# Programme principal

# Création de la fenêtre principale 
fen_princ = tk.Tk()
fen_princ.title("Projet de génération d’un terrain de jeu vidéo")
Canvas = tk.Canvas(fen_princ, width= Largeur, height= Hauteur, bg='black')
Canvas.bind("<Button-1>",personnage)
Canvas.grid()
etat=liste()#memorise toute les cellules
l=liste() #memorise le nouvel etat des cellules
c=liste() #memorise le nombre de case d'eau autour d'une case d'eau


proba(p)
liste()
Quadrillage()



fen_princ.mainloop()
