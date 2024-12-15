def Max(x,y):
    if x>y:
        return x
    else:
        return y

def isNumber(x):
    Flag=False
    if x=="0" or x=="1" or x=="2" or x=="3" or x=="4" or x=="5" or x=="6" or x=="7" or x=="8" or x=="9":
        Flag=True
        return Flag
    else:
        return Flag


def sumOfDigits(x):
    i=0
    sum=0
    while i < len(x):
        if isNumber(x[i]):
            sum+=int(x[i])
        i+=1
    return sum
print(sumOfDigits("Hello i am 23 and 72"))