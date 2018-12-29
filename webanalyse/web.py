#! /usr/lib/python
#coding:utf-8

import urllib.request 
from bs4 import BeautifulSoup
import jieba.analyse

def analyse_web(url):
    req = urllib.request.urlopen(url)
    f = req.read().decode('gb2312', 'ignore').encode('utf-8')
    req.close()

    soup = BeautifulSoup(f, 'html.parser')

    for k in soup.find_all('div', class_='cont'):
        txt = k.get_text().strip('\n').strip(' ')

    #t_list1 = jieba.analyse.extract_tags(txt, topK=5, withWeight=False, allowPOS=())
    t_list2 = jieba.analyse.textrank(txt, topK=10, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    return t_list2

if __name__ == "__main__":
    ahwht1 = "http://www.ahwh.gov.cn/zz/shwhc/zdhd5/49946.shtml"
    ahwht2 = "http://www.ahwh.gov.cn/zz/shwhc/zdhd5/47954.shtml"
    ahwht3 = "http://www.ahwh.gov.cn/zz/shwhc/zcwj3/49568.shtml"
    ahwht4 = "http://www.ahwh.gov.cn/xwzx/gzdt/50918.shtml"
    for url in [ahwht1,ahwht2,ahwht3,ahwht4]:
        print("Result of analyse: %s"%url)
        for s in analyse_web(url):
            print(str(s))

