# 字典homework
# 1. 定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
# 2. 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕 
# 3. 取出字典中关键字为d的值

dict_learn = {}

dict_abcd = 'abcd'
for i in dict_abcd:
    dict_learn[i] = 555

dict_learn['c'] = 'cake'
print(dict_learn)

print(dict_learn['d'])









dict_hello = {}

dict_learn2 = 'hello'

for xl_a in dict_learn2:
    print(xl_a)
    dict_hello[xl_a] = 0

print(dict_hello)


# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
str1 = 'hello'
# 集合里的元素不能重复
print(set(str1))