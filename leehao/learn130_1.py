# broadcast 广播 send
# 一个send端可以发送至多个resv端，一个网段内
from socket import *
from time import sleep

HOST = '<broadcast>'  # 广播地址为：172.60.50.255
PORT = 9999
DEST = (HOST, PORT)
s = socket(AF_INET, SOCK_DGRAM)  # udp

# 设置 可接受广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    sleep(1)
    s.sendto("三体三体，我是地球".encode('utf-8'), DEST)
    data, addr = s.recvfrom(1024)
    print("from %s : %s" % (addr, data.decode('utf-8')))
s.close()
