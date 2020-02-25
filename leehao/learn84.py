# 杨辉三角
#         1
#        1 1
#       1 2 1
#      1 3 3 1


def get_next_line(lst):
    # 第一步
    next_line = [1]  # 最左边的1
    # 第二步 计算中间的数据，中间的个数为上一行的个数减1（两两相加）
    last_line_len = len(lst)
    if last_line_len:
        if last_line_len >= 2:
            last_line = lst[last_line_len - 1]
            for i in range(0, last_line_len - 1):
                next_line.append(last_line[i] + last_line[i + 1])
        # 第三步，加入最右边的1
        next_line.append(1)
    lst.append(next_line)


lst = []
n = 5
for x in range(1, n + 1):
    get_next_line(lst)

max_length = 2 * n - 1
for y in lst:
    s = ''
    for z in y:
        s += ' ' + str(z)
    print(s.center(max_length))
