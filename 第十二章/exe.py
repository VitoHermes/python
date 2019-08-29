#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-29 20:17
# @Author  : Vito
# @File    : exe.py


class Hero:
    status = 1
    def __init__(self, name, blood = 100, level = 1, Q_hurt = 0, W_hurt = 0, E_hurt = 0):
        self.name = name
        self.blood = blood
        self.level = level
        self.Q_hurt = Q_hurt
        self.W_hurt = W_hurt
        self.E_hurt = E_hurt
    def death(self):
        print("%s is dead" % self.name)

    def Q(self, enemy):
        enemy.blood -= self.Q_hurt
        if enemy.blood <= 0:
            enemy.status = 0
            enemy.death()
    def W(self, enemy):
        enemy.blood -= self.W_hurt
        if enemy.blood <= 0:
            enemy.status = 0
            enemy.death()
    def E(self, enemy):
        enemy.blood -= self.E_hurt
        if enemy.blood <= 0:
            enemy.status = 0
            enemy.death()

A = Hero("hh",W_hurt=90)
B = Hero("yy",W_hurt=90)
A.Q(B)
B.W(A)
B.W(A)
B.W(A)
B.W(A)