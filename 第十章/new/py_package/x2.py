#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 09:34
# @Author  : Vito  
# @File    : x2.py

# 相对导入
def func2():
    print('pkg.x2.func2')

if __name__ == '__main__':
    from x1 import func1
    func1()