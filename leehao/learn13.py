# 输入很多正整数，当输入小于0时结束

L = []
while True:
    temp = int(input())
    if temp < 0:
        break
    L.append(temp)

L1 = L.copy()
L1.sort(reverse=True)
print('数字之和', sum(L))
# 输出这些和第二大的数字
print('最大的数字', L1[0])
print('第二大的数字', L1[1])
# 删除最小的数字
minNumber = L1[len(L1) - 1]
L.remove(minNumber)
print('删除最小的数字', minNumber)
# 按照原来输入的顺序打印剩余的这些数字
print(L)
