#!coding:utf-8

import voice1
import sobook2
import time

ahlib_url="http://opac.ahlib.com/opac/search"

DEBUG = 1

def yes_or_no(keyword):
    if keyword in {'要','是','是的','好','好的','好吧','嗯'}:
        return True
    else:
        return False

def hear(c):
    return voice1.voice_input(c)

def say_init():
    return voice1.voice_init()

def say(c, text):
    voice1.play_voice(c, text)

SAY = {
        "b1":"您好，请问有什么可以帮您",
        "b3":"好的, 请说出要查询的书名或作者姓名",
        "b5":"您是要查询关于 %s 的书吗",
        "b6":"好的,现在为您查询",
        "b9":"您好,我没有听清，请再说一遍",
        "b11":"您还要继续查询吗",
        "b12":"谢谢使用，下次再见"
        }

def search(keyword):
    return sobook2.get_book(keyword)

def say_init():
    return voice1.voice_init()

class State_machine:
    def __init__(self):
        self.state = 0
        self.c = say_init()
        self.KEY = '同学你好'
        self.flag =''

    def run(self):
        while True:
            if DEBUG:
                print("[*****进状态*****]:%d"%self.state)
            self.on_state()
            if DEBUG:
                print("[*****出状态*****]:%d"%self.state)

    def on_state(self):
        if self.state == 0:
           self.state = 1
           return

        if self.state == 1:
            if hear(self.c) == self.KEY:
                say(self.c,SAY.get("b1"))
                self.state = 2
            else:
                say(self.c, SAY.get("b9"))
            return

        if self.state == 2:
            if hear(self.c) == "搜索":
                say(self.c,SAY.get("b3"))
                self.state = 3
            else:
                say(self.c, SAY.get("b9"))
            return
        
        if self.state == 3:
            self.kw = hear(self.c)
            say(self.c,(SAY.get("b5"))%self.kw)
            self.flag = hear(self.c)
            if yes_or_no(self.flag):
                self.state = 4
            else:
                self.state = 5
            return

        if self.state == 4:
            print(self.flag)
            if yes_or_no(self.flag):
                say(self.c, SAY.get("b6"))
                say(self.c, search(self.kw))
                self.state = 6
            else:
                self.state = 7
            return

        if self.state == 5:
            if yes_or_no(self.flag) == False:
                say(self.c, SAY.get("b3"))
                self.state = 3 
            else:
                say(self.c,SAY.get("b9"))
            return

        if self.state == 6:
            say(self.c, SAY.get("b11"))
            if yes_or_no(hear(self.c)):
                say(self.c, SAY.get("b3"))
                self.state = 3
            else:
                self.state = 7
            return

        if self.state == 7:
            say(self.c, SAY.get("b12"))
            self.state = 0
            exit()


if __name__ == "__main__":
    sm = State_machine()
    sm.state = 6
    sm.run()

