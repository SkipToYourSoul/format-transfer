# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/22
Description:
"""

import sys
import os
import transfer
import bean


def main():
    if len(sys.argv) == 2:
        input = sys.argv[1]
        output = os.path.splitext(input)[0]+'.pdf'
    elif len(sys.argv) == 3:
        input = sys.argv[1]
        output = sys.argv[2]
    else:
        print "error input argv length."
        return -1

    if not os.path.isabs(input):
        input = os.path.abspath(input)

    if not os.path.isabs(output):
        output = os.path.abspath(output)

    print "Input path: " + input
    print "Output path: " + output

    try:
        transfer.GenerateSupport()
        # rc = transfer.doc2pdf(input, output)
        rc = transfer.ppt2pdf(input, output)
        return rc
    except:
        return -1

if __name__ == '__main__':
    # rc = main()
    # if rc:
    #     sys.exit(rc)
    # sys.exit(0)

    # transfer.doc_to_pdf("D:\\doc.docx", "D:\\doc.pdf")
    # transfer.ppt_to_pdf("D:\\ppt.pptx", "D:\\ppt.pdf")
    # transfer.excel_to_pdf("D:\\excel.xlsx", "D:\\excel.pdf")
    # transfer.ppt_to_jpg("D:\\ppt.pptx", "D:\\jpg\\")
    word = bean.Word("./input")

