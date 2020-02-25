# 面向对象编程
# 判断某个对象是否是某个类，或某组类中的一个


class Dog:
    pass


class Cat:
    pass


dog1 = Dog()
cat1 = Cat()

# 判断dog1是否是Dog类
print(isinstance(dog1, Dog))
# 判断dog1是否是Cat类
print(isinstance(dog1, Cat))

# 同上
print(isinstance(cat1, Cat))
print(isinstance(cat1, Dog))

# 判断dog1是否是元组（Cat Dog）中的某一个类
print(isinstance(dog1, (Cat, Dog)))
# 判断cat1是否是元组（Cat Dog）中的某一个类
print(isinstance(cat1, (Cat, Dog)))
