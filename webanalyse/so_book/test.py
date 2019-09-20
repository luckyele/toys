import voice1
import sobook
import time

ahlib_url="http://opac.ahlib.com/opac/search"

def yes_or_no(keyword):
    if keyword in {'是','是的','好','好的','好吧','嗯'}:
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

def b10(c, keyword):
    text = sobook.get_all_book(ahlib_url, keyword)
    say(c, text)

def say_init():
    return voice1.voice_init()

if __name__ == "__main__":

    c = say_init()
    while True:
        kw = hear(c)
        say(c, kw)
        if kw == "小爱同学":
            say(c,SAY.get("b1"))
            kw = hear(c)
            say(c, kw)
            if kw == "查一本书":
                say(c,SAY.get("b3"))
                kw1 = hear(c)
                say(c,kw1)
                say(c,SAY.get("b5")%kw1)
                if  yes_or_no(hear(c)):
                    say(c,SAY.get("b6"))
                    b10(c, kw1)
                    say(c,SAY.get("b11"))
                    if yes_or_no(hear(c)) == False:
                        say(c, SAY.get("b12"))
                        exit()
            elif kw == "现在几点":
                t = time.gmtime()
                say(c, "现在是 %d 点 %d 分"%(t.tm_hour, t.tm_min))





