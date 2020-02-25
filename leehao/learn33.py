# 函数Demo
def fun1():
    print('hello')


def fun2():
    print('world')


# 交换2个函数的变量绑定
fun1, fun2 = fun2, fun1

fun1()
fun2()
