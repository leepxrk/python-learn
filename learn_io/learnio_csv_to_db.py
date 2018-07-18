#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql,csv
import pymysql.cursors


# 连接数据库
linkDB = pymysql.connect(host='127.0.0.1',port =3306,user='root',password='19900807',database='learn_data',charset='utf8')

# 使用cursor方法创建游标
cur = linkDB.cursor()


#创建空列表
A_share_date = []

# 打开csv文件
csv_date = open('shanghai/600000.csv','rb')
f = csv_date.readline().splitlines() #仅读取一行数据

print(f)

stock_code = f,2
start_time
stop_time
stock_turnover
stock_trading_volume
opening_price
low
high
closing_price
opening_front_subscription_price
low_front_subscription_price
high_front_subscription_price
closing_front_subscription_price
opening_back_Subscription_price
low_back_Subscription_price
high_back_Subscription_price
closing_back_Subscription_price




# 写入数据
update_db = "INSERT INTO A_share_shanghai_bourse VALUES(),(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,)"


# A_share_date.append(f)




# 将一行数据写入列表




# 查询数据行数
QueryData = "select id,start_time from A_share_shanghai_bourse where stock_code = 'f' limit 10"
cur.execute(QueryData)
date = cur.fetchall()
for id,start_time in date:
    print(id,start_time)




# 查询
#QueryData = "select id,start_time from A_share_shanghai_bourse where stock_code = '600006' limit 10"
#cur.execute(QueryData)
#date = cur.fetchall()
#for id,start_time in date:
#    print(id,start_time)


#关闭数据库连接

linkDB.close()















