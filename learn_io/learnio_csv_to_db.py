#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import pymysql.cursors


# lianjie shujuku
linkDB = pymysql.connect(host='127.0.0.1',port =3306,user='root',password='qq19900807',database='DBLearnT',charset='utf8')


# chuangjianyoubiao
cursor = linkDB.cursor()


#charushuju
QueryData = "select nickName,sex from tme_musician where id > '%s' limit 10"
condition = ('10000',)
cursor.execute(QueryData % condition)

for row in cursor.fetchall():
    print("nickName:%s\sex:%.2f" % row)

print(cursor.execute(QueryData % condition))


# 运行查询:
#sql = "select * from tme_musician"
#a = cursor.execute(sql)
#print(a)



cursor.close()
linkDB.close()
