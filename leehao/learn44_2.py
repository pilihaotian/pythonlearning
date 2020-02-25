# 高阶函数


# 生成一个可迭代对象，要求此迭代对象生成 1**4 2**3 3**2 4**1

# 等价于pow
def fuc1(i, j):
    return i ** j


n = 4
for x in map(fuc1, range(1, n + 1), range(n, 0, -1)):
    print(x, end=" ")
print()
print(sum(map(fuc1, range(1, n + 1), range(n, 0, -1))))
