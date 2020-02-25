# 递归函数
# 1~n阶乘的和 1！+ 2! + 3! ... n!


def myfac(x):
    if x == 1 or x == 0:
        return 1
    else:
        return myfac(x - 1) * x


n = 3
L = map(myfac, range(1, n + 1))
print(sum(L))
