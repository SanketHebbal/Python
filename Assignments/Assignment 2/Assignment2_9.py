
def length(no):
    l = 0
    while(no):
        no = no // 10
        l = l + 1

    return l

no = int(input("Enter a number -> "))
print(length(no))

