#------------------------- Auteurs -------------------------#
# Complétez les noms et prénoms des deux élèves du groupe
#
# Élève 1 - Gottwald Timeo
# Élève 2 - Braz Arno
#
# RAPPEL : Tout plagiat entre groupes conduira à la note de 0 sans autre avertissement.
#          Recopier un code en modifiant quelques noms de variables sera considéré
#          comme du plagiat
#
#------------------------ Consignes ------------------------#
#
# Si vous souhaitez programmer des fonctions supplémentaires pour faciliter
# la programmation des fonctions de ce mini-projet, il ne faut pas hésiter.
#
# N'oubliez pas de TESTER vos fonctions avec vos propres images.
# Pour la Partie n°1, soyez patients à partir d'images de type 1024x1024
# Les tests des fonctions sont à placer dans le "main"
#
# Enlevez tous les affichages d'image en les mettant en commentaire.
# Seules les sauvegardes d'images avec un nouveau nom sont attendues.
#
#----------------------- C'est parti ! ----------------------#

from PIL import Image


#------------------------ Partie n°1 ------------------------#
#
# N'hésitez pas à ajouter des fonctions (avec docstring !) si besoin

def echangePixel(source, x1, y1, x2, y2):
    """
    source - image (importée dans le main)
    x1, y1 - int, coordonnées du premier pixel
    x2, y2 - int, coordonnées du second pixel
    Sortie: None - Les composantes des deux pixels ont été échangées
    """
    temp = source.getpixel((x1, y1))
    source.putpixel((x1, y1), source.getpixel((x2, y2)))
    source.putpixel((x2, y2), temp)


def rotationDpR(source) :
    """
    source - image carrée de dimension 2^k x 2^k (importée dans le main)
    Sortie: None - L'image est modifiée d'un quart de tour vers la droite
    """
    largeur, hauteur = source.size

    recursifDpR(source, 0, 0, largeur, hauteur)

def recursifDpR(source, lmin, hmin, lmax, hmax):
    '''
    source - image carrée de dimension 2^k x 2^k (importée dans le main)
    lmin - int, entier correspondant à la largeur de la borne inférieure sur lequel on va effectuer les modifications
    hmin - int, entier correspondant à la hauteur de la borne inférieure sur lequel on va effectuer les modifications
    lmax - int, entier correspondant à la largeur de la borne supérieure sur lequel on va effectuer les modifications
    hmax - int, entier correspondant à la hauteur de la borne supérieure sur lequel on va effectuer les modifications
    Sortie : None - L'image est modifiée d'un quart de tour vers la droite par un appel récursif de la fonction
    '''
    demiL = (lmax-lmin)//2
    demiH = (hmax-hmin)//2

    if (lmax-lmin)==1 or (hmax-hmin)==1:
        return None
    else:
        for x in range(lmin, lmin+demiL):
            for y in range(hmin, hmin+demiH):
                echangePixel(source, x, y, demiL+x, y)
                echangePixel(source, x, y, demiL+x, demiH+y)
                echangePixel(source, x, y, x      , demiH+y)

        for x in [lmin,lmin+demiL]:
            for y in [hmin,hmin+demiH]:
                recursifDpR(source, x, y, x+demiL, y+demiH)

#------------------------ Partie n°2 ------------------------#
#
# N'hésitez pas à ajouter des fonctions (avec docstring !) si besoin


def rotationCarree(source) :
    """
    source - image carrée (importée dans le main)
    Sortie: None - L'image est modifiée d'un quart de tour vers la droite
    """
    largeur, hauteur = source.size
    demiL = largeur//2
    demiH = hauteur//2
    for x in range(demiL):
        for y in range(demiH):
            temp = source.getpixel((largeur-1-y, x))
            source.putpixel((largeur-1-y, x), source.getpixel((x, y)))

            temp2 = source.getpixel((hauteur-1-x, largeur-1-y))
            source.putpixel((hauteur-1-x, largeur-1-y), temp)

            temp = source.getpixel((y, largeur-1-x))
            source.putpixel((y, largeur-1-x), temp2)

            source.putpixel((x, y), temp)

            # version avec une seule variable temp
            # temp = source.getpixel((largeur-1-y, x))
            # source.putpixel((largeur-1-y, x), source.getpixel((x, y)))
            #
            # source.putpixel((x, y),source.getpixel((hauteur-1-x, largeur-1-y)))
            # source.putpixel((hauteur-1-x, largeur-1-y), temp)
            #
            # temp = source.getpixel((y, largeur-1-x))
            # source.putpixel((y, largeur-1-x), source.getpixel((x,y)))
            #
            # source.putpixel((x, y), temp)


#------------------------ Partie n°3 ------------------------#
#
# N'hésitez pas à ajouter des fonctions (avec docstring !) si besoin


def rotation(source) :
    """
    source - Image (importée dans le main)
    Sortie: Image - Nouvelle image de même encodage (mais pas mêmes dimensions)
            que la source. Rotation de 90° à droite de l'image source.
    """
    longueur, hauteur = source.size
    source2 = Image.new(source.mode, (hauteur,longueur))

    for x in range(longueur):
        for y in range(hauteur):
            source2.putpixel((hauteur-1-y,x),source.getpixel((x,y)))

    return source2



#------------------------ Programme principal ------------------------#
#

if __name__ == '__main__':
    # décommentez puis complétez ce qui vous paraît nécessaire
    # importation des images:
    source  = Image.open('batman.png')
    source2 = Image.open('carre_nsi.png')
    source3 = Image.open('rectangle.png')

    #Partie 1:
    sourceDpR = source
    rotationDpR(sourceDpR)                                     # Rotation de l'image (Partie 1)
    sourceDpR.show()                                           # Affichage de l'image (Partie 1)
    sourceDpR.save('batman90_DPR.png')

    sourceDpR2 = source2
    rotationDpR(sourceDpR2)
    sourceDpR2.show()
    sourceDpR2.save('carre_nsi_DPR.png')

    #Partie 2:
    sourceCarree = Image.open('carre_nsi.png')
    rotationCarree(sourceCarree)
    sourceCarree.show()                                     # Affichage de l'image (Partie 2)
    sourceCarree.save('carre_nsi_Carree.png')

    sourceCarree2 = Image.open('batman.png')
    rotationCarree(sourceCarree2)
    sourceCarree2.show()                                     # Affichage de l'image (Partie 2)
    sourceCarree2.save('batman90_Carree.png')

    #Partie 3:
    source_rota = Image.open('batman.png')
    source_rota = rotation(source_rota)
    source_rota.show()                                           # Affichage de l'image (Partie 3)
    source.save('batman_Pt3.png')

    source3_rota = rotation(source3)
    source3_rota.show()                                          # Affichage de l'image (Partie 3)
    source3_rota.save('rect90d.png')



