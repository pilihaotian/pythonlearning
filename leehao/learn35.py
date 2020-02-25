# 全局变量和global 局部变量

a = 1

b = 2


def fu(d):
    global b
    b = 22
    e = 400
    d = 200

    print(a, b, d, e)


fu(4)
print(a, b)
