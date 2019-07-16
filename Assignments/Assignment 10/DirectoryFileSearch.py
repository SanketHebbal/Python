import os
import sys


def DirecortyTraversal(directory,extension):

    if(os.path.exists(directory)):
        if(os.path.isdir(directory)):
            if(os.path.isabs(directory) == False):
                directory = os.path.abspath(directory)

            for folder,subfolder,file in os.walk(directory):
                for filename in file:
                    if filename.endswith(extension):
                        print(filename)
        else:
            print(directory+" is not a directory")
    else:
        print(directory+" doesnot exist")

        
        
def main():

    if len(sys.argv) == 1:
        print("\n Use "+sys.argv[0]+" -h for help")
        print("\n Use "+sys.argv[0]+" -u for usage")
        exit()
        
    if(sys.argv[1].lower() == "-h"):
        print("\nThis automation script which display the files of specified extension")
        exit()

    if(sys.argv[1].lower() == "-u"):
        print("\n"+sys.argv[0]+" DirectoryName Extenion")
        exit()

    if(len(sys.argv)!=3):
        print("\nInvalid number of parameters")
        exit()

    try:
        DirecortyTraversal(sys.argv[1],sys.argv[2])

    except Exception as e:

        print("Error :",e)
        
              

if __name__ == "__main__":
    main()
