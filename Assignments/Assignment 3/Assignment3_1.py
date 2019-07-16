def sum(arr):
    result = 0
    for i in range(0,len(arr)) :
        result = result + arr[i]

    return result

def accept(no):
    arr = list()
    for i in range(0,no):
         num = input("Enter number ")
         arr.append(int(num))

    return sum(arr)
    
num = int(input("Enter a number ->"))
print(num)
print(accept(num))

