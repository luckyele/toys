#coding:utf-8

def input_txt():
    istr = input("input text:")
    return istr 

def filter_letter(istr):
    ostr = ""
    for c in istr:
    #    if c == ' ':
    #        continue
        ostr += code(c)
    return ostr

def code(c):
    intc = ord(c)-6
    if intc < 97:
        intc = 97 - intc
        intc = 122 - intc
    if intc > 122:
        intc = intc - 122
        intc = 97 + intc
    return chr(intc)

def prtmsg(istr):
    print("%s\n"%istr)

def test():
    i = input_txt()
    j = filter_letter(i)
    prtmsg(j)

if __name__ == "__main__":
    test()
