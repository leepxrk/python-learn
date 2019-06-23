#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import sys

# 三个因素

# 年份
year = int(input("请输入存款时间："))

# 利率
interest_rate = int(input("请输入年利率："))

# 储蓄额
saving_money = int(input("请输入每年储蓄额："))

# 计算
times = 1

# assets = (saving_money * (interest_rate/100) + saving_money)
a = (saving_money * ((interest_rate/100) + 1))


#a*1.1+assets

while times < year:
#   saving_money = saving_money * 1.1
    assets = (saving_money * ((interest_rate/100) + 1))
    a = assets + a * 1.1
    times = times + 1
else:
    print (a)
