# stdin
import sys

a = sys.stdin.readline()  # 读取一行
sys.stdout.write(a)
b = sys.stdin.read(5)  # 读取5个
sys.stdout.write(b)
c = sys.stdin.read()  # 读取文件，直到文件尾（Linux下 输入Ctr+D 表示文件尾）
sys.stdout.write(c)
