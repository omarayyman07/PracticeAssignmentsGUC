def multiply(n):
    i=0
    product=1
    while i <n:
        product*=n%10
        n//=10
        i+=1
    return product

def persistent(n):
    flag=False
    count=0
    while not flag:
        if n<10:
            flag=True
        else:
            n=multiply(n)
            count+=1
    return count
print(persistent(123))
        
            
    
        