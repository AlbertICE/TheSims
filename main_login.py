#!/usr/bin/env python
# _*_coding:utf-8_*_

#========================================
__author__ = 'Wang Xingbao'
__Date__ = 10 / 10 / 2016
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
import local_file_operate as io
import initialize_data as i_n
import utils
import random

def random_attri_func(param): #随机人物属性生成字典
    random_dict = {'height':[160,190,],
                   'weight':[90,180],
                   'status':["高兴的","沮丧的","平淡的","发奋的"],
                   'technology':["C语言","唱歌","跳舞","Java","Python","Shell"],
                   'job':["None","失业中","网吧网管","快递员","卖报纸"],
                   'cash':[200,30000],
                   'salary':[800,2000],
                   'nationality':["中国","韩国","日本","俄罗斯","美国"],
                   'charac':["歪瓜裂枣","长相平平","相貌端正","相貌俊俏","人中龙凤"],
                   'strength':["四肢无力","手无缚鸡","体力正常","身体强壮","力量过人","超人来了"],
                   'agility':[10,100],
                   'intelligence':[160,300],
                   }
    case: param =


def random_event_func(param):
    random_dict = {"":}



def init_data(name,sex):
    protagonist = utils.Human_Attr
    protagonist.name = name
    protagonist.sex = sex


def log_in():

    print '''-----------------------------------------------------------------
    -           你是不是已经感觉到了生命的意义，是否想重来一次？           -
    -   恭喜您获得了一次重回18岁的机会，在这茫茫人海中这机会也忒特么的难得了  -
    --------------------------It's starting--------------------------'''

#    time.sleep(5)

    current_time = time.time()
    decide_io = raw_input("是否查找读取上次的记录？(Y/ )")
    west_time = int(time.time() - current_time)
    print "做这个选择你已经浪费了你%d的生命!" %west_time

    #print(decide_io) #debug
    if decide_io == "Y":
        io.read_data()
        print "读取记录文件完成......"
    else:
        time.sleep(2)
        print "但是既然你选择一次新的旅程，阿尔伯特哥经过2秒钟的慎重考虑决定仍然让你从那个梦幻般的18岁开始......"
        name = raw_input("请输入你想拥有的名字：")
        sex = raw_input("请选择你想做男人还是做女人？(man/ )")

        if sex =="man" or sex == "Man":
            sex = "男"
        else:
            sex = "女"
        init_data(name,sex)

if __name__ == '__main__':
    log_in()
