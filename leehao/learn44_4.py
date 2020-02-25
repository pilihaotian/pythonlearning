# 高阶函数


# 求 1**9 2**8 3**7 ... 9**1的和

def func1(i, j):
    return i ** j


n = 9
# 方法1
print(sum(map(func1, range(1, n + 1), range(n, 0, -1))))

# 方法2
print(sum(map(lambda i, j: i ** j, range(1, n + 1), range(n, 0, -1))))

# 方法3
print(sum(map(pow, range(1, n + 1), range(n, 0, -1))))
