# 高阶函数
# 满足下列函数中的一个函数即为高阶函数
# 1、函数接受一个或多个函数作为传参
# 2、函数返回一个函数

# 内置的高阶函数 map filter sorted

# 生成一个可迭代对象，要求此迭代对象可以生成1~9自然数的平方，并求和


def power2(n):
    return n ** 2


# map 创建一个迭代器，生成一个可迭代对象
for x in map(power2, range(1, 10)):
    print(x, end=" ")
print()
print(sum(map(power2, range(1, 10))))