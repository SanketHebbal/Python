import sys

if __name__ == "__main__":

        filename = sys.argv[1]
        fd1 = open(filename,'r')
        data = fd1.read()
        fd1.close()

        fd1 = open("DemoCopy1.txt",'w')
        fd1.write(data)
        fd1.close()

