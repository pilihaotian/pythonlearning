# 生成器表达式
# 语法：(表达式 for 变量 in 可迭代对象 if 真值表达式)

# 1、元组
gen1 = (x ** 2 for x in range(1, 5))

# 生成后就是生成器表达式
print(gen1)  # <generator object <genexpr> at 0x0122DA38>

# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

# 2、列表
gen2 = [x ** 2 for x in range(1, 5)]

# 生成后就是列表
print(gen2)  # [1, 4, 9, 16]
# 需要使用迭代器
it2 = iter(gen2)
# print(next(it2))
# print(next(it2))
# print(next(it2))
# print(next(it2))
# print(next(it2))
