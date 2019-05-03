#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
import requests
import time


host = 'http://ct.ah.gov.cn'
INIT_LINKS = []
ACCESSED_LINKS = []
UNACCESSED_LINKS = []

''' Get all <a> links in the current page.
'''
def get_all_alink(url, links):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	for link in soup.findAll('a'):
		if 'href' in link.attrs:
			t = link['href'].split('//')
			if len(t) == 1 and t[0][0:1] == '/':
				new_link = host + t[0]
				if new_link not in links:
					links.append(new_link)
		
def test():
	get_all_alink(host, INIT_LINKS)
	UNACCESSED_LINKS = INIT_LINKS
	if len(UNACCESSED_LINKS) > 0:
		link = UNACCESSED_LINKS.pop(0)
		ACCESSED_LINKS.append(link)

def disp():
	for link in ACCESSED_LINKS:
		print(link)
	print("")
	
	for link in UNACCESSED_LINKS:
		print(link)
	print("")

if __name__ == "__main__":
	test()
	disp()
