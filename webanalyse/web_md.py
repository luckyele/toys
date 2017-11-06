import hashlib
import urllib2
import time, os

def open_webpage(url):
    try:
        page = urllib2.urlopen(url).read()
    except:
        print 'webpage cann\'t open.'
    return page
    
def webpage_is_updated(webpage, md_old_hex):
    md_new = hashlib.md5()
    md_new.update(webpage)
            
    if md_new.hexdigest() == md_old_hex:
        return False
    return True

def gen_MD_from_webpage(webpage):
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
                'beijingwhj':'http://www.bjwh.gov.cn/bjwh/whzx/qwdt85/index.html'
                }

    urlmd = get_MD()
        
    for n, u in url_list.items():
        p = open_webpage(u)
        md = gen_MD_from_webpage(p)
        print time_stamp(), n, u, md
        save_MD(n,md)
        if webpage_is_updated(p, urlmd[n]):
            print 'webpage is udpated.'
        else:
            print 'webpage isn\'t updated.'

