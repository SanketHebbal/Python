import os

def CheckExitance(filename):
        if(os.path.exists(filename)):
            return True
        else:
            return False

        
if __name__ == "__main__":

    filename = input("Enter a filename ->")

    if(CheckExitance(filename)):
        print("{} exits".format(filename))
    else:
        print("{} doesnot exits".format(filename))

    input("\nEnter a key ...")
