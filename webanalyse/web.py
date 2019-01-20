#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
#coding:utf-8

import requests
import time

host = 'http://www.ahwh.gov.cn'
def get_all_alink(url):
	alinks = []
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	for link in soup.findAll('a'):
		if 'href' in link.attrs:
			t = link['href'].split('//')
			if len(t) == 1 and t[0][0:1] == '/':
				alinks.append(host+t[0])
				
	return alinks

def gen_graph(alinks):
	
	url_grahp = {}
	i = 0
	for link in alinks:
		name = i 
		url_grahp[name] = link
		i += 1

	print(url_grahp)


if __name__ == "__main__":
	url = "http://www.ahwh.gov.cn"
	alinks = get_all_alink(url)
	print("*"*40)
	for link in alinks:
		print(link)
	
	print("*"*40)
	print('%d <a> link.'%len(alinks))

	gen_graph(alinks)
