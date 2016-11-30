# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description: 
"""

try:
    import sys
    from Tkinter import *
    import controller as CONTROLLER
    import tkFileDialog
    import tkMessageBox
    import os
except ImportError:
    print >> sys.stderr, """ !!!
    There was a problem importing one of the Python modules required.
    The error leading to this problem was:
    %s

    Please install a package which provides this module, or verify that the module is installed correctly.
    It's possible that the above module doesn't match the current version of Python, which is:
    %s

    """ % (sys.exc_info(), sys.version)
    sys.exit(1)

reload(sys)
sys.setdefaultencoding("utf8")


class MainContainer(object):
    dir_name = ""

    def guide(self):
        self.console_text.insert(END, 'Please check the README.md\n'
                                      'More information will show in https://github.com/SkipToYourSoul/format-transfer')

    def clear(self):
        self.console_text.delete('1.0', '999999.0')

    def help(self):
        tkMessageBox.showinfo(self.root,
                              u' Author: liye \n Version: 1.0 \n Help email: liye.forwork@foxmail.com')

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
        self.dir_label = Label(top_frame, text=u'The directory you choose is: ')
        self.entry_var = StringVar()
        self.dir_entry = Entry(top_frame, textvariable=self.entry_var)
        self.dir_button = Button(top_frame, command=self.open_dir, text=u'Choose directory')
        self.transfer_button = Button(top_frame, command=self.transfer_files, text=u'Transfer')

        self.dir_label.grid(row=0, column=0, sticky=W)
        self.dir_entry.grid(row=0, column=1)
        self.dir_button.grid(row=0, column=2, padx=5)
        self.transfer_button.grid(row=0, column=3, padx=5, sticky=E)

        # content area
        self.content_frame = Frame(master, bg='white')
        self.content_frame.pack(side=TOP, fill=BOTH)

        self.text_bar = Scrollbar(self.content_frame, orient=VERTICAL)
        self.console_text = Text(self.content_frame, yscrollcommand=self.text_bar.set, wrap=CHAR)

        self.text_bar.config(command=self.console_text.yview)

        self.text_bar.pack(side=RIGHT, fill=Y)
        self.console_text.pack(side=LEFT, fill=BOTH, expand=1)

    def hello_message(self):
        self.console_text.insert(END, '-----------------------------------------------------\n')
        self.console_text.insert(END, '| Welcome to use file transfer for your course file |\n')
        self.console_text.insert(END, '| 1. Check the config file.                         |\n')
        self.console_text.insert(END, '| 2. Please choose your course dir.                 |\n')
        self.console_text.insert(END, '| 3. Click transfer button and have fun ^-^         |\n')
        self.console_text.insert(END, '-----------------------------------------------------\n')
        self.console_text.update()

    def open_dir(self):
        self.dir_name = tkFileDialog.askdirectory()
        self.entry_var.set(self.dir_name)
        if not self.dir_name:
            self.message_info("No directory was choose!")
            self.dir_name = ""
            return
        self.console_text.insert(END, 'You choose the ' + self.dir_name + ', files are as follows:' + '\n')
        for each_dir in os.listdir(self.entry_var.get()):
            self.console_text.insert(END, each_dir + '\n')
        self.console_text.update()

    def transfer_files(self):
        if self.dir_name == "":
            self.message_info("You must choose your file directory first!")
            return
        CONTROLLER.course_for_teacher(self, self.dir_name)

    def message_info(self, message):
        tkMessageBox.showinfo(self.content_frame, message=message)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)
