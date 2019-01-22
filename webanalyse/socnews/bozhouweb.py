#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.bzwhly.gov.cn/zw/html/type/list-0101-1.html"
		self.website = "http://www.bzwhly.gov.cn"
		self.name = '[亳州市]'
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"article_list"}).find("ul",{"class":"list"}).li

		title = tr.find("a")['title']
		href = tr.find("a")["href"]
		time = tr.find('span').string
		msg.append((time, self.name + title, self.website + href))
		#print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
