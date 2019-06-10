import numpy as np
import matplotlib.pyplot as plt
import math
import copy
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

def fonctiondeltax(xcentre, ycentre,tabxdefo, tabydefo, tabx, taby ):
    """les arguments sont les coordonnées du centre le tableau des abscisses et celui des ordonnées , non déformées et déformées"""
    tabr = []
    long = len(tabx)
    tabimager = []
    for i in range(long):
        if tabxdefo[i] - xcentre >= 1:
            rcarre =(tabxdefo[i] - xcentre)**2 + (tabydefo[i] - ycentre) ** 2
            image = (tabx[i] - tabxdefo[i]) / (tabxdefo[i] - xcentre)
            tabr.append(rcarre)
            tabimager.append(image)

    return tabr, tabimager

def recupimage(longi,longj, i, j,xcentre, ycentre ,echelle,k0, k1, k2):
    rcarre =(i * echelle - xcentre)**2 + (j * echelle - ycentre) ** 2
    deltax = (k1 * rcarre + k2 * rcarre**2 + k0) * (i * echelle - xcentre)
    deltay = (k1 * rcarre + k2 * rcarre**2 + k0) * (j * echelle - ycentre)
    xantecedent = i * echelle + deltax
    yantecedent = j * echelle + deltay
    indicei = int(round(xantecedent / echelle))
    indicej = int(round(yantecedent /echelle))
    indicej = min(indicej, longj-1)
    indicej =max(0, indicej)
    indicei = min (longi-1, indicei)
    indicei = max(0, indicei)
    return indicei, indicej,deltax


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
    xcentre = len(image) / 2 * echelle
    ycentre = len(image[1]) / 2 * echelle
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
    """recuperation des lignes et de colonnes noires"""
    for i in range(nbri):
        ensembleligne.append(recupligne(image, tabindiceligne[i]))
    for j in range (nbrj):
        ensemblecolonne.append(recupcolonne(image, tabindicecollonne[j]))
    tabinterdeforx = []
    tabinterdefory = []
    tabinterx = []
    tabintery = []
    intervallei = len(image) // nbri * echelle
    intervallej = len(image[1]) // nbrj * echelle
    for i in range (nbri):
        for j in range(nbrj):

            tabinterx.append((i + 1) * intervallei)
            tabintery.append((j + 1) * intervallej)
            interx, intery = intersection(ensembleligne[i], ensemblecolonne[j])
            tabinterdeforx.append(interx * echelle)
            tabinterdefory.append(intery* echelle)
    tabr, tabimager = fonctiondeltax(xcentre, ycentre, tabinterdeforx, tabinterdefory, tabinterx, tabintery)

    """return recupcoeff(tabr, tabimager, 2)"""
    coeff = recupcoeff(tabr, tabimager, 2)
    k0 = 0
    k1 = coeff[0]
    k2 = coeff[1]
    """k1 = 10**-10
    k2 = 5*10**-12"""


    imagefinale = []
    for i in range(longi):
        imagefinale.append([])
        for j in range(longj):
            imagefinale[i].append([0.,0.,0.,0.])
    indice = []
    for i in range(longi):
        for j in range (longj):
            indicei, indicej, delta = recupimage(longi, longj, i, j, xcentre, ycentre, echelle,k0, k1, k2)

            indice.append(delta)

            imagefinale[indicei][indicej] = copy.deepcopy(image[i][j])

    plt.imshow(np.array(imagefinale))
    plt.show()







    """je considere que il s'agit d'uncadrillage d'image parfait"""

def recupcoeff (tabx, taby, degf):
    """le principe et de poser le systeme sous la forme matricielle pour obtenir facilement les coeff"""
    n = len(tabx)
    matsys = [[somme(2,tabx),somme(3,tabx)],[somme(3,tabx),somme(4,tabx)]]
    matconst = [coeffconstant(1, tabx, taby), coeffconstant(2,tabx, taby)]
    """matsys = []
    matconst = []
    for i in range (degf+1) :
        matsys.append([])
        matconst.append(coeffconstant(i,tabx, taby))
        for j in range(degf+1):
            matsys[i].append(somme(i + j, tabx))"""
    matsys = np.array(matsys)
    matconst = np.array(matconst)
    return np.linalg.inv(matsys).dot(matconst)

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