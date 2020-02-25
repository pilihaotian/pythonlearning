# 闭包，将内嵌函数的语句和这些语句的执行环境大包在一起，得到的函数对象成为闭包
# 三个条件：
# 1、有一个内嵌函数
# 2、内嵌函数引用外部函数中的变量
# 3、外部函数返回值是内嵌函数


# 如下例
def make_power(y):
    def fn(x):
        return x ** y

    return fn


pow2 = make_power(2)
print("5的2次方是：", pow2(5))

pow3 = make_power(3)
print("5的3次方是：", pow3(5))
