# 列表推导式的嵌套
# 嵌套语法
# [表达式1
#   for 变量1 in 可迭代对象1 if 真值表达式1
#       for 变量2 in 可迭代对象2 if 真值表达式2
#   列表1 和 列表2 笛卡尔乘积

L = [str(x) + '*' + str(y) + '=' + str(x * y)
     for x in range(1, 10)
     for y in range(1, 10) if y >= x]
print(L)
