# 写一个程序 读入任意行的文字数据 当输入空行时结束输入，打印带有行号的输入结果


def input_text():
    li = []
    while True:
        s = input("请输入文字，输入为空时结束：")
        if not s:
            break
        li.append(s)
    return li


def out_text(li):
    for t in enumerate(li, 1):
        print("第%d行：%s" % t)


def main():
    out_text(input_text())


main()
