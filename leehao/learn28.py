# 猴子吃桃，第一天吃了一半又1个，第二天吃了一半+1，第十天 只剩1个了。问 第一天多少个？
cnt = 1
for i in range(1, 10):
    cnt = (cnt + 1) * 2
print(cnt)


# 递归法
def getPeach(day):
    # 第十天，剩余1个
    if day == 10:
        return 1
    else:
        # 计算前一天和后一天之间的关系
        return (getPeach(day + 1) + 1) * 2


print(getPeach(1))
