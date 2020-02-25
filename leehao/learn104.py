# 继承、派生
# 继承是从已有类中派生出新类，新类具有原类的行为和属性
# 派生是从已有类中衍生出新类，在新类中添加新的属性和行为
# 基类、超类、父类、派生类、子类

# 单继承


class Human:
    def say(self, what):
        print("说", what)

    def walk(self, distance):
        print("走了", distance, "公里")


class Student(Human):
    # 重写父类
    def say(self, what):
        print("学生说", what)

    def study(self, subject):
        print("学生正在学习", subject)


class Teacher(Human):
    # 重写父类
    def say(self, what):
        print("老师", what)


stu1 = Student()
stu1.say("今天天气不错")
stu1.walk(10)
stu1.study('python')
