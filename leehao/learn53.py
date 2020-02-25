# 装饰器 decorators
# 用法 @函数
# 一个函数，主要作用是包装一个函数或类
# 传入一个函数 返回一个函数


def my_decorators(fn):  # 装饰器函数
    def fx():
        print("fx开始")
        fn()
        print("fx结束")

    return fx


def hello():  # 被装饰函数
    print("hello,leehao")


hello()  # hello,leehao

hello = my_decorators(hello)  # 此种做法可以用装饰器@语法解决
hello()  # hello,world!
