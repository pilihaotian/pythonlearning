# 高阶函数


# 求 1**2 2**2 3**2 ... n**2的和
# 求 1**3 2**3 3**3 ... n**3的和

def func1(i):
    return i ** 2


def func2(i):
    return i ** 3


n = 9
# 方法1
print(sum(map(func1, range(1, n + 1))))
# 方法2
print(sum(map(lambda i: i ** 2, range(1, n + 1))))

# 方法1
print(sum(map(func2, range(1, n + 1))))
# 方法2
print(sum(map(lambda i: i ** 3, range(1, n + 1))))
