import os
import sys
import shutil


def directoryrename(directory1,directory2):

    if os.path.exists(directory1):
        if os.path.isdir(directory1):
            if os.path.isabs(directory1) == False:
                directory1 = os.path.abspath(directory1)

            os.makedirs(directory2)
            
            for file in os.listdir(directory1):
                if os.path.isfile("\\".join([os.path.abspath(directory1),file])):
                    shutil.copy(os.path.abspath(directory1)+"\\"+file,os.path.abspath(directory2)+"\\"+file)
                
        else:
            print(directory1+" is not a directory")
    else:
        print(directory1+" doesnot exists")

def main():

    if len(sys.argv) == 1:
        print("\n"+sys.argv[0]+" -h for help")
        print("\n"+sys.argv[0]+" -u for usage")
        exit()

    if sys.argv[1].lower() == "-h":
        print("\n This scrpit copy the files from one folder to another folder")
        exit()
    if sys.argv[1].lower() == "-u":
        print("\n"+sys.argv[0]+" DirectoryNameToBeCopied NewDirectoryName")
        exit()
    if len(sys.argv) != 3:
        print("\n Invaild number of arguments")
        exit()

    try:
        directoryrename(sys.argv[1],sys.argv[2])

    except Exception as e:
        print("Error : ",e)
        

if __name__ == "__main__":

    main()
