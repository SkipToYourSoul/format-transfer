# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/25
Description: word, powerpoint, excel class unit
"""

# import transfer


class Word:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        # transfer.doc_to_pdf(self.input_path, output_path)
        print self.input_path
        print output_path


class PowerPoint:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        # transfer.ppt_to_pdf(self.input_path, output_path)
        print output_path

    def transfer_to_jpgs(self, output_path):
        # transfer.ppt_to_jpg(self.input_path, output_path)
        print output_path


class Excel:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        # transfer.excel_to_pdf(self.input_path, output_path)
        print output_path + self.input_path


if __name__ == '__main__':
    word = Word("./bean")
    print word.input_path
    word.transfer_to_pdf("./output")
