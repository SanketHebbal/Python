from MarvellousNum import CheckPrime

def accept(no):
    arr = list()
    for i in range(0,no):
        num = input("Enter a number ->")
        arr.append(int(num))

    return ListPrime(arr)

def ListPrime(arr):
    sum = 0
    print("Prime numbers")
    for i in range(0,len(arr)):
        if CheckPrime(arr[i]):
            print(arr[i],end=" ")
            sum = sum + arr[i]
            
    return sum

        
num = input("Enter number of element you want ->")
print("\nSum ->",accept(int(num)))
