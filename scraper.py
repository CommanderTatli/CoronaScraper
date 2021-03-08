END = 303

from requests_html import HTMLSession
import time

def getPage(url):
    global session
    r = session.get(url)
    r.html.render()
    dead = r.html.find('.odd', first=False)
    dead += r.html.find('.even', first=False)
    return dead

session = HTMLSession()
urls = ['https://koronavirus.gov.hu/elhunytak']
for i in range(1, END+1):
    urls.append('https://koronavirus.gov.hu/elhunytak?page='+str(i))

with open("dead.csv", "a", encoding="utf-8") as file:
    for i in range(len(urls)):
        print(i+1, "/", END+1)
        records = getPage(urls[i])
        for r in records:
            file.write(r.text.replace("\n", ";")+"\n")
        time.sleep(1)
        file.flush()
