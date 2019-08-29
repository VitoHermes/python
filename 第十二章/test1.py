#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-27 19:53
# @Author  : Vito  
# @File    : test1.py

class DeepSchool:
    school = 'deepshare'
    name = 'v'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def learn(self):
        print('%s is learning' % self)
    def eat(self):
        print('%s is eating' % self)
    def sleep(self):
        print('%s is sleeping' % self)

stu1 = DeepSchool('vito', 18, 'male')
stu2 = DeepSchool('vito', 19, 'male')
"""
print(stu1.__dict__)
print(stu2.__dict__)
print(stu1.name)
print(stu1.__dict__['name'])
print(stu1.school)
print(id(stu1.__dict__))
print(id(stu2.__dict__))

a = "123"
b = "123"
a = '1'
print(id(a))
print(id(b))

print(stu1.learn)
print(stu1.learn)
print(stu2.learn)
print(id(DeepSchool.learn))
print(id(stu1.learn))
print(id(stu2.learn))
"""
print(stu1)
stu1.learn()
# <__main__.DeepSchool object at 0x1033c2be0>
# <__main__.DeepSchool object at 0x1033c2be0> is learning
print(stu2)
stu2.learn()
DeepSchool.learn('vito')
# vito is learning
print(DeepSchool.learn)
# <function DeepSchool.learn at 0x1033c72f0>
print(stu1.learn)
print(stu2.learn)
# <bound method DeepSchool.learn of <__main__.DeepSchool object at 0x1033c2be0>>
# <bound method DeepSchool.learn of <__main__.DeepSchool object at 0x1033c2c18>>
