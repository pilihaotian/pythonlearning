# 集合练习

# 经理
Manager = {"李浩", "刘备", "孙权", "曹操"}

# 技术员

IT = {"李浩", "诸葛亮", "孙权", "司马懿"}

# 二者都是
print(Manager & IT)
# 只是Manager
print(Manager - IT)
# 只是IT
print(IT - Manager)
# 李浩是经理吗
print("李浩" in Manager)

# 身兼一职的
print(Manager ^ IT)

# 共有多少人
print(len(Manager | IT))
