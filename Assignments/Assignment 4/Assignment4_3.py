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
brr = list(filter(lambda no: (no >= 70 and no <= 90),arr))
print(brr)
crr = list(map(lambda no : no + 10,brr))
print(crr)
result = reduce(lambda no1,no2 : no1*no2 , crr)
print(result)

'print(reduce(lambda no1,no2 : no1*no2 , list(map(lambda no : no + 10,list(filter(lambda no: (no >= 70 and no <= 90),arr))))))'
