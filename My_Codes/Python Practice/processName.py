import psutil
import os
import schedule
import datetime
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import urllib.request


def is_connected():

    try:
        urllib.request.urlopen("http://google.com",timeout=5)
        return True
    except Exception as e:
        print("Error :",e)
        return False


def AddAttachments():

    msg = MIMEMultipart()
    msg['From'] = "sankethebbal100@gmail.com"
    msg['To'] = "marvellousinfosystem@gmail.com"
    msg['Subject'] = "Send a processlog file"

    body = "This file contains the log of all the currently running process in your system"
    msg.attach(MIMEText(body, 'plain'))


    filename = "ProcessLog.txt"
    attachment = open(os.path.abspath(filename), "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p) 
    
    return msg.as_string()

    
def SendMail(username,password):

    to = 'marvellousinfosystem@gmail.com'    
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(username,password)
    email_text = AddAttachments()
    server.sendmail(username,to,email_text)
    server.close()

    print("Mail sent")


def CreateHeader(fd):

    lines = "-"*100+"\n"
    header = "\t\t\t\t\tMarvellous Infosystems\n"
    fd.write(lines)
    fd.write(header)
    fd.write("\nFile created at : "+str(datetime.datetime.now())+"\n")
    fd.write(lines)
    
def KeepTrack():

    fd = open("ProcessLog.txt" , "a")
    CreateHeader(fd)
    
    for process in psutil.process_iter():
        fd.write(process.name()+" "+str(process.cpu_percent())+"\n")
    fd.close()


def Job():

    connection = is_connected()

    if connection:
        SendMail("sankethebbal100@gmail.com","sanketmcs18")
    else:
        print("No internet connection")

    
def main():

    try:
        schedule.every(0.1).minutes.do(KeepTrack)
        #schedule.every().day.at("13:07").do(Job)
        
        while True:
            schedule.run_pending()
    
    except Exception as e:
        print("Error :",e)
        
if __name__ == "__main__":
    main()
