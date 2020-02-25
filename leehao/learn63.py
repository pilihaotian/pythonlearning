# 随机6位密码 a-zA-Z0-9下划线
import random

source = ''
lower_char = [chr(x) for x in range(ord('a'), ord('z') + 1)]
upper_char = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
number_char = [chr(x) for x in range(ord('0'), ord('9') + 1)]
source += "".join(lower_char)
source += "".join(upper_char)
source += "".join(number_char)
source += "_"
print(source)

# 随机取出20位字符串，包括下划线
while True:
    s = "".join(random.sample(source, 20))
    if '_' in s:
        print(s)
        break
