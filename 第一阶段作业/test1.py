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

# part2（改进）：加上退出机制
layers = [trash_item, ]
while True:
    if len(layers) == 0:
        break

    current_layer = layers[-1]
    for key in current_layer:
        print(key)

    choice = input('>>: ').strip()

    if choice == 'b':
        layers.pop()
        continue

    if choice == 'q':
        break

    if choice not in current_layer:
        continue

    layers.append(current_layer[choice])