# 面向对象编程
# 类变量 Demo


class Human:
    total_cnt = 0

    def __init__(self, name):
        self.name = name
        self.__class__.total_cnt += 1  # 类变量+1
        print(name, '对象创建')

    def __del__(self):
        self.__class__.total_cnt -= 1


print('当前对象的个数是', Human.total_cnt)
h1 = Human('张飞')
h2 = Human('关羽')
print('当前对象的个数是', Human.total_cnt)
del h2
print('当前对象的个数是', Human.total_cnt)
