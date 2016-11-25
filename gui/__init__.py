# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/25
Description: __init__ file
"""

from Tkinter import *

master = Tk()

if __name__ == '__main__':
    console_label = Label(master, text="Console:").grid(row=0, column=0, sticky=E)
    input_label = Label(master, text="InputDir:").grid(row=1, column=0, sticky=E)

    console_message = Message(master).grid(row=0, column=1)
    input_entry = Entry(master).grid(row=1, column=1)

    button = Button(master, text='click', command=master.quit).grid(row=2, column=1)

    master.mainloop()
