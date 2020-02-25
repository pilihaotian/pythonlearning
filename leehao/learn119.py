# 复合运算符
# iadd +=
# isub -=
class MyList:

    def __init__(self, iterator):
        self.data = [x for x in iterator]

    # 重点
    def __repr__(self):
        return "MyList(%r)" % self.data

    def __add__(self, other):
        return MyList(self.data + other.data)

    # 复合运算 +=
    def __iadd__(self, other):
        # self.data += other.data
        # 或
        self.data.extend(other.data)
        return self


l1 = MyList([1, 2, 3])
l2 = MyList(range(4, 7))

print(l1 + l2)  # MyList([1, 2, 3, 4, 5, 6])
l1 += l2  # 优先去找 iadd 如果没有 那么去找add
print(l1)  # MyList([1, 2, 3, 4, 5, 6])
