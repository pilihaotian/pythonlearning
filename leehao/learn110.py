# 多继承 C++、Python中有多继承


class Car:
    def __init__(self):
        print("Car init")

    def run(self, speed):
        print("汽车以每小时", speed, "公里的速度在行驶")


class Plane:
    def __init__(self):
        print("Plane init")

    def fly(self, height):
        print("飞机在", height, "米的高空飞行")


class PlaneCar(Car, Plane):
    pass


pc = PlaneCar()  # 如果多继承且子类没有init方法，那么会调用第一个基类的init方法
pc.run(200)
pc.fly(5000)
