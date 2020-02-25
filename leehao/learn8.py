# 输入一些行文字，将文字保存在列表中，当输入空行时结束，并打印列表
L1 = []
while True:
    s = input("请输入文字（输入空行结束）：\n")
    if s == '':
        break
    else:
        L1.append(s)
print(L1)
