#!/usr/bin/python
# -*- coding: UTF-8 -*-

#面向对象

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