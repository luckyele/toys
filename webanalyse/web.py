#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
#coding:utf-8

import requests
import time

host = 'http://www.ahwh.gov.cn'
def _get_all_alink(url):
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
	url_graph = {}
	i = 0
	for link in alinks:
		name = i 
		url_graph[name] = link
		i += 1
	for url in url_graph.items():
		print(url)
		
def get_all_alinks(url):
	links = []
	links = _get_all_alink(url)
	print('%d <a> link.'%len(links))
	for link in links:
		_links = _get_all_alink(link)
		time.sleep(1)
		if _links != None:
			for l in _links:
				if l not in links:
					print("[%d Add] %s"%(len(links),l))
					links.append(l)
					if len(links) > 300:
						return links
	return links


if __name__ == "__main__":
	url = "http://www.ahwh.gov.cn"
	a = get_all_alinks(url)
	

				

