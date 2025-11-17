from PIL import Image
import random

image1 = Image.open("TableauVG.jpg")	# Ouverture de l’image se situant dans le même répertoire que le fichier python
L, H = image1.size                      # Récupération de la longueur et de la hauteur de l'image d'origine dans les variables L et H
image2 = Image.new("RGB",(L,int(H * 1.2)))   # Création d'une nouvelle image vierge 1,2 fois plus haute et de même largeur que l'image d'origine

for x in range(L):                                  # Itération pour chaque colonne
    N = random.randint(int(-0.1 * H), int(0.1 * H)) # Création d'un nombre aléatoire dans la variable N (correspond au décalage de la colonne)
    for y in range(H):                              # Itération pour chaque pixel de la colonne
        pixel = image1.getpixel((x,y))    #Récupération du pixel de coordonées x,y
        r = pixel[0]        #Récupération de la composante rouge du pixel (RVB) dans la variable r
        v = pixel[1]        #Récupération de la composante verte du pixel (RVB) dans la variable v
        b = pixel[2]        #Récupération de la composante bleue du pixel (RVB) dans la variable b
        image2.putpixel((x,(y + int(0.1 * H) + N)),(r,v,b))   #Placement du pixel sur la nouvelle image en tenant compte des marges hautes et basses et du décalage (N)

image2 = image2.crop((0, int(H * 0.2), L, int(H * 1.2) - int(H * 0.2)))      #"Rognage" des marges hautes et basses de l'image



L, H = image2.size                      # Récupération de la longueur et de la hauteur de l'image2 qui vient d'être créée dans les variables L et H
image3 = Image.new("RGB",(int(L * 1.2),H))   # Création d'une nouvelle troisième image vierge 1,2 fois plus large et de même hauteur que l'image d'origine

for y in range(H):                                  # Itération pour chaque ligne
    N = random.randint(int(-0.1 * L), int(0.1 * L)) # Création d'un nombre aléatoire dans la variable N (correspond au décalage de la ligne)
    for x in range(L):                              # Itération pour chaque pixel de la ligne
        pixel = image2.getpixel((x,y))    #Récupération du pixel de coordonées x,y
        r = pixel[0]        #Récupération de la composante rouge du pixel (RVB) dans la variable r
        v = pixel[1]        #Récupération de la composante verte du pixel (RVB) dans la variable v
        b = pixel[2]        #Récupération de la composante bleue du pixel (RVB) dans la variable b
        image3.putpixel(((x + int(0.1 * L) + N), y),(r,v,b))   #Placement du pixel sur la nouvelle image en tenant compte des marges droites et gauches et du décalage (N)

image3 = image3.crop((int(L * 0.2), 0, int(L * 1.2) - int(L * 0.2), H ))      #"Rognage" des marges droites et gauches de l'image

image3.save("maNouvelleImage.jpg")     #Enregistrement de l'image finale dans le même répertoire
