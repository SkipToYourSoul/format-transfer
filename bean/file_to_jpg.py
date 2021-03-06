# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/23
Description: transfer ppt(x) to jpgs
"""
import os
import traceback

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


def ppt_to_jpg(input_path, output_path):
    powerpoint = gencache.EnsureDispatch('Powerpoint.application')
    try:
        powerpoint.DisplayAlerts = 0
        ppt = powerpoint.Presentations.Open(input_path)
        for i, slide in enumerate(ppt.Slides):
            slide.Select
            full_path = os.path.join(output_path, "%d.jpg" % i)
            slide.Export(full_path, "JPG")
        return 0
    except Exception as e:
        traceback.format_exc()
        return 1
    finally:
        powerpoint.Quit()
