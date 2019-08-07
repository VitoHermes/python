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
            #print(login_time)
            current_user['username'] = name
            return func(*args, **kwargs)
        else:
            print("Wrong password!")
    return wrapper

def log_func(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        with open(log_url,'a+',encoding='utf-8') as f1:
            f1.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\t'+"function:"+ func.__name__ +'  executed\n')
        res = func(*args, *kwargs)
        return res
    return wrapper

@log_func
@auth
def index():
    print("From index.")
    time.sleep(1)

@log_func
@auth
def index1():
    print("From index1.")
    time.sleep(5)

@log_func
@auth
def index2():
    print("From index2.")
    time.sleep(5)

if __name__ == '__main__':
    index()
    index2()
    index1()
