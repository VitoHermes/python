#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 15:57
# @Author  : Vito  
# @File    : exe-10.8.py

# 练习8
# 写一个模拟撞库的程序，假如密码都是md5加密的，没有加盐。

import hashlib
password = '123456'
m = hashlib.md5()
password_has = m.update(password.encode('utf-8'))
password_hex = m.hexdigest()
ps_db = ['123', '1234', '12345', '1234356']
for pw in ps_db:
    m = hashlib.md5()
    tmp = m.update(pw.encode('utf-8'))
    if password_hex == m.hexdigest():
        print("找到密码：" + pw)
        break
else:
    print("没有找到密码")