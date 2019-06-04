def triprime (tableau1):
    tableau =np.copy(tableau1)
    long = len(tableau)
    ymin = tableau[0][1]
    ymax= ymin
    for i in range (long):
        j =i
        ymin = min( ymin, tableau[i][1])
        ymax = max(ymin, tableau[i][1])
        if i ==1000:

            print("premiere boucle passe")
        if i == 10000:
            print("10000")

        if i == long//4 :
            print("premiere moitie ok")

        while (j> 0 and ((tableau[j][0] -  tableau[j - 1][0] < - 0.001 )  or ( (abs(tableau[j][0] - tableau[j - 1][0]) <= 0.001) and (tableau[j][1] < tableau[j - 1][1]) ) )  ):
            tableau[j], tableau[j-1] = copy.deepcopy(tableau[j-1]), copy.deepcopy(tableau[j])
            j = j-1
            if j <0 :
                print("warning")
    return ymin, ymax, tableau
