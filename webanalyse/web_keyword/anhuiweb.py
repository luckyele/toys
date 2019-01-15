#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
# sys.path.append("../")

from webmonkey import Webmonkey

class Anhuiweb(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.ahwh.gov.cn/zz/shwhc/gzdt5/"
		self.website = "http://www.ahwh.gov.cn"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"list"}).find("div", {"class":"tr"})
		title = tr.find("div",class_="title").a["title"]
		href = tr.find("div",class_="title").a["href"]
		time = tr.find("div",class_="time").get_text()
		msg.append((time, title, self.website + href))
		return msg
	
	def print_msg(self, msg):
		# sourse: iso-8859-1, dest:gbk
		if sys.platform == 'win32':
			print(msg[0][0], msg[0][1].encode("iso-8859-1").decode('gbk'), msg[0][2])
		else:
			print(msg)
		
def test3():
	web = Anhuiweb()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
