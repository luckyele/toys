#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
import requests
import time

host = 'https://ct.ah.gov.cn'

''' Get all <a> links in the current page.
'''
def get_all_inner_alink_of_current_page(url, links):
	r = requests.get(url)
	try:
		soup = BeautifulSoup(r.text, 'html.parser')
	except:
		print("something error.")		
	
	for link in soup.findAll('a'):
		if 'href' in link.attrs:
			t = link['href'].split('//')
			if len(t) == 1 and t[0][0:1] == '/':
				new_link = host + t[0]
				if new_link not in links:
					links.append(new_link)
	return links

def test():
	url = 'http://ct.ah.gov.cn'
	INIT_LINKS = []
	ACCESSED_LINKS = []
	get_all_inner_alink_of_current_page(url, INIT_LINKS)
	for l in INIT_LINKS:
		if l not in ACCESSED_LINKS:
			ACCESSED_LINKS.append(l)
			print("[**UNACCESSED**]%s >>"%l)
			get_all_inner_alink_of_current_page(l, INIT_LINKS)

		# display the process of scanning
		print("[**info**]INIT_LINKS(%s) ACCESSED_LINKS(%s)"%(len(INIT_LINKS),
					len(ACCESSED_LINKS)))
		
if __name__ == "__main__":
	test()
