# file 打开 写入 关闭

# w+b 二进制随机读写，打开文件会清空内容
# r+b 二进制读和更新文件，打开文件不会清空内容
# r+  以文本模式读和更新打开文件，打开文件不会清空内容

try:
    f = open('test.txt', mode='a')  # append
    f.writelines("12345\n")
    f.writelines("6789\n")
    f.flush()
    f.close()
except IOError:
    pass
