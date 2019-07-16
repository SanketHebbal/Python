import os
import sys


def ChangeExtension(directory,extension1,extension2):

    if os.path.exists(directory):
        if os.path.isdir(directory):
            if os.path.isabs(directory) == False:
                directory = os.path.abspath(directory)

            for folder,subfolders,files in os.walk(directory):
                for file in files:
                    if file.endswith(extension1):
                        os.rename(folder+"\\"+file,'.'.join([folder+"\\"+file.split('.')[0],extension2]))
        else:
            print(directory+" is not a directory")
    else:
        print(directory+" doesnot exists")

        
def main():

    if len(sys.argv) == 1:
        print("\n"+sys.argv[0]+" -h for help")
        print("\n"+sys.argv[0]+" -u for usage")
        exit()
        
    if sys.argv[1].lower() == "-h":
        print("\n This automation scrpit change the file extension from the folder by the file extension provided it")
        exit()

    if sys.argv[1].lower() == "-u":
        print("\n"+sys.argv[0]+" DirectoryName FileExtenionToBeChange FileExtenionToBeChangedWith")
        exit()

    if len(sys.argv) != 4:
        print("\nInvalid number of parametes")
        exit()

    try:
        ChangeExtension(sys.argv[1],sys.argv[2],sys.argv[3])
    except Exception as e:
        print("Error :",e)
        

if __name__ == "__main__":

    main()
