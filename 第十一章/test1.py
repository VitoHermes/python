#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-21 16:24
# @Author  : Vito  
# @File    : test1.py

class DeepshareStudent:
    """
    docs
    """
    # 变量表示特征
    school = 'deepshare'
    # 用函数表示技能
    print("init....")
    def __init__(self, name, age, gender):
        print("init....")
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

# 类的查看
name_and_func = DeepshareStudent.__dict__
print(name_and_func)

"""
{'__module__': '__main__', 
 'school': 'deepshare', 
  'learn': <function DeepshareStudent.learn at 0x1033c60d0>, 
   'eat': <function DeepshareStudent.eat at 0x1033c62f0>, 
  'sleep': <function DeepshareStudent.sleep at 0x1033c6268>, 
  '__dict__': <attribute '__dict__' of 'DeepshareStudent' objects>, 
  '__weakref__': <attribute '__weakref__' of 'DeepshareStudent' objects>, 
  '__doc__': '\n    docs\n'}
"""

print(name_and_func['school'])  # deepshare
name_and_func['learn']('vito')  # vito is learning

# 也可以直接获取技能或者属性
print(DeepshareStudent.sleep('vito'))
print(DeepshareStudent.sleep)
print(DeepshareStudent.school)

# 类的修改
DeepshareStudent.school = 'UCB'
print(DeepshareStudent.school)
DeepshareStudent.conutry = 'USA'
print(DeepshareStudent.conutry)

del DeepshareStudent.conutry
# print(DeepshareStudent.conutry) 报错

# 产生对象
stu1 = DeepshareStudent('vito', 18, 'male')

print(stu1.school)
print(stu1.name)