import sys
import os
import hashlib
import schedule
import time
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

def AddAttachments(Information):

    msg = MIMEMultipart()
    msg['From'] = "sankethebbal100@gmail.com"
    msg['To'] = sys.argv[3]
    msg['Subject'] = "Marvellous Logger created at : "+time.ctime()

    body = """

    Hello %s,
    Welcome to Marvellous Infosystem
    Please find the attached document which contains Log of Running Process.
    Log file is created at :%s

    Start time of scanning :%s
    Total files scanned :%s
    Duplicate files :%s


    This is auto generated mail.

    Thanks & Regards,
    Sanket Hebbal
    Marvellous Infosystem
    """%(sys.argv[3].split('@')[0],time.ctime(),Information["start time"],Information["Files scanned"],Information["Duplicate files"])
    
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(os.path.abspath(Information["File Descriptor"].name), "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % Information["File Descriptor"].name)
    msg.attach(p) 
    
    return msg.as_string()

def SendMail(Information):

    username = 'sankethebbal100@gmail.com'
    password = 'sanketmcs18'
    to = sys.argv[3]    

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(username,password)
    email_text = AddAttachments(Information)
    server.sendmail(username,to,email_text)
    server.close()


def CreateHeader(fd):

    lines = "-"*100+"\n"
    header = "\t\t\t\t\tMarvellous Infosystems\n"
    fd.write(lines)
    fd.write(header)
    fd.write("\nFile created at : %s \n"%(time.ctime()))
    fd.write(lines)

def CreateLog(directory):

    if os.path.exists(directory) == False:
        os.mkdir(directory)
    filename = os.path.join(directory,"MarvellousLog%s.log"%(time.ctime()))
    filename = filename.replace(' ','_')
    filename = filename.replace(':','_')

    fd = open(filename,"w")
    print("File created")
    CreateHeader(fd)
    return fd

def checksum(file):
    return hashlib.md5(open(file,"rb").read()).hexdigest()

def FindDuplicate():

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    
    Information = {"start time":current_time , "Files scanned":0 , "Duplicate files":0}
    print(Information)
    directory = sys.argv[1]

    if os.path.exists(directory):
        if os.path.isdir(directory):
            if os.path.isabs(directory) == False:
                directory = os.path.abspath(directory)

            checksumdic = {}
            
            contents = os.listdir(directory)
            for content in contents:
                if os.path.isfile(os.path.join(directory,content)):
                    result = checksum(os.path.join(directory,content))
                    Information["Files scanned"] += 1
                    if result in checksumdic:
                        checksumdic[result].append(os.path.join(directory,content))
                        Information["Duplicate files"] += 1
                    else:
                        checksumdic[result] = [os.path.join(directory,content)]

            Information["File Descriptor"] = CreateLog("Marvellous")
            DeleteDuplicate(checksumdic , Information)
        else:
            print("\n"+directory+" is not a directory")
    else:
        print("\n"+directory+" directory doesnot exists") 

def DeleteDuplicate(checksums,Information):

    for key in checksums:
        if len(checksums[key]) > 1:
            for i in range(1,len(checksums[key])):
                Information["File Descriptor"].write(checksums[key][i]+"\n")
                os.remove(checksums[key][i])
    Information["File Descriptor"].close()
    print("Sending mail...")
    SendMail(Information)
    print("Mail sent")
    
def main():

    if len(sys.argv) == 1:
        print(sys.argv[0]+" -h for help")
        print(sys.argv[0]+" -u for usage")
        exit()

    if len(sys.argv) == 2:

        if sys.argv[1].lower() == "-u":
            print("Usage :"+sys.argv[0]+" DirectoryName"+" TimeInterval"+" MailID")
            exit()

        if sys.argv[1].lower() == "-h":
            print("This script delelte the duplicate files from the specified directory , creates a log file of deleted files and mail it to specified mailid")
            exit()

    if len(sys.argv) == 4:

        try:
            schedule.every(float(sys.argv[2])).minutes.do(FindDuplicate)

            while True:
                schedule.run_pending()

        except Exception as e:
            print("Error :",e)
    else:
        print("Invalid number of parameters")
        exit()
        
if __name__ == "__main__":
    main()
