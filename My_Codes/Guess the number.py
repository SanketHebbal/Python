import random

myNumber = random.randint(1,30)

def check(number):

    if number < myNumber:
        print("\nYour guess is too low")
        return 0
    elif number > myNumber:
        print("\nYour guess is too high")
        return 0
    else:
        return 1

print("I am thinking a number between 1 to 30\n")

chance = 0

while True:

    chance = chance + 1
    print("!!!! Take a guess !!!!")
    number = int(input())
    if(check(number)):
        print("Good job! You guessed my number in {} guesses!".format(chance))        
        break
input("\nEnter a key...")
