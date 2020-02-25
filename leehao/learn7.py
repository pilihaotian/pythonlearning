# 列表 list

L1 = []
L2 = [1, 2, 3, 4]
L3 = ['1', 2, '3', 'hello']
L4 = [L1, L2, L3]
L4[2][3] = 'world'
# 通过迭代创建list
L5 = list(range(1, 11))
print(L4)
print(L5)
# 可加
print(L2 + L3)
# 可乘
print(L2 * 2)
