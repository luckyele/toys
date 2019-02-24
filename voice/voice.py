#coding:utf-8

from aip import AipSpeech

APP_ID='15613908'
API_KEY='s9nT12dLc9bsNuhsETLxR8TK'
SECRET_KEY='NcgoWKIWHuezK3k6N2OieWV7zvS1WcID'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filepath):
	with open(filepath, 'rb') as fp:
		return fp.read()

r =  client.asr(get_file_content('output1.wav'),'pcm',16000,{'dev_pid':1536,})

print(r)
