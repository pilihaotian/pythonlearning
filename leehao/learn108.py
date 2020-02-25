#  私有属性和方法
# 以双下划线开始，但不以双下划线结束的标识符为私有成员，私有成员只能被方法调用，不能再子类中或其他方法中使用


class Human:
    def __init__(self, n):
        self.__name = n

    def __private_fun(self):
        print("Human's private function")


class Student(Human):
    def __init__(self, a, n):
        super().__init__(n)
        self.age = a


stu = Student('aaa', 20)
# 无法调用私有方法
# stu.private_fun('aaa')  # AttributeError: 'Student' object has no attribute '__private_fun'
# 无法调用私有属性
print(stu.age)
print(stu.__name)
