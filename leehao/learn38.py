#  一个mysum函数，可以传1、2、3个参数
# 当传入一个参数，这个参数代表中止数，
# 2个参数，第一个代表起始、第二个代表终止
# 3个参数，第三个参数代表步长
# 如 mysum(5) 0+1+2+3+4
# mysum(2,5) 2+3+4
# mysum(2,5,2) 2+4


# 方法三（缺省参数）
def mysum(start, stop=None, step=1):
    if stop is None:
        stop, start = start, 0
    return sum(range(start, stop, step))


print(mysum(5))
print(mysum(2, 5))
print(mysum(2, 5, 2))
