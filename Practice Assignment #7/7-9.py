def Perfect(n):
    i=1
    sum=0
    flag=False
    while i <n:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        flag=True
        return flag
    else:
        return flag

def AllPerfect(n):
    i=1
    while i <=n:
        if Perfect(i):
            print(i)
        i+=1
print(AllPerfect(496))
    
            
        