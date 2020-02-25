# 实现2个自定义表相加、相乘
# 并且支持反向相乘，比如：List * 2 、 2 * List
# 其中反向运算符，在前面加r
# 其他运算也类似

class MyList:

    def __init__(self, iterator):
        self.data = [x for x in iterator]

    # 重点
    def __repr__(self):
        return "MyList(%r)" % self.data

    def __add__(self, other):
        return MyList(self.data + other.data)

    def __mul__(self, other):
        return MyList(self.data * other)

    # 反向运算符 rmul
    def __rmul__(self, other):
        return MyList(self.data * other)


l1 = MyList([1, 2, 3])
l2 = MyList(range(4, 7))

print(l1 + l2)  # MyList([1, 2, 3, 4, 5, 6])

print(l1 * 2)  # MyList([1, 2, 3, 1, 2, 3])
# 反向乘
print(3 * l2)  # MyList([4, 5, 6, 4, 5, 6, 4, 5, 6])
