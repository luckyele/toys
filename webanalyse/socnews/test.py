#! /usr/lib/python
#coding:utf-8

# import sys
# sys.path.append("../")

import anhuiweb as ah
import bozhouweb as bzh
import chuzhouweb as chzh
import fuyangweb as fy
import huainanweb as hn
import huaibeiweb as hb
import huangshanweb as hsh
import luanweb as luan
import maanshanweb as msh

def scheduling(p_area):
	web = p_area.Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

def mailto(news):
	pass

def test():
	for p_area in [ah,bzh,chzh,fy,hn,hb,hsh,luan,msh]:
		scheduling(p_area)

if __name__=="__main__":
	test()