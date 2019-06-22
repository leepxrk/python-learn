import tushare

# 查询当前所有正常上市交易的股票列表
pro = ts.pro_api()


data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')