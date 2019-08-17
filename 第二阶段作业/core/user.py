#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 16:42
# @Author  : Vito  
# @File    : src.py

"""
用户核心逻辑:
1、用户登录
2、用户注册
3、退出
"""

import sys
import json
sys.path.append('../')
from conf import settings


# 登录流程
def login_fun():  # 登录
    wrong_time = 0  # 输错密码的次数
    with open('../db/db.json', 'r') as f:  # 读json文件
        user_list = json.load(f)
    while True:
        name = input("请输入用户名:")
        password = input("请输入密码:")
        for user_dict in user_list:  # 遍历寻找是否是注册用户
            if name == user_dict["user_name"]:  # 输入的用户名是已注册用户
                    if password == user_dict["user_pw"]:  # 密码正确
                        # 判断是否在黑名单
                        if user_dict["card_status"] == 0:
                            print("您的账号已经被冻结！")
                            sys.exit(0)
                        # 不在黑名单，登录成功
                        print("登录成功！")
                        return [True, user_dict]  # 登录成功，返回用户信息
                    elif wrong_time == 2:  # 超过次数，直接结束，加入黑名单
                        print("密码错误次数太多，进入黑名单!")
                        # 加人黑名单
                        user_dict["card_status"] = 0
                        with open('../db/db.json', 'w') as f:
                            json.dump(user_list, f)
                        return [False, None]
                    else:  # 密码错误,重新输入
                        print("密码错误，请重新输入.")
                        wrong_time += 1  # 错误次数加一
                        print(wrong_time)
                        break
            else:  # 遍历没找到，未注册
                print("您还没有注册，请先注册.")
                return [False, None]  # 登录失败


# 注册流程
def register_fun():  # 注册，初始信用卡额度为1万
    with open('../db/db.json', 'r') as f:
        user_list = json.load(f)
    user_name = input("请输入用户名:")
    password1 = input("请输入密码:")
    password2 = input("请再次输入密码:")
    # 两次密码不一致，注册失败
    if password1 != password2:
        print("两次密码不一致，注册失败。")
        return [False, None]
    # 用户名重复,注册失败
    for user_dict in user_list:
        if user_name == user_dict["user_name"]:
            print("已经有该用户名，注册失败。")
            return [False, None]

    user_new = {
        "user_name": user_name,
        "user_pw": password1,
        "card_status": 1,
        "card_account": 0,  # 初始余额为0
        "card_limit": 10000  # 初始信用卡额度为10000
    }
    user_list.append(user_new)
    print(user_list)
    with open('../db/db.json', 'w') as f:
        json.dump(user_list, f)
    print("注册成功！快去消费吧！")
    return [True, user_dict]


# 退出程序
def quit_fun():  # 退出
    print("欢迎下次使用!")
    sys.exit(0)

