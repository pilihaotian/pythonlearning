# 运算符重载
# 二元运算符
# __add__ 等价于 +
# __sub__       -
# ...       ...

# 可对__add__ 等运算符进行重载
# 如：
a = 1
b = 2
print(a + b)  # 等同于 print(a.__add__(b))


class MyNumber:
    def __init__(self, v):
        self.data = v

    # 重写运算符 add
    def __add__(self, other):
        return MyNumber(self.data + other.data)

        # 重写运算符 sub

    def __sub__(self, other):
        return MyNumber(self.data - other.data)

    # 重写repr
    def __repr__(self):
        return "MyNumber(%d)" % self.data


m1 = MyNumber(100)
m2 = MyNumber(200)

print(m1 + m2)  # 等同于 (m1.__add__(m2))   结果：MyNumber(300)
print(m1 - m2)
