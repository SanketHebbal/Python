import threading

def EvenFun():
    for i in range(2,2*11,2):
        print("Even",i)

def OddFun():
    for i in range(1,2*11,2):
        print("Odd",i)


if __name__ == "__main__":

    t1 = threading.Thread(target=EvenFun,args=())
    t2 = threading.Thread(target=OddFun,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    input()
