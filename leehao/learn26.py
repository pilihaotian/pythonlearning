# 固定集合 frozenset 是容器不可变、元素不可变的，无序的，不重复元素的集合
# 作用 可以作为字典的key，可以作为集合的值

# 空的
Fs = frozenset()

# 非空的，迭代器
Fs1 = frozenset(range(10))
print(Fs1)

# 交集、并集、补集、对称补集、超集、子集和Set一样
