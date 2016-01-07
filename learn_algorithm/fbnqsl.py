#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 斐波那契数列 定义  F（0）=0，F（1）=1，F（n）=F(n-1)+F(n-2)（n≥2，n∈N*）
# 记录400万以内的最大斐波那契数，同时求出这个数是第几个斐波那契数

#定义变量
import random,MySQLdb,sys

#a = int(input("数值A:"))
n = 4000000
res = 0
a = 1
b = 1

while res < n:
        a = res + b
        b = a + res
        res = a + b

print res
