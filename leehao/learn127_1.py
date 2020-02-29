# UDP协议 Socket
# 服务端
from socket import *
import time

'''
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口
绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
'''
# ipv4        SOCK_DGRAM指定了这个Socket的类型是UDP


HOST = gethostname()  # 服务端ip
PORT = 9999  # 服务端端口号
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)
udpServerSock = socket(AF_INET, SOCK_DGRAM)  # 创建socket对象
# 绑定 客户端口和地址:
udpServerSock.bind(ADDR)  # 绑定9999端口号
print('服务启动，监听客户端链接')
while True:
    # 接收数据 自动阻塞 等待客户端请求:
    data, addr = udpServerSock.recvfrom(BUFFER_SIZE)  # 接收客户端发过来的数据和ip地址
    data = data.decode('utf-8')
    print('客户端的ip信息', addr)
    print('【%r】发过来的数据 %s' % (addr, data))
    msg = input('>>>')  # 输入
    msg = '[%s]:%s' % (time.strftime("%Y-%m-%d %X"), msg)
    udpServerSock.sendto(msg.encode('utf-8'), addr)  # 把数据发送给客户端
# recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。

udpServerSock.close()
