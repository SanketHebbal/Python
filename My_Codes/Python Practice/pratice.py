def pattern(no):
    print("@"*no)

def reverseDigits(no):
    for i in range(no,0,-1):
        print(i,end=" ")

def DisplayClass(no):

    if (no > 0 and no <=50):
        print("Pass")
    elif (no > 50 and no <= 70):
        print("2nd class")
    elif (no > 70 and no <= 100):
        print("1st class")
    else:
        print("Invalid marks")
        

def GreetUser(no):
    if(no >= 5 and no <=11):
        print("Good moring")
    elif (no >= 12 and no <= 16):
        print("Good afternoon")
    elif (no >= 17 and no <=22):
        print("Good evening")
    elif (no >= 23 and no <= 24):
        print("Good night");
    else:
        print("Invalid  time")

def DisplayExamTime(no):

    if no.islower():
        no = no.upper()
    
    if( no == 'A'):
        print("exam is on 9 am")
    elif(no == 'B'):
        print("Exam is no 10 am")
    elif (no == 'C'):
        print("Exam is on 12 am")
    elif (no == 'D'):
        print("Exam is on 3 pm")
    else:
        print("Invalid division")

def Maximum2(arr):

    return max(arr)

def DisplayPercentage(obtain,total):
    return (obtain/total)*100;

def Leapyear(year):

    if(year % 4 == 0 and year % 100 !=0 or year % 400 == 0):
        return "leap year"
    else:
        return "not leap year"

def NumberLine(no):

    for i in range(-no,no+1):
        print(i,end=" ")

def DisplayChar(no):
    
    char = 'A'
    for i in range(no):
        print(char , end=" ")
        char = chr(ord(char)+1)

def secondMax(arr):

    arr.sort()
    return arr[-2]
    
    
arr = [1,2,3,4,5,6]

#number = int(input("Enter a number ->"))
print(secondMax(arr))
input()
