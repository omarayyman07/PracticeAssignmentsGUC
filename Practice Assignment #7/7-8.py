def factorial(n):
    i=1
    fact=1
    while i<=n:
        fact=fact*i
        i+=1
    return fact

def e(n):
    euler=0
    i=0
    while i <=n:
        euler+=(1)/(factorial(i))
        i+=1
    return euler
print(e(70))
 

