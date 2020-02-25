# 完全数 因数的和和原数相等 10000以内的完全数
for i in range(2, 10000):
    tmp = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            tmp += j
    if tmp == i:
        print(i)
