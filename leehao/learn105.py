# super


class A:
    def work(self):
        print("A类的work被调用")


class B(A):
    def work(self):
        print("B类的work被调用")


b = B()
# 调用子类的work方法
b.work()

# 调用父类的work方法
super(B, b).work()
