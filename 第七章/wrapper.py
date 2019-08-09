#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 17:37
# @Author  : Vito  
# @File    : wrapper.py

from functools import wraps
def new_one(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("before")
        res = func(*args,**kwargs)
        print("after")
        return res
    return wrapper

@new_one
def func1():
    print("1")