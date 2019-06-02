import numpy as np
import matplotlib.pyplot as plt
import math

def resolution(vecteur, rayon, x ,y ,z):
    """resolution du systeme d'intersection de la droite de vecteur directeur vecteur et passant par le point de coordonnées x,y,z avec le cylindre de rayon rayon d'axe Oz"""
    xvecteur = vecteur.dot([1,0,0])
    yvecteur = vecteur.dot([0,1,0])
    zvecteur = vecteur.dot([0,0,1])
    return equationsecond(xvecteur**2 + yvecteur**2, 2*(xvecteur * x + yvecteur * y),x**2 + y**2 - rayon**2)
    
    
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
        
        

def rotationvecteur (vecteur, normale):
    """vecteur dirigeant le rayon réfléchi par le cylindre"""
    compcol = - vecteur.dot(normale) * normale
    comportho = vecteur + compcol
    return compcol + comportho
    
def calculnormale(intersec):
    """calcul la normale à la surface du cylindre au point intersec"""
    x = intersec.dot([1,0,0])
    y = intersec.dot([0,1,0])
    norme = math.sqrt ( x**2 + y**2)
    normale = np.array([x,y,0])
    return normale / norme  
    
def tri (tableau):
    long = len(tableau)
    ymin = tableau[0][0][1]
    for i in range (tableau):
        j =i
        ymin = min( ymin, tableau[i][0][1])
        while (j> 0 and (tableau[j][0][0] < tableau[j - 1][0][0]) or ( (tableau[j][0][0] == tableau[j - 1][0][0]) and (tableau[j][0][1] < tableau[j - 1][0][1]) )):
            tableau[j], tableau[j-1] = tableau[j-1], tableau[j]
            j = j-1
    return ymin        


""" idee tracer les droites passants par tous les points de l'image dans le cylindre ajouter les origines dans un tabeau à trier selon abcisses et ordonnée pour obtenir image"""
"""rappel repere avec y entrant e vers le haut"""
def opti(tableau, rayon):
    longx = len(tableau[0])
    longy = len(tableau[1])
    echelle = rayon /longy
    zdebut =  longx * echelle/2
    ydebur = - rayon / 2
    tablim = []
    """on place l'image dans le cas tres simple orthogonale à axe Ox """
    tableaucoor = []
    for i in range(longx):
        tableaucoor.append([])
        for j in range(longy):
            tableucoor[i].append([i * echelle + ydebut, -j*echelle + zdebut])
    for i in range(longx):
        for j in range(longy):
            vect = calculvecteur(0, xs, tableaucoor[i][j][0], ys, tableaucoor[i][j][1], zs)
            intersec = intersectiondroite(xs, ys, zs,vect, rayon)
            vect = rotationvecteur(vect, calculnormale(intersec))
            tablim.append(interectangle(intersec, vect), tableau[i][j])
    ymin = tri(tablim)
    xmin = tablim[0][0][0]
    
    
    
            
            
            
             
    
    