def accept(no):
    arr = list()
    for i in range(0,no):
        num = input("Enter a number ->")
        arr.append(int(num))

    return findMin(arr)

def findMin(arr):
    min = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

num = input("Enter number of element you want ->")
print(accept(int(num)))
