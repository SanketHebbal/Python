def sumFactor(no):
    sum = 0
    for i in range(1,int(no/2)+1,1):
        if(no % i == 0):
            sum = sum + i
    return sum


no =  int(input("Enter a number"))
print(sumFactor(no))
