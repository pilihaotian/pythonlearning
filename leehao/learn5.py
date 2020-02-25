# 输入一个字符串，统计空格的个数

s = input("请输入：\n")
# 方法一
print(s.count(" "))

# 方法二
cnt = 0
for c in s:
    if c == ' ':
        cnt += 1
print(cnt)

# 方法三
length = len(s)
i = 0
cnt = 0
while i < length:
    if s[i] == ' ':
        cnt += 1
    i += 1
print(cnt)
