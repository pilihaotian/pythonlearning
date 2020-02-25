# 面向对象编程
# 析构方法 对象销毁前调用 和构造函数相反


class FileManager:
    """定义一个文件管理类"""

    def __init__(self):
        print("我是初始化函数")

    def __del__(self):
        print("我是析构函数")


fm = FileManager()
