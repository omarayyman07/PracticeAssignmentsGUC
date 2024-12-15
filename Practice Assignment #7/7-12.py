def Number(x):
    if x=="A" or x=="B" or x=="C":
        return 2
    elif x=="D" or x=="E" or x=="F":
        return 3
    elif x=="G" or x=="H" or x=="I":
        return 4
    elif x=="J" or x=="K" or x=="L":
        return 5
    elif x=="M" or x=="N" or x=="O":
        return 6
    elif x=="P" or x=="Q" or x=="R" or x=="S":
        return 7
    elif x=="T" or x=="U" or x=="V":
        return 8
    elif x=="W" or x=="X" or x=="Y" or x=="Z":
        return 9

def Translate(x):
    nlist=""
    x=x.upper()
    i=0
    while i<len(x):
        if x[i]>"A" and x[i]<="Z":
            nlist+=str(Number(x[i]))
        else:
            nlist+=x[i]
        i+=1
    return nlist
print(Translate("-800-Flowers"))
    
    