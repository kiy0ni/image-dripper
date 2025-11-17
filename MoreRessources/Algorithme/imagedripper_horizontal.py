from PIL import Image
import random

image1 = Image.open("Mon_Image.jpg")	# Ouverture de l’image se situant dans le même répertoire que le fichier python
L, H = image1.size                      # Récupération de la longueur et de la hauteur de l'image d'origine dans les variables L et H
image2 = Image.new("RGB",(int(L * 1.2),H))   # Création d'une nouvelle image vierge 1,2 fois plus large et de même hauteur que l'image d'origine

for y in range(H):                                  # Itération pour chaque ligne
    N = random.randint(int(-0.1 * L), int(0.1 * L)) # Création d'un nombre aléatoire dans la variable N (correspond au décalage de la colonne)
    for x in range(L):                              # Itération pour chaque pixel de la ligne
        pixel = image1.getpixel((x,y))    #Récupération du pixel de coordonées x,y
        r = pixel[0]        #Récupération de la composante rouge du pixel (RVB) dans la variable r
        v = pixel[1]        #Récupération de la composante verte du pixel (RVB) dans la variable v
        b = pixel[2]        #Récupération de la composante bleue du pixel (RVB) dans la variable b
        image2.putpixel(((x + int(0.1 * L) + N), y),(r,v,b))   #Placement du pixel sur la nouvelle image en tenant compte des marges latérales et du décalage (N)

image2 = image2.crop((int(L * 0.2), 0, int(L * 1.2) - int(L * 0.2), H ))      #"Rognage" des marges latérales de l'image

image2.save("maNouvelleImage.jpg")     #Enregistrement de l'image dans le même répertoire
image2.show()
