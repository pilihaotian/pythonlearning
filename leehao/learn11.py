# and or none any all的测试

# and
# a and b and c and d，返回第一个假的，如都为真，则返回最后一个
print(1 and 2 and 3)  # 1 2 3 都为真，则返回最后一个
print(1 and 0 and 3)  # 第一个假为0，则返回0
# or
# a or b or c or d，返回第一个真的，如都为假，则返回最后一个
print(0 or 2 or 3)  # 第一个真为2，则返回2
print(None or 0 or '' or None)  # 都为假0，则返回最后一个
# not 返回表达式结果的“相反的值”。其中None 0 '' [] 0.0 0j False都为False
print(not 1)
print(not None)
print(not 0)
print(not '')

# any 只要有一个为True 返回True
print(any([0, '', None]))
print(any([0, '', None, 1]))

# all 都为True则返回True
print(all([0, 1, "hi"]))
print(all([1, "hi"]))
