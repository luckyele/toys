#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
# sys.path.append("../")

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://wgxlj.ahsz.gov.cn/14245213.html"
		self.website = "http://wgxlj.ahsz.gov.cn/"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("ul", {"class":"doc_list list-14245213"})
		title = tr.a['title']
		href = tr.a["href"]
		time = tr.find("span", {"class":"right date"}).string
		msg.append((time, title, href))
		#print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()