# 模拟斗地主，三个人，底牌留三张
import random

# 排序规则，去除花色后，大小比较
all_number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '小王', '大王']


def cmp(s):
    if s != '大王' and s != '小王':
        s = s[1:]
    return all_number.index(s)


flower = ['♥', '♠', '♣', '♦']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# 存入列表，顺序
all_card = [i + j for i in flower for j in numbers]
# 加入大小王
all_card.append("大王")
all_card.append("小王")
print("洗牌前", all_card)
# 洗牌，打乱
random.shuffle(all_card)
print("洗牌后", all_card)

zhangsan_card = []
lisi_card = []
wangwu_card = []

# 每人17张
for i in range(17):
    zhangsan_card.append(all_card.pop())
    lisi_card.append(all_card.pop())
    wangwu_card.append(all_card.pop())

print("zhangsan_card的牌\n", sorted(zhangsan_card, key=cmp))
print("lisi_card的牌\n", sorted(lisi_card, key=cmp))
print("wangwu_card的牌\n", sorted(wangwu_card, key=cmp))
print("底牌\n", sorted(all_card, key=cmp))
