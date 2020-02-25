# 实现自定义有序集合类，2个集合的交集& 并集| 补集- 对称补集^ == != （与集合相同）
# 集合内部用list存储


class OrderSet:
    def __init__(self, iterator):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "OrderSet(%r)" % self.data

    # &
    def __and__(self, other):
        return OrderSet(set(self.data) & set(other.data))

    # |
    def __or__(self, other):
        return OrderSet(set(self.data) | set(other.data))

    # -
    def __sub__(self, other):
        return OrderSet(set(self.data) - set(other.data))

    # ^
    def __xor__(self, other):
        return OrderSet(set(self.data) ^ set(other.data))

    def __eq__(self, other):
        return set(self.data) == set(other.data)

    def __ne__(self, other):
        return set(self.data) != set(other.data)


os1 = OrderSet([1, 2, 3, 4])
os2 = OrderSet([3, 4, 5, 6])
os3 = OrderSet([3, 4, 5, 6])

print(os1 & os2)  # OrderSet([3, 4])
print(os1 | os2)  # OrderSet([1, 2, 3, 4, 5, 6])
print(os1 - os2)  # OrderSet([1, 2])
print(os1 ^ os2)  # OrderSet([1, 2, 5, 6])
print(os2 == os3)  # True
print(os2 != os3)  # False
print(os1 == os2)  # False
print(os1 != os2)  # True
