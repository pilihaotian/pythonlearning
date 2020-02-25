# in not in 重载
# contains


class MyList:

    def __init__(self, iterator):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __contains__(self, e):
        return e in self.data


l1 = MyList([1, 2, 3])
print(1 in l1)  # True
print(1 not in l1)  # False
print(4 in l1)  # False
