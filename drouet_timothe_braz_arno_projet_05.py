#------------------------- Auteurs -------------------------#
# Complétez les noms et prénoms des deux élèves du groupe
#
# Élève 1 - Braz Arno
# Élève 2 - Drouet Timothé
#
# RAPPEL : Tout plagiat entre groupes conduira à la note de 0 sans autre avertissement.
#          Recopier un code en modifiant quelques noms de variables sera considéré
#          comme du plagiat
#
#------------------------ Consignes ------------------------#
#
# Si vous souhaitez programmer des fonctions supplémentaires pour faciliter
# la programmation des fonctions de ce mini-projet, il ne faut pas hésiter
#
# N'oubliez pas de TESTER vos fonctions avec d'autres images que celle de la
# pomme rouge. Respectez bien le cahier des charges de chaque fonction.
# Ces tests sont à placer dans le "main".
# Pensez à fournir ces images en rendant votre projet
#
# Enlevez tous les affichages d'image en les mettant en commentaire.
# Seules les sauvegardes d'images avec un nouveau nom sont attendues.
#
#----------------------- C'est parti ! ----------------------#


from PIL import Image


def griser(source, nom_result):
    """
    source - Image
    nom_result - str, nom du fichier image qui sera renvoyé
    Sortie: Image - Nouvelle image de mêmes caractéristiques que la source.
            Version en « nuances de gris » de l'image source.
    """
    img=Image.open(source)
    largeur, hauteur=img.size
    result=Image.new(img.mode, img.size)
    for y in range(hauteur):
        for x in range(largeur):
            (r, g, b)=img.getpixel((x, y))
            gris = (r+g+b)//3
            result.putpixel((x, y), (gris, gris, gris))
    result.save(f'{nom_result}.png')
    result.show()


def negatif(source, nom_result):
    """
    source - Image
    nom_result - str, nom du fichier image qui sera renvoyé
    Sortie: Image - Nouvelle image de mêmes caractéristiques que la source.
            Version en « négatif » de l'image source.
    """
    img=Image.open(source)
    largeur, hauteur=img.size
    result=Image.new(img.mode, img.size)
    for y in range(hauteur):
        for x in range(largeur):
            (r, g, b)=img.getpixel((x, y))
            result.putpixel((x, y), (255-r, 255-g, 255-b))
    result.save(f'{nom_result}.png')
    result.show()


def symetrie(source, nom_result, hori):
    """
    source - Image
    nom_result - str, nom du fichier image qui sera renvoyé
    hori - bool, correspond à "horizontal" si True, à "vertical" sinon
    Sortie: Image - Nouvelle image de mêmes caractéristiques que la source.
            Version symétrique (horizontale ou verticale) de l'image source.
    """
    img=Image.open(source)
    largeur, hauteur=img.size
    result=Image.new(img.mode, img.size)
    for y in range(hauteur):
        for x in range(largeur):
            (r, g, b)=img.getpixel((x, y))
            if hori:
                result.putpixel((x, hauteur-1-y), (r, g, b))
            else:
                result.putpixel((largeur-1-x, y), (r, g, b))
    result.save(f'{nom_result}.png')
    result.show()


def rotation(source, nom_result, gauche):
    """
    source - Image
    nom_result - str, nom du fichier image qui sera renvoyé
    gauche - bool, correspond à "90° à gauche" si True, à "90° à droite" sinon
    Sortie: Image - Nouvelle image de même encodage (mais pas mêmes dimensions)
            que la source. Rotation de 90° à gauche (ou à droite) de l'image source.
    """
    img=Image.open(source)
    largeur, hauteur=img.size
    result=Image.new(img.mode, (hauteur, largeur))
    for y in range(hauteur):
        for x in range(largeur):
            (r, g, b)=img.getpixel((x, y))
            if gauche:
                result.putpixel((y, largeur-1-x), (r, g, b))
            else:
                result.putpixel((hauteur-1-y, x), (r, g, b))
    result.save(f'{nom_result}.png')
    result.show()




