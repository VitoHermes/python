#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 11:10
# @Author  : Vito  
# @File    : exe-3.py


def judge_length(data):
    if len(data) > 5:
        return True
    else:
        return False


res1 = judge_length('sahdlfk')
res2 = judge_length([12, 2, 3, ])
res3 = judge_length((2, 3, 4, 5, 6, 5,))
print(res1)
print(res2)
print(res3)