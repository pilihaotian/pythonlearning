# 生成器 my_integer(n) 生成1到n的整数


def my_integer(n):
    i = 1  # 先初始化变量
    while i <= n:
        yield i
        i += 1


for x in my_integer(5):
    print(x)
