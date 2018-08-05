#-*- coding:utf-8 -*-

# 文件的基本操作

import os

# 将名称“刘备”写入文件
# 写入的操作标记w，在文本末尾的操作标记a

# file3 = open(r'C:\Users\leepx\OneDrive\Myself\GitHub\python_learn\geek_time\name.txt','a')
# file3.write('刘备')
# file3.close 


# 读取文件
#file1 = open(r'name.txt')
#print(file1.read())
#file1.close



# 读取一行
#file2 = open(r'geek_time/name.txt')
#print(file2.readline())
#file2.close

# 按行读取整个文件
# file4 = open(r'geek_time/name.txt')
# print(file4.readline())
# file4.close


# file5 = open(r'./geek_time/name.txt')
# for line in file5.readlines():
#     print(line)


# file5.close



# read() 输入int 类型字符，能够调整读取文件的字符数 
# tell() 能输出当前指针所在位置
# seek() 能输入两个参数，第一个是偏移量，第二个参数是从哪个位置开始偏移

# 

file6 = open(r'./geek_time/name.txt')  
print(file6.read(1))

print(file6.tell())
print(file6.read(1))

file6.seek(5.0)
print(file6.read())






