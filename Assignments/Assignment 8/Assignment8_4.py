import threading

def DisplaySmall(string):

    for i in  range(len(string)):
        if(string[i].islower()):
           print("S->",string[i])

def DisplayCapital(string):

    for i in  range(len(string)):
        if(string[i].isupper()):
           print("C->",string[i])

def DisplayDigit(string):

    for i in range(len(string)):
        if(string[i].isdigit()):
            print("D->",string[i])


if __name__ == "__main__":

    string = input("Enter a string ->")
    t1 = threading.Thread(target=DisplaySmall , args=(string,))
    t2 = threading.Thread(target=DisplayCapital , args=(string,))
    t3 = threading.Thread(target=DisplayDigit , args = (string,))

    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()


    print("End of main \n\n\n\n")
    input("enter a key ....")
    
