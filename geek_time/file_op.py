#-*- coding:utf-8 -*-

# 文件的基本操作

import csv,os

#file1 = open('600000.csv')

#with open(r'C:\Users\leepx\OneDrive\Myself\GitHub\python_learn\geek_time\600000.csv') as file2:
#    file_read = file2.read()
#    print (file_read)


# 将名称“刘备”写入文件
# 写入的操作标记w，在文本末尾的操作标记a

# file3 = open(r'C:\Users\leepx\OneDrive\Myself\GitHub\python_learn\geek_time\name.txt','a')
# file3.write('刘备')
# file3.close 


# 读取文件
file1 = open(r'name.txt')
print(file1.read())
file1.close



# 读取一行
file2 = open(r'name.txt')
print(file2.readline())
file2.close

# 按行读取整个文件
file4 = open(r'name\name.txt')
print(file4.readlines())
file4.close







