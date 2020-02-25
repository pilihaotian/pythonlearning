# 面向对象编程
# slots 限定一个类创建的实例只能有固定的属性（实例变量）
# 是一个列表 ，含有slots创建的对象
# 没有 __dict__字典


class Student:
    __slots__ = ['name', 'age']

    def __init__(self, n, a):
        self.name = n
        self.age = a


s1 = Student("lihao", 23)

# Tips1
s1.__dict__  # AttributeError: 'Student' object has no attribute '__dict__'

# Tips2
# NAME不存在 且用slots绑定限定
s1.NAME = 'lihaohao'  # 报错 AttributeError: 'Student' object has no attribute 'NAME'
