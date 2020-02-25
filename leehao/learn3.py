# n以内的质数
n = int(input("输入一个正整数"))
i = 2
while i <= n:
    # 设置标识位，默认为质数
    flag = True
    # 从2到i的平方根
    m = int(pow(i, 0.5))
    j = 2
    while j <= m:
        if i % j == 0:
            # 若被整出，则不为质数，置为False，退出循环
            flag = False
            break
        j += 1
    if flag:
        print(i, end=" ")
    i += 1
print()
