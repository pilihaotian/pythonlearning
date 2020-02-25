# 递归函数 recursion
# 计算阶乘


def myfac(x):
    if x == 1 or x == 0:
        return 1
    else:
        return myfac(x - 1) * x


print(myfac(0))
print(myfac(1))
print(myfac(10))
