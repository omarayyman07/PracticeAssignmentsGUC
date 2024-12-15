def combine(x):
    i=0
    nlist=""
    while i <len(x):
        nlist+=x[i]
        i+=1
    return nlist

if combine(["o","m","a","r"])==combine(["o","mar"]):
    print("True")
else:
    print("False")
