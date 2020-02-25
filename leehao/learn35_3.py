v = 100


def outter():
    v = 200
    print("outter中的v=", v)

    def inner():
        global v  # 此时，v = 最外层
        v = 300
        print("inner里的v=", v)

    inner()
    print("调用inner后，outter中v=", v)


outter()
print("全局变量v=", v)
