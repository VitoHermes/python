#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 10:52
# @Author  : Vito  
# @File    : shopping.py
"""
购物过程核心逻辑：
1、购物主流程-shopping(user_dict)
2、删除购物车
3、清空购物车
4、显示购物车
5、结账
6、显示购物清单
"""

import sys
import json
sys.path.append('../')


def show_shop_list():
    pass


def del_shop_list():
    pass


def show_bought_list():
    pass


def shop_finish():
    pass


def shopping(user_dict):
    with open('../db/shop_list.json', 'r') as f:
        shop_list = json.load(f)
    print(shop_list)
