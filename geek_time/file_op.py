#-*- coding:utf-8 -*-

# 文件的基本操作

import csv,os

#file1 = open('600000.csv')

#with open(r'C:\Users\leepx\OneDrive\Myself\GitHub\python_learn\geek_time\600000.csv') as file2:
#    file_read = file2.read()
#    print (file_read)

#file3 = open('name.txt','a')
#file3.write('刘备')
#file3.close 


file1 = open(r'C:\Users\leepx\OneDrive\Myself\GitHub\python_learn\geek_time\name.txt')
print(file1.read())
print (file1.readline())

file1.close

