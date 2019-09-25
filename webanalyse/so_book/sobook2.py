#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

import sys
sys.path.append('../')
from sqlhelper import sqlhelper1

BOOK_URL = "http://opac.ahlib.com/opac/api/holding/"
SEARCH_URL = "http://opac.ahlib.com/opac/search"
BOOKMETA_URL = 'http://api.interlib.com.cn:6699/interes/api/book/isbn/9787308090957/'

def open_new_page(url,book_name='python'):
    ''' 打开新的查询页面,传入关键词 book_name,默认书名为 python
        近回页面对象.
    ''' 

    param = {"q":book_name,"searchWay":"title"}

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Itel Max OS X 10-9-5)\
                             AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
               "Accept":"text/html, appliation/xhtml+xml, application/xml;\
                        q=0.9,image/webp,*/*;q=0.8"}

    r = requests.get(url, param, headers=headers)
    bsObj = BeautifulSoup(r.text, "html.parser")
    return bsObj


def open_new_page_url(url):

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Itel Max OS X 10-9-5)\
                             AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
               "Accept":"text/html, appliation/xhtml+xml, application/xml;\
                        q=0.9,image/webp,*/*;q=0.8"}

    r = requests.get(url, headers=headers)
    bsObj = BeautifulSoup(r.text, "html.parser")
    return bsObj


def get_total_pages(bsObj):
    ''' 返回查询结果页面数量
    '''
    page_total = bsObj.find("span", class_="disabled").string[3:-1]
    return int(page_total)

def get_book_num(bsObj):
    ''' 返回查找到的书的数量
    '''
    result = bsObj.find('div', id='search_meta')\
        .div.get_text().split(":")[2].split(" ")[1].replace(",","",3)
    return int(result)

def next_page(bsObj, url):
    ''' 返回下一页的网址
    '''
    if "ah" in url:
        host = "http://opac.ahlib.com"
    else:
        host = "http://opac.hflib.gov.cn"
    next_page_url = bsObj.find("div", class_="meneame").find("a")['href'][0:-1]

    return host + next_page_url

def save_book(rows):
    ''' 保存为CSV格式文件
    '''
    csvFile = open("books.csv", "w+")
    try:
        writer = csv.writer(csvFile)
        writer.writerow(('No.', 'Book_id', 'Book_name'))
        for row in rows:
            writer.writerow(row)
    finally:
        csvFile.close()

def save_book_to_db(rows):
    ''' 保存为数据库文件
    '''
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

def get_book_code(bsObj):
    books_trs = bsObj.find('table', calss_='resultTable')
    return books_trs

def get_book_total_num(lib_url, book_name):
    ''' 获取图书检索系统中名称中包含bookd_name的书的数量
    '''
    bsObj = open_new_page(lib_url, book_name)
    return get_book_num(bsObj)

def get_book_isbn(bsObj):
    isbn = bsObj.find("img", class_="bookcover_img")['isbn']
    return isbn

def get_all_book(lib_url,book_name):
    ''' 获取图书检索系统中名称包含bookd_name的所有的书
    '''
    bsObj = open_new_page(lib_url,book_name)
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

        if j == pagenum - 1:
            break 
        else:
            next_page_url = next_page(bsObj, lib_url)
            bsObj = open_new_page(next_page_url+str(j+2))
#    save_book(rows)
    save_book_to_db(rows)

def get_book_state(book_url):
    ''' 从指定图书页面book_url,查询本书当前状态
        返回:条码代号,在馆状态
    '''
    r = open_new_page(book_url)
    data = json.loads(r.text)
    books = data["holdingList"]
    states = data["holdStateMap"]
    localmaps = data['localMap']

    text = "其中,第 1 本,共有 %d 个副本"%len(books)
    for book in books:
        book_sum = len(books)
        bs = book['state']
        cl = book['curlocal']

        book_state = states[str(bs)]['stateName']
        book_local = localmaps[str(cl)]
 #       print(book['barcode'], book_state, book_local)
        text = text + "," + book['barcode'] + "," + book_state + "," + book_local
    return text


def get_book_and_num(ahlib_url,book_name):
    ''' 返回书名、查到的数量
    '''
    n = get_book_total_num(ahlib_url,book_name)
    text =  "关于 %s 的书，共有 %d 本."%(book_name, n)
    return text

def get_book_barcode(ahlib_url, book_name):
    bsObj = open_new_page(ahlib_url, book_name)
    inputs = bsObj.find_all("input")
    isbn = get_book_isbn(bsObj)
    print(isbn)

    books_code = []
    for i in inputs:
        if i['type'] == "checkbox":
            books_code.append(i['value'])
    
    return books_code[0]

def get_book(bookname):
    txt1 = get_book_and_num(SEARCH_URL, bookname)
    barcode = get_book_barcode(SEARCH_URL, bookname)
    txt2 = get_book_state(BOOK_URL + barcode)
#    print(txt1+txt2)
    return txt1 + txt2, BOOK_URL + barcode

if __name__ == '__main__':

    print(get_book("朱自清"))
