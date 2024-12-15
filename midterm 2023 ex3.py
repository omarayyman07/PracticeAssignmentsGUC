
def runtotal(x):
    i=0
    res=[]
    count=0
    while i<len(x):
        if x[i]!=" ":
            count+=1
        else:
            res+=[count]
        i+=1
    res+=[count]
    return res
print(runtotal("KR Good luck"))
        
        
    