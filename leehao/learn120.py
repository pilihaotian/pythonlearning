# 测试


def test1(x):
    x = x + x  # add return new
    print(x)


def test2(x):
    x += x  # iadd return self
    print(x)


a1 = [100]
test1(a1)  # [100, 100]
print(a1)  # [100]
a2 = [100]
test2(a2)  # [100, 100]
print(a2)  # [100, 100]
