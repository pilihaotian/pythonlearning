# 输入结果是什么
# else语句是否会执行
# else : print("for-j")不会执行
for i in [1, 2]:
    for j in [1, 2, 3]:
        print(i, j)
        break
    else:
        print("for-j")
else:
    print("for-i")
