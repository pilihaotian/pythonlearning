# 用生成器生成 斐波那契的前n个数字 1 1 2 3 5 8 13


def fibonacci(n):
    i = 1
    first = 1  # 初始化第一个数字
    second = 1  # 初始化第二个数字
    yield first  # 生成第一个
    while i <= n:
        yield second
        first, second = second, first + second
        i += 1


for x in fibonacci(100):
    print(x)
