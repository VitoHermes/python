#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-21 20:32
# @Author  : Vito  
# @File    : test3.py

class DeepshareStudent:
    # 变量表示特征
    school = 'deepshare'
    name = '123'
    # 用函数表示技能
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def learn(self):
        """
        self是一个位置参数，必须有值，约定俗成为self
        """
        print("%s is learning" % self)
    def eat(self):
        print("is eating")
    def sleep(self):
        print("is sleeping")

stu1 = DeepshareStudent('vito', 26, 'male')
stu2 = DeepshareStudent('jenny', 26, 'male')
DeepshareStudent.learn(stu1)
DeepshareStudent.learn('vito')

print(stu1.learn())
print(stu2.learn())


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def talk():
        pass


p = People('xiaohua', 18)
print(People.talk)  # <function People.talk at 0x1033c7840>
print(p.talk)  # <bound method People.talk of <__main__.People object at 0x1033c3dd8>>