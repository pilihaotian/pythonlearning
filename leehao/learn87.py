# 读取data.txt文件中 数据如下：
# 小张  13888888888
# 小李  13999999999
# 小赵  13777777777
#   写程序读取数据，打印出姓名和电话号码

try:
    f = open('data.txt', 'rt', encoding='utf-8')  # 设置编码
    while True:
        s = f.readline()
        if not s:
            break
        s = s.rstrip().lstrip()  # 去掉左右的空格、制表符、换行符等
        info = s.split(' ')
        print("姓名：%s，电话：%s" % (info[0], info[1]))  # 过滤掉空格 换行等
    f.close()
except IOError:
    pass
