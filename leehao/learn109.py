# 多态，调用基类的方法，实际能调用子类的覆盖方法的现象叫做多态
# 与对象有关，不与类相关
# Python的全部对象只有运行时状态（动态，没有Java、C++中编译时的状态（静态）


class Shape:
    def draw(self):
        pass


class Point(Shape):
    def draw(self):
        print("画点。。。。。。。。")


class Circle(Shape):
    def draw(self):
        print("画圆。。。。。。。。")


def my_draw(s):
    s.draw()


s1 = Circle()
s2 = Point()

my_draw(s1)
my_draw(s2)
