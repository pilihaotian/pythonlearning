# 异常（高级）
# 异常处理5条语句  try except、try finally、raise、assert、with
# with 用于对资源访问的场合，无论异常是否发生，都会执行必要的清理工作
# with 表达式1[as 变量1],......
# with 与 try finally相似，相对简洁
# with目前只能用于文件的打开与关闭

# 不用with的方式
try:
    f = open('test_data.txt')
    try:
        while True:
            s = f.readline()
            if not s:
                break
            print(s)
    finally:
        f.close()
except IOError:
    print("IO异常已捕获")
except ValueError:
    print("Value异常已捕获")

# 采用with的方式
try:
    with open('test_data.txt') as f1:  # 此处调用后，会自动执行f1.close方法来关闭，类似于Java的AutoClose
        while True:
            s = f1.readline()
            if not s:
                break
            print(s)
except IOError:
    print("IO异常已捕获")
except ValueError:
    print("Value异常已捕获")
