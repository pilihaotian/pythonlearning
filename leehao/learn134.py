# fork
import os

# 只能linux上执行
# 结果：
# pid = os.fork()
# 如果创建进程失败，那么改程序执行一次
# 如果创建进程成果，那么改程序会执行2次，且每次的执行顺序都不一定样

pid = os.fork()

if pid < 0:
    print("创建pid失败")
elif pid == 0:
    print("创建了新的进程")
else:
    print('原有的进程')
print("End.")

# os.fork  不要在windows系统上用
# 在window下没有一个函数可以实现UNIX下的fork()函数,其原因是历史造成的.
# 对于UNIX来说它一出生就是多用户的系统,所以它的所有进程都共有一个最原始的父进程init.
# 而windows生下来时是个单用户系统(DOS),不存在这样的概念.所以fork这个函数是UNIX下特有的.
#
# 如果硬要模似,CreateProcess()不如用CreateThread()更接近实际情况,
# 把主thread中的所有公共变量都塞入一个结构/类的,带入新的thread中,这样可以大致完成"复制自身"的要求.
#
# 但由于是thread,所以主thread死后,子thread不能独立存在,
# 而fork()出来的子进程可以脱离主进程独立存在,这一点在window下只有CreateProcess()才略有相似之处.
#
# 总之,实现类似fork()的功能在window下是复杂,必须个案处理,无法"一言以蔽之曰".
