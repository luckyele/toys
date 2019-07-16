#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import csv
import sys
#sys.path.append('../')

from sqlhelper import sqlhelper1

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

def open_new_page(url):
    param = {"q":"python","searchWay":"title"}

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Itel Max OS X 10-9-5)\
                             AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
               "Accept":"text/html, appliation/xhtml+xml, application/xml;\
                        q=0.9,image/webp,*/*;q=0.8"}

    r = requests.get(url, param, headers=headers)
    bsObj = BeautifulSoup(r.text, "html.parser")
    return bsObj

def save_book(rows):
    csvFile = open("books.csv", "w+")
    try:
        writer = csv.writer(csvFile)
        writer.writerow(('No.', 'Book_id', 'Book_name'))
        for row in rows:
            writer.writerow(row)
    finally:
        csvFile.close()

def save_book_to_db(rows):    
    db_name = "booklib.db"
    tb_name = "book_python"

    sql = sqlhelper1.SQLite(db_name, tb_name)
    sql.create_table()

    for row in rows:
        if row[1] is None:
            r = "\"\",\"" + row[2].decode('utf-8') + "\""
        else:
            r = "\"" + row[1] + "\"" + "\""+ row[2].decode('utf-8') + "\"" 
        sql.insert_record(r)
    
    sql.select_all()
    sql.close()

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
#    save_book(rows)
    save_book_to_db(rows)

if __name__ == '__main__':
   
    ahlib_url="http://opac.ahlib.com/opac/search"
    hflib_url="http://opac.hflib.gov.cn/lib2/search"
    get_all_book(hflib_url)   
