# 根据身份证号计算生肖还有星座（仅仅考虑新历）

import time

# 属相列表
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# 星座列表
constellation = ('水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座')

# 对应星座的日期
constellation_Day = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))


# 新建两个字典，分别存储属相还有星座，并且为每个属相和星座在字典内的值赋值为0
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

cons_num = {}
for i in range(0,12):
    cons_num[constellation[i]] = 0


# 通过while 循环让用户重复输入身份证号码，并从身份证中提取用户信息存入字典中
while True:
    # 输入身份证号码
    idCart = input('输入你的身份证号码：')

    # 身份证中年月日身份提取
    Birthday_year = idCart[6:10]
    Birthday_month = idCart[10:12]
    Birthday_day = idCart[12:14]

    # 将月份和日期提取到程序中
    month_day = (int(Birthday_month),int(Birthday_day))

    # 计算属相并将属相值再字典中加一
    cz_num[chinese_zodiac[int(Birthday_year)%12 - 4]] += 1
    print(cz_num)


    # while循环法计算星座并将字典中的对应星座的值向上加1
    xhcs = 0

    while constellation_Day[xhcs] < month_day:
        if int(Birthday_month) >= 12 and int(Birthday_day) >= 23:
            xhcs = 12
            break
        xhcs += 1

    print(constellation[xhcs - 1])
    cons_num[constellation[xhcs - 1]] += 1
    print(cons_num)
