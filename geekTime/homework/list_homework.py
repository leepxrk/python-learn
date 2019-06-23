#字符串
# 字符串练习 - 定义一个字符串Hello Python 并使用print( )输出
str_learn1 = 'hello python'
print (str_learn1)

# 字符串练习 - 定义第二个字符串Let‘s go并使用print( )输出
str_learn2 = "let's go"
print (str_learn2)

# 字符串练习 - 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出
str_learn3 = "\"The Zen of Python\" -- by Tim Peters "
print (str_learn3)




#字符串的基本操作
# 字符串基本操作练习 - 定义两个字符串分别为 xyz 、abc
str_learn_operation1 = "xyz"
str_learn_operation2 = "abc"

# 字符串基本操作练习 - 对两个字符串进行连接
str_learn_operation3 = str_learn_operation1+str_learn_operation2
print(str_learn_operation3)

# 字符串基本操作练习 - 取出xyz字符串的第二个和第三个元素
str_learn_operation4 = str_learn_operation1[1:3]
print(str_learn_operation4)

# 字符串基本操作练习 - 对abc输出10次
print(str_learn_operation2*10)

# 字符串基本操作练习 - 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
print ("a"in str_learn_operation1)
print ("a"in str_learn_operation2)




# 练习三 列表的基本操作
# 列表的基本操作 - 定义一个含有5个数字的列表
list_learn1 = [1,2,3,4,5]
print(list_learn1)

# 列表的基本操作 - 为列表增加一个元素 100
list_learn2 = [100]
list_learn3 = list_learn1 + list_learn2
print(list_learn3)

# 列表的基本操作 - 使用remove()删除一个元素后观察列表的变化
list_learn2.remove(100)
print(list_learn2)

# 列表的基本操作 - 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
print(list_learn3[0:3])
print(list_learn3[-1])




# 练习四 元组的基本操作

# 元组的基本操作 - 定义一个任意元组，对元组使用append() 查看错误信息
list_learn_yz1 = ("aaa","bbb","ccc","ddd","fff","ggg")
# list_learn_yz1.append("eee")
print(list_learn_yz1)

# 元组的基本操作 - 访问元组中的倒数第二个元素
print(list_learn_yz1[-2])

# 元组的基本操作 - 定义一个新的元组，和 1. 的元组连接成一个新的元组
list_learn_yz2 = ("hhh","iii","jjj")
list_learn_yz3 = (list_learn_yz1+list_learn_yz2)
print(list_learn_yz3)

# 元组的基本操作 - 计算元组元素个数
print(len(list_learn_yz3))

