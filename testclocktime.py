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

import threading
import os
import time


life_time = raw_input("请输入你想要的生命：（）年")

def exit():
    time.sleep(int(life_time))
    print
    # 退出
    os._exit()


def main():
    # 创建一个线程
    t = threading.Thread(target=exit)
    # 设置为守护线程
    t.setDaemon(True)
    # 开始线程
    t.start()
    print
    a = raw_input("Input something(auto exit in 20 seconds):")
    print "your input is %s." % a
    time.sleep(20)

    print "OK"

if __name__ == '__main__':
    main()