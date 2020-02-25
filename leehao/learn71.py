# 定时器
import time


def my_clock():
    h = int(input("请输入小时:"))
    m = int(input("请输入分钟:"))
    while True:
        local_time = time.localtime()
        print("\r%02d:%02d:%02d" % (local_time.tm_hour, local_time.tm_min, local_time.tm_sec), end="")
        if local_time.tm_hour == h and local_time.tm_min == m:
            print()
            print("时间到！！！ 滴滴滴！！！")
            break


my_clock()
