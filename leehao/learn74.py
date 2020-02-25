# 重点理解
# 生成器Generator
# 生成器动态提供数据的对象，也是可迭代对象
# 生成器函数 生成器表达式

# 语法 yield 表达式

# 如：range(10000000000000000000000000)
# 程序不会一开始就生成如此多的数字，而是用的时候生成，等于用时间来换取空间

# 如果函数中有 yield，那么该函数不是可执行程序，而是生成器对象，可以生成一组值


def my_yield():
    print("生成2")
    yield 2
    print("生成3")
    yield 2 + 1
    print("生成5")
    yield 5
    print("生成7")
    yield 7
    print("生成a")
    yield 'a'


# 调用该函数，但不会执行函数中的程序，生成一个生成器对象
gen1 = my_yield()
print(gen1)  # <generator object my_yield at 0x0322DA38>

# 只取yield关键字的值，前面的语句执行，如：
print("第一个next：", next(gen1))
# 结果：
# 生成2
# 第一个next： 2


# 可迭代对象
for i in gen1:
    print(i)
print()

# 可迭代对象
gen2 = my_yield()
while True:
    try:
        print(next(gen2))
    except StopIteration as err:
        print(err)
        break
print()
