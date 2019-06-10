import numpy as np
import matplotlib.pyplot as plt
"""repère x vers le bas et y vers la droite"""
def main():
    return 0






def coeffconstant(indice, tabx,taby):
    """attention meme nombre d'y que de x"""
    long = len(tabx)
    resultat = 0
    for i in range(long):
        resultat += taby[i] * (tabx[i] ** indice)
    return resultat


def intersection(tab1, tab2):
    """intersection entre ligne tab1 et colonne tab2"""
    for i in range(len(tab1[0])):
        if tab1[0][i] in tab2[0] and tab1[1][i] in tab2[1]:
            return tab1[0][i], tab1[1][i]
    print("erreur intersection")


def recupcoor (echelle):
    image = plt.imread("/home/alexandre/Documents/Anamorphose/Anamorphose/python/cadrillage.png")
    longi = len( image)
    longj = len(image[0])
    arret =True
    indiligne = 0
    nbri = 0
    nbrj = 0
    tabindiceligne = []
    tabindicecollonne = []
    for indicei in range(longi):
        if  image[indicei][0][0] == 0 and image[indicei][0][1] == 0 and image[indicei][0][2] == 0 and image[indicei][0][3] == 1:
            if nbri == 0:
                nbri += 1
                tabindiceligne.append(indicei)

            elif abs(indicei - tabindiceligne[nbri - 1]) > 1:
                nbri += 1
                tabindiceligne.append(indicei)
    for indicej in range(longj):
        if image[0][indicej][0] == 0  and image[0][indicej][1] == 0 and image[0][indicej][2] == 0 and image[0][indicej][3] == 1:
            if nbrj == 0:
                nbrj += 1
                tabindicecollonne.append(indicej)

            elif (abs(indicej - tabindicecollonne[nbrj - 1])>1):
                nbrj += 1
                tabindicecollonne.append(indicej)

    ensembleligne = []
    ensemblecolonne = []
    for i in range(nbri):
        ensembleligne.append(recupligne(image, tabindiceligne[i]))
    for j in range (nbrj):
        ensemblecolonne.append(recupcolonne(image, tabindicecollonne[j]))
    tabinterdeforx = []
    tabinterdefory = []
    tabinterx = []
    tabintery = []
    for i in range (nbri):
        for j in range(nbrj):

            tabinterx.append(i * echelle)
            tabintery.append(j * echelle)
            interx, intery = intersection(ensembleligne[i], ensemblecolonne[j])
            tabinterdeforx.append(interx * echelle)
            tabinterdefory.append(intery* echelle)
    return tabinterdeforx, tabinterdefory




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

def recupcolonne(im, indicedepart):
    tabx = []
    taby = []
    indice = indicedepart
    long = len(im[indice])
    for i in range(long):
        """recuperation de la ligne commencant à [indicedepart] [0]"""




        if not(im[i][indice][0] ==0 and im[i][indice][1] ==0 and im[i][indice][2] ==0 and im[i][indice][3]  == 1):
            """remarque egalité stricte à surveiller"""
            if im[i][indice + 1][0] ==0 and im[i][indice + 1][1] == 0 and im[i][indice + 1][2] == 0 and im[i][indice + 1][3] == 1:
                indice += 1
            elif im[i][indice - 1][0] == 0 and im[i][indice - 1][1] == 0 and im[i][indice - 1][2] == 0 and im[i][indice - 1][3] == 1:
                indice -= 1

            else :
                return False
        taby.append(indice)
        tabx.append(i)
    return [tabx, taby]



def recupligne(im,  indicedepart):
    tabx = []
    taby = []
    indice = indicedepart
    long = len(im[indice])
    for i in range(long):
        """recuperation de la ligne commencant à [indicedepart] [0]"""




        if not(im[indice][i][0] ==0 and im[indice][i][1] ==0 and im[indice][i][2] ==0 and im[indice][i][3]  == 1):
            """remarque egalité stricte à surveiller"""
            if im[indice + 1][i][0] ==0 and im[indice + 1][i][1] == 0 and im[indice + 1][i][2] == 0 and im[indice + 1][i][3] == 1:
                indice += 1
            elif im[indice - 1][i][0] == 0 and im[indice - 1][i][1] == 0 and im[indice - 1][i][2] == 0 and im[indice - 1][i][3] == 1:
                indice -= 1

            else :
                return False
        tabx.append(indice)
        taby.append(i)
    return [tabx, taby]


def somme(indice, tableaucoorx):
    long= len(tableaucoorx)
    resultat = 0
    for i in range(long):
        resultat += tableaucoorx[i] ** indice
    return resultat