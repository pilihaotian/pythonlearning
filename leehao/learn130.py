# broadcast 广播 recv
from socket import *

HOST = ''
PORT = 9999

s = socket(AF_INET, SOCK_DGRAM)  # udp

# 设置 可接受广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# 设置地址可重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind((HOST, PORT))

while True:
    try:
        message, addr = s.recvfrom(4096)
        print("from %s : %s" % (addr, message.decode('utf-8')))
        s.sendto('I am here'.encode('utf-8'), addr)
    except (KeyboardInterrupt, SyntaxError):
        raise
    except Exception as e:
        print(e)
s.close()
