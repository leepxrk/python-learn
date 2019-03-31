
# 读取三国内的人物名称还有武器名称，并统计数量
# 逻辑是阅读全文，统计其中一项，然后从头开始阅读，统计第二项……

# 获取人物名称
f = open(r'./geek_time/txt/name.txt')
data_1 = f.read()
print(data_1)



# 获取weapon 内容，并通过for循环将其转化为列表并删除\r
file1 = open(r'./geek_time/txt/weapon1.txt')
for list_weapon_ls in file1.readlines():
    list_weapon_ls_1 = list_weapon_ls.split('\r')
#    print(list_weapon_ls_1)
file1.close














# 创建 武器 字典和 人物 字典
dic_weapon = {}
dic_person = {}


# 创建 武器 列表
list_weapon = []




# 将列表1 的内容写入临时文件weapon2
file2 = open(r'./geek_time/txt/weapon2.txt','a')
file2.write(list_weapon_ls_1)
file2.close

# 读取文件weapon2的内容，删除\n
file3 = open(r'./geek_time/txt/weapon2.txt','a')

for list_weapon_ls_2 in file3.readlines():
    list_weapon_ls_3 = list_weapon_ls_2.split('\r')
    print(list_weapon_ls_3)

file3.close

#print(list_weapon_ls_2)
#list_weapon.append(list(map(str,list_weapon_ls.split('\n'))))

#print(list_weapon)
file1.close


# 使用for循环将列表中的 武器 存入武器字典中
#for list_weapon_ls_ls in list_weapon:
#    dic_weapon[list_weapon_ls_ls] = 0

#print(dic_weapon)

