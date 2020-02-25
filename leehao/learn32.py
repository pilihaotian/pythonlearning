# 函数 形参传递


# 位置形参
def func1(a, b):
    print(a, b)


func1(1, 2)


# 星号元组形参
def func2(*args):
    print("实参个数：", len(args))
    print("args:", args)


func2(1, 2, 3)
func2('a', 'b')


# 命名关键字形参
def func3(a, *, k):
    print(a)
    print(k)


# 此处k强制使用关键字传参
func3(100, k=200)
# 双星号字典传参
func3(10, **{'k': 20})


# 双星号字典形参，注意和星号元组形参的区别
def func4(**kwargs):
    print("个数", len(kwargs))
    print("kwargs:", kwargs)


func4(a=1, b=2, c=3)
