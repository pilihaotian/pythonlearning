# 写一个函数 myfn(n)

# 每隔一秒打印一次hello world，共n次
# 加入文档说明
# 采用递归


def myfn(n):
    """打印hello world
    每隔一秒打印一个hello world，共n次
    """
    if n == 1:
        print("hello world!")
        return
    else:
        print("hello world!")
        return myfn(n - 1)


myfn(5)
