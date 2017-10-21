#!/usr/lib/python
#coding:utf-8

import sys, os

class Person():
    def __init__(self):
        self.name = "张三"
        self.tele = "0123456789"

class Contact():

    modifyflag = False

    def __init__(self):
        self.personlist = []

    def openexitsaddress(self):
        try:
            f = open("./address.txt", "r")
        except:
            print("Open file failure.")
            return -1

        for line in f.readlines():
            m, t = line.split('\t') 
            t = t[:-1]
            tmp = Person()
            tmp.name, tmp.tele = m, t
            self.add(tmp)
        f.close()

    def new(self):
        p = Person()
        return p
    
    def delperson(self, p):
        if len(self.personlist) > 0:
            self.personlist.remove(p)
            self.modifyflag = True
        
    def list(self):
        n = 1
        if len(self.personlist) > 0:
            for p in self.personlist:
                print("%4d\t%s\t%s"%(n, p.name, p.tele))
                n += 1

    def add(self,p):
        self.personlist.append(p)
        self.modifyflag = True

    def modify(self, index, name, tele):
        if index > len(self.personlist):
            print("Index error, please try again.")
        self.personlist[index].name = name
        self.personlist[index].tele = tele
        self.modifyflag = True
    
    def count(self):
        return len(self.personlist)

    def search(self, p=None, name="", tele=""):
        pass 

    def save2file(self):
        if self.modifyflag:
            f = open("./address.txt","w")
            for p in self.personlist:
                m,t = p.name, p.tele
                seq = m + "\t" + t + "\n"
                f.write(seq)
            f.close()

    def import4file(self):
        pass

def menu(contact):
    menubar = "(N)ew (I)mport (M)odify (S)ave (D)elete (Q)uit"
    statusbar = "Totle:" + str(contact.count())

    print('='*60)
    print(' '*20 + 'Smart Address 0.01')
    print('-'*60)
    
    contact.list()
    
    print('-'*60)
    print(statusbar)
    print('-'*60)
    print(menubar)
    print('='*60)

def menu_top():
    print('='*60)

def menu_bottom(contact):
    menubar_main = "(N)ew (I)mport (M)odify (S)ave (D)elete (Q)uit"
    menubar_page = '(T)op (Next) (U)p (E)nd'
    statusbar = "Totle:" + str(contact.count())
    print('-'*60)
    print(statusbar)
    print('-'*60)
    print(menubar_main)
    print('='*60)

def menu1(contact):
    
    maxpersonofapage = 20
    
    menu_top()

    if contact.personlist.__len__() > maxpersonofapage:
        contact.list()
    menu_bottom(contact)
    
def test1():

    mycontact = Contact()
    menu1(mycontact)
    a = ''

    while 1:
        a = raw_input()
        print("Your input：%s"%a)

        if a is 'n' or a is 'N':
            for i in range(100):
                newperson = mycontact.new()
                mycontact.add(newperson)
        elif a is 'm' or a is 'M':
            index = raw_input("which do you want to modify? ")
            name = raw_input("Name:")
            tele = raw_input("Tele:")
            mycontact.modify(int(index)-1, name, tele)
        
        elif a is 'q' or a is 'Q':
            mycontact.save2file()
            return

        elif a is 's' or a is 'S':
            pass

        elif a is 'i' or a is 'I':
            mycontact.openexitsaddress()

        elif a is 'd' or a is 'D':
            index = raw_input("Which do you want to delete? ")
            try:
                index = int(index)
            except:
                print("Index error.")
                break
            try:
                p = mycontact.personlist[index-1]
            except:
                print("Index error.")
                break
            mycontact.delperson(p)

        else:
            pass

        menu(mycontact)

if __name__ == "__main__":
    test1()
