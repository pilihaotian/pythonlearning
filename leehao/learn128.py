# tcp和udp的区别
# 1、tcp传输数据使用字节流的方式，udp是数据包
# 2、tcp会产生粘包现象，udp不会
# 3、tcp对网络条件要求高，udp更适合实时传输
# 4、tcp可保证传输的可靠性，udp不保证
# 5、tcp使用listen accept来保证连接过程，udp不需要
# 6、收发消息tcp使用recv send sendall，udp使用recvfrom sendto
