# module
# 模块是一个文件，以.py结尾
# 作用：1、将变量、函数、类组织起来 2、可供其他模块使用
# 分类：1、内置模块 2、标准库模块 3、第三方模块 4、用户自定义模块

import math as myMath
from math import pi, sqrt

# print(myMath.factorial(5))
# print(myMath.ceil(3.1))
# print(myMath.floor(3.1))
# print(myMath.pi)
# print(myMath.e)

# 输入半径，求面积
r = 10
print(myMath.pi * r ** 2)
print(pi * r ** 2)

# 输入面积，求半径
s = 100
print(myMath.sqrt(s / myMath.pi))
print(sqrt(s / myMath.pi))
