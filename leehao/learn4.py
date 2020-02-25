# 输入一个大于1的奇数，打印该三角形的各种形状
n = int(input("输入一个大于1的奇数"))
i = 1
while i <= n:
    print(("*" * i).center(n))
    i += 2

i = 1
print("-" * 20)
while i <= n:
    print(("*" * i).ljust(n))
    i += 2
i = 1
print("-" * 20)
while i <= n:
    print(("*" * i).rjust(n))
    i += 2

print("-" * 20)
i = n
while i > 0:
    print(("*" * i).rjust(n))
    i -= 2

print("-" * 20)

i = n
while i > 0:
    print(("*" * i).ljust(n))
    i -= 2
