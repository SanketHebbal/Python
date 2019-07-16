import threading

print("---- Marvellous Infosystems by Piyush Khairnar-----")
print("Demonstration of Multithreading")

def fun(number):
    for i in range(number):
        print(i)
def gun(number):
    for i in range(number):
        print(i)

if __name__ == "__main__":
    number = 5
    thread1 = threading.Thread(target=fun, args=(number,))
    thread2 = threading.Thread(target=gun, args=(number,))
    # Will execute both in parallel
    thread1.start()
    thread2.start()
# Joins threads back to the parent process, which is this
# program
    thread1.join()
    thread2.join()
