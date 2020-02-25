# 高阶函数 filter
# filter(func,iterable)
# 作用 筛选出iterable中的数据 返回一个可迭代对象
# 此时函数func将对iterable中的每个元素进行求值,求值后，返回False的时候将此数据丢弃，返回True则保留

# 返回100以内的奇数
for x in filter(lambda i: i % 2 == 1, range(1, 100)):
    print(x, end=" ")

print()
# 返回100以内的偶数
for x in filter(lambda i: i % 2 == 0, range(1, 100)):
    print(x, end=" ")
