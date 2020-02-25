# 1) 从L中返回随意元素
# 2） 将L乱序
# 3） 随机选择3个元素
import random

L = [1, 2, 2, 'bob', 'lucy']

print(L)
# 随机选取一个
print(random.choice(L))
# 将列表乱序
random.shuffle(L)
print(L)

# 随机选取n个 n=3
print(random.sample(L, 3))
