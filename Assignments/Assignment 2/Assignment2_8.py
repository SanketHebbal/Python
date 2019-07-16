def printPattern(no):
    for i in range(1 , no + 1 , 1):
        for j in range(1 , i + 1 , 1):
            print(j,end="")
        print()


no = int(input("Enter a number --> "))
printPattern(no)
