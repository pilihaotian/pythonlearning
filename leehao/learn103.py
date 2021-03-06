# 面向对象编程
# 静态方法 定义在类内部的函数，函数的作用域是类内部
# 静态方法需要@static装饰符定义
# 静态方法和普通方法相同，不需要传入self和cls
# 目的：静态方法只能凭借该类和该实例调用，限制作用域
# 静态方法不能访问类变量和实例变量


class A:
    @staticmethod
    def my_add(a, b):
        print(a + b)


A.my_add(100, 200)  # 类调用
A().my_add(300, 400)  # 实例调用
