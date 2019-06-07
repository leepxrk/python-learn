
import pymysql
import 

# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
db = pymysql.connect("127.0.0.1", "root", 
"19900807", "statisticalLearning")

# 接着我们获取 cursor 来操作我们的 statisticalLearning 这个数据库
cursor = db.cursor()

# 插入一条记录
# sql = "insert into beautyGirls(name, age) values ('Mrs.cang', 18)"
sql = "select low,high from stockData where stockCode = '600000'"

cs.execute(sql)
    datalist = []
    alldata = cs1.fetchall()
    for s in alldata:
        datalist.append(s[0])
    print(datalist)

# try:
#     cursor.execute(sql)
#     db.commit()
except:
    # 回滚
    db.rollback()

# 最后我们关闭这个数据库的连接
db.close()