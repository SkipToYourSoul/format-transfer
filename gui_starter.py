# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description: Start GUI
"""

try:
    import sys
    from Tkinter import *
    from gui import *
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


def main():
    root = Tk()
    root.title('File Transfer')
    root.resizable(0, 0)
    center_window(root, 640, 360)
    container = MainContainer(os.curdir, root)
    container.hello_message()
    root.mainloop()

if __name__ == '__main__':
    main()
