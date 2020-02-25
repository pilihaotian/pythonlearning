# 函数
# 获取最大值


def getMax(a, b, c):
    return max(a, b, c)


# 调用方式和传参方式

# 1、位置传参
print(getMax(3, 1, 2))

# 2、序列传参 *L
L = [3, 2, 1]
print(getMax(*L))
print(getMax(*'ABC'))
print(getMax(*(101, 202, 303)))

# 报错 个数不对
# print(getMax(L))
# print(getMax(*'ABCD'))

# 3、关键字传参
print(getMax(a=3, c=1, b=2))

# 字典关键字传参 **D
D = {'a': 3, 'c': 1, 'b': 2}
# 输出key的最大值
print(getMax(*D))
# 输出value的最大值
print(getMax(**D))


