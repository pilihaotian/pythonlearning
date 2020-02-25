# file 打开 读取 关闭

try:
    f = open('test.txt', mode='r')
    while True:
        s = f.readline()
        if s:
            print(s, end="")
        else:
            break
    f.close()
except IOError:
    pass
