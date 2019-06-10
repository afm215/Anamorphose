import numpy as np
import matplotlib.pyplot as plt
"""repère x vers le bas et y vers la droite"""
def main():
    return 0

def coordefor(im, echelle):
    tabx = [127 * echelle]
    taby = [0]
    indice = 127
    long = len(im[127])
    for i in range(long):
        if not(im[indice][i][0] <=10**-10 and im[indice][i][1] <=10**-10 and im[indice][i][2] <=10**-10 and abs(im[indice][i][3] - 1) <= 10**-10):
            if im[indice + 1][i][0] <= 10**-10 and im[indice + 1][i][1] == 0 and im[indice + 1][i][2] == 0 and im[indice + 1][i][3] == 1:
                indice += 1
            elif im[indice - 1][i][0] == 0 and im[indice - 1][i][1] == 0 and im[indice - 1][i][2] == 0 and im[indice - 1][i][3] == 1:
                indice -= 1

            else :
                return False
        tabx.append( indice * echelle)
        taby.append(i * echelle)
    return tabx, taby


def coeffconstant(indice, tabx,taby):
    """attention meme nombre d'y que de x"""
    long = len(tabx)
    resultat = 0
    for i in range(long):
        resultat += taby[i] * (tabx[i] ** indice)
    return resultat

def recupcoor (echelle):
    image = plt.imread("/home/alexandre/Documents/Anamorphose/Anamorphose/python/cadrillage.png")
    longi = len( image)
    longj = len(image[0])
    arret =True
    indiligne = 0
    nbr = 0
    for indicei in range(longi)
        if  image[indicei][0][0] == 0 and image[indicei][0][1] == 0 and image[indicei][0][2] == 0 and image[indicei][0][3] == 1:
            nbr + = 1
            if arret:
                arret = False
                indiligne = indicei


    tabxdefo, tabydefo = coordefor(image, echelle)
    """je considere que il s'agit d'uncadrillage d'image parfait"""
    xreel = echelle

    plt.imshow(image)
    plt.show()

def recupcoeff (tabx, taby, degf):
    """le principe et de poser le systeme sous la forme matricielle pour obtenir facilement les coeff"""
    n = len(tabx)
    matsys = []
    matconst = []
    for i in range (degf+1) :
        matsys.append([])
        matconst.append(coeffconstant(i,tabx, taby))
        for j in range(degf + 1):
            matsys[i].append(somme(i + j, tabx))
    matsys = np.array(matsys)
    matconst = np.array(matconst)
    return matconst.dot(np.linalg.inv(matsys))

def somme(indice, tableaucoorx):
    long= len(tableaucoorx)
    resultat = 0
    for i in range(long):
        resultat += tableaucoorx[i] ** indice
    return resultat