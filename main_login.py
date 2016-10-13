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

def other_human_create(lover_sex):
    list1 = ["张", "王", "李", "赵", "刘", "林", "田", "墨", "越", "曹", "孟", "孙", "郭", "于", "段", "易", "周", "吴", "吕", "朱", "杨",
             "黄", "陈", "诸葛", "东方", "欧阳", "司马", "上官", "独孤", "夏侯", "闻人", "尉迟", "南宫", "令狐", "公孙", "宇文", "马", "冯", "米", "沈",
             "韩", "秦", "许"]
    list2 = ["之桃", "沛珊", "慕灵", "梦柏", "冰兰", "谷雪", "书雪", "千兰", "半雪", "凝芙", "千凝", "碧菡", "芷卉", "映之", "凌瑶", "无双", "优璇", "凝霜",
             "落", "影", "依", "馨月", "诗韵", "含颖", "雅洁", "静和", "雪倩", "梦雨", "馨璐", "涵之", "安安", "琳雅", "芷萱", "千羽", "漫夜", "若晴",
             "斓依", "娴珍", "芸华", "凌之", "丹梅", "凝易", "梦夏", "如蕾", "孤竹", "丹晴", "尔梅", "友春", "思", "梦", "醉柔", "问雁", "听莲", "觅烟",
             "怀白", "雨薇", "海风", "丹", "念兰", "代蓉", "幼亦", "依绿", "凌", " 绮真", "盼海", "青", "冬", "映桃", "亦真", "慕玉", "听琴", "翠雁",
             "晓槐", "语", "念阳", "春芙", "飞凝", "醉竹", "凌菱", "雅荷", "绮春", "山薇", "雅夏", "涵霜", "香柔", "语雪", "恨冬", " 寒春", "飞莲", "平天",
             "念萱"]
    list3 = ["文麒", "德兴", "伯懿", "毅", "逐天", "辰", "浩宇", "瑾", "皓轩", "擎", "擎宇", "致远", "烨", "晟睿", "博", "天佑", "杰", "致", "俊驰",
             "雨泽", "磊", "伟", "晟睿", "文博", "天佑", "昊", "修洁", "黎昕", "远航", "旭尧", "荣轩", "泽", "轩", "睿", "弘文", "瀚", "泽", "瑞",
             "绍辉", "洋", "鑫", "鹏煊", "博文", "昊强", "越泽", "旭尧", "宸", "志泽", "博超", "君", "子", "鹏", "炎", "轩", "伟泽", "越彬", "风",
             "琪", "明辉", "伟诚", "明轩", "绍辉", "柏", "杰", "修杰", "志泽", "弘文", "峻熙", "嘉懿", "煜城", "懿轩", "烨伟", "苑博", "鹏涛", "炎彬",
             "鹤轩", "伟泽", "君昊", "熠彤", "鸿煊", "博涛", "苑杰", "黎昕", "霖", "烨", "煜祺", "智宸", "正豪", "昊然", "明杰"]

    if lover_sex == "女":
        print "Debuging-------------------------lover is girl> "
        lover = utils.Human_Attr()
        lover.name = random.choice(list1)+random.choice(list2)
        print "生成女一号的名字是",lover.name
        opponent = utils.Human_Attr
        opponent.name = random.choice(list1)+random.choice(list3)
        print "生成男反一号的名字是", opponent.name
    else:
        lover = utils.Human_Attr
        lover.name = random.choice(list1)+random.choice(list3)
        opponent = utils.Human_Attr
        opponent.name = random.choice(list1)+random.choice(list2)

    print "debug--------------------------lover is :",lover.name, "opponent name is: ",opponent.name

    return lover , opponent

def log_in():

    print'''-----------------------------------------------------------------
-           你是不是已经感觉到了生命的意义，是否想重来一次？
-   恭喜您获得了一次重回18岁的机会，在这茫茫人海中这机会也忒特么的难得了
--------------------------It's starting--------------------------\n\n\n\n'''

    print "\nThis is magnificentseparator!\n"

    current_time = time.time()
    decide_io = raw_input("是否查找读取上次的记录？(Y/ )")
    print "做这个选择没有那么难，别浪费你的生命!\n"

    #print(decide_io) #debug
    if decide_io == "y" or decide_io =='Y':
        io.read_data()
        print "读取记录文件完成......\n"

    else:
        time.sleep(1)
        print "既然你选择一次新的旅程，阿尔伯特哥经过2秒钟的慎重考虑决定让你从那个梦幻般的18岁开始......\n"
        name = raw_input("请输入你想拥有的名字：\n")
        sex = raw_input("请选择你想做男人还是做女人？(man/ )：\n")

        create_loop_start = 0 #随机循环开始值
        create_loop_end = random.randint(2,6) #随机循环结束值
        while  create_loop_start <=create_loop_end:

            print "\n 正在随机生成人物数据......\n"
            if sex =="man" or sex == "Man":
                sex = "男"
                lover_sex = "女"
                opponent_sex = "男"
                print "DEBUG-------------------------------->主人公的性别是",sex
            else:
                sex = "女"
                lover_sex = "男"
                opponent_sex = "女"
                print "DEBUG-------------------------------->主人公的性别是", sex
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
            # 把人物传给 魅力值计算方法 返回后 * charm
            protagonist.charm = utils.charm_calc(protagonist) * base_charm
            # print '--------------->',protagonist.charm
            # utils.print_out_message(protagonist)
            print "当前人物属性不显示，唯一显示总魅力值为：%s\n"%protagonist.charm
            random_attri_loop = raw_input("你有随机（0~6）次机会重新获取属性，是否重新生成属性？（yes/  ）\n")
            if random_attri_loop != 'yes':
                create_loop_start = create_loop_end
                break
            else:
                create_loop_start +=1
        print "++++++++++%s"%protagonist.name
        print "------\n好了，人物已经生成完毕！\n------\n"
        print "生成%s一号...===========================================\n" %lover_sex
        print "生成竞争对手%s一号...eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\n" %opponent_sex
        #调用 其他角色生成器，根据lover_sex属性生成两个其他角色
        lover,opponent = other_human_create(lover_sex)
        # io.save_data(protagonist,lover,opponent)
    print "目前%s的总魅力值是：%s\n"%(protagonist.name,protagonist.charm)
    print "debuging------------------------------->>>>>>>",protagonist




if __name__ == '__main__':
    log_in()
