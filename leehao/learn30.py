# 输入三角形高度，输出三角形
# 输入：4
# 输出：
#         1
#        121
#       12321
#      1234321

n = int(input())
maxLength = 2 * n - 1
for i in range(1, n + 1):
    s = ''
    # 从1-i
    for j in range(1, i + 1):
        s += str(j)
    # 反转后居中
    print((s[0:len(s) - 1] + s[::-1]).center(maxLength))
