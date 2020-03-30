from django.http import HttpResponse
import pandas as pd
import os

def read_data():
		file_name = "20180521.xls"
		s = pd.read_excel(file_name,sheet_name=57,usecols="A:E",header=None)
		return s


def hello(request):
		d = read_data()
		s = ''
		for c in d:
				s += "<p> %s"%c
		return HttpResponse(s)
