def collatz(number):

    if(number%2 == 0):
        print(number)
        return number // 2
    else:
        print(number)
        return 3*number + 1

try:
    number = int(input("Enter a number ->"))
    while(number != 1):
        number = collatz(number)

except:
    print("You must enter a integer value")
    
