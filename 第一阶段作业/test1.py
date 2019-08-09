#!/usr/bin/env python
# coding: utf-8
# @Time    : 2019-08-04
# @Author  : Vito
# @File    : test1.py

"""
要求打印三级菜单
可返回上一级
可随时退出
"""

# 定义垃圾分类毒菜单明细
trash_item = {
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

tag = True
while tag:
    menu1 = trash_item
    print("杭州垃圾分类查询".center(20, '-'))
    for key in menu1: # 打印一级菜单
        print(key)

    choice1 = input("请输入第一级分类：(b-返回上一级，q-退出程序)").strip() # 获取第一层选项

    # 特殊情况处理
    if choice1 == 'b': # 返回上一层
        print("欢迎下次使用杭州垃圾分类查询系统。")
        break
    if choice1 == 'q': # 退出程序
        tag = False
        print("欢迎下次使用杭州垃圾分类查询系统。")
        continue
    if choice1 not in menu1: # 不存在毒类目
        print("没有该分类毒垃圾，重新输入。")
        continue

    # 进入二级菜单
    while tag:
        menu2 = menu1[choice1] # 拿到一层字典
        choice2 = input("请输入二级类目：(b-返回上一级，q-退出程序)")

        # 特殊情况处理
        if choice2 == 'b':  # 返回上一层
            print("返回上一级。")
            break
        if choice2 == 'q':  # 退出程序
            tag = False
            print("欢迎下次使用杭州垃圾分类查询系统。")
            continue
        if choice2 not in menu2:  # 不存在毒类目
            print("没有该分类毒垃圾，重新输入。")
            continue

        while tag:
            menu3 = menu2[choice2] # 拿到二层字典
            for key in menu3:
                print(key)
            choice3 = input("请输入操作：(b-返回上一级，q-退出程序)")

            # 特殊情况处理
            if choice3 == 'b':  # 返回上一层
                print("返回上一级。")
                break
            if choice3 == 'q':  # 退出程序
                tag = False
        for key in menu2:
            print(key)
            print("欢迎下次使用杭州垃圾分类查询系统。")
            continue

