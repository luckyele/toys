#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import sys


DEBUG = 0

class Webmonkey:
		
	def __init__(self, url, website):
		self.url = url
		self.website = website
		
	def get_obj(self):
		'''Simulate web_browser to access website.'''
		par = urlparse(self.url)
		
		header = {"User-Agent":\
					'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like\
					Gecko) Chrome/48.0.2564.116 Safari/537.36',\
				  "Accept":\
					"text/html,appliation/xhtml+xml, \
					application/xml;q=0.9,image/webp,*/*;q=0.8",\
				  'Host':par[1],\
				  'Referer':par[0] + '://' + par[1]
				}
		try:			
			r = requests.get(self.url, headers=header, timeout=10)
			if r.status_code != 200:
				return None

		except Exception as e:
			print(e)
			r = urlopen(self.url)
		
		if DEBUG:
			print("[**DEBUG**] "+r.encoding)
			print("[**DEBUg**] "+self.url)
		try:
			bsObj = BeautifulSoup(r.text.encode('iso-8859-1').decode('utf-8'), "html.parser")
		except:
			bsObj = BeautifulSoup(r.text, "html.parser")
		
		return bsObj
	
	def print_msg(self, msg):
		print(msg[0][0], msg[0][1])
		print(msg[0][2])


	def get_charset(self, obj):
		return str(obj.find('meta')['content'].split(' ')[1].split('=')[1])
