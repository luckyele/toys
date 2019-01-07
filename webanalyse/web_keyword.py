#! /usr/lib/python
#coding:utf-8

import urllib.request 
from bs4 import BeautifulSoup
import jieba.analyse

def get_page_text(url):
	''' For www.ahwh.gov.cn
	'''
	with  urllib.request.urlopen(url) as req:
		f = req.read().decode('gb2312', 'ignore').encode('utf-8')
		req.close()
		soup = BeautifulSoup(f, 'html.parser')
	
		for k in soup.find_all('div', class_='cont'):
			txt = "".join(k.get_text().strip())
		return txt

def front100_text(text):
	print(text[0:100])
		
def page_keyword(txt, w=5):
	t_list = jieba.analyse.textrank(txt, topK=w, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
	return t_list

class Keywords:
	def __init__(self):
		self.keywords = []
		
	def add_keys(self, keywords=None):
		if keywords is not None:
			for key in keywords:
				if key not in self.keywords:
					self.keywords.append(key)

	def keys(self):
		return self.keywords

def keywords_stat(k1_list, k2_list):
	if k1_list is None :
		return
	i = 0
	for kk2 in k2_list:
		if kk2 in k1_list:
			i += 1
	if i > len(k2_list)*0.8:
		return "PCS."

def test():
	ahwht1 = "http://www.ahwh.gov.cn/zz/shwhc/gzdt5/57264.shtml"
	ahwht2 = "http://www.ahwh.gov.cn/zz/shwhc/zdhd5/47954.shtml"
	ahwht3 = "http://www.ahwh.gov.cn/zz/shwhc/zcwj3/49568.shtml"
	ahwht4 = "http://www.ahwh.gov.cn/xwzx/gzdt/50918.shtml"
	ahwht5 = "http://www.ahwh.gov.cn/zwgk/bmdt/sxgz/57631.shtml" 
	
	pcs = Keywords()	

	print("Building a keywords resp....")
	for url in [ahwht1,ahwht2,ahwht3,ahwht4]:
		txt = get_page_text(url)
		print(front100_text(txt))
		k_list =  page_keyword(txt,10)
		pcs.add_keys(k_list)
	print("Building completed....") 

	for url in [ahwht1,ahwht2,ahwht3,ahwht4,ahwht5]:
		k2 = Keywords()
		print(">>%s\t"%(url), end=' ')
		k2_list = page_keyword(get_page_text(url))
		k2.add_keys(k2_list)
		#print("Keywords:%s"%(k2.keys()))
		print(keywords_stat(pcs.keywords, k2.keywords))
	
if __name__ == "__main__":
	test()
