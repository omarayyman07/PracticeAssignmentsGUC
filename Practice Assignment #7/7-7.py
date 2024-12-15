def count(x,c):
    i=0
    count=0
    while i <len(x):
        if x[i]==c:
            count+=1
        i+=1
    return count

def occurrence(l,c):
    i=0
    nlist=[]
    while i <len(l):
        nlist+=[count(l[i],c)]
        i+=1
    return nlist


print(occurrence( ["aaa","aba","bcd","aaa"],"a"))
        
    