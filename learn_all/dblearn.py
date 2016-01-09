#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb,re,urllib2

url=raw_input("冒号后输入视频地址：")
urllist=list(url)

#www域名
if urllist[7:10]==['w','w','w']:
    urllist[7:10]=['m']
    url="".join(urllist)

#处理手游地址
if urllist[7:14]==['s', 'h', 'o', 'u', 'y', 'o', 'u']:
    urllist[7:14]=['m']
    url="".join(urllist)

content=urllib2.urlopen(url).read()               #获得网站源码
m=re.search(r'\bhttp\b.*\bmp4\b',content)         #在源码中寻找视频地址
a=m.group(0)                                      #调用方法获得符合条件的字符串
print a                                           #打印该视频地址


from urllib import urlopen
doc = urlopen("http://www.aipai.com").read()
print doc

conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="19900807",db="python_pc")
with conn:
    cursor = conn.cursor()
    cursor.execute ("insert into video_msg(id,video_url,mp4_url) values ('url+url','30018655','打酱油路过','1','2015-11-19')")
# cursor.execute(sql)
#row=cursor.fetchone()
#print row
cursor.close()
conn.close()




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
