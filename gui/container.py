# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/25
Description: gui container class
"""

from Tkinter import *


def init_container():
    master_container = Tk()
    master_container.title("Transfer")
    master_container.resizable(0, 0)
    center_window(master_container, 640, 360)

    console_frame = Frame(master_container)
    console_frame.pack(padx=5, pady=5, fill=BOTH, expand=YES)

    title_label = Label(console_frame, text="Console")
    title_label.pack(side=LEFT)
    scrollbar = Scrollbar(console_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(console_frame, yscrollcommand=scrollbar.set)
    listbox.pack(padx=5, pady=5, fill=BOTH, expand=YES)

    button_frame = Frame(master_container)
    button_frame.pack(padx=5, pady=5, fill=X)

    input_label = Label(button_frame, text="InputDir:")
    input_label.pack(side=LEFT)
    input_entry = Entry(button_frame)
    input_entry.pack(side=LEFT)

    transfer_button = Button(button_frame, text='TRANSFER', command=lambda : do_transfer(listbox))
    transfer_button.pack(side=LEFT)
    quit_button = Button(button_frame, text='QUIT', command=master_container.quit)
    quit_button.pack(side=RIGHT)

    master_container.mainloop()
    master_container.destroy()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)


def do_transfer(listbox, scrollbar):
    print "Hello"
    listbox.insert(END, "Hello")
    scrollbar.config(command=listbox.yview)


if __name__ == '__main__':
    init_container()

