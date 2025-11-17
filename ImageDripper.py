# Importation des modules nécessaires
import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import random
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller crée un dossier temporaire et y stocke le chemin dans _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Initialisation de la fenêtre principale
fen = tk.Tk()
fen.geometry("1200x700") # Définit la taille de la fenêtre
fen.title("ImageDripper") # Définit le titre de la fenêtre
fen.iconbitmap(resource_path("ImageDripper.ico")) # Définit l'icon de la fenêtre
fen.resizable(False,False) # Empêche le redimensionnement de la fenêtre

# Définition des couleurs et de la police
fond = "#171d26"
fond2 = "#333d4f"
texte = "#edeff5"
boutton = "#475a6b"
bouttonsurvol = "#576c82"

fontperso=("Roboto", 20, "bold")

fen.configure(background=fond, padx=10, pady=10) # Configure le fond et les paddings (écart de remplissage)

# Création des canvas pour les fonds d'image et de boutons
imageback = Canvas(fen, width=1000, height=500, background=boutton, highlightthickness=0)
imageback.place(x=150, y=60) # Positionnement du canvas d'image

buttonback = Canvas(fen, width=400, height=500, background=fond2, highlightthickness=0)
buttonback.place(x=750, y=60) # Positionnement du canvas d'image

# Variable pour le type de chemin d'image sélectionné
chemin = 1

# Fonctions pour modifier le type de chemin d'image sélectionné
def selectionchemin(value):
    global chemin
    chemin = value

# Fonctions pour prédéfinir le chemin (pour les presets et l'importation)
def preset1chemin(*args): selectionchemin(2)
def preset2chemin(*args): selectionchemin(1)
def preset3chemin(*args): selectionchemin(3)
def importerchemin(*args): selectionchemin(4)

# Variables globales pour les images importées et les presets
imageimporter, preset1_image, preset2_image, preset3_image = None, None, None, None

label_image = tk.Label(fen, border=0, background=fond)
label_image.place(x=150, y=60)

# Fonction pour importer une image
def importerimage():
    # Vérifie la valeur de la variable 'chemin' pour déterminer l'action à effectuer
    if chemin == 4:
        # Définit les types de fichiers que l'utilisateur peut choisir (JPG, PNG, ou tout autre fichier)
        extensionsimage = [("JPG", "*.jpg"),("PNG","*.png"),("Tous","*")]
        # Ouvre une boîte de dialogue permettant à l'utilisateur de sélectionner un fichier, avec les extensions spécifiées
        nomimage = filedialog.askopenfilename(filetypes=extensionsimage)
        if nomimage:  # Vérifie si un fichier a été sélectionné
            global imageimporter  # Utilise la variable globale 'imageimporter'
            imageimporter = Image.open(nomimage)  # Ouvre l'image sélectionnée
            imageimporter11 = imageimporter.resize((600,500))  # Redimensionne l'image pour qu'elle s'adapte à l'interface
            imageimporter11 = ImageTk.PhotoImage(imageimporter11)  # Convertit l'image pour qu'elle puisse être utilisée dans Tkinter
            label_image.configure(image=imageimporter11) # Permet de changer la configuration de label_image pour rajouter une image dans celui-ci
            label_image.image = imageimporter11  # Garde une référence de l'image pour éviter son effacement par le garbage collector
    if chemin == 1:
        global preset1_image  # Utilise la variable globale 'preset1_image'
        preset1_image = Image.open(resource_path("./Presets/Preset1.png"))  # Ouvre l'image du preset 1
        preset11_image = preset1_image.resize((600,500))  # Redimensionne cette image
        preset11_image = ImageTk.PhotoImage(preset11_image)  # Convertit pour Tkinter
        label_image.configure(image=preset11_image) # Permet de changer la configuration de label_image pour rajouter une image dans celui-ci
        label_image.image = preset11_image  # Garde une référence
    if chemin == 2:
        global preset2_image  # Utilise la variable globale 'preset2_image'
        preset2_image = Image.open(resource_path("./Presets/Preset2.png"))  # Charge le preset 2
        preset21_image = preset2_image.resize((600,500))  # Redimensionne
        preset21_image = ImageTk.PhotoImage(preset21_image)  # Convertit pour Tkinter
        label_image.configure(image=preset21_image) # Permet de changer la configuration de label_image pour rajouter une image dans celui-ci
        label_image.image = preset21_image  # Garde une référence
    if chemin == 3:
        global preset3_image  # Utilise la variable globale 'preset3_image'
        preset3_image = Image.open(resource_path("./Presets/Preset3.png"))  # Charge le preset 3
        preset31_image = preset3_image.resize((600,500))  # Redimensionne
        preset31_image = ImageTk.PhotoImage(preset31_image)  # Convertit pour Tkinter
        label_image.configure(image=preset31_image) # Permet de changer la configuration de label_image pour rajouter une image dans celui-ci
        label_image.image = preset31_image  # Garde une référence


