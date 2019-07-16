from functools import reduce

def accept(no):
    arr = list()
    for i in range(0,no):
        num = int(input("Enter a number ->"))
        arr.append(num)

    return arr

    
size = int(input("Enter the number of elements in list ->"))
arr = accept(size)

print(arr)
brr = list(filter(lambda no: no % 2 == 0,arr))
print(brr)
crr = list(map(lambda no : no * no ,brr))
print(crr)
result = reduce(lambda no1,no2 : no1+no2 , crr)
print(result)

