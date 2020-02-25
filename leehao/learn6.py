# 输出A-Z和Az-Zz
# 方法一：
i = 'A'
az = ''
while i <= 'Z':
    az += i
    # ord将字符转为对应的ascii
    i = chr(ord(i) + 1)
else:
    print(az)
print('-' * 100)

i = 'A'
az = ''
while i <= 'Z':
    az += (i + i.lower())
    # ord将字符转为对应的ascii
    i = chr(ord(i) + 1)
else:
    print(az)
print('-' * 100)

# 方法二：
az = ''
for c in range(ord('A'), ord('Z') + 1):
    az += chr(c)
else:
    print(az)
print('-' * 100)

az = ''
for c in range(ord('A'), ord('Z') + 1):
    az += (chr(c) + chr(c).lower())
else:
    print(az)
print('-' * 100)
