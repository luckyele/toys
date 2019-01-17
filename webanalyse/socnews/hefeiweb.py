#! /usr/lib/python
#coding utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

from webmonkey import Webmonkey

class Hefeiweb(Webmonkey): 
	
	def __init__(self): 
		# define the entrance and name of main website
		self.url = "http://swhj.hefei.gov.cn/4964/4965/"
		self.website = "http://swhj.hefei.gov.cn/"
		super().__init__(self.url, self.website)

	def get_obj(self):
		'''Simulate web_browser to access website.'''
		header = {
			"User-Agent":
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like\
				Gecko) Chrome/48.0.2564.116 Safari/537.36',\
			"Accept":
				"text/html,appliation/xhtml+xml, \
				application/xml;q=0.9,image/webp,*/*;q=0.8"\
			}
		proxies = { "http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080", }
		r = requests.get(self.url, headers=header, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		bsObj = BeautifulSoup(r.text, "html.parser")
		return bsObj
		
	def get_newest_message(self, obj):
		msg = []
		tr = obj.select("body > table nth-of-type(4) > tbody nth-of-type(1)> tr nth-of-type(1) > td nth-of-type(2) > table nth-of-type(3) > 		tbody nth-of-type(1) > tr nth-of-type(1) > td nth-of-type(1) > table nth-of-type(1) > tbody nth-of-type(1) > tr nth-of-type(1) > td nth-of-type(2)")
		print(tr)
		
		title = tr.find('a')["title"]
		href = tr.find('a')["href"]
		time = tr.next_sibling().get_text()
		msg.append((time, title, self.website + href))
		return msg
		
def test3():
	web = Hefeiweb()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()

