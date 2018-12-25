
import hashlib

# For compatible of Python2.7 and Python 3.x
try:
    import urllib2 as ur

except:
    import urllib.request as ur

import time, os


def open_webpage(url):
    try:
        page = ur.urlopen(url).read()
    except:
        print('webpage cann\'t open.')
    return page

def webpage_is_updated(webpage, md_old_hex):
    if gen_MD_from(webpage) == md_old_hex:
        return False
    return True

def gen_MD_from(webpage):
    md_tmp = hashlib.md5()
    md_tmp.update(webpage)
    return md_tmp.hexdigest()

def time_stamp():
    return time.strftime('%Y%m%d%H%M%S')

def save_MD(n, md):
    f = open('urlmd.txt', 'a')
    str1 = time_stamp() + '|' + n + '|' + md + '\n'
    f.write(str1)
    f.close()

def get_MD():
    url_md_list = {}
    f = open('urlmd.txt', 'r')
    for line in f.readlines():
        str1 = line.strip('\n').split('|')
        name, md5 = str1[1], str1[2]
        url_md_list[name] = md5
    f.close() 
    return url_md_list
   
if __name__ == '__main__':

    url_list = {'anhuiwht':'http://www.ahwh.gov.cn/zz/shwhc/',
                'hfswgxj':'http://swhj.hefei.gov.cn/4964/4977/',
                'whbggwhs':'http://www.mcprc.gov.cn/whzx/bnsjdt/ggwhs/',
                'beijingwhj':'http://www.bjwh.gov.cn/bjwh/whzx/qwdt85/index.html',
                'ahsuzhouwgxj':'http://www.whsz.org/news.asp?id=%C9%E7%BB%E1%CE%C4%BB%AF'
                }

    urlmd = get_MD()
        
    for n, u in url_list.items():
        p = open_webpage(u)
        md = gen_MD_from(p)
        print(time_stamp(), n, u, md)
#        save_MD(n,md)
        if webpage_is_updated(p, urlmd[n]):
            save_MD(n, md)
            print(n,'is udpated.')
        else:
            print(n,'isn\'t updated.')

