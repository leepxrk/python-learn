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






