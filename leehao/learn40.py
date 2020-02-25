# Lambda表达式 （匿名函数表达式）
# 作用 创建一个函数 但不提供函数名
# 语法： lambda [参数1、参数2...] 表达式

# lambda表达式创建的函数只能有一条表达式

myadd = lambda a, b: a + b
print(myadd(1, 2))

# 写一个lambda表达式，判断这个数字的3次放+1能否被5 整除，返回true或false

lam1 = lambda n: True if (n ** 3 + 1) % 5 == 0 else False
print(lam1(4))
print(lam1(3))

# 写一个lambda表达式，求两个变量的最大值
lam2 = lambda x, y: x if x > y else y  # 条件表达式

print(lam2(1, 2))
print(lam2(2, 1))
