# 浅拷贝shallow copy  深拷贝deep copy
# 其中copy方法是浅拷贝  Return a shallow copy of the list.
# 浅拷贝只复制引用地址，不复制具体的值

# 浅拷贝
L = [1.1, 2.1]
L1 = [L, 3.1]
print(L1)
L[1] = 2.2
print(L1)
print('-' * 20)

K = [1.1, 2.1]
K1 = [K, 3.1]
K2 = K1.copy()  # copy为浅拷贝，只拷贝了引用地址，不拷贝值
K[1] = 2.2
K1[1] = 3.2
print(K1)
print(K2)

print('-' * 20)

# 深拷贝 深拷贝只对可变对象进行深度复制，不可变对象通常不会被复制
import copy

K = [1.1, 2.1]
K1 = [K, 3.1]
K2 = copy.deepcopy(K1)  # 深拷贝
K[1] = 2.2
K1[1] = 3.2
print(K1)
print(K2)
