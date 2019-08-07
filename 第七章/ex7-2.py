#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 15:53
# @Author  : Vito  
# @File    : ex7-2.py.py
"""
import functools
import time

path_log = 'log'
current_user = {
    'username':None,
    'session_time':10,  # session 有效时间20 s
    'session_begin':0
}

with open('account','r',encoding='utf-8') as f:
    account = eval(f.read().strip())

def auth(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if current_user['username'] and (int(time.time()) - current_user['session_begin']) < current_user['session_time']:
            res = func(*args,**kwargs)
            return res
        else:
            name = input('请输入用户名:')
            passwd = input('请输入密码:')
            if name == account['name'] and passwd == account['passwd']:
                print('登录成功')
                current_user['username'] = name
                current_user['session_begin'] = int(time.time())
                res = func(*args,**kwargs)
                return res
            else:
                print('用户名或密码输入错误')
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        with open(path_log,'a+',encoding='utf-8') as f:
            f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\t'+
                    func.__name__  +' function executing...\n')
        res = func(* args, * kwargs)
        return res
    return wrapper

@logger
@auth
def shopping():
    time.sleep(5)
    print('shopping...')

@logger
@auth
def buy():
    time.sleep(10)
    print('buy...')

@logger
def test():
    print('testing ...')

"""


from functools import wraps
import time
auth_time = 5.0 # 登录有效时间为5秒
login_time = 0.0 # 记录登录时间，判断是否超时
with open('pwd.txt','r',encoding="utf-8") as f1:
    user_dic = eval(f1.readline())
    user_info = {user_dic["name"]:user_dic["pwd"]}
current_user = {'username':None}
def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global login_time
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
            login_time = time.time()
            print(login_time)
            current_user['username'] = name
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
