# Source download
* pywin32: https://sourceforge.net/projects/pywin32/
* python35: https://www.python.org/downloads/

# Project document
## prepare
1. 安装python3.5，链接如上
2. windows环境下需要配置环境变量，如何配置请参考：http://blog.csdn.net/lyj_viviani/article/details/51763101
3. 安装pywin32，该模块用来操作office软件，注意，需要下载python35对应的模块版本，可参考如上链接的README文档

## how to use
1. 配置config.conf文件，该文件主要用以控制文件转换的格式，具体配置方法见config.conf
2. 配置hand_over.conf文件，该文件主要用以控制交付文件清单的产出，具体配置方法见hand_over.conf
3. 配置好之后使用命令行进入format-transfer目录，输入命令：python gui_starter.py即可

# For help

* email: ly.forwork@foxmail.com
* QQ: 411732404

# source url
tkinter framework: http://blog.chinaunix.net/uid-22334392-id-3604020.html

how to use config file: http://blog.chinaunix.net/uid-24585858-id-4820471.html

win32shell: http://blog.csdn.net/thundor/article/details/5968581

how to copy file in py: http://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p07_copy_move_files_and_directories.html

py2exe: http://jingyan.baidu.com/article/a378c960b47034b3282830bb.html