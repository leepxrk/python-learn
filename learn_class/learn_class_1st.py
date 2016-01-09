#!/usr/bin/python
# -*- coding: UTF-8 -*-

#面向对象
#属性相近的分类：在该分类下，定义了bird,并定义了两个变量 have_faether 和 way_of_reperoduction
#动作分类：在该分类下，定义了一些行为的方法进行区分，即move

class bird(object):
    have_faether = true
    way_of_reperoduction = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position = position[0] + dx
        position = position[1] + dy
        return position
        
summer = bird()
print summer.way_of_reperoduction
print 'after move' , summer.move(5,8)


#大分类下会定义一个子类
#引如继承的概念

class chicken(bire)：
    way_of_move = 'walk'
    possile_in_kfc = ture
    
class oriole(bire):
    way_of_move = 'fly'
    possile_in_kfc = false
    
summer = chicken()
print = summer.have_faether
print = summer.move(5,8)

