#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-12 20:33
# @Author  : Vito  
# @File    : ex9.py

# exe-1  全部变为大写
names = ['albert','james','kobe','kd']
names = map(lambda x:x.upper(),names)
print(list(names))

# exe-2 将以shenjing结尾的名字过滤掉，保存剩下的名字长度
names = ['albert','jr_shenjing','kobe','kd']
names = filter(lambda x:not x.endswith('shenjing'),names)
names1 = map(lambda x:len(x),names)
# 先用filter过滤，再用map映射。

print(list(names1))

# exe-3 求文件a.txt 中最长的行的长度（长度按字符个数算，使用max函数）
def max_line(file_name):
    max_num = 0
    with open(file_name,'r',encoding="utf-8") as f1:
        for line in f1.readlines():
            if len(line) > max_num:
                max_num = len(line)
    return max_num

print(max_line("test1.py"))

# exe-4 shoping.txt 如下
"""
mac,20000,3
lenovo,3000,10
bmw,1000000,10
chicken,200,1
求：
1）花了多少钱
2）打印所有商品信息[{'name':'xxx','price':'xxx','count':'xxx'}]
3)求单价大于10000的商品信息，格式同上
"""
# 把商品信息存储在字典内。
shops = [] # 商品列表
total = 0
with open('shopping.txt','r',encoding='UTF-8') as f1:
    for line in f1.readlines():
        shop = {}
        shop['name'] = line.split(',')[0]
        shop['price'] = line.split(',')[1]
        shop['num'] = line.split(',')[2].replace('\n','')
        total += int(shop['num']) * int(shop['price'])
        print(shop)
        shops.append(shop)
    print(shops) # 打印商品信息 [{'name': 'mac', 'price': '20000', 'num': '3'}, {'name': 'lenovo', 'price': '3000', 'num': '10'}, {'name': 'bmw', 'price': '1000000', 'num': '10'}, {'name': 'chicken', 'price': '200', 'num': '1'}]
    print(total) # 总金额 10090200
    shops_new = filter(lambda x:int(x['price']) > 10000,shops)
    print(list(shops_new)) # [{'name': 'mac', 'price': '20000', 'num': '3'}, {'name': 'bmw', 'price': '1000000', 'num': '10'}]

