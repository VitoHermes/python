#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 15:53
# @Author  : Vito
# @File    : ex7-2.py.py
"""
用户登录时间有时效性，过期后还需要重新登录
"""

from functools import wraps
import time
auth_time = 5.0  # 登录有效时间为5秒
login_time = 0.0  # 记录登录时间，判断是否超时
with open('pwd.txt', 'r', encoding="utf-8") as f1:
    user_dic = eval(f1.readline())
    user_info = {user_dic["name"]: user_dic["password"]}
current_user = {'username': None, 'login_status': False}


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global login_time
        #print(time.time() - login_time)
        if (time.time() - login_time) > auth_time:
            current_user['login_status'] = False
            current_user['username'] = None
        if current_user['login_status'] and (time.time() - login_time) < auth_time:  # 登录有效
            print('Already login!')
            res = func(*args, **kwargs)
            return res
        name = input("name:")
        pwd = input("pwd:")
        if name not in user_info:
            print("Invalid user name.")
        elif user_info[name] == pwd:
            print('login in successful!')
            login_time = time.time()
            current_user['username'] = name
            current_user['login_status'] = True
            return func(*args, **kwargs)
        else:
            print("Wrong password!")
    return wrapper


@auth
def index():
    print("From index.")
    time.sleep(1)


@auth
def index1():
    print("From index1.")
    time.sleep(5)


@auth
def index2():
    print("From index2.")
    time.sleep(5)


if __name__ == '__main__':
    index()
    index2()
    index1()
