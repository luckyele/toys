#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import csv
import requests

url = "http://ah.wenhuayun.cn/frontVenue/venueListLoad.do"

def getObj(url):
	try:
		headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36"}
		
		
		r = requests.get(url, headers=headers)
	
	except HTTPError as e:
		return None
	
	bsObj = BeautifulSoup(r.text, "html.parser")
	
	print("OK")
	#print(r.text)
	return bsObj


def parserSite(bsObj):
	trs = bsObj.find("ul", {"id":"venue-list-ul"})
	print(trs)

	

def next_page(bsObj):
	return np_url

if __name__ == "__main__":
	bsObj = getObj(url)
	
	parserSite(bsObj)
	
		
