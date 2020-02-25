# 集合 Set
# 1.可变的容器 2.唯一 3.无序 4.集合内的元素是不可变的对象 5.可迭代 6。 集合等于只有key的字典

St1 = set()
print(St1)
# 无序且唯一
St2 = {1, 2, 3, 4, 5, 6, 6, 0, -1}
print(St2)
# 集合的运算 & | - ^ < <= > >= == != in  not in
St3 = {1, 2, 3, 4}
St4 = {3, 4, 5, 6}

# 交集
print(St3 & St4)

# 并集
print(St3 | St4)

# 补集 St3存在 St4不存在的元素
print(St3 - St4)

# 对称补集 St3存在St4不存在 或者 St4存在St3不存在的元素
print(St3 ^ St4)

St5 = {1, 2, 3, 4, 5}
St6 = {1, 2}
# > 判断是否是超集（爸爸）
print(St3 > St4)
print(St5 > St6)
# < 判断是否是子集（儿子）
print(St4 < St3)
print(St6 < St5)
