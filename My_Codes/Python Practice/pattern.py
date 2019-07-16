import time

def pattern1(no):
    for i in range(no):
        print(i+1,end=" ")

def pattern2(no):
    print("* "*no)

def pattern3(ch,no):
    print(ch*no)

def pattern4(no):
    for i in range(no):
        print(i+1,end=" ")
    for i in range(no,0,-1):
        print(i,end=" ")

def pattern5(no):
    for i in range(1,no+1):
        print(i,"* "*i,end="")

def pattern6(row,col):
#    print(end="  ")
#    for i in range(col):
#        print(i+1,end=" ")
#   print()
    for i in range(row):
        print("* "*col)

def pattern7(row,col):
    for i in range(row):
        print(" {} ".format(i+1)*col,end=" ")
        print()

def pattern8(row,col):
    for i in range(row):
        for j in range(col):
            print(j+1,end=" ")
        print()

def pattern9(row,col):
    for i in range(row):
        print("*"*(i+1),end=" ")
        print()

def pattern10(row,col):
    for i in range(1,row+1):
        time.sleep(0.5)
        print(" "*(col-i)," *"*(i))

    for i in range(row,0,-1):
        time.sleep(0.5)
        print(" "*(col-i)," *"*(i))

def pattern11(row,col):
    for i in range(1,row+1):
        print(" "*(col-i),"*"*(i))

def pattern12(row,col):
    for i in range(row,0,-1):
        print(" "*(col-i),"*"*(i))

def pattern13(row,col):
    for i in range(row,0,-1):
        print("*"*(i)," "*(col-i),)
 
def pattern14(row,col):
    for i in range(row,0,-1):
        print("*"*i," "*(col - i)," "*(col-i),"*"*i)

pattern14(5,5)
