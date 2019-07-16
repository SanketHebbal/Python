import smtplib

content = "Hello from sanket hebbal"

mail = smtplib.SMTP('smtp.gmail.com',25)

mail.ehlo()

mail.login('sankethebbal100@gmail.com','sanketmcs18')

mail.sendmail('sankethebbal100gmail.com','sankethebbal100@gmail.com',content)

mail.close()
