from MarvellousNum import *
import threading


def EvenFactor(number):

    for i in range(1,(number//2)+1):
        if(number % i == 0):
            if(Even(i)):
                print("Even factor" , i)

def OddFactor(number):

    for i in range(1,(number//2)+1):
        if(number % i == 0):
            if(Even(i) == False):
                print("Odd factor",i)



if __name__ == "__main__":

    number = int(input("Enter the number ->"))
    
    evenfactor = threading.Thread(target=EvenFactor,args=(number,))
    oddfactor = threading.Thread(target=OddFactor,args=(number,))



    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("Exit for Main")
    input()