# Initialisation d'une variable globale
variable = 1

# Définition d'une fonction pour sélectionner un effet en fonction de la valeur passée
def selectioneffet(value):
    global variable # Utilisation de la variable globale "variable"
    variable = value # Assignation de la nouvelle valeur à "variable"

# Définition d'une fonction appelée lors du clic sur le bouton horizontal
def bouton_horizontal_click(*args): selectioneffet(2) # Appelle la fonction "selectioneffet" avec la valeur 2
# Définition d'une fonction appelée lors du clic sur le bouton vertical
def bouton_vertical_click(*args): selectioneffet(1) # Appelle la fonction "selectioneffet" avec la valeur 1
# Définition d'une fonction appelée lors du clic sur le bouton pour un effet combiné vertical et horizontal
def bouton_verthoriz_click(*args): selectioneffet(3) # Appelle la fonction "selectioneffet" avec la valeur 3

# Initialisation des variables pour les images modifiées à None
horizontal2, vertical2, verthoriz3 = None, None, None

# Initialisation de la variable "force" pour stocker la force de l'effet
force = 0

# Définition d'une fonction pour mettre à jour la valeur de la force basée sur la position du curseur du slider
def mise_a_jour_force(event):
    global force # Utilisation de la variable globale "force"
    # Mise à jour de "force" en fonction de la position actuelle du slider
    force = (scale.get() * 0.4) / 100
    # Affichage de la valeur actuelle du slider et de la force calculée
    #print("Nouvelle valeur du curseur :", scale.get())
    #print("Force calculée :", force)

# Création d'un label pour le slider de Force
texte_force = tk.Label(fen, text="Force:", background=fond2, foreground=texte, font=fontperso, border=0)
# Positionnement du label
texte_force.place(x=840, y=280)

# Configuration du style pour le slider
style = ttk.Style()
# Configuration du style "Custom.Horizontal.TScale" avec des paramètres spécifiques pour l'arrière-plan, la couleur du texte, et la couleur de la "trough" (partie de la barre que le curseur peut parcourir)
style.configure('Custom.Horizontal.TScale', background=fond2, foreground=fond, troughcolor=fond)

# Création du slider (scale) avec une valeur allant de 0 à 100, orienté horizontalement
# La fonction "mise_a_jour_force" est appelée chaque fois que la valeur du slider change
scale = ttk.Scale(fen, from_=0, to=100, orient='horizontal', length=200, style='Custom.Horizontal.TScale', command=mise_a_jour_force)
# Positionnement du slider
scale.place(x=840, y=330)

derniere_image_modifiee = None # Variable permetant d'eviter l'enregistrement de plusieurs images modifié et de juste garder la dernière modifier pour l'enregistrement

