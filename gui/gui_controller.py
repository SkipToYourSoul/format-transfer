# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description:
    transfer controller
    1. read config file
    2. transfer/copy files according the config file
"""

import tkinter.messagebox
import tkinter
import configparser
import os
import traceback
import shutil
import logging
import datetime
import bean.office_unit as bean

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./logs/backend.' + str(datetime.date.today()) + '.log',
                    filemode='a')


def transfer_to_diff_dirs(gui, course_dir):
    # get course name: eg [LZ-Y1001]认识空气
    course_name = course_dir.replace(os.path.dirname(course_dir)+"/", "")
    if len(course_name.split("-")) < 2:
        tkinter.messagebox.showinfo(gui.content_frame, message="You choose an error directory.")
        show_message(gui, '> A correct course directory may be [LZ-Y1001]xxxx-0.1.\n')
        return
    course_name = course_name.split("-")[0] + "-" + course_name.split("-")[1]

    # check the course name: start with LZ
    if not str(course_name).startswith("LZ", 1, 3) or not os.path.dirname(course_dir).endswith("CourseSource"):
        tkinter.messagebox.showinfo(gui.content_frame, message="You choose an error directory.")
        show_message(gui, '> You choose an error directory, please retry.')
        show_message(gui, '>  1. Confirm your course name is start with <[LZ-XXXX]>')
        show_message(gui, '>  2. Confirm your course dirs are in <CourseSource/course_dir>\n')
        return

    show_message(gui, '>>>\n> Begin to handle course: ' + course_name)

    # get config file and do it
    config_dict = get_config(course_name)
    if len(config_dict) == 0:
        show_message(gui, '> Empty config file or Wrong config file, exit.\n')
        return
    for key, val in config_dict.items():
        show_message(gui, '---\n> Start to do ' + key + ' files')
        if sub_transfer_to_dirs(gui, course_dir, key, val, course_name) == 0:
            show_message(gui, '> Complete to do ' + key + ' files\n---')
        else:
            show_message(gui, '> Not complete to do ' + key + ' files\n---')

    tkinter.messagebox.showinfo(gui.content_frame, message="Complete")
    show_message(gui, '> Complete to handle course: ' + course_name + ', please check you files, see you!\n>>>')


def sub_transfer_to_dirs(gui, course_dir, dir_tag, sub_config_dict, course_name):
    try:
        # make new dirs if not exists
        new_dir_name = "Course4" + dir_tag
        new_path = make_dir_if_not_exists(course_dir, new_dir_name)

        # hand over file
        hand_over_file = new_path + "/交付文件清单.txt"
        file = open(hand_over_file, "a")
        file.write(">>> " + course_name + "文件交付清单...\n\n")
        file_count = 1

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
                if transfer_type == "jpg":
                    output_path = get_abs_path(output_path.replace(suffix, ''))
                else:
                    output_path = get_abs_path(output_path.replace(suffix, '.' + transfer_type))
                if os.path.exists(output_path):
                    show_message(gui, '> ' + val + ' has already exists, continue.')
                    continue
                show_message(gui, '> Transfer:\n ' + input_path + '\n To\n ' + output_path)
                transfer_files(suffix, transfer_type, input_path, output_path)

            # copy files
            elif key.startswith('copy'):
                output_path = get_abs_path(new_path + "/" + val)
                if os.path.exists(output_path):
                    show_message(gui, '> ' + val + ' has already exists, continue.')
                    continue
                show_message(gui, '> Copy:\n ' + input_path + '\n To\n ' + output_path)
                if key.split(".")[-1] == "dir":
                    shutil.copytree(input_path, output_path)
                elif key.split(".")[-1] == "file":
                    shutil.copy(input_path, output_path)

            # generate file list
            gen_hand_over_file(dir_tag, key, file, course_name, file_count)
            file_count += 1
        file.close()
    except Exception as e:
        traceback.print_exc()
        logging.error(e)
        tkinter.messagebox.showinfo(gui.content_frame, message="Some mistake occurred in " + dir_tag)
        return 1
    return 0


def gen_hand_over_file(dir_tag, file_name, file, course_name, file_count):
    # current_section: Teacher
    # hand_over_file_name: transfer.studentCourse.pdf

    config_file = configparser.ConfigParser()
    config_file.read("./hand_over.conf", "utf-8")

    current_file = dir_tag + "." + file_name.split(".")[1]

    for section in config_file.sections():
        if section.upper() == current_file.upper():
            file.write("材料" + str(file_count) + ":\n")
            for key, value in config_file.items(section):
                value = value.replace('$CN', course_name)
                file.write(key + " > " + value + "\n")
    file.write("\n")


def transfer_files(suffix, transfer_type, input_path, output_path):
    if transfer_type == "jpg":
        dir_path = output_path
    else:
        dir_path = os.path.dirname(output_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    input_path = input_path.replace('/', '\\')
    output_path = output_path.replace('/', '\\')

    if suffix == ".docx" or suffix == ".doc":
        word = bean.Word(input_path)
        word.transfer_to_pdf(output_path)
    elif suffix == ".xls" or suffix == ".xlsx":
        excel = bean.Excel(input_path)
        excel.transfer_to_pdf(output_path)
    elif suffix == ".pptx" or suffix == ".ppt":
        ppt = bean.PowerPoint(input_path)
        if transfer_type == "pdf":
            ppt.transfer_to_pdf(output_path)
        elif transfer_type == "jpg":
            ppt.transfer_to_jpgs(output_path)


def make_dir_if_not_exists(course_dir, dir_name):
    # make new dirs if not exists
    parent_dir = os.path.dirname(course_dir)
    further_parent_dir = os.path.dirname(parent_dir)
    course_dir_name = course_dir.replace(parent_dir+"/", "")

    file_path = further_parent_dir + "/" + dir_name + "/" + course_dir_name
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def get_config(course_name):
    config_dict = {}

    try:
        config_file = configparser.ConfigParser()
        config_file.read("./config.conf", "utf-8")
        for section in config_file.sections():
            section_dict = {}
            for key, value in config_file.items(section):
                value = value.replace('$CN', course_name)
                section_dict[key] = value
            config_dict[section] = section_dict
    except Exception as e:
        traceback.print_exc()
        logging.error(e)
    finally:
        return config_dict


def show_message(gui, message):
    gui.console_text.insert(tkinter.END, message + '\n')
    gui.console_text.update()


def get_abs_path(current_path):
    if not os.path.isabs(current_path):
        return os.path.abspath(current_path)
    else:
        return current_path
