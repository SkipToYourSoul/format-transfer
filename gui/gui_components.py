# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description: gui frame
"""

import os
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import gui.gui_controller as gui_controller


class MainContainer(object):
    dir_name = ""

    def guide(self):
        self.console_text.insert(END, 'Please check the README.md\n'
                                      'More information will show in https://github.com/SkipToYourSoul/format-transfer\n\n')

    def clear(self):
        self.console_text.delete('1.0', '999999.0')

    def help(self):
        tkinter.messagebox.showinfo(self.root, ' Author: liye \n Version: 1.0 \n Help email: liye.forwork@foxmail.com')

    def __init__(self, init_dir=None, master=None):
        # menu
        self.root = master
        self.menu_bar = Menu(master)

        # file menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Guide", command=self.guide)
        file_menu.add_command(label="Clear", command=self.clear)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=file_menu.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # help menu
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.help)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        master.config(menu=self.menu_bar)

        # top area
        top_frame = Frame(master, height=80)
        top_frame.pack(side=TOP, padx=5, pady=5)
        self.dir_label = Label(top_frame, text='The directory you choose is: ')
        self.entry_var = StringVar()
        self.dir_entry = Entry(top_frame, textvariable=self.entry_var, width=50)
        self.dir_button = Button(top_frame, command=self.open_dir, text='Choose directory')
        self.transfer_button = Button(top_frame, command=self.transfer_files, text='Transfer')

        self.dir_label.grid(row=0, column=0, sticky=W)
        self.dir_entry.grid(row=0, column=1)
        self.dir_button.grid(row=0, column=2, padx=5)
        self.transfer_button.grid(row=0, column=3, padx=5, sticky=E)

        # content area
        self.content_frame = Frame(master, bg='white')
        self.content_frame.pack(side=TOP, fill=BOTH)

        self.text_bar = Scrollbar(self.content_frame, orient=VERTICAL)
        self.console_text = Text(self.content_frame, yscrollcommand=self.text_bar.set, wrap=CHAR, height=600)

        self.text_bar.config(command=self.console_text.yview)

        self.text_bar.pack(side=RIGHT, fill=Y)
        self.console_text.pack(side=LEFT, fill=BOTH, expand=1)

    def hello_message(self):
        self.console_text.insert(END, '>>>\n')
        self.console_text.insert(END, '> Welcome to use file transfer for your course file \n')
        self.console_text.insert(END, '> 1. Write your config file with the template in \'config.conf\'.\n')
        self.console_text.insert(END, '> 2. Press the Choose Button to choose your course dir.\n')
        self.console_text.insert(END, '> 3. Click transfer button and have fun ^-^\n')
        self.console_text.insert(END, '>>>\n\n')
        self.console_text.update()

    def open_dir(self):
        self.dir_name = tkinter.filedialog.askdirectory()
        self.entry_var.set(self.dir_name)
        if not self.dir_name:
            self.message_info("No directory was choose!")
            self.dir_name = ""
            return
        self.console_text.insert(END, '> You choose:\n' + self.dir_name + '\n> Files are as follows:' + '\n')
        for each_dir in os.listdir(self.entry_var.get()):
            self.console_text.insert(END, '> ' + each_dir + '\n')
        self.console_text.insert(END, '\n')
        self.console_text.update()

    def transfer_files(self):
        if self.dir_name == "":
            self.message_info("You must choose your file directory first!")
            return
        gui_controller.transfer_to_diff_dirs(self, self.dir_name)

    def message_info(self, message):
        tkinter.messagebox.showinfo(self.content_frame, message=message)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)
