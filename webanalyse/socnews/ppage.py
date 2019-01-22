#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
from webmonkey import Webmonkey
import requests
import re

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.ahwh.gov.cn/zwgk/bmdt/sxgz/6654.SHTML"
		self.website = "http://www.ahwh.gov.cn"
		self.name ='[省厅]'.encode('GBK').decode('iso-8859-1')
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		segments = obj.find("div", {"class":"content"}).findAll("p")
		
		for s in segments:
			dr = re.compile(r'<[^>]+>', re.S)
			dd = dr.sub(' ', s)
			print(dr)
			msg.append(dd)
		return msg
		
	def print_msg(self, segs):
		for seg in segs:
			print(seg.encode('iso-8859-1').decode('GBK'))
		

		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
