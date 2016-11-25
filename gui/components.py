# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description: 
"""

from Tkinter import *
import tkFileDialog
import tkMessageBox
import os


class MainContainer(object):
    def __init__(self, init_dir=None, master=None):
        # top area
        top_frame = Frame(master, height=80)
        top_frame.pack(side=TOP)
        self.dir_label = Label(top_frame, text=u'The directory you choose is: ')
        self.entry_var = StringVar()
        self.dir_entry = Entry(top_frame, textvariable=self.entry_var)
        self.dir_button = Button(top_frame, command=self.open_dir, text=u'Choose directory')
        self.transfer_button = Button(top_frame, command=self.transfer_files, text=u'Transfer')

        self.dir_label.grid(row=0, column=0, sticky=W)
        self.dir_entry.grid(row=0, column=1)
        self.dir_button.grid(row=0, column=2)
        self.transfer_button.grid(row=0, column=4, sticky=E)

        #self.dir_entry.bind('', func=self.refresh)

        # content area
        self.content_frame = Frame(master, bg='white')
        self.content_frame.pack(side=TOP, fill=BOTH)

        self.text_bar = Scrollbar(self.content_frame, orient=VERTICAL)
        self.bottom_bar = Scrollbar(self.content_frame, orient=HORIZONTAL)
        self.console_text = Text(self.content_frame, yscrollcommand=self.text_bar.set, wrap=CHAR)

        self.text_bar.config(command=self.console_text.yview)

        self.text_bar.pack(side=RIGHT, fill=Y)
        self.console_text.pack(side=LEFT, fill=BOTH, expand=1)

    def open_dir(self):
        self.console_text.delete('1.0', '999999.0')
        self.dir_name = tkFileDialog.askdirectory()
        self.entry_var.set(self.dir_name)
        show_message = 'just for tip!'
        if not self.dir_name:
            self.message_box = tkMessageBox.showinfo(self.content_frame, message=show_message)
        for each_dir in os.listdir(self.entry_var.get()):
            self.console_text.insert(END, each_dir + '\r\n')
        self.console_text.update()

    def refresh(self, event=None):
        self.console_text.delete('1.0', '9999999.0')
        for each_dir in os.listdir(self.entry_var.get()):
            self.console_text.insert(END, each_dir + '\r\n')
        self.console_text.update()

    def transfer_files(self):
        self.console_text.insert(END, 'Hello')
        self.console_text.update()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)


if __name__ == '__main__':
    root = Tk()
    root.title('File Transfer')
    root.columnconfigure(0, minsize=50)
    # root.resizable(0, 0)
    # center_window(root, 640, 360)

    #root.columnconfigure(0, weight=1)
    #root.rowconfigure(0, weight=1)
    #root.geometry('640x360')  #设置了主窗口的初始大小960x540 800x450 640x360

    MainContainer(os.curdir, root)
    mainloop()