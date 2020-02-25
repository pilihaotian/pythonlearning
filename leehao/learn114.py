# 重写repr和str
# 对象-字符串
# repr(obj) 返回一个能代表此对象的字符串，通常 eval(repr(obj)) == obj
# str(obj)  通过给定的对象返回一个字符串（方便人阅读）


# 重写前的测试
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = A('leehao', 18)
print(repr(a))  # 默认返回的是obj的id <__main__.A object at 0x03501328>
print(str(a))  # 默认返回的是obj的id <__main__.A object at 0x03501328>


# 重写str、repr，当对象没有str，则返回repr
class B:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '[name:' + str(self.name) + ',' + 'age:' + str(self.age) + ']'

    def __repr__(self):
        return 'B(' + str(self.name) + ',' + str(self.age) + ')'


b = B('leehao', 18)
print(repr(b))  # B(leehao,18)  返回自定义的repr
print(str(b))  # [name:leehao,age:18]   返回自定义的str
