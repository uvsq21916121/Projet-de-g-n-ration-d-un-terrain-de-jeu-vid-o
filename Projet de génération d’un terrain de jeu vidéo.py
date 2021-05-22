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
import random

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
            x = random.random()
            if x <= p :
                Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="blue")
            else :
                Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="brown")



##################################################################################
# Programme principal

# Création de la fenêtre principale 
fen_princ = tk.Tk()
fen_princ.title("Projet de génération d’un terrain de jeu vidéo")
Canvas = tk.Canvas(fen_princ, width= Largeur, height= Hauteur, bg='black')
Canvas.grid()

Quadrillage()

proba(p)





fen_princ.mainloop()
