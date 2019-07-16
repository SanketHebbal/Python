import sys
import os
import shutil


def DirectoryCopyExt(directory1,directory2,extension):

    if os.path.exists(directory1):
        if os.path.isdir(directory1):
            if os.path.isabs(directory1) == False:
                directory1 = os.path.abspath(directory1)

            os.makedirs(directory2)
            
            for file in os.listdir(directory1):
                if os.path.isfile(os.path.abspath(directory1)+"\\"+file):
                    if file.endswith(extension):
                        shutil.copy(os.path.abspath(directory1)+"\\"+file,os.path.abspath(directory2)+"\\"+file)
                
        else:
            print(directory1+" is not a directory")
    else:
        print(directory1+" doesnot exists")
        

def main():

    if sys.argv[1].lower() == "-h":
        print("\n This script copy all files with the specified extension from first directory into second directory")
        exit()

    if sys.argv[1].lower() == "-u":
        print("\n"+sys.argv[0]+" Directory1 Directory2 Extension")
        exit()

    if len(sys.argv) != 4:
        print("Invalid number of paramenters")
        exit()

    try:

        DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])

    except Exception as e:
        print("Error :",e)
        
if __name__ == "__main__":

    main()
