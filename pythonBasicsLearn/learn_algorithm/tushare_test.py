import tushare as ts

# 查询当前所有正常上市交易的股票列表
# pro = ts.pro_api()


# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

a = ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')

print (a)


b = ts.get_hist_data('600848') #一次性获取全部日k线数�

print (b)

data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

print (data)