# Fonction pour les différents effets présents
def effetsimage():
    global derniere_image_modifiee
    # Si "variable" est égale à 2, applique un effet horizontal.
    if variable == 2:
        # Sélection de l'image source basée sur la valeur de "chemin"
        if preset1_image is not None and chemin == 1 :
            horizontal1 = preset1_image
        if preset2_image is not None and chemin == 2 :
            horizontal1 = preset2_image
        if preset3_image is not None and chemin == 3 :
            horizontal1 = preset3_image
        if imageimporter is not None and chemin == 4 :
            horizontal1 = imageimporter
        L, H = horizontal1.size # Récupère les dimensions de l'image source

        # Crée une nouvelle image plus large que l'original
        horizontal2 = Image.new("RGB",(int(L * 1.2),H))

        for y in range(H): # Parcourt chaque ligne de l'image.
            N = random.randint(int(-0.1 * force * L), int(0.1 * force * L)) # Génère un décalage aléatoire selon la force
            for x in range(L): # Parcourt chaque colonne de l'image.
                pixel = horizontal1.getpixel((x,y)) # Récupère le pixel actuel
                # Sépare les valeurs RGB du pixel.
                r = pixel[0]
                v = pixel[1]
                b = pixel[2]
                # Place le pixel dans la nouvelle image en ajoutant le décalage
                horizontal2.putpixel(((x + int(0.1 * L) + N), y),(r,v,b))

        # Coupe les bords ajoutés pour ajuster l'image à sa nouvelle taille.
        derniere_image_modifiee = horizontal2.crop((int(L * 0.2), 0, int(L * 1.2) - int(L * 0.2), H ))
        # Redimensionne et affiche l'image résultante.
        horizontal31 = derniere_image_modifiee.resize((600,500))
        horizontal31 = ImageTk.PhotoImage(horizontal31)
        label_image.configure(image=horizontal31) # Permet de changer la configuration de label_image pour rajouter une image dans celui-ci
        label_image.image = horizontal31 # Garde une référence de l'image.


    # Si "variable" est égale à 1, applique un effet vertical.
    if variable ==1:
        # Sélection de l'image source basée sur la valeur de "chemin"
        if preset1_image is not None and chemin == 1 :
            vertical1 = preset1_image
        if preset2_image is not None and chemin == 2 :
            vertical1 = preset2_image
        if preset3_image is not None and chemin == 3 :
            vertical1 = preset3_image
        if imageimporter is not None and chemin == 4 :
            vertical1 = imageimporter
        L, H = vertical1.size # Récupère les dimensions de l'image source

        # Crée une nouvelle image plus haute que l'original
        vertical2 = Image.new("RGB", (L, int(H * 1.2)))

        for x in range(L): # Parcourt chaque colonne de l'image.
            N = random.randint(int(-(0.1 * H * force)), int(0.1 * H * force)) # Génère un décalage aléatoire selon la force
            for y in range(H): # Parcourt chaque ligne de l'image.
                pixel = vertical1.getpixel((x,y)) # Récupère le pixel actuel
                # Sépare les valeurs RGB du pixel.
                r = pixel[0]
                v = pixel[1]
                b = pixel[2]
                # Place le pixel dans la nouvelle image en ajoutant le décalage
                vertical2.putpixel((x,(y + int(0.1 * H) + N)),(r,v,b))

        # Coupe les bords ajoutés pour ajuster l'image à sa nouvelle taille.  
        derniere_image_modifiee = vertical2.crop((0, int(H * 0.2), L, int(H * 1.2) - int(H * 0.2)))
        # Redimensionne et affiche l'image résultante.
        vertical31 = derniere_image_modifiee.resize((600, 500))
        vertical31 = ImageTk.PhotoImage(vertical31)
        label_image.configure(image=vertical31) # Permet de changer la configuration de label_image pour rajouter une image dans celui-ci
        label_image.image = vertical31 # Garde une référence de l'image.


    # Si "variable" est égale à 3, applique un effet vertical et horizontal.
    if variable ==3:
        # Sélection de l'image source basée sur la valeur de "chemin"
        if preset1_image is not None and chemin == 1 :
            verthoriz1 = preset1_image
        if preset2_image is not None and chemin == 2 :
            verthoriz1 = preset2_image
        if preset3_image is not None and chemin == 3 :
            verthoriz1 = preset3_image
        if imageimporter is not None and chemin == 4 :
            verthoriz1 = imageimporter

        L, H = verthoriz1.size # Récupère les dimensions de l'image source
        # Crée une nouvelle image plus haute que l'original
        verthoriz2 = Image.new("RGB",(L,int(H * 1.2)))

        for x in range(L): # Parcourt chaque colonne de l'image.
            N = random.randint(int(-0.1 * force * H), int(0.1 * force * H)) # Génère un décalage aléatoire selon la force
            for y in range(H): # Parcourt chaque ligne de l'image.
                pixel = verthoriz1.getpixel((x,y)) # Récupère le pixel actuel
                # Sépare les valeurs RGB du pixel.
                r = pixel[0] 
                v = pixel[1]
                b = pixel[2]
                # Place le pixel dans la nouvelle image en ajoutant le décalage
                verthoriz2.putpixel((x,(y + int(0.1 * H) + N)),(r,v,b))
        # Coupe les bords ajoutés pour ajuster l'image à sa nouvelle taille.
        verthoriz2 = verthoriz2.crop((0, int(H * 0.2), L, int(H * 1.2) - int(H * 0.2)))

        L, H = verthoriz2.size  # Récupère les dimensions de l'image source
        # Crée une nouvelle image plus large que l'original
        verthoriz3 = Image.new("RGB",(int(L * 1.2),H))

        for y in range(H): # Parcourt chaque ligne de l'image.
            N = random.randint(int(-0.1 * force * L), int(0.1 * force * L)) # Génère un décalage aléatoire selon la force
            for x in range(L): # Parcourt chaque colonne de l'image.
                pixel = verthoriz2.getpixel((x,y)) # Récupère le pixel actuel
                # Sépare les valeurs RGB du pixel.
                r = pixel[0]
                v = pixel[1]
                b = pixel[2]
                # Place le pixel dans la nouvelle image en ajoutant le décalage
                verthoriz3.putpixel(((x + int(0.1 * L) + N), y),(r,v,b))

        # Coupe les bords ajoutés pour ajuster l'image à sa nouvelle taille.  
        derniere_image_modifiee = verthoriz3.crop((int(L * 0.2), 0, int(L * 1.2) - int(L * 0.2), H )) 
        # Redimensionne et affiche l'image résultante.
        verthoriz41 = derniere_image_modifiee.resize((600,500))
        verthoriz41 = ImageTk.PhotoImage(verthoriz41)
        label_image.configure(image=verthoriz41) # Permet de changer la configuration de label_image pour rajouter une image dans celui-ci
        label_image.image = verthoriz41  # Garde une référence de l'image.

