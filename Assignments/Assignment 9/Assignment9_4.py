import sys


if __name__ == "__main__":

    fd1 = open(sys.argv[1],'r')
    buffer1 = fd1 .read()
    fd1.close()

    fd2 = open(sys.argv[2], 'r')
    buffer2 = fd2.read()
    fd2.close()

    if (buffer1 == buffer2):
        print("Success")
    else:
        print("Failure")
