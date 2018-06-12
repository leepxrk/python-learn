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

stock_code = f[0]
start_time = f[1]
stop_time = f[2]
stock_turnover = f[3]
stock_trading_volume = f[4]
opening_price = f[5]
low = f[6]
high = f[7]
closing_price = f[8]
opening_front_subscription_price = f[9]
low_front_subscription_price = f[10]
high_front_subscription_price = f[11]
closing_front_subscription_price = f[12]
opening_back_Subscription_price = f[13]
low_back_Subscription_price = f[14]
high_back_Subscription_price = f[15]
closing_back_Subscription_price = f[16]




# 写入数据
update_db = """INSERT INTO A_share_shanghai_bourse (stock_code,start_time,stop_time,stock_turnover,stock_trading_volume,opening_price,low,high,closing_price,opening_front_subscription_price,low_front_subscription_price,high_front_subscription_price,closing_front_subscription_price,opening_back_Subscription_price,low_back_Subscription_price,high_back_Subscription_price,closing_back_Subscription_price)VALUES(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)",(stock_code,start_time,stop_time,stock_turnover,stock_trading_volume,opening_price,low,high,closing_price,opening_front_subscription_price,low_front_subscription_price,high_front_subscription_price,closing_front_subscription_price,opening_back_Subscription_price,low_back_Subscription_price,high_back_Subscription_price,closing_back_Subscription_price)"""


# 将一行数据写入列表




# 查询数据行数
QueryData = "select id,start_time from A_share_shanghai_bourse where stock_code = '600000' limit 10"
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















