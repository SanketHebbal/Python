def accept(no):
    arr = list()
    for i in range(0,no):
        num = input("Enter a number ->")
        arr.append(int(num))

    no = int(input("Enter the number to be searched -->"))
    return findFeq(arr,no)

def findFeq(arr,no):
    count = 0
    for i in range(0,len(arr)):
        if arr[i] == no:
            count = count + 1
    return count

num = input("Enter number of element you want ->")
print(accept(int(num)))
