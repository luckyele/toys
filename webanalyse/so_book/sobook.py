#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import csv
import voice1

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

def open_new_page(url, keyword):
    param = {"q":keyword,"searchWay":"title"}

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

def get_book_msg(bsObj):

    book_title = bsObj.find("span",class_= "bookmetaTitle")\
                .a.string.lstrip().strip('/').rstrip()
    book_id = bsObj.find("span", class_="callnosSpan").string
    return book_id, book_title
    
def get_all_book(lib_url, keyword):

    bsObj = open_new_page(lib_url, keyword)
    pagenum = get_total_pages(bsObj)
    booknum = get_book_num(bsObj)
    
    txt = '我们从安徽省图书馆找到 %d 本关于 %s 的书.'%(booknum, keyword)
    print(txt)
    return txt
'''
    rows = []    
    for j in range(pagenum):
        if j > 1: break
        tb = bsObj.find('table', class_='resultTable')
        books = tb.find_all("tr")

        i = 0 
        for book in books:
            book_id, book_title = get_book_msg(book)
            print("%4d %25s %s"%(j*10+i+1, book_id, book_title))
            rows.append((j*10+i+1, book_id, book_title))
            i += 1
        time.sleep(5)

        if j == pagenum-1:
            break 
        else:
            next_page_url = next_page(bsObj, lib_url)
            bsObj = open_new_page(next_page_url+str(j+2), keyword)
    save_book(rows)
'''

if __name__ == '__main__':
   
    ahlib_url="http://opac.ahlib.com/opac/search"
    hflib_url="http://opac.hflib.gov.cn/lib2/search"
    c = voice1.voice_init()
    text1 = "请看屏幕提示，说出您要找的书名或者作者姓名"
    voice1.play_voice(c,text1)

    while True:
        kw = voice1.voice_input(c)
        text = get_all_book(ahlib_url, kw)
        voice1.play_voice(c,text)
