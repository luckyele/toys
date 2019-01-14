#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

class Web:
    def __init__(self):
        self.url = ''
    
    def get_obj(self, url):
        header = {"User-Agent":"Mozilla/5.0 (Macintosh; Itel Max OS X 10-9-5)\
                    AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                    "Accept":"text/html, appliation/xhtml+xml, application/xml;\
                    q=0.9,image/webp,*/*;q=0.8"}
        r = requests.get(url, headers=header)
        self.url = url
        bsObj = BeautifulSoup(r.text, "html.parser")
        return bsObj

    def get_page_text(self):
        pass

    def parser_page(self, obj):
        rows = []
        return rows

    def get_page_text(self, url):
        pass

    def get_url_list(self):
        pass
    
    def print_url(self):
        print(self.url)


def get_url_list():
    url = "http://www.ahwh.gov.cn/zz/shwhc/gzdt5/"
    website = "http://www.ahwh.gov.cn"
    url_list = []
    url1 = url

    for i in range(5):
        print(i, url1)
        r = get_obj(url1)
        rows = parser_site(r)
        
        for row in rows:
            url_list.append(website+row[2])

        url1 = url+'index_%d.shtml'%(i+2)

    return url_list


def test3():
    url = "http://www.ahwh.gov.cn/zz/shwhc/gzdt5/"
    web = Web()
    obj = web.get_obj(url)
    print(web.print_url())

if __name__ == "__main__":
    test3()
