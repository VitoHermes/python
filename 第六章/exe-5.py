#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 11:12
# @Author  : Vito  
# @File    : exe-5.py


def get_odd_list(data):
    """
    获取奇数位索引的新列表
    :param data: 输入列表
    :return: 输出列表
    """
    odd_list = []
    for i in data:
        if data.index(i) % 2:
            odd_list.append(i)
    return odd_list


print(get_odd_list([1, 2, 3, 4, ]))
print(get_odd_list((13, 4322, 2333, 114,)))
print(get_odd_list(['a', 'b', 'c', 'd']))