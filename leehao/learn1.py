# 输入三行文字，以最长的字符串右对齐。
s1 = 'hello world'
s2 = 'abcd'
s3 = 'a'

maxLength = max(len(s1), len(s2), len(s3))

print(("%" + str(maxLength) + "s") % s1)
print(("%" + str(maxLength) + "s") % s2)
print(("%" + str(maxLength) + "s") % s3)
