import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


import sys
import importlib
importlib.reload(sys)
 




#   引入 tushare
import tushare as ts

# 引入pymysql
import pymysql

# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
db = pymysql.connect("127.0.0.1", "root", 
"19900807", "statisticalLearning")


# 设置token
ts.set_token('41f23d83224913cd79af2c386919c0b84c23d46d6a798890eecc53ee')

# 初始化api
# pro = ts.pro_api()


# 获取股票列表数据
stock = ts.get_stock_basics()

print (stock)


stock.to_sql(‘stock_basic’,cn,index=False)




