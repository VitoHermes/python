#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-12 16:21
# @Author  : Vito  
# @File    : test.py

# 9.1-1 三元表达式
x = 11
y = 12
res = x if x > y else y
print("x =", res)


# 函数中的应用
def max2(x, y):
    return x if x > y else y


print(max2(2, 4))


def get_age(n):
    if n == 1:
        return 18
    return get_age(n - 1) + 2


print('age', get_age(5))


items = [1, [1, [3, [4, [5, [2, [9, [1, ]]]]]]]]


def tell1(l):
    for item in l:
        if type(item) is list:
            tell1(item)
        else:
            print(item)


tell1(items)


lambda x, n: x ** n

salaries = {
    'james': 30000,
    'kd': 13414,
    'zimuge': 1234431
}


def get(k):
    return salaries[k]


print(max(salaries, key=get))
print(max(salaries, key=lambda x: salaries[x]))
print(min(salaries, key=lambda x: salaries[x]))
print(sorted(salaries, key=lambda x: salaries[x]))
print(sorted(salaries, key=lambda x: salaries[x], reverse=True))

# MAP：映射、REDUCE：合并、FILTER：过滤
# MAP
# 数字映射
nums = [1, 2, 3, 4, 5]
res = map(lambda x1: x1 ** 2, nums)
print(list(res))

# 字符串映射
names = ['tom', 'jerry', 'zed']
res1 = map(lambda x1: x1.upper(), names)
print(list(res1))

# REDUCE
# 计算求和
from functools import reduce
res = reduce(lambda x1, y1: x1 + y1, range(0, 101))
print(res)
# 字符串合并
names = ['tom', 'jerry', 'zed', 'tommy', 'tonny']
res = reduce(lambda x1, y1: x1 + y1, names)
print(res)

# FILTER
# 过滤出年龄不小于30岁的
age = [18, 19, 20, 21, 99, 30]
res = filter(lambda n: n >= 30, age)
print(list(res))
# 过滤出裁判
names = ['James is super star', 'harden is super star', 'harden is super man']
res = filter(lambda x1: x1.endswith('star'), names)
print(list(res))

# 内置函数
# format用法
res = '{} {} {}'.format('vito', 18, 'male')
print(res)
res = '{1} {0} {1}'.format('vito', 18, 'male')  # 索引值
print(res)
res = '{sex} {name} {age}'.format(name='vito', age=18, sex='male')  # 索引值
print(res)


# format 和 % 的异同
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return "This guy is %s, %s years old." % (self.name, self.age)


p1 = Person('vito', 18)
print(p1)


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return "This guy is {self.name}, {self.age} years old.".format(self=self)


p1 = Person('vito', 26)
print(p1)

c = (250, 250)
s1 = "point:{}".format(c)
print(s1)

# 填充与对齐
print("{:>10}".format('18'))
print("{:3<10}".format('18'))
print("{:*^10}".format('18'))

# float精度调整
print('{:.5f}'.format(3.141592653))

# 千位分隔符
print("{:,}".format(123456789))

# 进制转换
print("{:b}".format(18))
print("{:d}".format(18))
print("{:o}".format(18))
print("{:x}".format(18))

# 其他内置函数
print(abs(-10))
print(all([1, 'a', True]))
print(any([0, None, 1]))
print(any([]))

# 进制转换
print(bin(11))
print(oct(11))
print(hex(11))

# 布尔值判断
print(bool(0))


# 判断对象是否可以调用
def func():
    pass


print(callable(func))  # True
print(callable('abc'.strip()))  # False
print(callable(max))  # True

# 字符与十进制转换
print(chr(90))  # z
print(ord('z'))  # 122

# 查看对象下可调用方法
print(dir('abc'))

# 商和余数，返回元组
print(divmod(1311, 25))

# 将字符内的表达式拿出来运行，并拿到执行结果
res1 = eval('2*3')
print(res1,type(res1))  # 6  <class 'int'>
res2 = eval('[1,2,3,4]')
print(res2,type(res2))  # [1, 2, 3, 4] <class 'list'>
res3 = eval('{"name":"vito","age":18}')
print(res3,type(res3))  # {'name': 'vito', 'age': 18} <class 'dict'>

# 集合添加
s = {1, 2, 3}
s.add(4)
print(s)

# 不可变集合
f_set = frozenset({1, 2, 3})

# 名字和值的绑定关系
x = 2
print(globals())
#print(dir(globals()['__builltins__']))


def func():
    x = 1
    print(locals())