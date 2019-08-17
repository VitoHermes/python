#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 16:42
# @Author  : Vito  
# @File    : start.py

"""
启动程序
"""

import sys
import json

sys.path.append('../')  # 添加项目根目录到路径
from core import user  # 导入核心逻辑
from core import shopping
from core import card_account


func_dict1 = {"1": user.login_fun, "2": user.register_fun, "3": user.quit_fun}
func_dict2 = {"1": user.login_fun, "2": user.register_fun, "3": user.quit_fun}

if __name__ == '__main__':
    print("欢迎来到电子商城！")
    login_status = False  # 登录状态
    while True:
        print("*" * 20)
        choice = input("1 登录\n2 注册\n3 退出\n请选择您要进行的操作:")

        if choice in func_dict1:
            login_status, current_user = func_dict1[choice]()
            print(login_status)
            print(current_user)
        else:
            print("请输入正确的选择。")

        # 登录成功后进入下级功能
        if login_status:
            shopping.shopping(current_user)
