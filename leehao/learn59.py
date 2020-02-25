# exit
import sys


def fun():
    print("进入函数")
    sys.exit()
    print("退出函数")  # 并不执行


fun()
print("退出程序")  # 并不执行，在函数中就已经退出程序了
