# 高阶函数 sorted
# sorted(iterable,key=None,reverse=False)
# 作用 将原可迭代对象进行排序，生成排序后的列表
# key 绑定函数，此函数提供一个可排序的依据
L = [-4, 5, 2, -3, 1, 0]

# 默认为升序
print(sorted(L))
# 降序
print(sorted(L, reverse=True))
# key为一个排序依据，自定义排序规则
print(sorted(L, key=abs))
