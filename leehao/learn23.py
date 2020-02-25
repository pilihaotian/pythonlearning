# 字典推导式

# 生成一个字典，key为1-9 value为 key的平方
D = [{k: k ** 2} for k in range(1, 10)]
print(D)

# 有字符串列表，生成字典，字典的值为key的长度
L = ["java", "C language", "Python"]
D1 = [{key: len(key)} for key in L]
print(D1)

# 有2个列表，生成字典
Numbers = [1, 2, 3, 4]
Names = ["zhangsan", "lisi", "wangwu", "zhaoliu"]

D2 = [{Numbers[i], Names[i]} for i in range(len(Numbers))]
print(D2)

# 字典推导式 嵌套 语法同列表的语法


# 字典 VS 列表
# 1.都是可变的 2.索引方式不同 3.字典的查找速度快鱼列表 4.有序无序（Python3.6之后都是有序的）