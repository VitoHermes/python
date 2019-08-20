#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 11:11
# @Author  : Vito  
# @File    : exe-4.py


def check_up_list(data_list):
    """
    保留列表前两位输出
    :param data_list: 输入列表
    :return: 列表前两位
    """
    if len(data_list) > 2:
        return data_list[:2]


res1 = check_up_list([1, 2, 3, 4, 4, 5, ])
res2 = check_up_list(['a', 'v', 'v', 'e'])
res3 = check_up_list(['x', ])

print(res1)
print(res2)
print(res3)