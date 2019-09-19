import voice1
import sobook

ahlib_url="http://opac.ahlib.com/opac/search"

def yes_or_no(keyword):
    if keyword in {'是','是的','好','好的','好吧','嗯'}:
        return True
    else:
        return False

def say_yes(c):
    voice1.play_voice(c, "好的，马上为您查询")

def ask_again(c):
    voice1.play_voice(c, "我没有听懂，请再说一遍。")

def say_bye(c):
    voice1.play_voice(c, "谢谢使用，下次再见")
    exit()

def first_say(c):
    text1 = "说出您要找的书名或者作者姓名"
    voice1.play_voice(c,text1)

def hear(c):
    return voice1.voice_input(c)

def say_something(c, text):
    voice1.play_voice(c, text)

def say_init():
    return voice1.voice_init()

if __name__ == "__main__":

    c = say_init()

    while True:
    
        first_say(c)
        
        kw = hear(c)
        if kw == 0:
            ask_again(c)
            kw = hear(c)

        say_something(c, "你是要查关于 %s 的书吗 "%kw)
    
        kw1 = hear(c)
        if yes_or_no(kw1):
            say_yes(c)
            text = sobook.get_all_book(ahlib_url, kw)
            say_something(c, text)
        else:
            ask_again(c)
        

        say_something(c, "您还要继续查询吗")

        kw1 = hear(c) 
        if yes_or_no(kw1) is False:
            say_bye(c)
