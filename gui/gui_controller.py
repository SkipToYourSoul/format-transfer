# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/11/26
Description:
    transfer controller
    1. read config file
    2. transfer/copy files according the config file
"""

from gui.__init__ import *
import gui.gui_config as CONFIG

# define the log
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./logs/backend.' + str(datetime.date.today()) + '.log',
                    filemode='a')


# entrance function
def transfer_to_diff_dirs(gui, course_dir):
    # STEP1: get course name and check the directory
    # A course name may: [LZ-Y1001]认识空气-1.0版
    course_name = course_dir.replace(os.path.dirname(course_dir)+"/", "")

    # check the course name: start with LZ
    if len(course_name.split("-")) < 2 or \
            not str(course_name).startswith("LZ", 1, 3) or \
            not os.path.dirname(course_dir).endswith("CourseSource"):
        tkinter.messagebox.showinfo(gui.content_frame, message="你选择了一个错误的目录")
        show_message(gui, '> 请确认你选择的目录，注意以下两点')
        show_message(gui, '>  1. 确认你的课程名为以下格式 <[LZ-XXXX]-xx>')
        show_message(gui, '>  2. 确认你的课程目录结构为 <CourseSource/course_dir>\n')
        return

    # filter course name to normal format: [LZ-Y1001]认识空气
    course_name = course_name.split("-")[0] + "-" + course_name.split("-")[1]

    # STEP2: begin to transfer file according to the config file
    show_message(gui, '>>>\n> 开始处理课程文件: ' + course_name)

    # get config file and check the config is correct
    config_dict = CONFIG.get_config(course_name)
    if len(config_dict) == 0:
        show_message(gui, '> 配置文件出错，中断程序.\n')
        return

    # do the transfer work
    for key, val in config_dict.items():
        show_message(gui, '---\n> 开始处理 ' + key + ' 文件夹')
        if sub_transfer_to_dirs(gui, course_dir, key, val, course_name) == 0:
            show_message(gui, '> ' + key + ' 文件夹处理完成\n---')
        else:
            show_message(gui, '> ' + key + ' 文件夹处理异常\n---')

    show_message(gui, '> ' + course_name + '转换完成, 请查看文件是否正确!\n>>>')


# course_dir: xxxx/CourseSource/[LZ-Y1001]认识空气-1.0版
# dir_tag: teacher, production, business etc.
# sub_config_dict: detail config of a config section
# course_name: [LZ-Y1001]认识空气
def sub_transfer_to_dirs(gui, course_dir, dir_tag, sub_config_dict, course_name):
    try:
        # make new dirs if not exists
        new_dir_name = "Course4" + dir_tag
        new_path = make_dir_if_not_exists(course_dir, new_dir_name)

        for key, val in sub_config_dict.items():
            # check input file exists in current course
            input_path = get_abs_path(course_dir + "/" + val)
            if not os.path.exists(input_path):
                continue

            # transfer files
            if key.startswith('transfer'):
                # transfer [suffix] to [transfer_type]
                transfer_type = key.split(".")[-1]
                suffix = os.path.splitext(input_path)[1]
                output_path = get_abs_path(new_path + "/" + val)

                # put jpgs to a directory
                if transfer_type == "jpg":
                    output_path = get_abs_path(output_path.replace(suffix, ''))
                else:
                    output_path = get_abs_path(output_path.replace(suffix, '.' + transfer_type))
                if os.path.exists(output_path):
                    show_message(gui, '> 文件' + val + ' 已经转换完成')
                    continue
                show_message(gui, '- 将：' + input_path + '\n - 转换为： ' + output_path + '\n')
                transfer_files(suffix, transfer_type, input_path, output_path)

            # copy files
            elif key.startswith('copy'):
                output_path = get_abs_path(new_path + "/" + val)
                if os.path.exists(output_path):
                    show_message(gui, '> 文件' + val + ' 已经复制完成')
                    continue
                if key.split(".")[-1] == "dir":
                    shutil.copytree(input_path, output_path)
                elif key.split(".")[-1] == "file":
                    shutil.copy(input_path, output_path)
                show_message(gui, '- 将：' + input_path + '\n - 复制到： ' + output_path + '\n')
    except Exception as e:
        traceback.print_exc()
        logging.error(e)
        tkinter.messagebox.showinfo(gui.content_frame, message="转换如下文件夹中的文件时发生错误： " + dir_tag)
        return 1

    try:
        # hand over file
        hand_over_file = new_path + "/" + dir_tag + "交付文件清单.txt"
        hand_over_config = CONFIG.get_handover_config(course_name)
        file = open(hand_over_file, "w")

        for key, val in sub_config_dict.items():
            handover_config_section = "%s.%s" % (dir_tag, key.split('.')[1])
            if handover_config_section in hand_over_config.keys():
                file.write("%s -> 交付说明:\n" % val)
                for handover_key, handover_value in hand_over_config[handover_config_section].items():
                    file.write("%s: %s\n" % (handover_key, handover_value))
                file.write("\n")
        file.close()
    except Exception as e:
        traceback.print_exc()
        logging.error(e)
        tkinter.messagebox.showinfo(gui.content_frame, message="生成如下交付文件清单时发生错误： " + dir_tag)
        return 1

    return 0


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


def show_message(gui, message):
    gui.console_text.insert(tkinter.END, message + '\n')
    gui.console_text.update()


def get_abs_path(current_path):
    if not os.path.isabs(current_path):
        return os.path.abspath(current_path)
    else:
        return current_path
