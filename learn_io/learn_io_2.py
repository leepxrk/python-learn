#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入 Phone 包
#import Phone
import pymysql
import pymysql.cursors


#Phone.Pots()
#Phone.Isdn()
#Phone.G3()




#import sys

#def print_func( par ):
#    print 'hello:',par
#    return

# lianjie shujuku
conn = pymysql.connect(host = 'localhost',port = '3306',user = 'root',password = 'qq19900807',db = 'mysql',charset = 'utf-8')

cursor = db.cursor()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where host = localhost & user = root limit 2', ('1',))
values = cursor.fetchall()
values
[('1', 'Michael')]
# 关闭Cursor和Connection:
cursor.close()

