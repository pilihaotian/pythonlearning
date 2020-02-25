# 装饰器 decorators
# 接上，主要是装饰原来的函数


def my_decorators(fn):  # 装饰器函数
    def fx():
        print("fx开始")
        fn()
        print("fx结束")

    return fx


@my_decorators
def hello():  # 被装饰函数
    print("hello,leehao")


hello()
