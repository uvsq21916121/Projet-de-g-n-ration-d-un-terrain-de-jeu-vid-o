#IN200: projet de génération d’un terrain de jeu vidéo

##################################################################################

#Stalin SIVASANGAR 21916121
#Ali GOUMANE
#Elive DIPOKO
#Marie PHILIBERT 22004191
#Pierre RATCLIFFE
#MPCI TD5
#https://github.com/uvsq21916121/Projet_de_generation_de_terrain_de_jeu_video.git

##################################################################################
# Importation des bibliothèques

import tkinter as tk
import random as rd


##################################################################################
# constantes du programme

Largeur = 800
Hauteur = 800
COTE=20
cellule=50 
Largeur_de_cellule = Largeur // cellule
hauteur_de_cellule = Hauteur // cellule
Nombre_de_colonne = Hauteur // COTE
Nombre_de_ligne = Largeur // COTE

a = 1
perso = 1

####################################################################################
#les listes
etat=[] #memorise toute les cellules
cell_eau=[] #memorise le nombre de case d'eau autour d'une case d'eau
terrain = [] #memorise le nouvel état du terrain et permet la sauvegarde




####################################################################################
# Les valeurs pour les paramètres de l’automate

p=0.5
n=4
T=5
k=1

##################################################################################
# Fonctions


##Associés a la generation du terrain
def terrain_de_jeu():
    global etat ,Largeur_de_cellule,hauteur_de_cellule,Largeur,Hauteur
    Largeur_de_cellule = Largeur // cellule
    hauteur_de_cellule = Hauteur // cellule
    if (len(etat))!=0:
        del etat[:]
        Canvas.delete("all")
    etat=[cellule*[0]for i in range(cellule)]




def proba(p) :
    "Attribue une valeur a chaque type de cellule et les affiche dans la grille"
    for j in range(cellule):
        for i in range(cellule):
            global r 
            r = rd.randint(0,10)
            if r <= (p*10):
                etat[i][j]=0
                etat[i][j]=Canvas.create_rectangle(i*20+1, j*20+1, i*20 +20, j*20+20, fill="blue")
                
            else :
                etat[i][j]=1
                etat[i][j]=Canvas.create_rectangle(i*20+1, j*20+1, i*20 +20, j*20+20, fill="saddlebrown")
               



def Moore(n, k):
    "Nombre de fois ou l'automate sera repetée"
    for r in range(n):
        cell_eau
        for i in range(cellule):
            for j in range(cellule):
                change_var(i,j,k)
            x = 0
            for i in range(cellule):
                for j in range(cellule):
                    if cell_eau[x]==0:
                        etat[i][j] = 0
                        etat[i][j]=Canvas.create_rectangle(i*20+1, j*20+1, i*20 +20, j*20+20, fill="blue")
                    else:
                        etat[i][j]=1
                        etat[i][j]=Canvas.create_rectangle(i*20, j*20, i*20 +20, j*20+20, fill="saddlebrown")
                        x+=1
            del cell_eau[:]



def change_var(i,j,k):
    "converti les cellules en eau ou en terre par rapport au voisinage"
    case_eau =0
    cxh,cxb = x+k,x-k
    cyb , cyh =  y- k, y + k
    if cxb < 0:
        cxb = 0
    if cyb < 0 :
        cyb = 0
    if cxh > cellule  :
        cxh = cellule
    if cyh > cellule :
        cyh =cellule


    for i in range(cyb-1,cyh,1):
        for j in range (cxb-1,cxh,1):
            if i!=x and j!=y:
                if etat[i][j]==0:
                    case_eau+=1
    if case_eau >=T:
        cell_eau.append(0)
    else:
        cell_eau.append(1)

def nouveau_terrain():
    global perso
    terrain_de_jeu()
    proba(p)
    Moore(n,k)
    Canvas.delete(perso)
    perso = 1


                        






            
#Associées au personnage
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
        if  etat[i][j]==0:
            etat[i][j] = 0
            Canvas.delete()
            a = 1 - a


