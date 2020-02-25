# assert 断言
# assert 真值表达式，错误数据（一般为字符串）
# 当表达式为False时候，用错误数据创建一个 AssertionError类型的错误，并进入异常
# 等同于
# if 表达式 == False:
#     raise AssertionError(错误数据)


def get_age():
    a = input("请输入年龄:")
    a = int(a)
    assert a <= 140, '年龄不可能大于140岁'
    assert a > 0, '年龄不可能小于1岁'
    return a


try:
    a = get_age()
except AssertionError as error:
    print("发生了断言异常！错误对象是：", error)
    a = 1
print("age:", a)
