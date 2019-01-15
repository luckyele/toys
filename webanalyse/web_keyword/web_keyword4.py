#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# import sys
# sys.path.append("../")

from webmonkey import Webmonkey

class Anhuiweb(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.ahwh.gov.cn/zz/shwhc/gzdt5/"
		self.website = "http://www.ahwh.gov.cn"
		super().__init__(self.url, self.website)

	def parser_page(self, obj):
		rows = []
		trs = obj.find("div", {"class":"list"}).findAll("div", {"class":"tr"})
		for tr in trs:
			title = tr.find("div",class_="title").a["title"]
			href = tr.find("div",class_="title").a["href"]
			time = tr.find("div",class_="time").get_text()
			rows.append((time, title, href))
		return rows
	
	def get_url_list_first(self):
		url_list = []
		r = self.get_obj()
		rows = self.parser_page(r)
		for row in rows:
			url_list.append(self.website + row[2])
		return url_list
		
def test3():
	web = Anhuiweb()
	obj = web.get_obj()
	for r in web.get_url_list_first():
		print(r)


if __name__ == "__main__":
	test3()
