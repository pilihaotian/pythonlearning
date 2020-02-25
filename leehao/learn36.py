#  一个mysum函数，可以传1、2、3个参数
# 当传入一个参数，这个参数代表中止数，
# 2个参数，第一个代表起始、第二个代表终止
# 3个参数，第三个参数代表步长
# 如 mysum(5) 0+1+2+3+4
# mysum(2,5) 2+3+4
# mysum(2,5,2) 2+4


# 方法一
def mysum(*args):
    result = 0
    r = []
    if len(args) == 1:
        r = range(args[0])
    elif len(args) == 2:
        r = range(args[0], args[1])
    elif len(args) == 3:
        r = range(args[0], args[1], args[2])
    else:
        return None
    for i in r:
        result += i
    return result


print(mysum(5))
print(mysum(2, 5))
print(mysum(2, 5, 2))
