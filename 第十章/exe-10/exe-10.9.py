#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 16:02
# @Author  : Vito  
# @File    : exe-10.9.py

import re

# 中国大陆手机号正则表达式 (13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}
pattern_tel = '(13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}'
with open("嫩模联系方式.txt", 'r', encoding='utf-8') as f:
    for line in f:
        tel = re.split(r'[\s]*', line)[4]  # 用任意空格分割，取出电话号码
        # print(re.match(pattern_tel, tel))
        if re.match(pattern_tel, tel):
            print("你要的嫩模：" + line)


