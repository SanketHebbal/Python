import imaplib,email

username = "sankethebbal100@gmail.com"
password = "sanketmcs18"
imap_url = 'imap.gmail.com'

def get_body(msg):

    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)


def search(key,value,con):

    result,data = con.search(None,key,'"{}"'.format(value))
    return data

def get_emails(result_bytes):

    msgs = []
    for num in result_bytes[0].split():
        typ,data = con.fetch(num,'(RFC822)')
        msgs.append(data)

    return msgs
    
con = imaplib.IMAP4_SSL(imap_url)
con.login(username,password)
con.select('INBOX')

result,data = con.fetch(b'8','(RFC822)')
raw = email.message_from_bytes(data[0][1])
print(get_body(raw))
