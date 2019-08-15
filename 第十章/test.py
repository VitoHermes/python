#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 20:37
# @Author  : Vito  
# @File    : test.py
"""
import spam as sm

# print(spam)

print(sm.money)
sm.read1()

money = 1
read1 = 2
read2 = 3

print(sm.read1)
sm.read1()
sm.read2()
sm.change()
print(money)
sm.read1()

engine = input(">>".strip())
if engine == 'mysql':
    import mysql as db
else:
    import oracle as db


from spam import money, read1, read2, change

print(money)
read1()
read2()
change()

money = 2
change()
print(money)
# print(spam.money)  报错
read1 = 4
print(money)
read1()   # TypeError: 'int' object is not callable
from spam import *  # 全部导入


from spam import *  # 全部导入
print(read2)  # NameError: name 'read2' is not defined


# 绝对导入 执行文件在包所在文件夹外
from new.py_package import x1, x2

x1.func1()
x2.func2()

# 绝对导入
from pk.sub_pkg1 import moduleX


# 常用模块
# time
# 1、时间戳
import time
print(time.time())

# 2、格式化字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %X %p'))

# 3、struct_time对象
print(time.localtime())
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=15, tm_hour=11, tm_min=45, tm_sec=32, tm_wday=3, tm_yday=227, tm_isdst=0)
print(time.localtime().tm_year)  # 2019
print(time.localtime().tm_mday)  # 15

print(time.gmtime())  # UTC时区


# 用time模块来模拟网络延迟打印进度条
def progress(percent, width=50):
    if percent > 1:
        percent = 1
    show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
    print('\r%s %d%%' % (show_str, int(100 * percent)), end='')

recv_size = 0
total_size = 809700
while recv_size < total_size:
    time.sleep(0.1)
    recv_size += 8096
    percent = recv_size / total_size
    progress(percent)

# datatime模块
import datetime
print(datetime.datetime.now())
datetime.timedelta(365).total_seconds() # 一年包含的总秒数
dt = datetime.datetime.now()
dt + datetime.timedelta(3) # 3天后
datetime.datetime(2017, 2, 8, 9, 39, 40, 102821)
dt + datetime.timedelta(-3) # 3天前
datetime.datetime(2017, 2, 2, 9, 39, 40, 102821)
dt + datetime.timedelta(hours=3) # 3小时后
datetime.datetime(2017, 2, 5, 12, 39, 40, 102821)
dt + datetime.timedelta(hours=-3) # 3小时前
datetime.datetime(2017, 2, 5, 6, 39, 40, 102821)
dt + datetime.timedelta(hours=3, seconds=30) # 3小时30秒后
datetime.datetime(2017, 2, 5, 12, 40, 10, 102821)

# shutil 和 tarfile
import shutil
import time

ret = shutil.make_archive(
    "模块对象_%s" % time.strftime('%Y-%m-%d'),
    'gztar',
    root_dir=r'/Users/zhangzhiyu/Desktop/python/github_test/python/第十章'
)

import tarfile

t = tarfile.open('')

import json
dic1 = {'name': 'vito', 'age': 18}

# 序列化
with open('db1.json', 'wt', encoding='utf-8') as f1:
    json.dump(dic1, f1)

# 反序列化
with open('db1.json', 'rt', encoding='utf-8') as f1:
    dic2 = json.load(f1)
    print(dic2)

import os
# 输出当前目录
res = os.getcwd()
print(res)

# 输出目录下的文件名
res = os.listdir()
print(res)

#
print(os.sep)  # https://blog.csdn.net/LittleStudent12/article/details/81020633
print(os.pathsep)
print([os.pathsep, ])
path = os.getcwd()
print(os.path.split(path))  # ('/Users/zhangzhiyu/Desktop/python/github_test/python', '第十章')

# 判断文件是否存在
print(os.path.exists(path))
print(os.path.exists(r'/Users/zhangzhiyu/Desktop/python/github_test/python'))
print(os.path.isfile(r'/Users/zhangzhiyu/Desktop/python/github_test/python'))  # 判断是否是文件

# 判断文件夹是否存在
print(os.path.isdir(r'/Users/zhangzhiyu/Desktop/python/github_test/python'))
print(os.path.join('C:\\','a','b','c.txt'))

# 得到文件大小
print(os.path.getsize(r'/Users/zhangzhiyu/Desktop/python/github_test/python/README.md'))
"""

import hashlib


# 1 字符串加密
m = hashlib.md5()
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
m.update('vito'.encode('utf-8'))
print('字符串md5值：', m.hexdigest())
#  字符串md5值： 147a5c6f36b66c189f09d529b4fcd265

# 2 文件md5校验
m = hashlib.md5()
with open(r'/Users/zhangzhiyu/Desktop/python/github_test/python/README.md', 'rb') as f1:
    for line in f1:
        m.update(line)
    file_md5 = m.hexdigest()
print('文件md5值：', file_md5)

# 3 密码加盐
import hashlib


pwd = 'vito123'
m = hashlib.md5()
m.update('天王盖地虎'.encode('utf-8'))
m.update(pwd.encode('utf-8'))
m.update('小鸡炖蘑菇'.encode('utf-8'))
print('密码md5值：', m.hexdigest())