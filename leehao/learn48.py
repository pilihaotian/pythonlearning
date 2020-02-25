# 递归函数 recursion
# 直接或间接调用自己

# 递归求100+99+...2+1


def getSum(n):
    if n == 1:  # 结束，如果n=1
        return 1
    else:  # 寻找规律
        return getSum(n - 1) + n


print(getSum(100))
