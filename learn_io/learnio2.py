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
Conn = pymysql.connect(host='127.0.0.1',port =3306,user='root',password='qq19900807',database='CrawlerDate',charset='utf8')


# chuangjianyoubiao
cursor = Conn.cursor()

# 运行查询:
sql = "select * from DoubanMoviesFull limit 1"
cursor.execute(sql)



# 运行查询:
#cursor = conn.cursor()
#cursor.execute('select * from DoubanMoviesFull limit 1', ('1',))
#values = cursor.fetchall()
#values
#[('1', 'Michael')]
# 关闭Cursor和Connection:

cursor.close()
Conn.close()
