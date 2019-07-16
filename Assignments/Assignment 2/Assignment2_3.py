def factorial(no):
    res = 1;
    for i in range(no,1,-1):
        res = res * i
    return res

no = int(input("Enter as number"))
print(factorial(no))
