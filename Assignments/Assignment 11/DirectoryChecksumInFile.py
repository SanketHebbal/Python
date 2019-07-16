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

            checksumdic = {}
            
            contents = os.listdir(directory)
            for content in contents:
                if os.path.isfile(os.path.join(directory,content)):
                    result = checksum(os.path.join(directory,content))
                    
                    if result in checksumdic:
                        checksumdic[result].append(os.path.join(directory,content))
                    else:
                        checksumdic[result] = [os.path.join(directory,content)]

            WriteIntoFile(checksumdic)
            
        else:
            print("\n"+directory+" is not a directory")
    else:
        print("\n"+directory+"directory doesnot exists") 

def WriteIntoFile(checksums):

    fd = open("Dulplicate.txt","w")

    for key in checksums.keys():
        if len(checksums[key]) > 1:
            for file in checksums[key]:
                fd.write(file+"\n")
        


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
        print("\nThis script write the checksum of duplicate files of  specified directory into duplicate.txt ")
        exit()

    try:
        displaychecksum(sys.argv[1])
    except Exception as e:
        print("Error :",e)

if __name__ == "__main__":

    main()
