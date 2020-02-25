print("a" > "b")
print("a" > "A")
print("abc" > "ab")
print("abc" > "acb")

print("a" in 'abc')
print("a" in 'bcd')
print('a' not in "abc")

s = "hello world!"
print(s[0], s[1], s[-1], s[-2], s[-len(s)], s[len(s) - 1], sep=" ")

s = "hello world!"
# 打印字符串1-最后一位
print(s[1:len(s)])
# 打印字符串0-最后一位
print(s[0:len(s)])
# 打印字符串0-最后一位，步长为2
print(s[0:len(s):2])
# 反向打印字符串，步长分别为1和2
print(s[-1:-len(s) - 1:-1])
print(s[-1:-len(s) - 1:-2])
print(s[::])

s = "上海自来水来自海上"
i = 0
# 偶数，取长度/2个字符串
if (len(s) % 2) == 0:
    i = len(s) // 2
# 奇数，取长度/2+1个字符串
else:
    i = len(s) // 2 + 1
s1 = s[0:i]
s2 = s[-1:-i - 1:-1]
print(s1, s2, sep="\n")
print(s1 == s2)

print(ord("浩"))
print(chr(28009))

print(str(2) == '2')

a = 3
b = 1
c = 2
print(b < a > c)