def sauvegarderimage():
    if derniere_image_modifiee is not None:
        extensionimage = [("JPG", "*.jpg"),("PNG","*.png"),("Tous","*")] # Permet de définir le type d'image pris en compte
        cheminimage = filedialog.asksaveasfilename(defaultextension=".png",filetypes=extensionimage,initialfile="Sans-titre") # Permet d'ouvrire la boîte de dialogue pour choisir un chemin où enregistrer l'image
        if cheminimage:  # Vérifie si il y a un emplacement choisi
            derniere_image_modifiee.save(cheminimage) # sauvegarde l'image
            print(f"L'image a été sauvegardée sous : {cheminimage}")
        else:
            print("Sauvegarde annulée.")
    else:
        print("Aucune image modifiée à sauvegarder.")

# Fonction pour quitter l'application
def quitter():
    fen.destroy()  # "Détruie"/Ferme la fenêtre et quitte l'application

# Effets au survol pour les boutons
def on_enter(event):
    event.widget.config(background=bouttonsurvol) # Change la couleur du bouton au survol

def on_leave(event):
    event.widget.config(background=boutton) # Rétablit la couleur d'origine lorsque la souris quitte le bouton

# Bouton pour importer une image
btnimport = tk.Button(fen, text="Importer", background=boutton, foreground=texte,font=fontperso, border=0, command= lambda:[importerchemin(),importerimage()])
btnimport.place(x=150, y=600) # Position du bouton
btnimport.bind("<Enter>", on_enter) # Lie l'événement de survol
btnimport.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

