# 99乘法表

L = [str(i) + "*" + str(j) + "=" + str(i * j) for j in range(1, 10) for i in range(1, 10) if i <= j]
for i in range(1, 10):
    cnt = 1
    while L:
        print(L.pop(0), end="\t")
        if cnt == i:
            print()
            break
        cnt += 1
