# 迭代器Iterator和
# 迭代器 iter next来获取 StopIteration结束
L = [2, 4, 6, 9]
it = iter(L)
while True:
    try:
        n = next(it)
        print(n)
    except StopIteration as err:
        print(err)
        break
