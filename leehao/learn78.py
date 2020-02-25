# 迭代工具函数
# 生成一个个性化的可迭代对象
# zip(iter1，iter2,...)  生成元组，元组内容是iter1,iter2...中元素的组合，个数由最小的可迭代对象决定
# enumerate(iterable[,start]) 生成带索引的枚举对象

numbers = [10086, 10000, 10010, 95577]
name = ['移动', '电信', '联通']
z = zip(numbers, name)
for x in z:
    print(x)

# (10086, '移动')
# (10000, '电信')
# (10010, '联通')

en = enumerate(numbers)
for x in en:
    print(x)

# 已经有2个列表，如何将这2个列表生成字典。

d = dict(zip(numbers, name))
print(d)
