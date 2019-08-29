#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-21 20:12
# @Author  : Vito  
# @File    : test2.py

na = "1"
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
        print("%s is learning" % self.name)
    def eat(self):
        print("is eating")
    def sleep(self):
        print("is sleeping")

stu1 = DeepshareStudent('vito', 26, 'male')
stu2 = DeepshareStudent('jenny', 16, 'female')
print(DeepshareStudent.__dict__)
print(id(DeepshareStudent.__dict__))
print(stu1.__dict__)
print(id(stu1.__dict__))
print(id(stu2.__dict__))
print(id(stu1.name))
print(id(stu2.name))
print(id(stu1.school))
print(id(stu2.school))
DeepshareStudent.learn('vito')
stu1.learn()

