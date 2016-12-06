# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/25
Description: word, powerpoint, excel class unit
"""

try:
    import sys
    import transfer
    import chardet
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


class Word:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        transfer.doc_to_pdf(self.input_path, output_path)


class PowerPoint:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        transfer.ppt_to_pdf(self.input_path, output_path)

    def transfer_to_jpgs(self, output_path):
        transfer.ppt_to_jpg(self.input_path, output_path)


class Excel:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        transfer.excel_to_pdf(self.input_path, output_path)


if __name__ == '__main__':
    input_path = "D:/CourseSource/[LZ-Y1001]认识空气-1.0版/[LZ-Y1001]认识空气-学生课程材料/doc-副本.doc"
    print chardet.detect(input_path)

    # word = Word(input_path)
    # print word.input_path

    output_path = "D:/doc-副本.pdf"
    # word.transfer_to_pdf(output_path)

    transfer.doc_to_pdf(input_path, output_path)
