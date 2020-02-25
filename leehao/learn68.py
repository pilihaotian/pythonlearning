# get_score()，来获取用户输入的学习成绩（0-100）整数，如果输入错误，则此函数返回0


def get_score():
    try:
        score = int(input("请输入学习成绩："))
    except ValueError as err:
        print(err)
        return 0
    else:
        if 0 <= score <= 100:
            return score
        else:
            return 0


while True:
    print(get_score())
