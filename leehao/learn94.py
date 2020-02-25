# 面向对象编程
# 初始化


class Car:
    """小汽车类"""

    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

    def run(self, speed):
        print(self.color, "的", self.brand, self.model, "正在以", speed, "公里每小时的速度行驶")

    def change_color(self, c):
        self.color = c


a4 = Car("红色", "奥迪", "A4")
a4.run(200)
a4.change_color('白色')
a4.run(199)

x5 = Car('蓝色', '宝马', 'X5')
x5.run(260)
