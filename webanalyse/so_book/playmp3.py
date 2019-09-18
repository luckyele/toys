import os
from playsound import playsound

def play_mp3(file_name):
#    os.system("ffplay %s"%(file_name))
#    clip = mp3play.load(file_name)
##    clip.play()
#    time.sleep(10)
#    clip.stop()
    playsound(file_name)
