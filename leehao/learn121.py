# 一元运算符重载
# neg pos invert
# isub -=
class MyList:

    def __init__(self, iterator):
        self.data = [x for x in iterator]

    # 重点
    def __repr__(self):
        return "MyList(%r)" % self.data

    def __neg__(self):
        return MyList([-x for x in self.data])


l1 = MyList([1, 2, 3])
print(-l1)  # MyList([-1, -2, -3])
