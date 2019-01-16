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

	def get_newest_message(self, obj):
		msg = []
		tr = obj.select("body > table nth-of-type(4) > tbody nth-of-type(1) > tr nth-of-type(1) > td nth-of-type(2) > table nth-of-type(3) > tbody nth-of-type(1) > tr nth-of-type(1) > td nth-of-type(1) > table nth-of-type(1) > tbody nth-of-type(1) > tr nth-of-type(1) > td nth-of-type(2)")
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

