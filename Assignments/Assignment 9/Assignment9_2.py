import os


def acceptFile():

    filename = input("Enter a filename ->")

    if os.path.exists(filename):
        return filename
    else :
        return -1

if __name__ == "__main__":

    filename = acceptFile()

    if filename == -1:
        print("file doesnot exist")
    else:
        fd = open(filename,"r")
        data = fd.read()
        print(data)

    input("\n\nEnter a key ...")
