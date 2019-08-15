#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-12 18:56
# @Author  : Vito  
# @File    : test1.py

# 名字和值的绑定关系
x = 2
print(globals())
print(dir(globals()['__builtins__']))


def func():
    x = 1
    print(locals())


func()

# 哈希
print(hash('a'))
print(hash((1, 2, 3, 4)))
# 不可hash的类型list,dict,set == 可变类型
# 可hash的类型int,float,str,tuple == 不可变类型


# 查看文档注释
def func():
    """
    help_info
    :return: None
    """
    pass

print(help(max))
print(help(func))

# len,next,iter 自动执行方法
print(len({'x': 1, 'y': 2}))
print({'x': 1, 'y': 2}.__len__)
obj = iter('vito')
print(next(obj))

# 2**3%3
print(pow(2, 3, 3))

# 顺序反转
l = [1, 2, 3, 4]
l.reverse()
print(list(reversed(l)))

# 四舍五入
print(round(3.5))
print(round(3.4))

# 切片对象
sc = slice(1, 5, 2)
l = ['a', 'b', 'c']
print(l[sc])

# 求和
print(sum([1, 2, 3, 4]))

# 拉链函数
left = 'hello'
right1 = {'x': 1, 'y': 2, 'z': 3}
right2 = [1, 2, 3, 4, 5]
res1 = zip(left, right1)
res2 = zip(left, right2)
print(list(res1))
print(list(res2))

x = [1,2,3]
y = ['a', 'b', 'c']
print(([x for x in zip(x,y)]))




# 列表生成式
l = []
for i in range(1000):
    l.append('egg%s' % i)

l1 = ['egg%s' % i for i in range(1000)]
l2 = ['egg%s' % i for i in range(1000) if i > 10]
print(l1)
print(l2)

from functools import wraps
import time


def timmer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return res
    return wrapper


@timmer
def lis1():
    l1 = ['egg%s' % i for i in range(10000000)]


@timmer
def lis2():
    l1 = []
    for i in range(10000000):
        l.append('egg%s' % i)


lis1()
lis2()

time1 = time.time()
l1 = ['egg%s' % i for i in range(10000000)]
time2 = time.time()
print(time2 - time1)

time3 = time.time()
l2 = []
for i in range(10000000):
    l2.append('egg%s' % i)
time4 = time.time()
print(time4 - time3)

# 生成器表达式
l = ('egg%s' % i for i in range(10000000000))
print(next(l))
print(next(l))