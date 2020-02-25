# 如下代码输出什么
import copy

L1 = [1.1, 2.2, [3.1, 3.2]]

L2 = L1  # 同L1
L3 = L1.copy()  # 浅拷贝若L1[2]有变化，L3也会变
L4 = copy.deepcopy(L1)  # 深拷贝 独立的对象不会随之L1的变化而变化
print(L1, L2, L3, L4, sep="\n")
L1[2][0] = 999
print("-" * 20)
print(L1, L2, L3, L4, sep="\n")
