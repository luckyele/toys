#-*- coding:utf-8 -*-
#!/usr/bin/python3

import sqlhelper1
from bs4 import BeautifulSoup
import requests
import time


class Web:
    def __init__(self):
        self.bsObj = None
         
    def open(self, page_url):
        r = requests.get(page_url)
        
        # requests package guess encoding content of page_url, sometime it will
        # be wrong. so must set response encoding to 'utf-8'
        r.encoding = 'utf-8'
        
        self.bsObj = BeautifulSoup(r.text, "html.parser")
        return self.bsObj

    def find(self):
        pass

    def save(self, rows):
        db = "web_mct.db"
        tb = "ggwh"

        sql = sqlhelper1.SQLite(db, tb)
        sql.create_table()

        for row in rows:
            r = "\"%s\",\"%s\""%(row[0],row[1])
            sql.insert_record(r)

        sql.select_all()
        sql.close()

def get_book_num(bsObj):
    result = bsObj.find('div', id='search_meta')\
        .div.get_text().split(":")[2].split(" ")[1].replace(",","",3)
    return int(result)

def next_page(bsObj, url):
    if "ah" in url:
        host = "http://opac.ahlib.com"
    else:
        host = "http://opac.hflib.gov.cn"
    next_page_url = bsObj.find("div", class_="meneame")\
        .find("a")['href'][0:-1]
    return host+next_page_url
    
def get_total_pages(bsObj):
    page_total = bsObj.find("span", class_="disabled").string[3:-1]
    return int(page_total)


def get_book_msg(bsObj):

    book_title = bsObj.find("span",class_= "bookmetaTitle")\
                .a.string.lstrip().strip('/').rstrip()
    book_id = bsObj.find("span", class_="callnosSpan").string
    return book_id, book_title.encode('utf-8')
    
def get_all_book(lib_url):

    bsObj = open_new_page(lib_url)
    pagenum = get_total_pages(bsObj)
    booknum = get_book_num(bsObj)

    print('----------------------')
    print('from %s find %d books.'%(lib_url, booknum))
    print('----------------------')

    rows = []    
    for j in range(pagenum):
        tb = bsObj.find('table', class_='resultTable')
        books = tb.find_all("tr")

        i = 0 
        for book in books:
            book_id, book_title = get_book_msg(book)
            print("%4d %25s %s"%(j*10+i+1, book_id, book_title.decode('utf-8')))
            rows.append((j*10+i+1, book_id, book_title))
            i += 1
        
        time.sleep(5)

        if j == pagenum-1:
            break 
        else:
            next_page_url = next_page(bsObj, lib_url)
            bsObj = open_new_page(next_page_url+str(j+2))


def get_msg():
    rows=[] 
    row = []

    web_site = "http://www.mct.gov.cn/" 
    page_url = "http://www.mct.gov.cn/whzx/bnsj/ggwhs"
    w = Web()
    obj = w.open(page_url)
    tb =  obj.find("table", class_="lm_tabe")
    
    articles = tb.find_all("tr")

    for article in articles:
    #    time = article.find('td', class_="bt_time").string
        row.append(web_site + article.td.a['href'][2:])
        row.append(article.td.a['title'])
        rows.append(row)
        row = []

    w.save(rows)


if __name__ == "__main__":
    get_msg()


