#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-12 15:04
# @Author  : Vito  
# @File    : ex8-1.py

import random

def conflict(state,nextX): # 检测下一个皇后和之前的是否冲突
    nextY = len(state) # 计算Y坐标值
    for i in range(nextY):
        if abs(nextX-state[i]) in (0, nextY-i): # 这个皇后和其他皇后的水平距离不能为0或者等于垂直距离（在一条对角线上）
            return True
    return False

def queens(num=8,state=()): # 程序主体部分
    for pos in range(num):
        if not conflict(state,pos): # 不冲突，则增加
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num,state + (pos,)): # 递归
                    yield (pos,) + result

def prettyprint(solution):
    def line(pos, length = len(solution)):
        return 'O'*(pos) + 'X' + 'O'*(length-pos-1)
    for pos in solution:
        print(line(pos))

prettyprint(random.choice(list(queens(8)))) # 图形化输出，92组解中选择一个

# 方法二
from itertools import permutations
for vec in permutations(range(8)):
    if (8 == len(set(vec[i]+i for i in range(8)))== len(set(vec[i]-i for i in range(8)))):
        print(vec)