#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 11:18
# @Author  : Vito
# @File    : test1_new.py

"""
改写垃圾分类三级菜单代码
"""

# 定义垃圾分菜单明细
trash_menu = {
    '可回收物': {
        '瓶子类':{
            '玻璃瓶': {},
            '塑料瓶': {},
        },
        '纸质类': {
            '报纸': {},
            '包装盒': {},
        }
    },
    '有害垃圾': {
        '有毒': {
            '药品': {},
            '毒': {},
        },
        '有放射性': {
            '灯管': {},
            '工业垃圾': {},
        }
    },
    '易腐垃圾': {
        '家庭垃圾': {
            '剩菜': {},
            '剩饭': {},
        },
        '环境': {
            '树叶': {},
            '花蕊': {},
        }
    },
    '其他垃圾': {
        '妇女用品': {
            '卫生巾': {},
            '卫生棉': {},
        },
        '婴儿用品': {
            '纸尿裤': {},
        }
    }
}

print('欢迎来到杭州垃圾分类查询系统！'.center(30,'*'))
menu = []#声明以空列表来存储菜单
menus = trash_menu
while True:
    menu_now = {} #当前菜单的数字-菜单内容字典，方便选择
    for index,good in enumerate(menus,1): #使用枚举函数遍历字典的键
        print(index,good)
        menu_now[index] = good #把序号作为字典的key，垃圾名称作为字典的value传入该字典中
    if menus == {}: #没有下级菜单
        print('（温馨提示：1.选择B或者b返回上一级菜单 2.选择Q或者q退出）')
        choose = input('\033[31m该菜单内没有内容，请返回或退出：\033[0m').strip()
        if choose.upper() =='Q':
            print('欢迎再次查询垃圾分类！')
            break
        elif choose.upper() == 'B':
            menus = menu[-1] #把菜单赋值给列表的最后一个元素
            menu.pop() #删掉列表的最后一个元素
#            print("menus", menus)
#            print("menu", menu)
        else:
            print('error')
    else: #要购买有下级菜单可以继续操作
        print('（温馨提示：1.输入数字选择类目 2.选择B或者b返回上一级菜单 3.选择Q或者q退出）')
        choice = input('请选择垃圾分类进入下一级菜单：').strip()
        if choice.isdigit():
            if int(choice) in menu_now.keys():
                menu.append(menus)#把菜单添加到列表中
                menus = menus[menu_now[int(choice)]]#重新赋值菜单
#                print("menus", menus)
#                print("menu", menu)
            else:
                print('range out')
        else:
            if choice.upper() == 'B':

                if len(menu) < 1:
                    print('由于当前处于首层菜单，因此本次返回将退出程序！')
                    break
                menus = menu[-1]#把菜单赋值给列表的最后一个元素
                menu.pop()#删掉列表的最后一个元素
#                print("menus", menus)
#                print("menu", menu)
            elif choice.upper() == 'Q':
                print('欢迎再次查询垃圾分类！')
                break
            else:
                print('您的输入有误，请重新输入！')