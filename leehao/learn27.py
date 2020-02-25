# 求出100-999以内的水仙花数（个位的三次方、十位的三次方、百位的三次方之和等于原数字）
for i in range(100, 1000):
    baiwei = int(str(i)[0])
    shiwei = int(str(i)[1])
    gewei = int(str(i)[2])
    if i == (baiwei ** 3 + shiwei ** 3 + gewei ** 3):
        print(i)
