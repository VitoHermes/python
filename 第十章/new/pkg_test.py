#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 09:35
# @Author  : Vito  
# @File    : pkg_test.py

import py_package.x1, py_package.x2

"""
1 产生一个包的空间
2 执行包下的__init__.py 文件，将产生的名字存于包的名称空间中
3 在当前执行文件中拿到一个名字a，该名字指向包的名称空间
"""

py_package.x1.func1()
py_package.x2.func2()
print(py_package.x1.func1())  # None
print(py_package.x2.func2())  # None

# 绝对导入
from new.py_package import x1, x2

x1.func1()
x2.func2()
