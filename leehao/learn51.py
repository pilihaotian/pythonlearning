# 递归函数
# 1、打印列表中所有数字
# 2、输出所有数字和
# type可返回一个变量的类型

L = [[3, 5, 8], 10, [[13, 14], 15], 18]

Result = []


def getNumber(li):
    for x in li:
        if type(x) is int:
            Result.append(x)
        elif type(x) is list:
            getNumber(x)


getNumber(L)
print(Result)
print(sum(Result))
