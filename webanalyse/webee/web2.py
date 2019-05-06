#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import csv

def save(data):
	with open('data.csv', 'w+') as csvFile:
		for d in data:
			csvFile.write(d)
			csvFile.write('\n')

host = 'https://ct.ah.gov.cn'

''' Get all <a> links in the current page.
'''
links = set()

def get_all_inner_alink_of_current_page(url, recursionLevel):
	global links
	if recursionLevel > 4:
		return;
	print(">"*recursionLevel)
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
					print("%d %s"%(len(links),new_link))
					links.add(new_link)
					get_all_inner_alink_of_current_page(new_link,
							recursionLevel+1)

def test():
	get_all_inner_alink_of_current_page(host, 0)
	global links
	save(links)

if __name__ == "__main__":
	test()
