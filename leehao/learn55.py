# module

# fun1(n) 求 Sn = 1/0!+1/1!+1/2!+1/3!+...+1/n!
# fun2(n,x) 求 Sn = x**0/0! + x**1/1! + x**2/2! + x**n/n!
import math


# 方法1
def fun1(n):
    mysum = 0
    for i in range(n + 1):
        mysum += 1 / (math.factorial(i))
    return mysum


# 方法2
def fun11(n):
    return sum(map(lambda i: i / (math.factorial(i)), range(n + 1)))


# 方法1
def fun2(x, n):
    mysum = 0
    for i in range(n + 1):
        mysum += math.pow(x, i) / (math.factorial(i))
    return mysum


# 方法2
def fun22(x, n):
    return sum(map(lambda i: math.pow(x, i) / (math.factorial(i)), range(n + 1)))


print(fun1(20))
print(fun11(20))
print("-" * 20)
print(fun2(3.1, 10))
print(fun22(3.1, 10))
print("-" * 20)
print(fun2(1, 10))
print(fun22(1, 10))
