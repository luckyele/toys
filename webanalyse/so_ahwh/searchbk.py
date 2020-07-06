#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import csv

url = "https://ct.ah.gov.cn/zwgk/bmdt/"

def getObj(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None

	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
	except AttributeError as e:
		return None

	return bsObj

def getHtmlSourceCode(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	return html.read()

def parserSite(bsObj):
	trs = bsObj.find("div", {"class":"list"}).findAll("div", {"class":"tr"})
	
	rows = []

	for tr in trs:
		title = tr.find("div",class_="title").a["title"]
		href = tr.find("div",class_="title").a["href"]
		time = tr.find("div",class_="time").get_text()
		rows.append((time,title,href))

	return rows

def save_msg(rows, csvFile):
	writer = csv.writer(csvFile)
	for row in rows:
		writer.writerow(row)

def next_page(bsObj):
	return np_url

if __name__ == "__main__":
	bsObj = getObj(url)
	csvFile = open("search_result.csv", "wt", newline='', encoding='utf-8')
	
	for i in range(10):
		rows = parserSite(bsObj)
		save_msg(rows, csvFile)
		url_ = url + "index_%d.shtml"%(i+2)
		print(url_)
		bsObj = getObj(url_)

	csvFile.close() 
