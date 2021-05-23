import tkinter as tk
import random as rd



def xy_to_ij(x, y):
    "Retourne les coordonnées de la case du tableau correspondant au pixel de coordonnées (x, y)"""
    return x // COTE, y // COTE


def personnage (event):
    "crée un personnage sur une zone de terre a l'aide d'un clic"
    i, j = xy_to_ij(event.x, event.y)
    if  etat[i][j]==0:
        #si la case est de la terre
        x, y = i * COTE, j * COTE
        carre = canvas.create_rectangle((x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
        tableau[i][j] = carre
    