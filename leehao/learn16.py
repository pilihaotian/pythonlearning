# split 和 join
s = "i am your dad"
L = s.split(' ')
print(L)
s1 = '\t'
# s.join(L)的意思是 将L迭代器用s连接起来。
# 如例子，将L用s1即“\t”连接起来
print(s1.join(L))
