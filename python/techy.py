import numpy as np
import matplotlib.pyplot as plt
import math
import copy

def convert(tableau):
    resultat = []
    for i in range(len (tableau)):
        resultat.append (np.append(tableau[i][0] , tableau[i][1]))
    return np.array(resultat)   

def coninvers(tableau):
    resultat = []
    for i in range(len(tableau)):
        resultat.append([tableau[i][0:2], tableau[i][3:6]])
    return resultat        


def recherchetab ( tableau):
    """confirme le probleme au niveau du tri"""
    long = len(tableau)
    res = 0
    resultat = []
    for i in range(1, long ):
        if abs(tableau[i][0][0] - 51.8) <=0.06:
            res += 1
            resultat.append(tableau[i])
    return np.array(resultat) 
    
    
def veriftri (tableau):
    long = len(tableau)
    for i in range(1,long):
        if tableau[i][0][0] - tableau[i-1][0][0] < -0.001:
            return i
    return True                     
     
def main():
    a = plt.imread("/home/alexandre/Images/lena.png")
    return opti(a, 20, 350,0,250)
    
    
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
    



def tri (tableau1):
    tableau =np.copy(tableau1)
    long = len(tableau)
    ymin = tableau[0][0][1]
    ymax= ymin
    for i in range (long):
        j =i
        ymin = min( ymin, tableau[i][0][1])
        ymax = max(ymin, tableau[i][0][1])
        if i ==1000:
            
            print("premiere boucle passe")
        if i == 2000:
            print("10000") 
            return ymin, ymax, tableau   
        if i == long//4 :
            print("premiere moitie ok") 
            
        while (j> 0 and ((tableau[j][0][0] -  tableau[j - 1][0][0] < - 0.001 )  or ( (abs(tableau[j][0][0] - tableau[j - 1][0][0]) <= 0.001) and (tableau[j][0][1] < tableau[j - 1][0][1]) ) )  ):
            tableau[j], tableau[j-1] = copy.deepcopy(tableau[j-1]), copy.deepcopy(tableau[j])
            j = j-1
            if j <0 :
                print("warning")
    return ymin, ymax, tableau   

    


def reorgan(tableau):
    long1 = len(tableau)
    resultat = [[tableau[0]]]
    j = 0
    k = 0
    for i in range(1,long1):
        if tableau[i][0][0] - tableau[i-1][0][0] >= -0.001  :
            resultat[j].append(tableau[i])
        else:
            resultat.append([tableau[i]])
            j = j+1    
    return np.array(resultat)        
 
 
         


def derniereverif(tableau):
    longi = len(tableau)
    ymax = 0
    for i in range(longi):
        ymax = max(ymax, len(tableau[i]))
    for i in range(longi):
        ecart = ymax - len(tableau[i])
        for j in range(ecart):
            tableau[i].append([0.,0.,0.,1.])
            


            
def remplissage(tableau, xmin , xmax , ymin , ymax, echelle):
    resultat = []
    longi = len(tableau)
    
    for i in range(longi):
        ajoutdebut = []
        a = int( (tableau[i][0][0][1] - ymin) // echelle)
        """le rang -1 correspond au dernier element d une liste"""
        for j in range (a):
            ajoutdebut.append([0.,0.,0.,1.])
        resultat.append(ajoutdebut)
            
    print("premier stade")    
            
                 
            
    for i in range (longi):
        for j in range(len(tableau[i]) -1):
            pixel = tableau[i][j][1]
            resultat[i].append(pixel)
            nbrpoint = int((tableau[i][j+1][0][1] - tableau[i][j+1][0][1])// echelle -1)
            for k in range (nbrpoint):
                resultat[i].append(pixel)

        
    """for i in range(longi):
        ajoutfin = []
        """"""le rang -1 correspond au dernier element d une liste""""""
        b =  int((- tableau[i][-1][0][1] + ymax) // echelle)    
        for j in range(b):
            ajoutfin.append([0.,0.,0.,1.])
        resultat[i] = resultat[i] + ajoutfin """
        
        
    derniereverif(resultat)    
    return np.array(resultat)     

""" idee tracer les droites passants par tous les points de l'image dans le cylindre ajouter les origines dans un tabeau à trier selon abcisses et ordonnée pour obtenir image"""
"""rappel repere avec y entrant z vers le haut"""




def opti(tableau, rayon, xs, ys ,zs):
    longx = len(tableau)
    longy = len(tableau[0])
    echelle = rayon /longy
    zdebut =  longx * echelle/2
    ydebut = - rayon / 2
    tablim = []
    """on place l'image dans le cas tres simple orthogonale à axe Ox """
    tableaucoor = []
    for i in range(longx):
        tableaucoor.append([])
        for j in range(longy):
            tableaucoor[i].append([j * echelle + ydebut, -i*echelle + zdebut])
    print("step 1 done")        
    for i in range(longx):
        for j in range(longy):
            vect = calculvecteur(0, xs, tableaucoor[i][j][0], ys, tableaucoor[i][j][1], zs)
            intersec = intersectiondroite(xs, ys, zs,vect, rayon)
            vect = rotationvecteur(vect, calculnormale(intersec))
            tablim.append([interectangle(intersec, vect), tableau[i][j]])
    print("step2 done")
    
    tablim = np.array(tablim)
    return tablim
    ymin, ymax, tablim = tri(tablim)
    return tablim
    
    print("step 3 done")
    
    xmin = tablim[0][0][0]
    xmax = tablim[len(tablim) -1][0][0]
    
    tablim = reorgan(tablim)
    
    
    print("step 4 done")
    
    tablim = remplissage(tablim, xmin ,xmax, ymin, ymax, echelle)
    return tablim
    
    plt.imshow(np.array(tablim))
    plt.show()
    

            
           
    
    
    
    
    
    
            
            
            
             
    
    