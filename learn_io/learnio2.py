#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
# import pymysql.cursors
# import pymysql

# 连接数据库
#linkDB = pymysql.connect(host='127.0.0.1',port =3306,user='root',password='qq19900807',database='DBLearnT',charset='utf8')


# 选择文件



# 使用标准库读取csv文件
#csv_reader = csv.reader(open("shanghai/600000.csv"))
#for row in csv_reader:
#    print (row)


# 读取整个csv文件
with open('shanghai/600000.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file,1,None)
    for row in csv_reader:
        print(row)


# 读取文件某一列
#with open('shanghai/600000.csv','r') as csv_file:
#    csv_reader = csv.reader(csv_file)
#    column = [row[2] for row in csv_reader]
#    print(column)



# 读取文件的行数
a=open('shanghai/600000.csv','rb')
b=len(a.readline())
print(b)


#with open('shanghai/600000.csv',encoding='utf-8') as csvfile:
#    reader=csv.reader(csvfile)
#    column=[row[2] for row in reader]
#    print(column)





# 选择数据表
#cursor = linkDB.cursor()


#插入数据
#QueryData = "select nickName,sex from tme_musician where id > '%s' limit 10"
#condition = ('10000',)
#cursor.execute(QueryData % condition)

#for row in cursor.fetchall():
#    print("nickName:%s\sex:%.2f" % row)

#print(cursor.execute(QueryData % condition))
