# 练习一 条件语句的使用
# 条件语句练习 - 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
chinese_zodiac = str(input("请输入想说的话："))

if len(chinese_zodiac) == 10:
    print("恭喜你，猜对了")
else:
    print("很遗憾，猜错了")


# 条件语句练习 - 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，
# 如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出

a = int(input("请输入1-40之间任意一个数字:"))

if a <= 10:
    print("aaaaa")
elif a <= 20:
    print("bbbbb")
elif a <= 30:
    print("ccccc")
elif a <= 40:
    print("ddddd")
else:
    print("输入错误，程序结束")


# 练习二 循环语句的使用
#1. 使用for语句输出1-100之间的所有偶数
import time

fff = []

b = range(1,101)
for c in b:
    print(c)
#    time.sleep(1)
#2. 使用while语句输出1-100之间能够被3整除的数字
    d = c % 3
    if d == 0:
        fff.append(c)

print (fff)







