# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description: Start GUI here
"""
from tkinter import *
import os
import gui.gui_components as gui


def main():
    root = Tk()
    root.title('File-Transfer')
    root.resizable(0, 0)
    gui.center_window(root, 800, 600)
    container = gui.MainContainer(os.curdir, root)
    container.hello_message()
    root.mainloop()

if __name__ == '__main__':
    main()
