#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
# sys.path.append("../")

from webmonkey import Webmonkey

class Hefeiweb(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://swhj.hefei.gov.cn/4964/4965/"
		self.website = "http://swhj.hefei.gov.cn/"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		t = obj.body.find('table')
		print("obj.body is %s"%t)
		t = t.find_next_siblings('table')
		print(tr)
		title = tr.find("div",class_="title").a["title"]
		href = tr.find("div",class_="title").a["href"]
		time = tr.find("div",class_="time").get_text()
		msg.append((time, title, self.website + href))
		return msg
	
	def print_msg(self, msg):
		# sourse: iso-8859-1, dest:gbk
		if sys.platform == 'win32':
			print(msg[0][0], msg[0][1].encode("iso-8859-1").decode('gbk'), msg[0][2])
		else:
			print(msg)
		
def test3():
	web = Hefeiweb()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()


#---------------------------------
#/     从根标签开始
#//    从当前标签
#*     通配符，选择所有
#//div/book[1]/title  选择div下第一个book标签的title元素
#//div/book/title[@lang='zh'] 选择title属性含有lang且内容为zh的title元素
#//div/book/title[@*] 将含有属性的title标签选出来
#//div/book/title/@*  将title标签中的属性值选出来
#//div/book/title/text() 选出title标签中的内容，使用内置函数text()
#//div/book/title  //book/title  //title具有相同的结果
#//a[@href='link1.html' and @id='places_neighbours__row'] 把两个条件都满足的a标签选出来
#//a[@href='link1.html' or @id='places_neighbours__row'] 把满足任意一个条件的a标签选出来
#//a[not(@href)] 将不存在href元素的a标签选出来
#//a[@href!='link1.html'] 将存在href元素 但不等于link1.html的a标签选出来
#//li[starts-with(@class,'item')] 将class属性前缀是item的li标签选出来
#//li[contains(@class,'ct')] 将class属性中含有ct关键字的li标签选出来
#//div/book[last()]/title/text() 将最后一个book元素中title内容选出来
#//div/book[last()-1]/title/text() 将倒数第二个book元素中title内容选出来
#//div/book[price > 39]/title/text() 将book中price标签中的内容大于39的选出来
#//book/descendant::* 将后续节点全部选出
#//book/ancestor::* 将祖先节点全部选出

