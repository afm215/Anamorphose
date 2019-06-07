import numpy as np
import matplotlib.pyplot as plt
import math
import copy
"""idée faire plein de trifusion avec un parametre gros au début et plus fin ensuite"""

def comptecol (tableau):
    for i in range(len(tableau)):
        if len(tableau[i] ) <2:
            return False
        return True

def parcourir(tableau):
    """programme test"""
    taillex = len(tableau)
    tailley = len(tableau[0])
    resultat = 0
    moyennex = 0
    moyenney =0
    for i in range(taillex):
        for j in range(len(tableau[i])):
            if type(tableau[i][j]) != type(False):
                resultat += 1
                moyennex += tableau[i][j][0]
                moyenney += tableau[i][j][1]
    return moyennex/resultat, moyenney/resultat 
    
    
def ecartaucentre(tableau):
    """ecart des abscisses et ordonnées par rapport au point central"""
    xcentre , ycentre = parcourir(tableau)
    longupx = len(tableau)
    longupy = len(tableau[0])
    somme = 0
    longueurx = 0
    longueury = 0 
    for i in range(longupx):
        for j in range(len(tableau[i])):
            if type(tableau[i][j])!=type(False):
                longueurx  += abs(tableau[i][j][0] - xcentre)
                longueury += abs(tableau[i][j][1] - ycentre)
                somme += 1
    return longueurx//somme, longueury//somme                
          
    
    
def main():
    a = plt.imread("/home/alexandre/Images/lena.png")
    return opti(a, 200, 400,800)


def calculnormale(intersec):
    """calcul la normale à la surface du cylindre au point intersec"""
    x = intersec[0]
    y = intersec[1]
    norme = math.sqrt ( x**2 + y**2)
    normale = np.array([x,y,0])
    return normale / norme
    
        
def calculvecteur (x1, x2, y1, y2, z1, z2):
    """prend deux point et renvoie un tableau representant le vecteur défini par ces points"""
    resultat = np.array([x2 - x1, y2-y1, z2- z1])
    return resultat  
      
    
    
def convert(tableau):
    resultat = []
    for i in range(len (tableau)):
        resultat.append (np.append(tableau[i][0] , tableau[i][1]))
    return np.array(resultat)   

def coninvers(tableau):
    resultat = []
    for i in range(len(tableau)):
        resultat.append([tableau[i][0:3], tableau[i][3:7]])
    return np.array(resultat) 
 
 
 
 
def derniereverif(tableau):
    longi = len(tableau)
    ymax = 0
    ymin = 10058
    for i in range(longi):
        ymax = max(ymax, len(tableau[i]))
        ymin = (min(ymin, len(tableau[i])))
    print(ymax)  
    print(ymin)  
    for i in range(longi):
        ecart = ymax - len(tableau[i])
        for j in range(ecart):
            tableau[i].append([0.,0.,0.,1.])
            
            
            
            
            
def equationsecond (a,b,c):
    """resout une équationdu second d"gré de la forme aX² + bX + C"""
    delta = b**2 - 4 * a * c


    if delta < 0:
        return [False,0,0]
    else:
        return [True, (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)]          
    
def Fusion(tableau,p,q,r, precision):
    G =[]
    D =[]
    for i in range( q-p +1):
        G.append(copy.deepcopy(tableau[p+i]))
    for j in range(r-q):
        D.append(copy.deepcopy(tableau[q+j+1]))
    G.append([math.inf,0,-2,-2])
    D.append([math.inf,0,-2,-2])
    i = 0
    j = 0
    for k in range(p, r+1):
        if G[i][0] - D[j][0] < -precision or ((abs(G[i][0] - D[j][0]) <= precision) and (G[i][1]< D[j][1])):
            tableau[k] = G[i]
            i = i+1
        else:
            tableau[k] = D[j]
            j = j+1
            
            
            
def interectangle (intersec, vecteur):
    """intersecton de la droite de vecteur directeur vecteur et passant par le point intersec avec le plan (O,0x,0y"""
    zvecteur = vecteur[2]
    z = intersec[1]
    if zvecteur == 0:
        return False
    else:
        k = - z / zvecteur
        return k * vecteur[0] + intersec[0],k * vecteur[1] + intersec[1]



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
        
        



""" idee tracer les droites passants par tous les points de l'image dans le cylindre ajouter les origines dans un tabeau à trier selon abcisses et ordonnée pour obtenir image"""
"""rappel repere avec y entrant z vers le haut"""




def opti(tableau, rayon, xs,zs):
    ys = 0
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
            x,y = interectangle(intersec, vect)
            tablim.append([x,y,i,j])
    print("step2 done")
    
    long = len(tablim)
    Trifusion(tablim, 0, long -1, 0.5)
    print("premier tri fait")
    
    
    
    ymin, ymax = recherchyminmax(tablim)
    
    print("step 3 done")
    
    xmin = tablim[0][0]
    xmax = tablim[-1][0]
    nbrelement = 0 
    tablim = reorgan(tablim)
    print("step 4 done")
    
    tablim = remplissage(tablim,tableau, xmin ,xmax, ymin, ymax)
    return tablim
    
    
    plt.imshow(np.array(tablim))
    plt.show()
    
    
    
    

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
    
    
    
