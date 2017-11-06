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

def gen_MD_for_webpage(webpage):
    md_tmp = hashlib.md5()
    md_tmp.update(webpage)
    return md_tmp.hexdigest()

def time_stamp():
    return time.strftime('%Y%m%d%H%M%S')

def save_MD(n, u):
    if os.path.isfile('urlmd.txt'):
        print('urlmd.txt is exists, It will be fresh.')
    f = open('urlmd.txt', 'a')
    str = time_stamp() + '|' + n + '|' + md1 + '\n'
    f.write(str)
    f.close()

if __name__ == '__main__':

    url_list = {'ahswht':'http://www.ahwh.gov.cn/zz/shwhc/',
                'hfswgxj':'http://swhj.hefei.gov.cn/4964/4977/'}

    for n, u in url_list.items():
        p = open_webpage(u)
        md1 = gen_MD_for_webpage(p)
        print time_stamp()
        print n, u
        print md1
        save_MD(n, u)
        if webpage_is_updated(p, md1):
            print 'webpage is udpated.'
        else:
            print 'webpage isn\'t updated.'
    
