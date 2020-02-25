# 标准输入输出 stdout stdin stderr
import sys

# stdout
sys.stdout.write("hello,world1\n")
# 由于stdout关闭了，所以print的时候会出错
# sys.stdout.close()
# print('dsadasdasd')  # ValueError: I/O operation on closed file.


sys.stderr.write("i am error!\n")
