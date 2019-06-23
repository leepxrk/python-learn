# 引入sys&io&importlit,并确认文件的编码格式
import io
import sys
import importlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
importlib.reload(sys)


# 引入pandas&sqlalchemy&pymysql用于操作数据和写入数据库
import pandas as pd
from sqlalchemy import create_engine
import pymysql

# 引入CSV模块
import csv


# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
con = pymysql.connect("127.0.0.1", "root", 
"19900807", "statisticalLearning")

# 接着获取 cursor 操作statisticalLearning数据库
cursor = con.cursor()


# 引入 tushare 用于获取股市交易资料
import tushare as ts

# 设置token 用于通过tushare提供的API获取股市交易资料
ts.set_token('41f23d83224913cd79af2c386919c0b84c23d46d6a798890eecc53ee')

# 初始化api（tushare提供的初始化API的方案）
# pro = ts.pro_api()


# 获取股票列表数据
stock = ts.get_stock_basics()
# print (stock)

# 将获取到的数据写入数据库
stock.to_sql(name='stockBasicsList',con = con,if_exists='append',index=False)

# 关闭数据库连接
con.close()


# 将获取的数据写入CSV文件
# with open("shareData.csv","w",newline="") as datacsv:  # 通过允许写入的方式打开csv文件
#     csvwriter = csv.writer(datacsv,dialect = ("excel"))
#     csvwriter.writerow(stock)
# datacsv.close()


# stock.to_csv('shareData.csv') 




