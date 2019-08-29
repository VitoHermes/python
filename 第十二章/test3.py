#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-29 17:18
# @Author  : Vito  
# @File    : test3.py

# 初始化对象的增删改查
class Bar:
    n = 111

    def __init__(self, x):
        self.x = x


obj = Bar('abc')
print(obj.__dict__)
print(obj.x)
print(obj.n)
obj.abc = 'abc'
print(obj.abc)
obj.abc = '123'
print(obj.abc)


# 练习一
class Foo:
    count = 0

    def __init__(self):
        Foo.count += 1


obj1 = Foo()
obj3 = Foo()
obj2 = Foo()
print(Foo.count)
print(obj1.count)


# 练习二
class People:
    def __init__(self, name, aggre, life_value=100):
        self.name = name
        self.aggre = aggre
        self.life_value = life_value

    def bite(self, enemy):
        enemy.life_value -= self.aggre
        print("""
        people:[%s], bite dog[%s]
        dog lose value[%s]
        dog left value[%s] 
        """ % (self.name, enemy.name, self.aggre, enemy.life_value)
              )


class Dog:
    def __init__(self, name, dog_type: object, aggre: object, life_value: object = 100) -> object:
        self.name = name
        self.aggre = aggre
        self.life_value = life_value

    def bite(self, enemy):
        enemy.life_value -= self.aggre
        print("""
        people:[%s], bite dog[%s]
        dog lose value[%s]
        dog left value[%s] 
        """ % (self.name, enemy.name, self.aggre, enemy.life_value)
              )


p1 = People('hi', 100)
d1 = Dog('erhuang', 'dog1', 200, 200)
p1.bite(d1)
d1.bite(p1)