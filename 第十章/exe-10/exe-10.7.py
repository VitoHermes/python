#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 15:40
# @Author  : Vito  
# @File    : exe-10.7.py

# 练习7
# 使用random模块写一个随机生成8位验证码的程序，验证码中由大小写字母和数字。
import random
import re
all_char = 'abcdefghijklmnopqrstuvwxyz'
all_char += all_char.upper()
all_char += '1234567890'

password = ''
for i in range(8):
    password += random.choice(all_char)
print(password)