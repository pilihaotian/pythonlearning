# 自定义module
"""自定义module

自定义module说明
"""

# 表示可以被导入的，要求导入格式：from learn60 import  *
__all__ = ['call', 'message', 'name', 'age']


def call():
    print("打电话...")


def message():
    print("发短信...")


def private_fun():
    print("私有方法不能被导入...")


def _fun1():
    print("私有方法不能被导入...")


name = "张三"
age = 20
private_salary = 100000
_sex = '男'

print("module模块名", __name__)  # 如果是运行的 那么输出__mail__， 如果是被导入的，那么输出文件名
