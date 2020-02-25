# 高阶函数 sorted

# 根据名字的长度进行排序
names = ['Tom', 'Jerry', "Spike", 'Tyke']
L = sorted(names, key=len, reverse=True)
print(L)


def getReverseName(name):
    return name[::-1]


# 根据名字首字母进行排序，默认
L1 = sorted(names)
print(L1)

# 根据名字最后一个字母进行排序，将字符串倒序后进行排列
L2 = sorted(names, key=getReverseName)
print(L2)
