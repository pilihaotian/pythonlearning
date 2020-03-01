# 异常 traceback
# 输入详细的信息
import traceback

try:
    a = 2 / 0
except ZeroDivisionError:
    traceback.print_exc()
print("END")
