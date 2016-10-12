#!/usr/bin/env python
# _*_coding:utf-8_*_
#-*-coding:utf-8-*-

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

def random_attri_func(): #随机人物属性生成字典
    random_dict = {'height':random.choice([[0.5,160],[1,170],[2,180]]),
                   'weight':random.choice([[0.5,"太轻"],[0.5,"太重"],[2,"正常"],[3,"完美"]]),
                   'status':random.choice([[2,"高兴的"],[0.5,"沮丧的"],[1,"平淡的"],[3,"发奋的"]]),
                   'technology':random.choice([[2,"C语言"],[4,"唱歌"],[4,"跳舞"],[3,"Java"],[3,"Python"],[2,"Shell"],[0.5,"None"]]),
                   'job':random.choice([[0.3,"失业中"],[0.3,"失业中"],[1,"网吧网管"],[2,"快递员"],[0.7,"卖报纸"]]),
                   'cash':random.randint(10000,100000),
                   'salary':random.randint(800,8000),
                   'nationality':random.choice([[1,"中国"],[0.5,"韩国"],[0.5,"日本"],[0.7,"俄罗斯"],[2,"美国"]]),
                   'charac':random.choice([[0.5,"歪瓜裂枣"],[1,"长相平平"],[3,"相貌端正"],[4,"相貌俊俏"],[5,"人中龙凤"]]),
                   'strength':random.choice([[0.3,"四肢无力"],[0.5,"手无缚鸡"],[1,"体力正常"],[1.5,"身体强壮"],[2,"力量过人"],[3,"超人来了"],[5,"上帝模式"]]),
                   'agility':random.randint(10,100),
                   'intelligence':random.randint(160,300),
                   'charm':random.randint(2,8)
                   }
    print "DEBUGING,random_dict",random_dict
    return random_dict


def random_event_func(param):
    pass



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
        random_ditc = random_attri_func() #返回人物属性的一个随机字典
        # 实例化主人公
        protagonist = utils.Human_Attr

        # 在random_dict中取得主人公的属性
        protagonist.name = name
        protagonist.age = 18
        protagonist.sex = sex
        protagonist.height = random_ditc['height']
        protagonist.weight = random_ditc['weight']
        protagonist.status = random_ditc['status']
        protagonist.technology = random_ditc['technology']
        protagonist.job = random_ditc['job']
        protagonist.cash = random_ditc['cash']
        protagonist.salary = random_ditc['salary']
        protagonist.nationality = random_ditc['nationality']
        protagonist.charac = random_ditc['charac']
        protagonist.strength = random_ditc['strength']
        protagonist.agility = random_ditc['agility']
        protagonist.intelligence = random_ditc['intelligence']
        base_charm = random_ditc['charm']
        # 把计算魅力值需要的数据整合成列表传给 魅力值计算方法
        # reay_calc_charm = [protagonist.age,protagonist.height,protagonist.weight,protagonist.status,protagonist.technology,protagonist.job,protagonist.cash,protagonist.salary,protagonist.strength,protagonist.intelligence]
        # print "DEBUG......打印传递列表长度", len(reay_calc_charm)
        protagonist.charm = utils.charm_calc(protagonist) * base_charm

        print '--------------->',protagonist.charm
        print "_____________________charm should bigger than 200w you win!!!!!!!!!!!!!!!!!!!____________________"




if __name__ == '__main__':
    log_in()
