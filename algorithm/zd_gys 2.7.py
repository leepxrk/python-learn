#!/usr/bin/python
# -*- coding: UTF-8 -*-

#定义变量
import random,MySQLdb,sys

a = int(input("数值A:"))
b = int(input("数值B:"))

def gys(a,b):
    """zd_gys"""
    i = max(a,b) % min(a,b)
    if i == 0:
        return min(a,b)
    else:
        return gys(min(a,b),i)
    
print gys(a,b)
