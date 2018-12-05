# 练习一 文件的创建和使用
# 1. 创建一个文件，并写入当前日期
# 2. 再次打开这个文件，读取文件的前4个字符后退出

import datetime,os

# 读取当前时间
time_now = datetime.datetime.now()
time_now_str = str(time_now) # 将当前时间转化为字符串

# 打开一个文件，将当前时间写入,并且关闭文件
file_homework = open(r'./date.txt','w')
file_homework.write(time_now_str)
file_homework.close


# 打开刚才写入了当前时间的文件，读取文件中前四个字符

file_homework1 = open(r'./date.txt')
print(file_homework1.read())
file_homework1.close

#print(datetime.datetime.now())