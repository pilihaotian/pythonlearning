# 循环语句 输入一个n，输出 hello1-hellon

n = int(input("输入一个正整数"))
for i in range(n):
    print('hello', str(i + 1))

i = 0;
while i < n:
    print('hello', str(i + 1))
    i += 1