def noir_blanc(source, nom_result, seuil):
    """
    source - Image
    nom_result - str, nom du fichier image qui sera renvoyé
    seuil - int, entier positif compris entre 0 et 255 (faire une assertion)
                 intensité en-deçà de laquelle le pixel sera affiché en noir
    Sortie: Image - Nouvelle image de mêmes caractéristiques que la source.
            Version en « noir et blanc » de l'image source.
    """
    assert 0<=seuil<=255, "Valeur décimal trop élevé !"
    img=Image.open(source)
    largeur, hauteur=img.size
    result=Image.new(img.mode, img.size)
    for y in range(hauteur):
        for x in range(largeur):
            (r, g, b)=img.getpixel((x, y))
            if r<seuil or g<seuil or b<seuil:
                pxl=0
            else:
                pxl=255
            result.putpixel((x, y), (pxl, pxl, pxl))
    result.save(f'{nom_result}.png')
    result.show()




def compresse(source, nom_result, k):
    """
    source - Image
    nom_result - str, nom du fichier image qui sera renvoyé
    k - int, entier strictement positif (coefficient de réduction)
    Sortie: Image - Nouvelle image de même encodage que la source.
            Version « compressée » de l'image source, c'est-à-dire dont
            le nombre de pixels est divisé par k².
    """
    img=Image.open(source)
    largeur, hauteur=img.size
    result=Image.new(img.mode, (largeur//k, hauteur//k))
    for y in range(hauteur-k, -1, -k):
        for x in range(largeur-k, -1, -k):
            (r, g, b)=img.getpixel((x, y))
            for pixel in range(1, k):
                (r2, g2, b2)=img.getpixel((x+pixel, y+pixel))
                r+=r2
                g+=g2
                b+=b2
            (r, g, b)=(r//k, g//k, b//k)
            result.putpixel((x//k, y//k), (r, g, b))
    result.save(f'{nom_result}.png')
    result.show()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # Nous avons choisi une image relativement sombre pour principalement tester noir_blanc
    # et une image coloré et rectangle pour tester griser, rotation et noir_blanc

    # print(griser('pommeRouge.png', 'griser1'))
    # print(griser('Hades.png', 'griser2'))
    # print(griser('DarkSideMoon.png', 'griser3'))
    #
    # print(negatif('pommeRouge.png', 'negatif1'))
    # print(negatif('Hades.png', 'negatif2'))
    # print(negatif('DarkSideMoon.png', 'negatif3'))
    #
    # print(symetrie('pommeRouge.png', 'symetrie1', True))
    # print(symetrie('pommeRouge.png', 'symetrie1', False))
    # print(symetrie('Hades.png', 'symetrie2', True))
    # print(symetrie('Hades.png', 'symetrie2', False))
    # print(symetrie('DarkSideMoon.png', 'symetrie3', True))
    # print(symetrie('DarkSideMoon.png', 'symetrie3', False))
    #
    # print(rotation('pommeRouge.png', 'rotation1', True))
    # print(rotation('pommeRouge.png', 'rotation1', False))
    # print(rotation('Hades.png', 'rotation2', True))
    # print(rotation('Hades.png', 'rotation2', False))
    # print(rotation('DarkSideMoon.png', 'rotation3', True))
    # print(rotation('DarkSideMoon.png', 'rotation3', False))
    #
    # print(noir_blanc('pommeRouge.png', 'noir_blanc1', 115))
    # print(noir_blanc('pommeRouge.png', 'noir_blanc1', 230))
    # print(noir_blanc('Hades.png', 'noir_blanc2', 25))
    # print(noir_blanc('Hades.png', 'noir_blanc2', 200))
    # print(noir_blanc('DarkSideMoon.png', 'noir_blanc3', 111))
    # print(noir_blanc('DarkSideMoon.png', 'noir_blanc3', 222))
    #
    # print(compresse('pommeRouge.png', 'compresse1', 2))
    # print(compresse('pommeRouge.png', 'compresse1', 10))
    # print(compresse('Hades.png', 'compresse2', 4))
    # print(compresse('Hades.png', 'compresse2', 11))
    # print(compresse('DarkSideMoon.png', 'compresse3', 3))
    # print(compresse('DarkSideMoon.png', 'compresse3', 7))
