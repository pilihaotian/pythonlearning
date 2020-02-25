# 面向对象编程
# 预置的实例属性
# dict 存储此实例自身的字典
# class 绑定创建实例的类


class Dog:
    pass


dog1 = Dog()
print(dog1.__dict__)
dog1.color = 'white'
print(dog1.__dict__)  # 输出自身属性
print(dog1.__class__)  # 绑定Dog类
