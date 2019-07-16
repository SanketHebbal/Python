import smtplib
import time
import urllib.request


def is_connected():

    try:
        urllib.request.urlopen("http://google.com",timeout=1)
        return True
    except Exception as e:
        print("Error :",e)
        return False

def SendMail(username,password):

    to = ['sankethebbal100@gmail.com','sanketshebbal@gmail.com']

    email_text = 'hello world'

    try:

        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(username,password)
        print(server.sendmail(username,to,email_text))
        server.close()

        print("Mail sent")
        
    except Exception as e:
        print("Unable to send",e)


def main():


    connection = is_connected()

    if connection:
        starttime = time.time()
        username = '--------------------------'
        password = '-----------------------'
        
        SendMail(username,password)

        endtime = time.time()

        print("Time require ",(endtime-starttime))

    else:

        print("No internet connection")


if __name__ == "__main__":
    main()
