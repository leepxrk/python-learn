#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 斐波那契数列 定义  F（0）=0，F（1）=1，F（n）=F(n-1)+F(n-2)（n≥2，n∈N*）
# 记录400万以内的最大斐波那契数，同时求出这个数是第几个斐波那契数

#定义变量
import random,sys


n = int(input("数值A:"))
a = 0
b = 1
c = 1

q = random.randint(1,5)

Fbnqsl=[]

while c < n:
    a = b + c
    if a < n:
        b = a + c
        Fbnqsl.append(c)
        Fbnqsl.insert(q,a)
    else:
        print(c)
        break
    if b < n:
        c = a + b
        Fbnqsl.append(b) 
    else:
        print(a)
        break
    if c > n:
        print(b)
        break

print(Fbnqsl)

#print (random.random())