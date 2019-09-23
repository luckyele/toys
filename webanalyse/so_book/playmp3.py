import os

def play_mp3(file_name):
    os.system("ffplay -autoexit -hide_banner -nodisp %s"%(file_name))
