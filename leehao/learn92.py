# 面向对象编程
# 类
# 类名（继承列表）
# """类文档字符串"""
# 实例方法的定义
# 类变量的定义
# 类方法的定义
# 静态方法定义
# 类的定义最后面加2个空格告诉解析器 类的定义已结束


class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s


def input_student():
    L = []
    while True:
        n = input("姓名:")
        if not n:
            break
        a = input("年龄:")
        if not a:
            break
        s = input("成绩:")
        if not s:
            break
        stu = Student(n, a, s)  # 创建对象
        L.append(stu)
    return L


def output_student(lst):
    for stu in lst:
        print("姓名：", stu.name,
              "年龄：", stu.age,
              "成绩：", stu.score)


def main():
    L = input_student()
    output_student(L)


main()
