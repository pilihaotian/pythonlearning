# 面向对象编程
# 类方法，属于类 不属于实例
# 第一个参数用来绑定类，默认cls
# 类和实例都可以调用
# 类方法不能访问此类创建的对象的属性


class Dog:
    total_cnt = 0

    @classmethod
    def get_total(cls):
        print(cls.total_cnt)

    @classmethod
    def set_total(cls, cnt):
        cls.total_cnt = cnt


# 测试1 类调用
Dog.get_total()
Dog.total_cnt = 2
Dog.get_total()
Dog.set_total(100)
Dog.get_total()

# 测试2 实例调用
dog2 = Dog()
dog2.get_total()
dog2.set_total(200)
dog2.get_total()
