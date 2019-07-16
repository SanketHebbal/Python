import sys
import time
import os
import psutil
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import urllib.request



def CreateHeader(fd):

    lines = "-"*100+"\n"
    header = "\t\t\t\t\tMarvellous Infosystems\n"
    fd.write(lines)
    fd.write(header)
    fd.write("\nFile created at : %s \n"%(time.ctime()))
    fd.write(lines)


def ProcessInformation():

    processInfo = list()

    for proc in psutil.process_iter():
        try:
            
           info = proc.as_dict(attrs=['pid','name','username'])
           processInfo.append(info)
           
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return processInfo

def CreateLogFile(directory):

    if os.path.isdir(directory) == False:
        os.mkdir(directory)
        
    filename = os.path.join(directory,"MarvellousLog%s.log"%(time.ctime()))
    filename = filename.replace(":","_")
    filename = filename.replace(" ","_")
    fd = open(filename,"w+")

    CreateHeader(fd)
    for procInfo in ProcessInformation():
        fd.write("%s\n"%(procInfo))

    fd.close()

    SendMail(filename)

    
def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        exit()

    if sys.argv[1].lower() == "-u":
        print("Usage :"+sys.argv[0]+" "+"directory path")
        exit()

    if sys.argv[1].lower() == "-h":
        print("This script create a log file in the specified directory which contains the information of all running process")
        exit()

    try:
        CreateLogFile(sys.argv[1])
    except Exception as e:
        print("Error :",e)



if __name__ == "__main__":
    main()
