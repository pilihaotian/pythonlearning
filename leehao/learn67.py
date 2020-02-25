# 异常 exception

a = 2
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print("除数不能为0")
else:
    print(a / b)
print("END")
