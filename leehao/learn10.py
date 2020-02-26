# Demo1
# Pyton
for letter in 'Python':
    if letter == 'h':
        continue
    print('当前字母：', letter)

# Demo2
# 9 8 7 6 4 3 2 1 0 Good Bye!
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前var值：', var)
print('Good Bye!')
