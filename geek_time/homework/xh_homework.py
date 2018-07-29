# 根据身份证号计算生肖还有星座（仅仅考虑新历）

import time

# 属相列表
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# 星座列表
constellation = ('水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座')

# 对应星座的日期
constellation_Day = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

# 输入身份证号码
idCart = input('输入你的身份证号码：')

# 身份证中年月日身份提取
Birthday_year = idCart[6:10]
Birthday_month = idCart[10:12]
Birthday_day = idCart[12:14]

# 计算属相的方法
zodiac = chinese_zodiac[int(Birthday_year)%12 - 4]
#print(chinese_zodiac[1990%12 - 4])


# 计算星座的方法
#    将月份和日期提取到程序中
month_day = (int(Birthday_month),int(Birthday_day))

xhcs = 0

#    计算月份和日期对应的星座
# print (constellation[int(len(list(filter(lambda x : x < month_day,constellation_Day)))-2)])

# for循环判断
#for constellation_num in range(len(constellation_Day)):
#    print(constellation_num)
#    if month_day <= constellation_Day[constellation_num]:
#        print (constellation[constellation_num - 1])
#        break
#    else:
#        print(constellation[11])
#        break
#    break


# while 循环判断
while constellation_Day[xhcs] < month_day:
    if int(Birthday_month) >= 12 and int(Birthday_day) >= 23:
#        print (constellation[11])
        break
    xhcs += 1
#    print (xhcs)

print (constellation[xhcs - 1])



# 输入属相
# print("您的属相是：" + zodiac)

# 输出星座

