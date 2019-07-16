from MarvellousNum import Even
import threading

def DisplayEven(numbers):

    sum = 0
    for i in range(len(numbers)):
        if(Even(numbers[i])):
            sum = sum + numbers[i]
    print("Even number addition ",sum)
    
def DisplayOdd(numbers):

    sum = 0
    for i in range(len(numbers)):
        if(Even(numbers[i]) == False):
            sum = sum + numbers[i]
    print("Odd number addition ",sum)


def Accept():

    arr = list()
    size = int(input("Enter how many elements you want ->"))

    for i in range(size):
        num = int(input("Enter {} number ->".format(i)))
        arr.append(num)
                  
    return arr
                  
if __name__ == "__main__":


    numbers = Accept()
    t1 = threading.Thread(target=DisplayEven,args=(numbers,))
    t2 = threading.Thread(target=DisplayOdd,args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit for main")
    input("Enter a key")
