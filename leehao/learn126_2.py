#!/usr/bin/python3
# -*-coding:utf-8 -*-
from socket import *
import time

HOST = gethostname()  # 服务端ip
PORT = 9999  # 服务端端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
tcpCliSock.connect(ADDR)  # 连接服务器
while True:
    data = input('>>').strip()
    if not data:
        break
    data1 = '[%s]:%s' % (time.strftime("%Y-%m-%d %X"), data)
    tcpCliSock.send(data1.encode('utf-8'))  # 发送消息
    msg = tcpCliSock.recv(BUFSIZ)  # 读取消息
    if not data:
        break
    print(msg.decode('utf-8'))
tcpCliSock.close()  # 关闭客户端
