# *************重点********
# 重写
# 为一个类写迭代器 next iter


class MyList:

    def __init__(self, iterable):
        self.data = [i for i in iterable]
        self.length = len(self.data)
        self.cur_pos = 0  # 游标位置初始化为0

    def __repr__(self):
        return 'MyList(%s)' % self.data

    # 重写iter，返回自身
    def __iter__(self):
        return MyList(self.data)

    # 重写next，每次取一个值，游标+1
    def __next__(self):
        if self.cur_pos >= self.length:
            raise StopIteration
        current_data = self.data[self.cur_pos]
        self.cur_pos += 1
        return current_data


mylst = MyList([x for x in range(1, 10) if x % 2])
print(repr(mylst))

# 方法1遍历
for x in mylst:
    print(x, end=" ")
print()

# 方法2遍历

it = iter(mylst)
while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        print()
        break

# Result::
# MyList([1, 3, 5, 7, 9])
# 1 3 5 7 9
# 1 3 5 7 9
