#coding:utf-8

from selenium import webdriver
import os
import sys

url = "http://swhj.hefei.gov.cn/4964/4965/"

browser = webdriver.Firefox()

browser.get(url)
print(browser.page_source)