#def deplacement(event):
    #global perso
    #touche = event.keysym
    #i, j = xy_to_ij(event.x, event.y)
    #x, y = i*COTE ,j*COTE
    #if etat[i][j]==0:
        #if touche == "Up" :
            #déplacement vers le haut
            #y -= COTE
            #Canvas.move(perso, 0, y)
            
        #if touche == "Down" :
            #déplacement vers le bas
            #y += COTE
            #Canvas.coords(perso,(x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
            #Canvas.delete(perso)
        #if touche == "d" :
            #x += COTE
            #Canvas.coords(perso,(x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
            #Canvas.delete(perso)
            #déplacement vers la droite
        #if touche =="g" :
            #déplacement vers la gauche
            #x -= COTE
            #Canvas.coords(perso,(x, y), (x+COTE, y+COTE), fill="cyan", outline="green2")
            #Canvas.delete(perso)








#Sauvegarde

def sauvegarder():

    """Sauvegarde le tableau dans le fichier sauvegarde.txt"""

    fic = open("sauvegarde.txt", "w")

    for i in range(Nombre_de_colonne):

        for j in range(Nombre_de_ligne):

            fic.write(str(etat[i][j]) + "\n")

    fic.close()

##################################################################################
# Création du menu 
def creation_menu():
    "Crée un menu permettant de changer les parametres du terrain"
    global valT, valn, valk, valp, valn,cel 
    label1 = tk.Label(Choisir ,text = "p = ")
    valp = tk.Spinbox(Choisir ,from_= 0.1 , to = 1.0 ,increment=0.1, wrap=True  , command = choix_p)
    label1.grid(row = 0 , column = 0 )
    valp.grid(row = 0, column = 1 , columnspan= 2)  
    label2 = tk.Label(Choisir ,text = "T =")
    valT = tk.Spinbox(Choisir, from_=1 , to = 50 ,increment=1 , command = choix_T)
    label2.grid(row = 1 , column=0 , columnspan=2)
    valT.grid(row = 1 , column = 1 , columnspan = 2) 
    label3 = tk.Label(Choisir,text = " k = ")
    valk = tk.Spinbox(Choisir, from_ = 1, to = 10 , increment=1 , command = choix_k)
    label3.grid(row = 2 , column = 0 , columnspan= 2)
    valk.grid(row = 2 , column = 1 , columnspan=2)
    label4 = tk.Label(Choisir, text = "n = ") 
    valn = tk.Spinbox (Choisir, from_ = 1 ,to = 10 , increment= 1 , command = choix_n )
    label4.grid(row = 3 , column = 0 )
    valn.grid(row = 3 , column = 1 , columnspan =  2)
    label5 = tk.Label(Choisir, text= "Nombre de cellules = ")
    cel = tk.Spinbox( Choisir,from_ = 10, to = 100, increment= 10, command = choix_cel)
    label5.grid(row=4, column=0)
    cel.grid(row = 4 , column = 1 , columspan = 2 )


#Fonctions associés aux menus
def choix_p ():
    global p 
    p = float(valp.get())

def choix_T():
    global T
    T = int(valT.get())

def choix_k ():
    global k
    k = int(valk.get())

def choix_n():
    global n 
    n = int(valn.get())

def choix_cel():
    global choix_cel
    choix_cel = int(cel.get())



        



##################################################################################
# Programme principal

# Création de la fenêtre principale 
fen_princ = tk.Tk()
fen_princ.title("Projet de génération d’un terrain de jeu vidéo")
Canvas = tk.Canvas(fen_princ, width= Largeur, height= Hauteur, bg='black')
Choisir = tk.Canvas(fen_princ, bg="white", width=Largeur, height=Hauteur)
Choisir.grid(row=0, column=0)
Canvas.bind("<Button-1>",personnage)
#Canvas.bind('<Key>',deplacement)
Canvas.grid()





# Création des boutons
bouton_de_sauvegarde = tk.Button(fen_princ, text="Sauvegarder", command=sauvegarder)
bouton_generer_terrain = tk.Button(fen_princ, text="Nouveau Terrain",command=nouveau_terrain)
bouton_de_sauvegarde.grid(column=1, row=0)
bouton_generer_terrain.grid(column=2, row=0)





#Autres Fonctions
creation_menu()
terrain_de_jeu()
proba(p)

fen_princ.mainloop()
