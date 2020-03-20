"""
__title__ = ''
__author__ = 'yonghui Luo'
__mtime__ = '2019-02-27'
"""
#!/usr/bin/env python3

# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import *
import sqlite3


def set_degree(value):
    global input_degree
    input_degree = value


def select_db_file():
    db_file = askopenfilename(title="请选择BaiduYunCacheFileV0.db文件", filetypes=[('db', '*.db')])
    db.set(db_file)
    print("run select_db_file end!")


def select_save_file():
    save_file = asksaveasfilename(filetypes=[('文件', '*.txt')])
    f.set(save_file + ".txt")
    print("run select_save_file end!")


def select_save_csv_file():
    save_file = asksaveasfilename(filetypes=[('文件', '*.csv')])
    f.set(save_file + ".csv")
    print("run select_save_file end!")


def set_degree_value(*args):
    value = comboxlist.get()
    if value == "全部":
        set_degree(100)
    else:
        set_degree(value)
    print(input_degree)


def write_csv_file(file_dict, f, item, gap="", curr_degree=-1):
    # print("degree=" + str(curr_degree) + "  input_degree=" + str(input_degree))
    tem_list = ["┣━"]
    if item == "/":
        f.write("━" + "/" + "\n")
        for i in file_dict["/"]:
            f.write("┣" + "━" + i + "\n")
            i = item + i + "/"
            if i in file_dict:
                write_csv_file(file_dict, f, i, gap="┣━", curr_degree=1)
    else:
        curr_degree += 1
        tem_list.insert(0, "┃  ")
        gap = "┃  " + gap
        for i in file_dict[item]:
            tem_list.append(i)
            f.write(gap + i + "\n")
            i = item + i + "/"
            if i in file_dict and curr_degree < int(input_degree):
                write_csv_file(file_dict, f, i, gap, curr_degree=curr_degree)


def create_baiduyun_filelist():
    print("start get baidun_filelist..... ")
    file_dict = {}
    conn = sqlite3.connect(db.get())
    cursor = conn.cursor()
    cursor.execute("select * from cache_file")
    while True:
        value = cursor.fetchone()
        if not value:
            break
        path = value[2]
        name = value[3]
        size = value[4]
        isdir = value[6]
        if path not in file_dict:
            file_dict[path] = []
            file_dict[path].append(name)
        else:
            file_dict[path].append(name)

    with open(f.get(), "w", encoding='utf-8') as fp:
        write_csv_file(file_dict, fp, "/")

window = Tk()
window.geometry('600x300')
window.title('百度云文件列表生成工具')

db_select = Button(window, text=' 选择DB文件 ', command=select_db_file)
db_select.grid(row=1, column=1, sticky=W, padx=(2, 0), pady=(2, 0))

db = StringVar()
db_path = Entry(window, width=80, textvariable=db)

db_path['state'] = 'readonly'
db_path.grid(row=1, column=2, padx=3, pady=3, sticky=W + E)

save_path = Button(window, text='选择保存地址', command=select_save_csv_file)
save_path.grid(row=2, column=1, sticky=W, padx=(2, 0), pady=(2, 0))

f = StringVar()
file_path = Entry(window, width=80, textvariable=f)
file_path['state'] = 'readonly'
file_path.grid(row=2, column=2, padx=3, pady=3, sticky=W + E)

degree_button = Button(window, text='选择文件深度')
degree_button.grid(row=3, column=1, sticky=W, padx=(2, 0), pady=(2, 0))

input_degree = 100   #默认为所有的

comboxlist = Combobox(window, textvariable=input_degree)
comboxlist["values"] = ("全部", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
comboxlist.current(0)  #选择第一个
comboxlist.bind("<<ComboboxSelected>>", set_degree_value)  #绑定事件,(下拉列表框被选中时，绑定set_degree_value()函数)
comboxlist.grid(row=3, column=2, padx=3, pady=3, sticky=W + E)

print(input_degree)

create_btn = Button(window, text='生成文件列表', command=create_baiduyun_filelist)
create_btn.grid(row=4, column=1, columnspan=2, pady=(0, 2))

window.columnconfigure(2, weight=1)
window.mainloop()
