# 生成器函数
# 可用于大数据
# my_odd(start,stop) 生成区间奇数，不包括stop


def my_odd(start, stop):
    i = start  # 先初始化变量
    while i < stop:
        if i % 2:
            yield i
        i += 1


# 这样操作 程序不会崩溃
for x in my_odd(1, 100000000000000):
    print(x)

# L = [x for x in range(100000000000000)]   # 程序会卡住
