#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import csv


def get_book_num(bsObj):
    result = bsObj.find('div', id='search_meta')\
        .div.get_text().split(":")[2].split(" ")[1].replace(",","",3)
    return int(result)

def next_page(bsObj):
    host = "http://opac.ahlib.com/"
    next_page_url = bsObj.find("div", class_="meneame")\
        .find("a")['href'][0:-1]
    return host+next_page_url
    
def get_total_pages(bsObj):
    page_total = bsObj.find("span", class_="disabled").string[3:-1]
    return(int(page_total))

def open_new_page(url):
    r = urlopen(url)
    bsObj = BeautifulSoup(r.read(), "html.parser")
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

def get_all_book():

    ahlib_url="http://opac.ahlib.com/opac/search"

    param = {"q":"python",
            "searchWay":"title",
            "scWay":"dim",
            "searchSource":"reader"}
    
    r = requests.get(ahlib_url, param)
    bsObj = BeautifulSoup(r.text, "html.parser")
    pagenum = get_total_pages(bsObj)

    booknum = get_book_num(bsObj)
    print('----------------------')
    print('from %s find %d books.'%(ahlib_url, booknum))
    print('----------------------')

    rows = []    
    for j in range(pagenum):
        tb = bsObj.find('table', class_='resultTable')
        books = tb.find_all("tr")

        i = 0 
        for book in books:
            book_title = book.find("span").a.string.lstrip().rstrip().strip('/')
            book_id = book.find('span', class_='callnosSpan').string
            print("%4d %25s %s"%(j*10+i+1, book_id, book_title))
            rows.append((j*10+i+1, book_id, book_title))
            i += 1
        
        time.sleep(3)
        if j == pagenum-1:
            break 
        else:
            next_page_url = next_page(bsObj)
            bsObj = open_new_page(next_page_url+str(j+2))
    save_book(rows)

if __name__ == '__main__':
    get_all_book()    