#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 15:34
# @Author  : Vito  
# @File    : exe-10.6.py

# 练习6
# 使用递归打印斐波那契数列


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


num = int(input("需要产生几项？：>>"))
for i in range(num):
    print(recur_fibo(i), end=' ')