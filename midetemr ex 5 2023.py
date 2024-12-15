n=eval(input())
flag=True
count=1
sum=0
while n>0:
    temp=n%10
    count+=1
    sum+=temp
    n//=10
    if sum%count!=0:
        flag=False
        break
print(flag)
    
        
    