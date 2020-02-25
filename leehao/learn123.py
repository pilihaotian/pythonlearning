# index和切片 重载
# getitem setitem delitem 重载


class MyList:
    def __init__(self, iterator):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "MyList(%r)" % self.data

    # 支持index索引取值
    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        self.data.remove(self.data[key])


mlst = MyList([1, 2, 3, 4, 5])
print(mlst[1])  # getitem
print(mlst[1:4:2])  # getitem
# 等价于
print(mlst[slice(1, 4, 2)])  # getitem
mlst[1] = 222222  # setitem
print(mlst[1])
del mlst[1]  # delitem
print(mlst)
# 结果
# 2
# [2, 4]
# [2, 4]
# 222222
# MyList([1, 3, 4, 5])
