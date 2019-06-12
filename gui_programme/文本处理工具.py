#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/11/24 22:21
from tkinter import *
import os

class myGUI():
    def __init__(self, init_window):
        self.tk = init_window

    def json_to_yaml(self):
        source = self.text1.get(1.0, END).strip()
        #print('call json to yaml')
        self.text2.delete(1.0, END)
        self.text2.insert(1.0, source)

    def init_window(self):
        #self.tk.title = '文本处理v1.0'
        self.tk.geometry('400x300+400+200')
        #tk['bg'] = 'green'
        self.tk.attributes("-alpha", 0.8)

        self.label1 = Label(self.tk, text='源数据')
        self.label1.grid(row=1, column=0)
        self.label1 = Label(self.tk, text='结果')
        self.label1.grid(row=1, column=2)

        self.text1 = Text(self.tk, width=20, height=15, bg='lightgrey')
        self.text1.grid(row=2, column=0, rowspan=1, columnspan=1)
        self.text2 = Text(self.tk, width=20, height=15, bg='lightgrey')
        self.text2.grid(row=2, column=2, rowspan=1, columnspan=1)

        self.bt1 = Button(self.tk, text='json转yaml', bg='green', command=self.json_to_yaml)
        self.bt1.grid(row=2, column=1)



def main():
    mainwindow = Tk('文本处理v1.0')
    d = myGUI(mainwindow)
    d.init_window()
    mainloop()

if __name__ == '__main__':
    main()
