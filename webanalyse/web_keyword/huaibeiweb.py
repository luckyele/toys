#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys

# import sys
# sys.path.append("../")

from webmonkey import Webmonkey

class Huaibeiweb(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://wltw.huaibei.gov.cn/gzdt/bmdt/index.html"
		self.website = "http://wltw.huaibei.gov.cn/"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		m = obj.find("ul", {"class":"doc_list list-4697572"}).li
		title = m.a["title"]
		href = m.a["href"]
		time = m.findAll("span")[1].string
		msg.append((time, title, href))
		return msg
	
	def print_msg(self, msg):
		# sourse: iso-8859-1, dest:gbk
		if sys.platform == 'win32':
			print(msg[0][0], msg[0][1], msg[0][2])
		else:
			print(msg)
		
def test3():
	web = Huaibeiweb()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
