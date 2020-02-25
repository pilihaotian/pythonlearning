# 重写内建函数
# 规则 __XXX__ 为XXX()
# 如 __abs__ 则为 abs()


class A:
    pass


# a = A()
# # 报错
# len(a)  # TypeError: object of type 'A' has no len()

class B:
    def __len__(self):
        return 200

    def __bool__(self):
        return True


b = B()
print(len(b))  # 200
print(bool(b))  # True
