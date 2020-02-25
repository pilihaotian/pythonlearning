# 面向对象编程
# 类变量，类的属性，属于类不属于实例

# 总结：如果类属性和实例属性都存在，那么各自独立，如果有不存在，则共用

class Dog:
    total_cnt = 0  # 类属性


# 测试1
print(Dog.total_cnt)  # 0
dog1 = Dog()
print(dog1.total_cnt)  # 0

# 测试2
Dog.total_cnt = 1
print(Dog.total_cnt)  # 1   类属性为1
print(dog1.total_cnt)  # 1  实例属性不存在，采用的是类属性

# 测试3
dog1.total_cnt = 2
print(Dog.total_cnt)  # 1   修改实例属性后，类属性不变
print(dog1.total_cnt)  # 2

# 测试4
Dog.total_cnt = 3
print(Dog.total_cnt)  # 3
print(dog1.total_cnt)  # 2  修改类属性后，实例属性不变
