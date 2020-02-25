# 摇骰子游戏
import random
import math

i = 0
j = 0
k = 0
cnt = 10000
for n in range(cnt):
    a = random.randrange(1, 7)
    print("李浩开始摇骰子：", a)
    b = random.randrange(1, 7)
    print("白雪开始摇骰子：", b)
    if a > b:
        print("李浩胜利！")
        i += 1
    elif a < b:
        print("白雪胜利！")
        j += 1
    else:
        print("打成平手！")
        k += 1

print("李浩胜的次数：", i)
print("李浩败的次数：", j)
print("平手的次数：", k)
print("李浩的胜率：", i / (i + j))
