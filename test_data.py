import sqlite3
import requests, lxml
from bs4 import BeautifulSoup

website = 'http://www.csie.ncku.edu.tw/ncku_csie/depmember/teacher'


conn = sqlite3.connect('Database/ChatBot.db')
c=conn.cursor()

def search_all():
    r = requests.get(website)
    r.encoding = 'utf-8'
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'html.parser')
    tag = soup.find_all("span",class_="content_title2")
    for item in tag:
        tag2 = item.find_all("a")
        for href in tag2:
            temp = href.get('href')
            temp = temp[17:len(temp)]
            t = int(temp)
            name = href.string
            c.execute("SELECT ID FROM Teacher WHERE ID = %d" % t)
            value = c.fetchall()
            if not value:
                last = name[0]
                first = name[1:3]
                c.execute("INSERT INTO Teacher VALUES (" + temp +",'"+ last +"','"+first+"')")
                conn.commit()

        

#c.execute("CREATE TABLE Teacher (ID var(20) primary key,Last_name text,First_name text)")
#search_all()

def search_last_name(text):
    conn = sqlite3.connect('Database/ChatBot.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Teacher WHERE Last_name = '"+text+"'")
    value = c.fetchall()
    list = ""
    for index in range(len(value)):
        list = list + value[index][1] + value[index][2] + " \ "
    c.close()
    conn.close()
    return list

#print(search_last_name("李"))
