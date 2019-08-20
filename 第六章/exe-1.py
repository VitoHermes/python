#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-19 20:30
# @Author  : Vito  
# @File    : exe-1.py

"""
写函数，用户传入修改的文件名，与要修改的内容，执行函数完成修改操作
"""
file_data = ""


def alter_info(file_name, old_str, new_str):
    global file_data
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file_name, 'w', encoding='utf-8') as f1:
        f1.write(file_data)