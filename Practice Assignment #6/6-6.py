n=input()
i=0
Flag=False
count=1
while i<len(n)-1 and not Flag:
    if n[i]==n[i+1]:
        count+=1
    else:
        print(count,n[i])
        count=1
    i+=1
print(count,n[i])