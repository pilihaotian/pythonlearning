# 列表推导式
# 用可迭代对象生成带有多个元素的列表的表达式
# 语法
# [表达式 for 变量 in 可迭代对象] 或者 [表达式 for 变量 in 可迭代对象 if 真值表达式]

# 生成i的平方列表
L = [x ** 2 for x in range(1, 10)]
print(L)

# 生成100以内的奇数
L1 = [x for x in range(1, 100) if x % 2 != 0]
print(L1)
# 或者
L2 = [x for x in range(1, 100, 2)]
print(L2)

# 生成i的平方，并跳过偶数
L3 = [x ** 2 for x in range(1, 10, 2)]
print(L3)

# 输入开始值begin 结束值end 将开始至结束值中，平方+1能被5整除的放到列表中

begin = int(input())
end = int(input())
L = [x for x in range(begin, end + 1) if (x ** 2 + 1) % 5 == 0]
print(L)

