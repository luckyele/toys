#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://whw.huangshan.gov.cn/Content/showList/JA022/16276/1/page_1.html?menu=16274&loc=8"
		self.website = "http://whw.huangshan.gov.cn"
		self.name = "[黄山市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("dl", {"class":"key-list"}).find('dt')
		title = tr.a['title']
		href = tr.a["href"]
		time = tr.find("span").string
		msg.append((time, self.name+title, self.website + href))
		# print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
