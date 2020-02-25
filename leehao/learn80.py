# 字节串 bytes 和字节数组 bytearray
# 字节串是不可改变的序列 字节是0-255之间的整数

# 空字节创建
print(b'')
print(b"")
print(b'''''')
print(b"""""")

# 非空
print(b'hello')
print(b"hello")
print(b'''hello''')
print(b"""hello""")
print(b'abc\n123')
print(b'\x41')
print(type(b''))
# print(b'你好')  # 报错 字节>255

# 字符串的其他特性同样也适用于字节串 如：+ * 索引 切片等
