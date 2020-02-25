# raise 语句
# 触发一个错误 让程序进入异常状态
# 语法 raise 异常类型 或者 raise 异常对象


def make_exception(n):
    # 0-100 合法 之外的数据抛异常
    if 0 <= n <= 100:
        print(n)
    else:
        raise ValueError("超出了范围")


try:
    make_exception(101)
except ValueError as error:
    print(error)
