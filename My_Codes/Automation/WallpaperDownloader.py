import requests
import bs4
import os
import requests
from urllib.parse import urlparse
import sys
import subprocess,io

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

def MarvellousDownload(url,foldername):

    allowed = is_downloadable(url)

    if allowed:
        try:
            res = requests.get(url,allow_redirects = True)

            filename = get_filename(url)
            filename = os.path.join(foldername,filename)
            fd = open(filename,'wb')
            for buffer in res.iter_content(1024):
                fd.write(buffer)
            fd.close()
            return True
        except Exception as e:
            return False

def FetchContents(url,keyword):

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')

    foldername = "Pics/"+keyword
    
    try:
        os.makedirs(foldername)
        
    except Exception as e:
        print("Error :"+foldername+" already created")
        exit()

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
        
    t = soup.findAll("li",{"class":"wallpapers__item"})   
    for i in t:
        url = i.a.span.img['src']
        MarvellousDownload(url,foldername)        

    subprocess.run(['explorer', os.path.realpath(foldername)])

def get_keyword():
    return sys.argv[1]

def main():

    if len(sys.argv) == 1:
        print(sys.argv[0]+" -h\tfor help")
        print(sys.argv[0]+" -u\tfor usage")
        exit()
        
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "-h":
            print("\nThis script download the Wallpapers for the given keyword")
            exit()
            
        elif sys.argv[1].lower() == "-u":
            print("\n"+sys.argv[0]+" Search")
            exit()
            
    keyword = get_keyword()
    url="https://wallpaperscraft.com/search/?order=&page=1&query="+keyword+"&size=1600x1200"

    FetchContents(url,keyword)
        
if __name__ == "__main__":
    main()
