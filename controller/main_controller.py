# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description:
"""

import configparser
from tkinter import *
import tkinter.messagebox
import os
import traceback
import bean.office_unit as bean
import shutil
import logging
import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./logs/backend.' + str(datetime.date.today()) + '.log',
                    filemode='a')


def transfer_to_diff_dirs(gui, course_dir):
    # get course name
    course_name = course_dir.replace(os.path.dirname(course_dir)+"/", "")
    course_name = course_name.split("-")[0] + "-" + course_name.split("-")[1]

    # check the course name: start with LZ
    if not str(course_name).startswith("LZ", 1, 3):
        tkinter.messagebox.showinfo(gui.content_frame, message="You choose an error directory.")
        show_message(gui, '> You choose an error directory, please retry.')
        return

    show_message(gui, '>>>\n> Begin to handle course: ' + course_name)

    # get config file and do it
    config_dict = get_config(course_name)
    logging.info(config_dict)
    for key, val in config_dict.items():
        show_message(gui, '---\n> Start to do ' + key + ' files')
        sub_transfer_to_dirs(gui, course_dir, key, val)
        show_message(gui, '> Complete to do ' + key + ' files\n---')

    tkinter.messagebox.showinfo(gui.content_frame, message="Success")


def sub_transfer_to_dirs(gui, course_dir, dir_tag, sub_config_dict):
    try:
        # make new dirs if not exists
        new_dir_name = "Course4" + dir_tag
        new_path = make_dir_if_not_exists(course_dir, new_dir_name)

        for key, val in sub_config_dict.items():
            # check input file exists
            input_path = get_abs_path(course_dir + "/" + val)
            if not os.path.exists(input_path):
                show_message(gui, '> Current course has not ' + val + ', continue.')
                continue

            # transfer files
            if key.startswith('transfer'):
                transfer_type = key.split(".")[-1]
                suffix = os.path.splitext(input_path)[1]
                output_path = get_abs_path(new_path + "/" + val)
                output_path = get_abs_path(output_path.replace(suffix, '.' + transfer_type))
                if os.path.exists(output_path):
                    show_message(gui, '> ' + val + ' has already exists, continue.')
                    continue
                show_message(gui, '> Transfer ' + input_path + ' to ' + output_path)
                transfer_files(suffix, input_path, output_path)

            # copy files
            elif key.startswith('copy'):
                output_path = get_abs_path(new_path + "/" + val)
                if os.path.exists(output_path):
                    show_message(gui, '> ' + val + ' has already exists, continue.')
                    continue
                show_message(gui, '> Copy ' + input_path + ' to ' + output_path)
                if key.split(".")[-1] == "dir":
                    shutil.copytree(input_path, output_path)
                elif key.split(".")[-1] == "file":
                    shutil.copy(input_path, output_path)
    except Exception as e:
        traceback.print_exc()
        logging.error(e)
        tkinter.messagebox.showinfo(gui.content_frame, message="Some mistake occurred.")
        return


def transfer_files(suffix, input_path, output_path):
    # if suffix == ".docx" or suffix == ".doc":
    #     word = bean.Word(input_path)
    #     word.transfer_to_pdf(output_path)
    #
    # if suffix == ".pptx" or suffix == ".ppt":
    #     ppt = bean.PowerPoint(input_path)
    #     if transfer_type == "pdf":
    #         ppt.transfer_to_pdf(output_path)
    #     elif transfer_type == "jpg":
    #         ppt.transfer_to_jpgs(output_path)
    return


def make_dir_if_not_exists(course_dir, dir_name):
    # make new dirs if not exists
    parent_dir = os.path.dirname(course_dir)
    further_parent_dir = os.path.dirname(parent_dir)
    file_path = further_parent_dir + "/" + dir_name
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


def get_config(course_name):
    config_file = configparser.ConfigParser()
    config_file.read("./config.conf", "utf-8")
    config_dict = {}

    for section in config_file.sections():
        section_dict = {}
        for key, value in config_file.items(section):
            value = value.replace('$CN', course_name)
            section_dict[key] = value
        config_dict[section] = section_dict

    return config_dict


def show_message(gui, message):
    gui.console_text.insert(END, message + '\n')
    gui.console_text.update()


def get_abs_path(current_path):
    if not os.path.isabs(current_path):
        return os.path.abspath(current_path)
    else:
        return current_path
