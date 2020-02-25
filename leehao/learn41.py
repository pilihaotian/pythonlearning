# eval

# eval函数把字符串当作表达式执行
# 语法 eval(表达式，全局变量（None），局部变量，（None）)

# Demo1
print(eval("max([1,2,3])"))

# Demo2
a = 2
b = 2
# 取值顺序，从右到左，如果都没有，那么取内建值即a=2 b=2
print(eval("a+b"))
print(eval("a+b", {"a": 10, "b": 20}))  # 此处的a、b的值不从上面的a和b取 在本地取全局变量
# print(eval("a+b", {"a": 10}))  # 报错，无法取到b的值
print(eval("a+b", {"a": 10, "b": 20}, {"a": 30, "b": 40}))  # 此处的a、b的值不从上面的a和b取 在本地取局部变量
print(eval("a+b", {"a": 10, "b": 20}, {"a": 30}))  # 此处的a取值为30 b为20

# Demo3
print(eval("list(range(10))"))
