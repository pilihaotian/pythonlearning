# file
# r 只读模式（默认）
# w 只写模式 打开的时候会清空原有文件，若不存在则创建
# x 创建一个新文件 并以写模式打开，如果文件存在则会产生异常：FileExistsError
# a 以只写模式打开，如果有原有文件，则追加

# b 二进制打开   t 文本模式打开（默认）
# + 为更新内容打开一个文件（可读可写）

try:
    f = open('test_data.txt', 'w')  # 只写模式，清空原文件
    f.write('hello11111111\n')
    f.write('world\n')

    f.flush()
    f.close()
except IOError:
    pass
