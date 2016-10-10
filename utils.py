#!/usr/bin/env python
# _*_coding:utf-8_*_

#========================================
__author__ = 'Wang Xingbao'
__Date__ = 10 / 8 / 16
#   Function:   
#========================================
# 人生有两种事，一种是想做的，一种是必须做的！
# 很多时候，我们必须做完必须做的事情，才有资本
# 去做想做的！

# so, 现实很残酷
# but......
# All growth is a leap in the dark!
# 所有的成长都是黑暗中的一跃
#========================================
# Be a loser for now or forever!
#========================================

import time
import random

def random_func(random_event):
    print "=====Time=====print=========================================================================================="
    random_divisor = random.random() #随机
    print random.random()

    print time.localtime(time.time())
    print time.strftime('%Y-%m-%d:%H-%M-%S', time.localtime(time.time()))



    print "=====End======print=========================================================================================="


class Human_Attr(object):


    def __init__(self,name,age,sex,height,weight,status,technology,job,cash,salary,nationality,charac,strength,agility,intelligence): #定义人的属性
        self.name = name #人物的姓名
        self.age = age #年龄
        self.sex = sex #性别
        self.height = height #身高
        self.weight = weight #体重
        self.status = status #心理状态/高兴/伤心/迷茫/......
        self.technology =technology #技能
        self.job = job #工作
        self.cash = cash #存款
        self.salary = salary #工资
        self.nationality = nationality #国籍
        self.charac = charac #人物特征
        self.strength = strength #力量
        self.agility =agility #敏捷
        self.intelligence = intelligence #智力


    def talk(self):
        pass

    def walk(self):
        pass

    def study(self):
        pass

    def buy(self):
        pass

    def fight(self):
        pass

    def drink(self):
        pass

    def singing(self):
        pass


class Life_Time(object):

    Lift_start = 20
    Life_time = 100


if __name__ == '__main__':
    random_func()
