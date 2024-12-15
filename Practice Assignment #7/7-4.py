def isPrime(n):
    i=1
    count=0
    flag=False
    while i<=n:
        if n%i==0:
            count+=1
        i+=1
    if count==2:
        flag=True
    return flag
print(isPrime(11))
  