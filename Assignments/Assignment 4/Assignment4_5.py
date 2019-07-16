from functools import reduce

def accept(no):
    arr = list()
    for i in range(0,no):
        num = int(input("Enter a number ->"))
        arr.append(num)

    return arr

def CheckPrime(no):
    
    if(no<=1):
        return False
    for i in range(2,(no//2)+1):
        if(no % i == 0):
            return False;
    return True

fp = lambda no1 , no2 : no1 % no2 

size = int(input("Enter the number of elements in list ->"))
arr = accept(size)

print(arr)
brr = list(filter(CheckPrime , arr))
print(brr)
crr = list(map(lambda no : 2 * no ,brr))
print(crr)
result = reduce(lambda no1,no2 : no2 if no2 > no1 else no1  , crr)
print(result)

