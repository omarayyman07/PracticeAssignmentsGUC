def printstars(n):
    i=0
    stars=""
    while i<n:
        stars+="*"
        i+=1
    return stars


def printsquare(n):
    i=0
    while i <n:
        x=print(printstars(n))
        i+=1
    return x


def printtriangle(n):
    i=0
    while i <=n:
        print(printstars(i))
        i+=1
        
printtriangle(1)
        
     



        
            
        
        