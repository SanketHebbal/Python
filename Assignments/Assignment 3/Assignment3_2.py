def accept(no):
    arr = list()
    for i in range(0,no):
        num = input("Enter a number ->")
        arr.append(int(num))

    return findMax(arr)

def findMax(arr):
    max = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

num = input("Enter number of element you want ->")
print(accept(int(num)))


i = int(input("Enter a  number"))
print(i)
