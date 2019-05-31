import numpy as np
import matplotlib.pyplot as plt
import math
""" idee tracer les droites passants par tous les points de l'image dans le cylindre ajouter les origines dans un tabeau à trier selon abcisses et ordonnée pour obtenir image"""
def opti(tableau, rayon):
    longx = len(tableau[0])
    longy = len(tableau[1])
    echelle = rayon /long
    xdebut = -rayon /2
    ydebur = rayon / 2
    """on place l'image dans le cas tres simple orthogonale à axe Ox """
    tableaucoor = []
    for i in range(longx):
        tableaucoor.append([])
        for j in range(longy):
            tableucoor[i].append([i * echelle + xdebut, j*echelle + ydebut])
             
    
    