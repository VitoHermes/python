#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-29 15:16
# @Author  : Vito  
# @File    : test2.py

class DeepSchool:
    school = 'deepshare'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def choose(self,course):
        print("%s is chooing %s" % (self.name,course))
    def learn(self):
        print('%s is learning' % self.name)
    def eat(self):
        print('%s is eating' % self)
    def sleep(self):
        print('%s is sleeping' % self)

stu1 = DeepSchool('vito', 18, 'male')
stu2 = DeepSchool('vito', 19, 'male')
stu1.learn()
stu2.learn()
stu1.choose('python')
stu2.choose('math')

li = [1,2]
dict1 = {1:1,2:1}
tuple = (1,2,3)
print(type(li))
print(type(dict1))
print(type(tuple))
print(stu1)  # <__main__.DeepSchool object at 0x102bc2cc0>
print(type(stu1))  # <class '__main__.DeepSchool'>
print(type(stu1.learn))  # <class 'method'>
print(type(stu1.name))  # <class 'str'>
print(id(stu1))  # 4340853952

# 类和类型是一个概念。
