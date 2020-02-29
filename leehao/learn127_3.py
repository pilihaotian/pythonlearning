# UDP协议 Socket
# 客户端2 和 客户端1一样
from socket import *
import time

'''
客户端使用UDP时，首先仍然创建基于UDP的Socket，然后不需要连接，直接通过sendto()给服务器发数据：
'''
HOST = gethostname()  # 服务端ip
PORT = 9999  # 服务端端口号
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
    try:
        data = input('>>>')
        if not data:
            break
        data = '[%s]:%s' % (time.strftime("%Y-%m-%d %X"), data)
        udpCliSock.sendto(data.encode('utf-8'), ADDR)
        recv = udpCliSock.recv(BUFFER_SIZE)  # 返回的数据
        if not recv:
            break
        print(recv.decode('utf-8'))
    except Exception:
        print("断开的客户端", ADDR)
        break
# 接收数据:
udpCliSock.close()
