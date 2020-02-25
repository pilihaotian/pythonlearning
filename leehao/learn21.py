# 元组 tuple 不可改变的序列，同list一样，存放元素
# 不能赋值外 其他和list基本一样
t = ()
t1 = 200,
t2 = 200, 300, 400
t3 = (20,)
t4 = (1, 2, 3, 4)

# t4[0] = 5 # 报错 'tuple' object does not support item assignment


# 元组里是否可以存列表，列表的值是否可修改
# 答案是可以的
t5 = (1, [2, 3, 4])
t5[1][1] = 33
print(t5)
