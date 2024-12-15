def palindrome(x):
    i=len(x)-1
    Flag=False
    count=0
    k=0
    nlist=[]
    while i>=0:
        nlist+=[x[i]]
        i-=1
    while k<len(x):
        if x[k]==nlist[k]:
            count+=1
        k+=1
    if count==len(x):
        Flag=True
    return Flag
        
    
print(palindrome("noon"))
        