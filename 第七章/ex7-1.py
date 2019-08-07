#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 14:53
# @Author  : Vito  
# @File    : ex7-1.py

from functools import wraps
with open('pwd.txt') as f1:
    user_dic = eval(f1.readline())
    user_info = {user_dic["name"]:user_dic["pwd"]}
current_user = {'username':None}
def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user['username']:
            print('Already login!')
            res = func(*args, **kwargs)
            print("After")
            return res
        name = input("name:")
        pwd = input("pwd:")
        if name not in user_info:
            print("Invalid user name.")
        elif user_info[name] == pwd:
            print('login in successful!')
            current_user['username'] = name
            return func(*args, **kwargs)
        else:
            print("Wrong password!")
    return wrapper

@auth
def index():
    print("From index.")
@auth
def index1():
    print("From index1.")
@auth
def index2():
    print("From index2.")
index()
index2()
index1()
