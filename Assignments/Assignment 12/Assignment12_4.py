import os
import sys
import time
import psutil
import smtplib
import urllib.request
from email import encoders
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 


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


def AddAttachments(filename):

    msg = MIMEMultipart()
    msg['From'] = "sankethebbal100@gmail.com"
    msg['To'] = sys.argv[2]
    msg['Subject'] = "Marvellous Process Logger"

    body = "This file contains the information of all the currently running process in your system"
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(os.path.abspath(filename), "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p) 
    
    return msg.as_string()

def SendMail(filename):

    username = 'sankethebbal100@gmail.com'
    password = '---------'
    to = sys.argv[2]    

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(username,password)
    email_text = AddAttachments(filename)
    server.sendmail(username,to,email_text)
    server.close()
    
    print("Mail sent to "+to)

    
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
