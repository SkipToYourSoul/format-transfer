# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/19
Description: get config file
"""

from gui.__init__ import *

# define the log
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./logs/backend.' + str(datetime.date.today()) + '.log',
                    filemode='a')
config_path = "./config.conf"
handover_config_path = "./hand_over.conf"


def get_config(course_name):
    config_dict = {}

    try:
        config_file = configparser.ConfigParser()
        config_file.read(config_path, "utf-8")
        for section in config_file.sections():
            section_dict = {}
            for key, value in config_file.items(section):
                value = value.replace('$CN', course_name)
                section_dict[key] = value
            config_dict[section] = section_dict
    except Exception as e:
        config_dict = {}
        traceback.print_exc()
        logging.error(e)
    finally:
        return config_dict


def get_handover_config(course_name):
    config_dict = {}

    try:
        config_file = configparser.ConfigParser()
        config_file.read(handover_config_path, "utf-8")
        for section in config_file.sections():
            section_dict = {}
            for key, value in config_file.items(section):
                value = value.replace('$CN', course_name)
                section_dict[key] = value
            config_dict[section] = section_dict
    except Exception as e:
        config_dict = {}
        traceback.print_exc()
        logging.error(e)
    finally:
        return config_dict
