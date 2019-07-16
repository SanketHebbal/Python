import threading

def DisplayNumbers(number):

    for i in range(1,number+1):
        print(i)

def DisplayReverse(number):

    for i in range(number,0,-1):
        print(i)

if __name__ == "__main__":


    number = int(input("Enter a number ->"))
    
    t1 = threading.Thread(target = DisplayNumbers , args = (number,))
    t2 = threading.Thread(target = DisplayReverse , args = (number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main\n\n\n\n")

    input("Enter a key ....")
