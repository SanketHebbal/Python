import os
import sys
import hashlib



def checksum(file):
    return hashlib.md5(open(file,"rb").read()).hexdigest()
    
def displaychecksum(directory):

    if os.path.exists(directory):
        if os.path.isdir(directory):
            if os.path.isabs(directory) == False:
                directory = os.path.abspath(directory)

            for folder,subfolder,files in os.walk(directory):
                for file in files:
                    print(os.path.join(os.path.abspath(directory),file)+"   "+checksum(os.path.join(os.path.abspath(directory),file)))
        else:
            print("\n"+directory+" is not a directory")
    else:
        print("\n"+directory+"directory doesnot exists") 



def main():

    if len(sys.argv)<1 or len(sys.argv)>2:
        print("\nInvaild number of parameters")
        exit()

    if len(sys.argv) == 1:
        print(sys.argv[0]+" -h for help")
        print(sys.argv[0]+" -u for usage")
        exit()

    if sys.argv[1].lower() == "-u":
        print("\n"+sys.argv[0]+" DirectoryName")
        exit()

    if sys.argv[1].lower() == "-h":
        print("\nThis script display the checksum of files in specified directory")
        exit()

    try:
        displaychecksum(sys.argv[1])
    except Exception as e:
        print("Error :",e)

if __name__ == "__main__":

    main()
