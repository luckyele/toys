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
		self.url = "http://wgxj.bengbu.gov.cn/sitefiles/services/cms/page.aspx?s=1&n=9"
		self.website = "http://wgxj.bengbu.gov.cn"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"contain_page"}).div.findAll("div")
		title = tr[0].a.get_text()
		href = tr[0].a["href"]
		time = tr[1].get_text()[5:]
		msg.append((time, title, self.website + href))
		return msg

		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()