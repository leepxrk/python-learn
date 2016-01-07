#!/usr/bin/python
# -*- coding: UTF-8 -*-

#定义变量
import random,MySQLdb,sys

#以下为变量赋值
zone_id = random.randint(1,10)*1111
v_id = random.randint(1,10)+1000
vv_number = random.uniform(0,1) * 300
sj_number = raw_input("输入使用虎牙源的几率：")
ydz_ap = "使用爱拍源"
ydz_hy = "使用虎牙源"
gg_hy = "使用虎牙广告"
gg_ap = "使用爱拍广告"
a=0

# 判断使用的视频源
def dy_ywj_dz(sj_number):
    if zone_id == [1111,2222,3333,4444]:
        print ydz_ap
    elif v_id == [1001,1002,1003,1004]:
        print ydz_ap
    elif vv_number > 150:
        print ydz_ap
    elif sj_number < random.uniform(0,1):
        print ydz_ap
    else:
        print ydz_hy
    return
    
dy_ywj_dz(sj_number)

if dy_ywj_dz(sj_number) == ydz_ap:
    print gg_ap
elif dy_ywj_dz(sj_number) == ydz_hy:
    print gg_hy

