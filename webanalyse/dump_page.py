# !/usr/bin/python
# coding:utf-8

import sys, urllib2, re, requests
from bs4 import BeautifulSoup

#reload(sys) 
#sys.setdefaultencoding('utf-8') 

def get_sys_encoding():
    print("系统缺省编码:%s"%sys.getdefaultencoding()) #ascii
    print("文件系统编码:%s"%sys.getfilesystemencoding()) #utf8 
    print("终端输入编码:%s"%sys.stdin.encoding) #utf8
    print("终端输出编码:%s"%sys.stdout.encoding) #utf8

def get_charset(url):
    """Get the charset from the source code of URL
    """
    try:
        req = urllib2.Request(url)
    except:
        return str('utf-8') 
    try:
        f = urllib2.urlopen(req)
    except: 
        return str('utf-8')
    s = BeautifulSoup(f,'lxml')

    # <meta content="charset="utf-9"">
    return str(s.find('meta')['content'].split(' ')[0].split('=')[0])

if __name__=="__main__":
    all_sites = (
        'http://www.mcprc.gov.cn/whzx/bnsjdt/ggwhs/',
        'http://www.ahwh.gov.cn/',
        'http://swhj.hefei.gov.cn/',
        'http://wltw.huaibei.gov.cn/',
        'http://www.bzwhly.gov.cn/zw/',
        'http://www.whsz.org/',
        'http://www.bbswgxj.gov.cn/',
        'http://www.fywgxj.gov.cn/',
        'http://wgx.huainan.gov.cn/',
        'http://wgxj.chuzhou.gov.cn/',
        'http://www.lawgxj.gov.cn/',
        'http://www.masly.gov.cn/index.html')
    for site in all_sites:
        print(get_charset(site))

