# 多继承的问题，标识符冲突


class A:
    def f(self):
        print("A.f()")


class B:
    def f(self):
        print("B.f()")


class AB(A, B):
    pass


ab = AB()
ab.f()  # 调用的是A的f方法，类似于上一个Demo的 init方法
