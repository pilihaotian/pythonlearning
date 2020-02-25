# 函数中动态创建函数


# 计算类型
def calculator(calType):
    if calType == 1:
        def myadd(a, b):
            return a + b

        return myadd
    if calType == 2:
        def mysub(a, b):
            return a - b

        return mysub
    if calType == 3:
        def mymulti(a, b):
            return a * b

        return mymulti
    if calType == 4:
        def mydiv(a, b):
            return a / b

        return mydiv


a = calculator(1)
print(a(100, 200))

b = calculator(2)
print(b(100, 200))

c = calculator(3)
print(c(100, 200))

d = calculator(4)
print(d(100, 200))
