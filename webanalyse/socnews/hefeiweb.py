#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://swhj.hefei.gov.cn/4964/4965/"
		self.website = "http://swhj.hefei.gov.cn/"
		self.name = "[合肥市]"
		super().__init__(self.url, self.website)

	
	def get_cookies(self):
		from selenium import webdriver
		try:
			browser = webdriver.Chrome()
		except e:
			return
		
		browser.get(self.url)
		browser.refresh()
		cookies = browser.get_cookies()
		s = ""
		for item in cookies:
			s += "%s=%s;"%(item['name'],item['value'])
		return s
	
	def get_obj(self):
		cookies = self.get_cookies()
		header={
			"Host": "swhj.hefei.gov.cn",
			"Connection": "keep-alive",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"Referer": "http://swhj.hefei.gov.cn/4964/4965/",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
			"Cookie":cookies}
		
		res = requests.get(self.url, headers=header)
		obj = BeautifulSoup(res.text.encode("iso-8859-1").decode('utf-8'), "html.parser")		
		return obj

	def get_newest_message(self, obj):
		msg = []
		table = obj.findAll(attrs={"width":"90%","align":"center"})
		tr = table[0].tbody.findAll("tr")
		td = tr[0].findAll("td")
		title = td[1].a['title']
		href = td[1].a["href"]
		time = td[2].get_text()
		msg.append((time, self.name + title, self.website + href[2:]))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()

