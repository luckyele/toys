#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

class Webmonkey:
		
	def __init__(self, url, website):
		self.url = url
		self.website = website
		
	def get_obj(self):
		'''Simulate web_browser to access website.'''
		header = {"User-Agent":"Mozilla/5.0 (Macintosh; Itel Max OS X \
				0-9-5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
				"Accept":"text/html, appliation/xhtml+xml, \
				application/xml;q=0.9,image/webp,*/*;q=0.8"}
				
		r = requests.get(self.url, headers=header)
		if r is None:
			r = urlopen(url)
		print(r)
		try:
			bsObj = BeautifulSoup(r.text.encode("iso-8859-1").decode('utf-8'), "html.parser")
		except:
			bsObj = BeautifulSoup(r.text, "html.parser")
		print(bsObj)
		return bsObj

	def get_page_text(self):
		pass

	def parser_page(self, obj):
		print("parser_page() doesn't finish.")
		pass

	def get_page_text(self, url):
		pass

	def get_url_list_first(self):
		pass

#classend
