# exec

# 和eval略微不同，也是把字符串当作《程序文件》*.py来执行
# exec就是python编译器编译python语言文件的时候，调用的函数
# 如 s = cat a.py   exec(s)
# 格式：exec(表达式，全局变量（None），局部变量，（None）)


# 自己写一个编译解析器，编译用户输入的语句

while True:
    s = input("请输入语句（bye结束）>>>")
    if s == 'bye':
        break
    else:
        exec(s)

# 测试
# 请输入语句（bye结束）>>>a = 100
# 请输入语句（bye结束）>>>b = 200
# 请输入语句（bye结束）>>>c = 300
# 请输入语句（bye结束）>>>print(max(a,b,c))
# 300
