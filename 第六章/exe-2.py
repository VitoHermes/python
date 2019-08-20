#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 11:07
# @Author  : Vito  
# @File    : exe-2.py.py


def calculate_count(data_str):
    dict_count = {'alpha': 0, 'number': 0, 'space': 0, 'other': 0}
    for i in data_str:
        if i.isalpha():
            dict_count['alpha'] += 1
        elif i.isdigit():
            dict_count['number'] += 1
        elif i.isspace():
        # elif i is ' ':
            dict_count['space'] += 1
        else:
            dict_count['other'] += 1
    return dict_count


res = calculate_count('32441adhjf  ^&%$#@()*')
print(res)