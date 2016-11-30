# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description:
"""

from Tkinter import *
import ConfigParser
import tkMessageBox
import os
import sys
import bean

reload(sys)
sys.setdefaultencoding("utf8")

teacher_config_map = {}


def course_for_teacher(gui, course_dir):
    # get config file
    course_name = course_dir.replace(os.path.dirname(course_dir)+"/", "")
    print course_name
    if not str(course_name).startswith("LZ", 1, 3):
        tkMessageBox.showinfo(gui.content_frame, message="You choose an error directory.")
        gui.console_text.insert(END, 'You choose an error directory.\n')
        gui.console_text.update()
        return
    get_config(course_name)

    # make new dirs if not exists
    teacher_path = make_dir_if_not_exists(course_dir, "Course4Teacher")

    # transfer and copy files to new directory
    try:
        for key, val in teacher_config_map.items():
            if key.startswith('transfer'):
                transfer_type = key.split(".")[-1]
                input_path = course_dir + "/" + val
                output_path = teacher_path + "/" + val
                suffix = os.path.splitext(input_path)[1]
                output_path = output_path.replace(suffix, '.' + transfer_type)

                if not os.path.isabs(input_path):
                    input_path = os.path.abspath(input_path)

                if not os.path.isabs(output_path):
                    output_path = os.path.abspath(output_path)

                # print key
                # print val
                # print transfer_type
                # print suffix
                # print input_path
                # print output_path

                if suffix == ".docx" or suffix == ".doc":
                    word = bean.Word(input_path)
                    word.transfer_to_pdf(output_path)

                if suffix == ".pptx" or suffix == ".ppt":
                    ppt = bean.PowerPoint(input_path)
                    if transfer_type == "pdf":
                        ppt.transfer_to_pdf(output_path)
                    elif transfer_type == "jpg":
                        ppt.transfer_to_jpgs(output_path)
    except Exception, e:
        tkMessageBox.showinfo(gui.content_frame, message="Some mistake occurred.")

    tkMessageBox.showinfo(gui.content_frame, message="Success")


def make_dir_if_not_exists(course_dir, dir_name):
    # make new dirs if not exists
    parent_dir = os.path.dirname(course_dir)
    further_parent_dir = os.path.dirname(parent_dir)
    file_path = further_parent_dir + "/" + dir_name
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


def get_config(course_name):
    config_file = ConfigParser.ConfigParser()
    config_file.read("./config.conf")

    for key, value in config_file.items("teacher"):
        value = value.replace('$CN', course_name)
        teacher_config_map[key] = value
