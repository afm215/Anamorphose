

def Fusion(tableau,p,q,r):
    G =[]
    D =[]
    for i in range( q-p +1):
        G.append(copy.deepcopy(tableau[p+i]))
    for j in range(r-q):
        D.append(copy.deepcopy(tableau[q+j+1]))
    G.append([math.inf,0,0 ,0,0,0,0])
    D.append([math.inf,0,0,0,0,0,0])
    i = 0
    j = 0
    for k in range(p, r+1):
        if G[i][0] - D[j][0] < -0.001 or ((abs(G[i][0] - D[j][0]) <= 0.001) and (G[i][1]< D[j][1])):
            tableau[k] = G[i]
            i = i+1
        else:
            tableau[k] = D[j]
            j = j+1



def Trifusion(tableau,p,r):
    if p <r:
        q = int( (p + r) // 2)
        Trifusion(tableau, p, q)
        Trifusion(tableau, q+1 ,r)
        Fusion(tableau, p, q, r)
