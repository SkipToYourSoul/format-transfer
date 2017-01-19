# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/24
Description: __init__ file
"""

try:
    from win32com.client import constants, gencache
except ImportError:
    import sys
    print(sys.stderr, """ !!!
    There was a problem importing one of the Python modules required.
    The error leading to this problem was:
    %s

    Please install a package which provides this module, or verify that the module is installed correctly.
    It's possible that the above module doesn't match the current version of Python, which is:
    %s

    """) % (sys.exc_info(), sys.version)
    sys.exit(1)

import os
import traceback