import numpy as np
import matplotlib.pyplot as plt
import math
def main():
    resultat = pointimage(350,0,250,1300,600)
    indice =  testimage(resultat)
    return indice





def calculnormale(intersec):
    """calcul la normale à la surface du cylindre au point intersec"""
    x = intersec.dot([1,0,0])
    y = intersec.dot([0,1,0])
    norme = math.sqrt ( x**2 + y**2)
    normale = np.array([x,y,0])
    return normale / norme


def calculvecteur (x1, x2, y1, y2, z1, z2):
    """prend deux point et renvoie un tableau representant le vecteur défini par ces points"""
    resultat = np.array([x2 - x1, y2-y1, z2- z1])
    return resultat

def equationsecond (a,b,c):
    """resout une équationdu second d"gré de la forme aX² + bX + C"""
    delta = b**2 - 4 * a * c


    if delta < 0:
        return [False,0,0]
    else:
        return [True, (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)]







def intersectiondroite(x, y ,z, vecteur, rayon):
    """ce programme n'est qu'une sorte de bilan des fonction précédente et renvoie la solution de l'intersection la plus adéquate au problème"""
    systeme = resolution(vecteur, rayon, x, y ,z)
    if systeme[0]:
        k1 = systeme[1]
        k2 = systeme[2]
        vecteur1 =  vecteur * k1
        vecteur2 =  vecteur * k2
        if vecteur1.dot(vecteur1) >= vecteur2.dot(vecteur2):
            resultat = vecteur2 + np.array([x,y,z])
        else:
            resultat = vecteur1 + np.array([x,y,z])
        return resultat
    else :
        return False


def interectangle (intersec, vecteur):
    """intersecton de la droite de vecteur directeur vecteur et passant par le point intersec avec le plan (O,0x,0y"""
    zvecteur = vecteur.dot([0,0,1])
    z = intersec.dot([0,0,1])
    if zvecteur == 0:
        return False
    else:
        k = - z / zvecteur
        return np.array([k * vecteur[0] + intersec[0],k * vecteur[1] + intersec[1], 0])

def parcourir(tableau):
    """programme test"""
    taillex = len(tableau)
    tailley = len(tableau[0])
    resultat = 0
    moyennex = 0
    moyenney =0
    for i in range(taillex):
        for j in range(tailley):
            if type(tableau[i][j]) != type(False):
                resultat += 1
                moyennex += tableau[i][j][0]
                moyenney += tableau[i][j][1]
    return moyennex/resultat, moyenney/resultat


def pointimage (xs,ys,zs,longuz, longuy):
    """renvoie un tableau des coordonnées des "points image" pour chaque pixel"""
    rayon = 20
    """26"""

    echelle = 8
    xdebut = 30
    ydebut = -(longuy/echelle)//2
    zdebut = 246
    resultat = []

    for i in range(longuz):
        resultat.append([])
        for j in range(longuy):
            vecteur = calculvecteur(xs,xdebut, ys, ydebut + j/echelle,zs, zdebut -i/echelle)
            intermed = intersectiondroite(xs, ys, zs, vecteur,rayon)
            if type(intermed) == type(False):
                resultat[i].append(False)
            else:
                normale = calculnormale(intermed)
                vecteur = rotationvecteur(vecteur, normale)
                resultat[i].append(interectangle(intermed, vecteur))
    return np.array(resultat)




def resolution(vecteur, rayon, x ,y ,z):
    """resolution du systeme d'intersection de la droite de vecteur directeur vecteur et passant par le point de coordonnées x,y,z avec le cylindre de rayon rayon d'axe Oz"""
    xvecteur = vecteur.dot([1,0,0])
    yvecteur = vecteur.dot([0,1,0])
    zvecteur = vecteur.dot([0,0,1])
    return equationsecond(xvecteur**2 + yvecteur**2, 2*(xvecteur * x + yvecteur * y),x**2 + y**2 - rayon**2)








def rotationvecteur (vecteur, normale):
    """vecteur dirigeant le rayon réfléchi par le cylindre"""
    compcol = - vecteur.dot(normale) * normale
    comportho = vecteur + compcol
    return compcol + comportho













def testimage (tableau):
    """affiche l'image des pixels"""
    tableauim = plt.imread("/home/alexandre/Images/lena.png")
    image = []
    echelle2 = 0.6
    xcentre, ycentre = parcourir(tableau)
    xcentre = int(xcentre)
    ycentre = int(ycentre)
    longuimagex = len(tableauim)
    """longuimagex = (len(tableauim)/echelle)//2"""
    """ longuimagey = (len(tableauim[0])/echelle)//2"""
    longuimagey = len(tableauim[0])
    indicentre = len(tableauim) //2
    indjcentre = len(tableauim)//2

    tableauindice = []

    longupx = len(tableau)
    longupy = len(tableau[0])
    for i in range(longupx):
        image.append([])
        for j in range(longupy):
            if type(tableau[i][j]) != type(False):
                x = tableau[i][j][0]
                y = tableau[i][j][1]
                imagi = int((x - xcentre) *echelle2) + indicentre
                imagj = int((y- ycentre) * echelle2)+indjcentre
                if imagi < longuimagex and imagi >= 0 and imagj >= 0 and imagj< longuimagey :

                    tableauindice.append( (imagi,imagj))
                    image[i].append([tableauim[imagi][ imagj][0], tableauim[imagi][ imagj][1], tableauim[imagi][ imagj][2], 1.])

                else:
                    image[i].append([0,0,0,1.])
            else:
                image[i].append([1.,0,0,1.])
    plt.imshow(np.array(image))
    plt.show()
    return np.array(tableauindice)



























