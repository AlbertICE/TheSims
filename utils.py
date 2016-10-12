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

def random_func():
    random_event = ["中彩票了","的老板高兴了","的老板生气了","遇到了经济危机了","在的城市房价上涨","涨薪水了","什么也没有做","什么也没有做","生病了","什么也没有做","的心情好","的心情坏","去买衣服","什么也没有做","什么也没有做","去旅游了","去看电影了","去图书馆看书了","什么也没有做","与别人打仗了","什么也没有做","什么也没有做"]
    print "在Albert的不明力量的影响下，" + random.choice(random_event) #打印随机事件
    return random_event


class Human_Attr(object):


    def __init__(self,name,age,sex,height,weight,status,technology,job,cash,salary,nationality,charac,strength,agility,intelligence,charm): #定义人的属性
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
        self.charm = charm #魅力值

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


def Life_Time():

    Lift_start = 18
    Life_time = 100


def charm_calc(people):
    pass
    charm_calc_result = ((100 - int(people.age)) * 2 + people.height[0] * 0.8) * people.weight[0]  * people.status[0] * 0.2 * people.technology[0]  * people.job[0] + (people.cash* 0.01 + people.salary * 0.1) * people.charac[0] * 0.8 * people.strength[0] * people.intelligence * 0.6
                    #((剩余寿命的2倍 +  身高的0.8倍) * 体重指标) * 状态指标的 0.2倍 * 技能指标 * 工作指标 + (存款的百分之一 + 工资的十分之一) * 长相的指标 * 0.8 体力的指标

    # random_dict = {'height':random.choice([[0.5,160],[1,170],[2,180]]),
    #                'weight':random.choice([[0.5,"太轻"],[0.5,"太重"],[2,"正常"],[3,"完美"]]),
    #                'status':random.choice([[2,"高兴的"],[0.5,"沮丧的"],[1,"平淡的"],[3,"发奋的"]]),
    #                'technology':random.choice([[2,"C语言"],[4,"唱歌"],[4,"跳舞"],[3,"Java"],[3,"Python"],[2,"Shell"],[0.5,"None"]]),
    #                'job':random.choice([[0.3,"失业中"],[0.3,"失业中"],[1,"网吧网管"],[2,"快递员"],[0.7,"卖报纸"]]),
    #                'cash':random.randint(10000,100000),
    #                'salary':random.randint(800,8000),
    #                'nationality':random.choice([[1,"中国"],[0.5,"韩国"],[0.5,"日本"],[0.7,"俄罗斯"],[2,"美国"]]),
    #                'charac':random.choice([[0.5,"歪瓜裂枣"],[1,"长相平平"],[3,"相貌端正"],[4,"相貌俊俏"],[5,"人中龙凤"]]),
    #                'strength':random.choice([[0.3,"四肢无力"],[0.5,"手无缚鸡"],[1,"体力正常"],[1.5,"身体强壮"],[2,"力量过人"],[3,"超人来了"],[5,"上帝模式"]]),
    #                'agility':random.randint(10,100),
    #                'intelligence':random.randint(160,300),
    #                'charm':random.randint(50,100)
    #                }

    print "_____DEBUG______charm_calc_result is ------------------------------->>>>>>>> ready to add base:",charm_calc_result


    #根据传过来的人物属性参数得到人物魅力值并传回
    return charm_calc_result

def feel_check(people):
    pass
    # calc
    return "good !"




def print_out_message(people):
    pass
    people.height

    print '''现在让我们来看看你如今的成就吧！
    xxx到目前已经存活了xxx年。
    经过你的不懈的努力和莫名的命运之神的干预，如今你是xxx（职业）。
    身为xxx（国人），到也长得xxxx，体力上算是xxxx了。
    工资也不算太少，辛辛苦苦攒了xxxx。
    '''
    print "目前女主人公xxx对你", feel_check(people)




if __name__ == '__main__':
    random_func()
