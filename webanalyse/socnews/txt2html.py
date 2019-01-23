#!/usr/bin/python3
#coding:utf-8

FILE = 'msg.txt'
HTML = 'index.html'

msg = {}

f = open(FILE,"r")
h = open(HTML,"w")

h.write(
'''
<html>
	<head>
		<meta charset='utf-8'>
	</head>
	<body>
''')

i = 0
date = ''
title = ''
url = ''
for line in f.readlines():
	if i == 0:
		date = line[0:10]
		title = line[11:]
		i = 1
	else:
		url = line
		h.write("<li>")
		h.write("<span>%s</span>"%date)
		h.write("<a href='%s'>%s</a>"%(url,title))
		h.write("</li>")
		i = 0
		
h.write("</body>\r\n")
h.write("</html>\r\n")
h.close()
f.close()

