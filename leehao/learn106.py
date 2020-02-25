# 继承后，父类的初始化方法会被覆盖掉，需要显示的去调用父类的初始化方法
# super

class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print("Human的init被调用")


class Student(Human):

    def __init__(self, n, a, s):
        super().__init__(n, a)  # 调用父类的init方法
        self.score = s
        print("Human的init被调用")


stu = Student('zhangsan', 20, 100)
print(stu.age)
print(stu.name)
