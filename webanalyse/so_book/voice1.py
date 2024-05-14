#coding:utf-8
import wav2pcm
import pyrec

from aip import AipSpeech

def voice_init():
    ''' Initial Baidu speech AI.
    '''
    APP_ID='...'
    API_KEY='...'
    SECRET_KEY='...'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return client

def voice_input(client):
    ''' Record the speech to .WAV file
        Transformate to .PCM file
        Get text from .PCM file by Baidu Speech AI fuction.
    '''
    pyrec.rec('file.wav')
    pcm_file = wav2pcm.wav_to_pcm('file.wav')

    with open(pcm_file,'rb') as fp:
        file_context = fp.read()
    r =  client.asr(file_context, 'pcm', 16000, {'dev_pid':1536,})

    print(r.get("result"))
    
    if r.get('err_msg') != 'success.':
        return 0
    
    return r.get("result")[0]

def play_voice(c, r):
    ''' Synthesis text to Speech.
        then play
    '''
    synth_context = c.synthesis(r, "zh", 1, {
        "vol":5,
        "spd":5,
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
