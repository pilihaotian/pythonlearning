# 面向对象编程


class Dog:
    """这是一个狗的类"""

    def eat(self, food):
        """小狗吃的行为"""
        print("小狗吃了：", food)
        self.food = food

    def sleep(self, hour):
        """小狗睡觉行为"""
        print("小狗睡了：", hour, "小时")

    def food_info(self):
        print("上次吃的是：", self.food)


dog1 = Dog()
dog1.eat("牛奶")
# 等价于
Dog.eat(dog1, "牛奶")

dog1.sleep(2)
# 等价于
Dog.sleep(dog1, 2)

dog1.food_info()
