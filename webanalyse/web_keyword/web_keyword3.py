#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import jieba.analyse

import logging

jieba.setLogLevel(logging.DEBUG)
	
def get_obj(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
	except AttributeError as e:
		return None
	return bsObj

def parser_site(bsObj):
	rows = []

	trs = bsObj.find("div", {"class":"ctNewsList"}).ul.findAll("a")
	print(trs)
	for tr in trs:
		href = tr["href"]
		title = tr.get_text()
		rows.append((title,href))

	return rows

def get_page_text(url):
	with  urlopen(url) as req:
		f = req.read()
		req.close()
		
		soup = BeautifulSoup(f, 'html.parser')
		k =  soup.find('div', {"class":"articleMain"})
		txt = "".join(k.get_text().strip())
		return txt


def page_keyword(txt, w=5):
	''' function: get top 5 keywords in txt;	return  : list of keywords.
	'''
	t_list = jieba.analyse.textrank(txt, topK=w, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
	return t_list

class Keywords:
	def __init__(self):
		self.keywords = []

	def add_keys(self, keywords=None):
		if keywords is not None:
			for key in keywords:
				#if key not in self.keywords:
				self.keywords.append(key)

	def keys(self):
		return self.keywords

	def print(self):
		for key in self.keywords:
			print(key, end=' ')
		print('\n')	
	
	def sort(self):
		kws = {}
		for key in self.keywords:
			if key in kws.keys():
				kws[key] += 1
			else:
				kws[key] = 1
		print(sorted(kws.items(), key=lambda d:d[1]))

	def save(self):
		import csv
		csvfile = open("key.csv", "wt", newline='')
		writer = csv.writer(csvfile)
		for key in self.keywords:
			writer.writerow(key)

def keywords_stat(k1_list, k2_list):
	if k1_list is None :
		return
	i = 0
	for k2 in k2_list:
		if k2 in k1_list:
			i += 1
	if i > len(k2_list)*0.8:
		return "公共文化服务类"
	else:
		return "未知"

def get_url_list():
	url = "https://ct.ah.gov.cn/html/article/list-0105-1.html"
	website = "https://ct.ah.gov.cn"
	url_list = []
	url1 = url

	r = get_obj(url1)
	rows = parser_site(r)
		
	for row in rows:
		url_list.append(website+row[1])

	return url_list

def test2():
	url_lists = get_url_list()
	pcs = Keywords()

	print("Building a keywords resp....")
	print("*"*40)
	
	for url in url_lists:
		txt = get_page_text(url)
		k_list =  page_keyword(txt)
		print(k_list)
		pcs.add_keys(k_list)

	pcs.save()	
	pcs.sort()

def test():
	url_lists = get_url_list()
	pcs = Keywords()

	print("Building a keywords resp....")
	print("*"*40)
	
	for url in url_lists:
		txt = get_page_text(url)
		k_list =  page_keyword(txt, 10)
		pcs.add_keys(k_list)

	pcs.save()	
	pcs.print()	

	print("Building completed....") 
	print("*"*40)
	
	for url in url_lists:
		k2 = Keywords()
		print(">>%s\t"%(url), end=' ')
		k2_list = page_keyword(get_page_text(url))
		k2.add_keys(k2_list)
		print(keywords_stat(pcs.keywords, k2.keywords))

if __name__ == "__main__":
	test2()
