import requests, lxml
from bs4 import BeautifulSoup
import operator

website = 'http://www.csie.ncku.edu.tw/ncku_csie/depmember/teacher'
csie_url = "http://www.csie.ncku.edu.tw/ncku_csie"

def search_url(name):
    r = requests.get(website)
    r.encoding = 'utf-8'
    if r.status_code == requests.codes.ok:
        """
        print("encoding: %s" % r.encoding)
        print("content: \n%s"% r.text)
        """
        soup = BeautifulSoup(r.text,'html.parser')
        tag = soup.find_all("span",class_="content_title2")
        for item in tag:
            if operator.eq(item.string,name):
                tag2 = item.find_next_sibling("p")
                tag3 = tag2.find_all("a")
                url = tag3[0].get('href')
                return url
                break
        
def search_image(name):
    r = requests.get(website)
    r.encoding = 'utf-8'
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'html.parser')

    tag_image = soup.find("img",alt=name)
    src = tag_image.get('src')
    src = csie_url + src[2:len(src)]
    return src

def search_name(name):
    r = requests.get(website)
    r.encoding = 'utf-8'
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'html.parser')
    tag_image = soup.find("img",alt=name)
    if not tag_image:
        return False
    else:
        return True

    
#print(search_url("李家"))
#print(search_url("李家岩"))
#print(search_image("李家岩"))
