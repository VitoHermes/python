#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 14:53
# @Author  : Vito  
# @File    : ex7-1.py
"""
写装饰器为多个函数增加auth功能。要求登录一次，其他函数不需要密码。
auth_type='input_file': 文件输入用户名和密码
auth_type='input_info': 用户输入用户名密码
默认：用户输入用户名和密码
"""
from functools import wraps

current_user = {'username': None, 'login_status': False}
db = "pwd.txt"


def auth(auth_type='input_file'):
    def auth2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user['login_status']:
                return func(*args, **kwargs)
            if auth_type == 'input_file':
                print("yes")
                with open(db, encoding='utf-8') as f:
                    dic = eval(f.read())
                name = input('username: ').strip()
                password = input('password: ').strip()
                if name == dic['name'] and password == dic['password']:
                    current_user['login_status'] = True
                    current_user['username'] = name
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('username or password error')
            elif auth_type == 'input_info':
                pass

        return wrapper

    return auth2


@auth()
def index():
    print('index')


@auth(auth_type='input_file')
def home(name):
    print('welcome %s to home' % name)


index()
index()
home('vito')
