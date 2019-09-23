#coding:utf-8
import wav2pcm
import pyrec

from aip import AipSpeech

APP_ID='15613908'
API_KEY='s9nT12dLc9bsNuhsETLxR8TK'
SECRET_KEY='NcgoWKIWHuezK3k6N2OieWV7zvS1WcID'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

pyrec.rec('file.wav')

pcm_file = wav2pcm.wav_to_pcm('file.wav')


#def get_file_content(filepath):
#	with open(filepath, 'rb') as fp:
#		return fp.read()

with open(pcm_file,'rb') as fp:
    file_context = fp.read()

r =  client.asr(file_context, 'pcm', 16000, {'dev_pid':1536,})

print(r)

#res_str = r.get("result")[0]

res_str = "from http://opec.ahlib.com/opac/search find 322 books"

synth_context = client.synthesis(res_str, "zh", 1, {
    "vol":5,
    "spd":4,
    "pit":9,
    "per":4
    })

with open("synth.mp3", "wb") as f:
    f.write(synth_context)

import playmp3

playmp3.play_mp3("synth.mp3")
