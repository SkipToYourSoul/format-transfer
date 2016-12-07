# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/25
Description: word, powerpoint, excel class unit
"""

import bean.file_to_jpg as ppt_to_jpg
import bean.file_to_pdf as file_to_pdf


class Word:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        file_to_pdf.doc_to_pdf(self.input_path, output_path)


class PowerPoint:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        file_to_pdf.ppt_to_pdf(self.input_path, output_path)

    def transfer_to_jpgs(self, output_path):
        ppt_to_jpg.ppt_to_jpg(self.input_path, output_path)


class Excel:
    def __init__(self, input_path):
        self.input_path = input_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def get_input_path(self):
        return self.input_path

    def transfer_to_pdf(self, output_path):
        file_to_pdf.excel_to_pdf(self.input_path, output_path)


if __name__ == '__main__':
    input_path = "C:/Users/liye/Desktop/format-test/CourseSource/[LZ-Y1001]认识空气-1.0版/[LZ-Y1001]认识空气-器材清单.xlsx"
    input_path = input_path.replace('/', '\\')
    excel = Excel(input_path)

    output_path = "C:/Users/liye/Desktop/format-test/Course4Teacher/[LZ-Y1001]认识空气-1.0版/[LZ-Y1001]认识空气-器材清单.pdf"
    output_path = output_path.replace('/', '\\')

    excel.transfer_to_pdf(output_path)