def recherchyminmax (tableau):
    long = len(tableau)
    ymin = tableau[0][1]
    ymax = ymin
    for i in range(long):
        ymax = max(ymax, tableau[i][1])
        ymin = min(ymin, tableau[i][1])
    return ymin ,ymax


def remplissage(tableau,tabpix, xmin , xmax , ymin , ymax):
    echelle = 1.5
    resultat = []
    longi = len(tableau)
    
    for i in range(longi):
        resultat.append([])
        a = int( (tableau[i][0][1] - ymin) // echelle)
        """le rang -1 correspond au dernier element d une liste"""
        for j in range (a):
            resultat[i].append([0.,0.,0.,1.])
            
    print("premier stade")    
            
                 
            
    for i in range (longi):
        for j in range(len(tableau[i]) -1):
            pixel = tabpix[tableau[i][j][2]][tableau[i][j][3]]
            resultat[i].append(pixel)
            nbrpoint = int((tableau[i][j+1][1] - tableau[i][j][1])// echelle -1)
            for k in range (nbrpoint):
                resultat[i].append(pixel)
            del pixel
    pixel = [0,0,0,1.]        
    print("deuxieme stade")    
    """for i in range(longi):
        ajoutfin = []
        """"""le rang -1 correspond au dernier element d une liste""""""
        b =  int((- tableau[i][-1][0][1] + ymax) // echelle)    
        for j in range(b):
            ajoutfin.append([0.,0.,0.,1.])
        resultat[i] = resultat[i] + ajoutfin """
        
    del tableau
           
    derniereverif(resultat)   
    print("phase fin") 
    for j in range (len(resultat[0])):
        xmax = 0 
        xmin =  len(resultat)
        for i in range(len(resultat)):
            if resultat[i][j][0] != 0. or resultat[i][j][1] != 0. or resultat[i][j][2] != 0. or resultat[i][j][3] != 1. :
                xmin = min(xmin, i)
                xmax = max(xmax , i)
        if xmax > xmin:
            del pixel
            pixel = copy.deepcopy(resultat[xmin] [j])
            for i in range(xmin, xmax + 1):
                if resultat[i][j][0] != 0. or resultat[i][j][1] != 0. or resultat[i][j][2] != 0. or resultat[i][j][3] != 1.:
                    del pixel
                    pixel = copy.deepcopy(resultat[i][j])
                    """return resultat[i][j]"""
                else:
                    """print (resultat[i][j])"""
                    resultat[i][j] = copy.deepcopy(pixel)
                    """return resultat[i][j] """   
    return resultat     
    
    
"""idee trouver ordre des grandeurs en regardant les ecart minimus entre abscisses..."""
def reorgan(tableau):    
    long1 = len(tableau)
    resultat = [[tableau[0]]]
    j = 0
    k = 0
    ref = tableau[0][0]
    nbr = 0
    for i in range(1,long1):
        if abs(-ref + tableau[i][0]) <= 0.093 :
            resultat[j].append(tableau[i]) 
            nbr += 1 
        else:
            if nbr <2 :
                del resultat[j]
                j = j - 1
            nbr = 0    
            ref = tableau[i][0]
            resultat.append([tableau[i]])
            j = j+1  
              
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
    
        
    
    
def Trifusion(tableau,p,r, precision):
    if p <r:
        q = int( (p + r) // 2)
        Trifusion(tableau, p, q,precision)
        Trifusion(tableau, q+1 ,r, precision)
        Fusion(tableau, p, q, r, precision)



def triinsertion (tableau,precision):
    """tri insertion n'est pas optimale pour le traitement du tableau"""
    """tableau =np.copy(tableau1)"""
    long = len(tableau)
    
    for i in range (long):
        j =i
            
        while (j> 0 and ((tableau[j][0] -  tableau[j - 1][0] < - precision)  or ( (abs(tableau[j][0] - tableau[j - 1][0]) <= precision) and (tableau[j][1] < tableau[j - 1][1]) ) )  ):
            tableau[j], tableau[j-1] = copy.deepcopy(tableau[j-1]), copy.deepcopy(tableau[j])
            j = j-1
            if j <0 :
                print("warning")
    



       



    
    
def veriftri (tableau):
    long = len(tableau)
    for i in range(1,long):
        if tableau[i][0] - tableau[i-1][0] <- 0.001:
            return i
    return True                     
 
 
 
 
 
 
 
 
def ultro(tableau):
    resultat = []
    longx = len(tableau)
    longy = len(tableau[0])
    for i in range(longx):
        resultat.append([])
        for j in range(longy):
            resultat[i].append([])
            for k in range(4):
                resultat[i][j].append(float(tableau[i][j][k]))
    plt.imshow(np.array(resultat) )
    plt.show()
    
                 
     

    
    

    
    

        
        


    

        
        


    



    





    


 
 
 
         



            


            



    

            
           
    
    
    
    
    
    
            
            
            
             
    
    