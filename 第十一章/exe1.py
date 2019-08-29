#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-29 17:43
# @Author  : Vito  
# @File    : exe1.py

import json
with open('students.json', 'r', encoding="utf-8") as f1:
    stus = json.load(f1)
    print(stus)


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def check_score():
    stu_name = input("Input student name:")
    for student in stus:
        if student['name'] == stu_name:
            print(student['score'])
            break
    else:
        print("Wrong name.")


def check_lecture():
    subject = input("Input subject name:")
    for student in stus:
        if subject in student['score']:
            print(student['name'] + ":", end="")
            print(student["score"][subject])
        else:
            print("Wrong subject!")
            break


def check_average():
    total_score = 0
    subject = input("Input subject name:")
    for student in stus:
        if subject in student['score']:
            total_score += student["score"][subject]
        else:
            print("Wrong subject!")
            break
    print("average_score is %.3f" % (float(total_score) / 3.0))


def check_single():
    stu_name = input("Input student name:")
    subject = input("Input subject name:")
    for student in stus:
        if student['name'] == stu_name:
            print(student['name'], end=":")
            if subject in student['score']:
                print(student['score'][subject])
            else:
                print("Wrong subject!")
            break
    else:
        print("Wrong name.")


def dele_score():
    stu_name = input("Input student name:")
    for stu in stus:
        if stu_name == stu['name']:
            stus.remove(stu)
            print(stus)
            with open('students.json', 'w') as f1:
                json.dump(stus, f1)


stu1 = Student(stus[1]['name'], stus[1]['score'])
stu2 = Student(stus[2]['name'], stus[2]['score'])
stu3 = Student(stus[0]['name'], stus[0]['score'])

fundic = {
    1: check_score,
    2: check_lecture,
    3: check_average,
    4: check_single,
    5: dele_score
}

while True:
    print(
        """
        1-查询学生所有成绩
        2-查询所有人某科成绩
        3-查询平均分
        4-查看某人的某学科成绩
        5-根据学生姓名删除信息
        """
        )
    func = int(input("make your choice:"))
    fundic[func]()
