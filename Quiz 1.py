n1=eval(input())
n2=eval(input())

def numd(x):
    i=0
    while x>0:
        x//=10
        i+=1
    return i
def big(x,y):
    if x>y:
        return x
    else:
        return y

def omar(x,y):
    total=0
    i=0
    while x>0 and y>0:
        temp1=x%10
        temp2=y%10
        total+=big(temp1,temp2)*(10**i)
        x//=10
        y//=10
        i+=1
    return total

if n1<10 or n2<10:
    print("Sorry")
else:
    if numd(n1)!=numd(n2):
        print("Not equal number of digits")
    else:
        print(omar(n1,n2))
        

        
        
        




    