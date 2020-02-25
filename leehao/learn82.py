# 字节数组 bytearray 可变的
print(bytearray())
print(bytearray(1))  # 整数
print(bytearray([1, 2, 3, 4]))  # 可迭代
print(bytearray("hello,world", encoding='utf-8'))  # 字符串 encod

ba = bytearray([1, 2, 3, 4])
print("更改前：", ba)
ba[0] = 2
print("更改后：", ba)
