#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 11:14
# @Author  : Vito  
# @File    : exe-6.py


dict1 = {"k1": "v1v1", "k2": [11, 22, 33, 44], 'k3': (9, 8, 7, 65, 4)}


def check_up_list(data_dict):
    """
    检查字典value，保留前两位
    :param data_dict: 输入字典
    :return: 输出字典
    """
    for key, value in data_dict.items():
        if len(value) > 2:
            data_dict[key] = value[:2]
    return data_dict


res = check_up_list(dict1)
print(res)