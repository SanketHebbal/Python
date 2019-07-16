def sum(no):

    res = 0
    while(no):
        res = res + (no % 10)
        no = no // 10
    return res

no = int(input("Enter a number --> "))
print(sum(no))
