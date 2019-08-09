#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 19:48
# @Author  : Vito  
# @File    : test.py
"""
dict1 = {'x':1,'y':2}
iter_dict1 = dict1.__iter__()
print(iter_dict1.__next__())
print(iter_dict1.__next__())
#print(iter_dict1.__next__())

str1 = 'hello!'
iter_str1 = str1.__iter__()
print(iter_str1.__next__())
print(iter_str1.__next__())
print(iter_str1.__iter__() is iter_str1)
print(iter_str1.__iter__().__iter__() is iter_str1)

set1 = {1, 2, 3, 4}
iter_set1 = set1.__iter__()
while True:
    try:
        print(iter_set1.__next__())
    except StopIteration:
        break

# yield
def test_yeild():
    print("1")
    yield 1
    print('2')
    yield 2
    print('3')

res = test_yeild()
print(res)
print(res.__iter__() is res)
print(res.__iter__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
"""
def foo():
    print("starting")
    while True:
        res = yield 4
        print("res:",res)

g = foo()
print(next(g))
print('*'*20)
print(g.send(7))

def foo(num):
    print("starting...")
    while num < 10:
        num += 1
        yield num

for n in foo(0):
    print(n)

name = "  abc  "
print(name.lstrip())
print(name.rstrip())
l = [
    {'name':'vito','age':18,'sex':'male'},
    {'name':'vito','age':18,'sex':'male'},
    {'name':'vito','age':18,'sex':'male'},
    {'name':'vito','age':18,'sex':'male'},
]
set1 = set()
l1 = []
for item in l:
    val = (item['name'],item['age'],item['sex'])
    if val not in set1:
        set1.add(val)
        l1.append(item)
print(l1)

# 第三章 练习四-字典list去重
def func(items, key = None):
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item

print(list(func(l, key=lambda dic:(dic['name'], dic['age'], dic['sex']))))

for i in range(1, 10, 1):
    print(i)

def show_in(start, stop, step = 1):
    n = start
    while n < stop:
        yield n
        n += step
for item in show_in(1,10,3):
    print(item)

def eat(name):
    print("%s is ready for eating" % name)
    while True:
        food = yield
        print("%s is ready for eating %s" %(name,food))

person1 = eat('vito')
next(person1)
person1 = eat('apple')
person1.__next__()

i = 4
j = 1
for num in range(10):
    print('name'.center(num, '*'))

a = [1,2,3,4,5,5,5,6,6,6,7,7,8,8]
b = [i for i in a if i != 6]
print(b)

dict1 = {'name':'vito','name1':'vito','name2':'vito'}


for num, item in enumerate(dict1, 1):
    print("%d %s" % (num, item))