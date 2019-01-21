#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
from webmonkey import Webmonkey
from urllib.request import urlopen
import requests

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.ahwh.gov.cn/zz/shwhc/gzdt5/"
		self.website = "http://www.ahwh.gov.cn"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"list"}).find("div", {"class":"tr"})
		title = tr.find("div", class_="title").a["title"]
		href = tr.find("div", class_="title").a["href"]
		time = tr.find("div", class_="time").get_text()[1:-1]
		msg.append((time, title, self.website + href))
		return msg
		
	def print_msg(self, msg):
		print(msg[0][0], msg[0][1].encode('iso-8859-1').decode('GBK'))
		print(msg[0][2])

		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
