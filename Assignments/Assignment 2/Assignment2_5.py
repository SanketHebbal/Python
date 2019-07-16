def ChkPrime(no):
    for i in range(2,int(no / 2)+1,1):
        if(no % i == 0):
            return False
    return True

no = int(input("Enter a number --> "))

res = ChkPrime(no)
if(res == True):
    print("Number is prime")
else:
    print("Number is not prime")