# Bouton pour sauvegarder l'image
btnsave = tk.Button(fen, text="Sauvegarder", background=boutton, foreground=texte,font=fontperso, border=0, command=sauvegarderimage)
btnsave.place(x=960, y=600) # Position du bouton
btnsave.bind("<Enter>", on_enter) # Lie l'événement de survol
btnsave.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

# Bouton pour appliquer l'effet sélectionné à l'image
btneffet = tk.Button(fen, text="Appliquer", background=boutton, foreground=texte,font=fontperso, border=0, command=effetsimage)
btneffet.place(x=870, y=450) # Position du bouton
btneffet.bind("<Enter>", on_enter) # Lie l'événement de survol
btneffet.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

# Bouton pour sélectionner un des trois effets
btnhorizontal = tk.Button(fen, text="\u2191", background=boutton, foreground=texte,font=fontperso, border=0, command=bouton_vertical_click)
btnhorizontal.place(x=850, y=150) # Position du bouton
btnhorizontal.bind("<Enter>", on_enter) # Lie l'événement de survol
btnhorizontal.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

btnvertical = tk.Button(fen, text="\u2191 \u2192", background=boutton, foreground=texte,font=fontperso, border=0, command=bouton_verthoriz_click)
btnvertical.place(x=900, y=150) # Position du bouton
btnvertical.bind("<Enter>", on_enter) # Lie l'événement de survol
btnvertical.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

btnverthoriz = tk.Button(fen, text="\u2192", background=boutton, foreground=texte,font=fontperso, border=0, command=bouton_horizontal_click)
btnverthoriz.place(x=985, y=150) # Position du bouton
btnverthoriz.bind("<Enter>", on_enter) # Lie l'événement de survol
btnverthoriz.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

# Boutton pour sélectionner un preset
btnpreset1 = tk.Button(fen, text="1", background=boutton, foreground=texte,font=fontperso, border=0, command= lambda:[preset1chemin(),importerimage()])
btnpreset1.place(x=50, y=200) # Position du bouton
btnpreset1.bind("<Enter>", on_enter) # Lie l'événement de survol
btnpreset1.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

btnpreset2 = tk.Button(fen, text="2", background=boutton, foreground=texte,font=fontperso, border=0, command= lambda:[preset2chemin(),importerimage()])
btnpreset2.place(x=50, y=300) # Position du bouton
btnpreset2.bind("<Enter>", on_enter) # Lie l'événement de survol
btnpreset2.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

btnpreset3 = tk.Button(fen, text="3", background=boutton, foreground=texte,font=fontperso, border=0, command= lambda:[preset3chemin(),importerimage()])
btnpreset3.place(x=50, y=400) # Position du bouton
btnpreset3.bind("<Enter>", on_enter) # Lie l'événement de survol
btnpreset3.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

# Bouton pour fermer l'application
btnimport = tk.Button(fen, text="Quitter", background=boutton, foreground=texte,font=fontperso, border=0, command=quitter)
btnimport.place(x=800, y=600) # Position du bouton
btnimport.bind("<Enter>", on_enter) # Lie l'événement de survol
btnimport.bind("<Leave>", on_leave) # Lie l'événement de sortie du survol

fen.mainloop()
