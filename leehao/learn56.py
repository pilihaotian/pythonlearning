# time
import time

# 写一个程序，以电子时钟的格式显示时间：HH:MM:SS
while True:
    ctime = time.localtime()
    # \r让光标在首位置，end=""不换行显示
    print("\r%02d:%02d:%02d" % (ctime.tm_hour, ctime.tm_min, ctime.tm_sec), end="")
    time.sleep(1)
