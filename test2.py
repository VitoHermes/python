#!/usr/bin/env python
# coding: utf-8
# @Time    : 2019-08-04
# @Author  : Vito
# @File    : test2.py
import sys
def login(): # 登录
    wrong_time = 0 # 输错密码的次数
    with open("users.txt", 'r') as f1:
        data = f1.readlines()
        user_name = []
        user_info_dict = {} # 用户名-用户密码的字典
        for user_info in data:
            user_info_dict[user_info.split('|')[0]] = user_info.split('|')[1]
        #print(user_info_dict) # 生成用户信息

    while True:
        name = input("Input your name:")
        password = input("Input your password:")
        for user in user_info_dict: # 遍历寻找是否是注册用户
            if name in user_info_dict: # 输入的用户名是已注册用户
                if password == user_info_dict[name]: # 密码正确，登录成功
                    print("Login successfully!")
                    return [True, name] # 登录成功
                elif wrong_time == 2: # 超过次数，直接结束
                    print("Your password is wrong for too many times!")
                    return [False, None]
                else: # 密码错误,重新输入
                    print("Your password is wrong, do it again.")
                    wrong_time += 1 # 错误次数加一
                    print(wrong_time)
                    break
        else:# 遍历没找到，未注册
            print("You haven't sign up. Please sign up first.")
            return [False, None] # 登录失败

def signUp(): # 新用户注册（没有判断用户名是否已存在）
    name = input("Input your name:")
    password1 = input("Input your password:")
    password2 = input("Input your password again:")
    if password1 != password2: # 两次密码不一致，注册失败
        print("Please input the same password.")
        return False
    print("signUp successful!") # 注册成功
    sal = input("Input your salary:")
    lines = '|'.join([name,password1,sal]) # 生成一条用户信息
    print(lines)
    with open('users.txt', 'a') as f1:
        f1.writelines('\n'+lines) # 写入文件
    return True

def buyGoods(user_now, shop_car, shop_all): # 商品结算
    with open('users.txt', 'r') as f1:
        data = f1.readlines()
        money_left = 0
        for user_info in data:
            if user_now == user_info.split('|')[0]:
                money_left = user_info.split('|')[2].replace('\n','')
        print(money_left)

        # 计算购物车内商品总金额
        total_money = 0
        for good, num_single in shop_car.items():
            total_money += num_single * shop_all[good]

        print("totol money is:", total_money)

        # 余额不够，结算失败
        if int(money_left) < total_money:
            print("Not enough money!")
            return False
    print(data)
    # 结算流程
    with open('users.txt', 'w') as f1:
        money_left_now = int(money_left) - total_money # 剩余的钱
        # 替换金额
        for user_info in data:
            if user_now == user_info.split('|')[0]:
                f1.writelines(user_info.replace(money_left, str(money_left_now))) # 替换现有的金额
            else:
                f1.writelines(user_info) # 不是该用户的内容不变
        return True
  #  print(data)
  #  print(total_money)
  #      f1.writelines('\n'+lines) # 写入文件


while True:
    print("1-login\n2-signup\n")
    login_status = False # 登录状态
    user_now = None # 当前登录的用户名
    choice = input("Make your choice:")
    if choice == '1':
        login_status,user_now = login()
    elif choice == '2':
        signUp()
    else:
        print("Please input 1 or 2.")

    # 定义商品集和购物车
    shop_all = {
        'iPhone': 9000,
        'macBook': 12000,
        'bike': 1000
    }
    shop_car = {}

    if not login_status:# 登录不成功，继续循环
        continue

    # 打印商品
    while True:
        print("Choose the good you want to buy:")
        for num, good in enumerate(shop_all, 1):
            print(num," ",good)
        print("buy   buy!")
        print("exit   exit!")
        shop_list = list(enumerate(shop_all, 1))
        shop_choice = input()
        if shop_choice == 'buy': # 结算
            buyGoods(user_now, shop_car, shop_all)
        elif shop_choice == 'exit': # 退出程序
            print("Good Bye!")
            print(shop_car)
            money = 0
            with open('users.txt', 'r') as f1:
                data = f1.readlines()
                for user_info in data:
                    if user_now == user_info.split('|')[0]:
                        money = user_info.split('|')[2].replace('\n','')
            print(money)
            sys.exit(0)# 退出程序
        elif int(shop_choice) in range(1, 4): # 选择了正确的商品代码
            shop_num = int(input("How many do you want?")) # 输入购买数量
            if shop_list[int(shop_choice)-1][1] in shop_car: # 购物车内已有商品
                shop_car[shop_list[int(shop_choice)-1][1]] += shop_num
                print(shop_car)
            else: # 购物车内没有商品
                shop_car[shop_list[int(shop_choice)-1][1]] = shop_num
                print(shop_car)
        else:
            print("Input 1-3 or q.")
            continue


#    user_info = f1.readline().split('|')
#    print(user_info)

