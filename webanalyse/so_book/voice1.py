#coding:utf-8
import wav2pcm
import pyrec

from aip import AipSpeech

def voice_init():

    APP_ID='15613908'
    API_KEY='s9nT12dLc9bsNuhsETLxR8TK'
    SECRET_KEY='NcgoWKIWHuezK3k6N2OieWV7zvS1WcID'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return client

def voice_input(client):
    pyrec.rec('file.wav')
    pcm_file = wav2pcm.wav_to_pcm('file.wav')

    with open(pcm_file,'rb') as fp:
        file_context = fp.read()
    r =  client.asr(file_context, 'pcm', 16000, {'dev_pid':1536,})
    print(r)
    if r.get('err_msg') != 'success.':
        return 0
    return r.get("result")[0]

def play_voice(c, r):
    synth_context = c.synthesis(r, "zh", 1, {
        "vol":5,
        "spd":4,
        "pit":9,
        "per":0
        })

    with open("synth.mp3", "wb") as f:
        f.write(synth_context)

    import playmp3

    playmp3.play_mp3("synth.mp3")

if __name__ == '__main__':
    c = voice_init()
    txt = voice_input(c)
    play_voice(c, txt)
