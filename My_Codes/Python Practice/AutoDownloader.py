import os
import requests
from urllib.parse import urlparse

def is_downloadable(url):

    r = requests.head(url,allow_redirects=True)
    header = r.headers
    
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    elif 'html' in content_type.lower():
        return False
    else:
        return True

def get_filename(url):

    a = urlparse(url)
    return os.path.basename(a.path)

def MarvellousDownload(url):

    allowed = is_downloadable(url)

    if allowed:

        try:

            res = requests.get(url,allow_redirects = True)

            filename = get_filename(url)
            fd = open(filename,'wb')
            print("Filecreated")
            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True
        except Exception as e:
            print("Error ",e)
            return False


def main():

    #url = "https://funksyou.com/fileDownload/Songs/128/32878.mp3"
    url1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Sachin_Tendulkar_at_MRF_Promotion_Event.jpg/260px-Sachin_Tendulkar_at_MRF_Promotion_Event.jpg"
    result = MarvellousDownload(url1)
    
    if result:
        print("File downloaded")
    else:
        print("File couldn't be downloaded")


if __name__ == "__main__":
    main()
