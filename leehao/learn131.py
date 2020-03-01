# http协议
# http server
# 启动后，在浏览器中输入：127.0.0.1:9999
# 结果：输出请求头，并返回服务器信息

from socket import *


# 1 接受http请求
# 2 给出一定的相应

# 处理客户端请求
def handleClient(connfd):
    # 读取信息
    request = connfd.recv(2048)
    request_headers = request.splitlines()
    for line in request_headers:
        print(line)
    # 结果：
    # b'GET / HTTP/1.1'
    # b'Host: 127.0.0.1:9999'
    # b'Connection: keep-alive'
    # b'Upgrade-Insecure-Requests: 1'
    # ...

    # 返回
    try:
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        response += 'OKOKOK'
        connfd.send(response.encode('utf-8'))
    except Exception as e:
        print(e)
    finally:
        connfd.close()


# 流程控制
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('', 9999))
    sockfd.listen(10)
    while True:
        connfd, addr = sockfd.accept()
        handleClient(connfd)


main()
