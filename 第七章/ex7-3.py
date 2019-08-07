#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 16:55
# @Author  : Vito
# @File    : ex7-3.py

from functools import wraps
import time
auth_time = 5.0 # 登录有效时间为5秒
login_time = 0.0 # 记录登录时间，判断是否超时
log_url = 'function_time.txt'
with open('pwd.txt','r',encoding="utf-8") as f1:
    user_dic = eval(f1.readline())
    user_info = {user_dic["name"]:user_dic["pwd"]}
current_user = {'username':None}
def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global login_time # 允许函数内修改login_time
        #print(time.time() - login_time)
        if current_user['username'] and (time.time() - login_time) < auth_time: # 登录有效
            print('Already login!')
            res = func(*args, **kwargs)
            return res
        name = input("name:")
        pwd = input("pwd:")
        if name not in user_info:
            print("Invalid user name.")
        elif user_info[name] == pwd:
            print('login in successful!')
            login_time = time.time() # 记录登录成功的时间
            current_user['username'] = name
            return func(*args, **kwargs)
        else:
            print("Wrong password!")
    return wrapper

def log_func(log_file = 'run.log'): # 记录运行时间的log,可以指定log文件目录
    """
    改写了日志记录函数
    :param func: 被修饰函数
    :return: 新函数
    """
    def log_deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(log_file,'a+',encoding='utf-8') as f1:
                f1.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\t'+"function:"+ func.__name__ +'  executed\n')
            return func(*args, **kwargs)
        return wrapper
    return log_deco


@log_func(log_file='index.log')
@auth
def index():
    print("From index.")
    time.sleep(1)

@log_func(log_file='index1.log')
@auth
def index1():
    print("From index1.")
    time.sleep(5)

@log_func(log_file='index2.log')
@auth
def index2():
    print("From index2.")
    time.sleep(5)

if __name__ == '__main__':
    index()
    index1()
    index2()
