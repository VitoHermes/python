#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 20:37
# @Author  : Vito  
# @File    : spam.py
print('from the spam.py')
__all__ = ['money', 'read1']

money = 0


def read1():
    print("spam.read1", money)


def read2():
    print("spam.read2")
    read1()


def change():
    global money
    money = 1

print(__name__)

if __name__ == '__main__':
    print('文件在脚本中被执行')
    read1()
else:
    print('文件被导入啦')
