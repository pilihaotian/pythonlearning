# 多继承的问题，标识符冲突
# MRO（Method Resolution Order）问题
# 类多继承关系，方法优先调用算法
#     A.m()   B.m()       C.m()   D.m()
#
#        AB.m()              CD.m()
#
#                 ABCD.m()

# python2，为广度优先调用，ABCD->AB->CD->A->B->C->D
# python3之后，为深度优先调用，即ABCD->AB->A->B->CD->C->D


class A:
    def m(self):
        print("A.m()")

    pass


class B:
    def m(self):
        print("B.m()")

    pass


class C:
    def m(self):
        print("C.m()")

    pass


class D:
    def m(self):
        print("D.m()")

    pass


class AB(A, B):
    def m(self):
        print("AB.m()")

    pass


class CD(C, D):
    def m(self):
        print("CD.m()")

    pass


class ABCD(AB, CD):
    def m(self):
        print("ABCD.m()")

    pass


# 测试 python3.8 mro() 之前版本为  __mro__
print(AB.mro())  # AB A B
print(CD.mro())  # CD C D
print(ABCD.mro())  # ABCD AB A B CD C D
print(ABCD.mro())  # ABCD AB A B CD C D

# 结论 3之后的版本 方法搜索为深度搜索
