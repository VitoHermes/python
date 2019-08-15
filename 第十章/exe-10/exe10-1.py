#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 14:43
# @Author  : Vito  
# @File    : exe10-1.py

# 练习1 - 练习5
"""
文件内容如下：
vito male 18 300000
james male 38 30000
林志玲 female 28 20000
石原里美 female 28 100000
要求从文件中取出每一条记录放入列表中，列表的每个元素都是如下格式：
{'name':'vito','sex':'male','age':18,'salary':300000}
"""
list1 = []
with open('123.txt', 'r', encoding='utf-8') as f:
    for line in f:
        dic1 = {}
        dic1['name'] = line.split(' ')[0]
        dic1['sex'] = line.split(' ')[1]
        dic1['age'] = line.split(' ')[2]
        dic1['salary'] = line.split(' ')[3].replace('\n', '')
        list1.append(dic1)
print(list1)

# 取出薪资最高的人的信息
super_man = max(list1, key=lambda x: x['salary'])
print(super_man)

# 取出最年轻的人的信息
youth_man = min(list1, key=lambda x: x['age'])
print(youth_man)
# print(len(max(f1, key=lambda x: len(x))))  # max函数和匿名函数联用

# 将每个人个人信息的名字映射成首字母大写
list2 = []
for l in list1:
    if l['name'].isalpha():
        l['name'] = l['name'].capitalize()
    list2.append(l)
print(list2)

# 过滤掉名字以v开头的人的信息
list1 = list(filter(lambda x: not x['name'].startswith('V'), list1))
print("list1", list1)