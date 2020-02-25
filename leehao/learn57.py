# time
import time


# 输入生日 计算出星期几 计算出距离现在多少天


def getBirthInfo(x, y, z):
    weeks = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    time_float = time.mktime((x, y, z, 0, 0, 0, 0, 0, 0))
    time_birth = time.localtime(time_float)
    print("我的生日是：", weeks[time_birth.tm_wday], sep="")
    print("我出生已经：", int((time.time() - time_float) // (3600 * 24)), "天", sep="")


# 大于1970, 1, 1
getBirthInfo(1990, 9, 21)

getBirthInfo(1991, 1, 1)

getBirthInfo(2020, 2, 16)
