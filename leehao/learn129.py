# socket 内部方法

from socket import *

s1 = socket()
print(s1.fileno())  # IO操作 文件描述符，序列号，每次都不一样且唯一
print(s1.type)  # socket的类型 SocketKind.SOCK_STREAM
s1.bind(('127.0.0.1', 8888))
print(s1.getsockname())  # ('127.0.0.1', 8888)

# eg.
