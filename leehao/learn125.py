# sql操作
# pycharm 在 set pip中导入pymysql
import pymysql


class Student:
    def __init__(self, stuid, name, age, sex, height):
        self.stuid = stuid
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


def query_stu(cs):
    # 查询
    cs.execute("select * from student")
    # 显示结果
    return cursor.fetchall()


def insert_stu(cs, stu):
    # 查询
    return cs.execute(
        "insert into student(id,name,age,sex,height) values('%d','%s','%d','%d','%f')" % (
            stu.stuid, stu.name, stu.age, stu.sex, stu.height))


def insert_stu(cs, stu):
    # 插入
    return cs.execute(
        "insert into student(id,name,age,sex,height) values('%d','%s','%d','%d','%f')" % (
            stu.stuid, stu.name, stu.age, stu.sex, stu.height))


def update_stu_by_id(cs, stu):
    # 插入
    return cs.execute(
        "update student set name='%s',age='%d',sex='%d',height='%f' where id='%d'" %
        (stu.name, stu.age, stu.sex, stu.height, stu.stuid))


def del_stu(cs, stuid):
    # 删除
    return cs.execute(
        "delete from student where id=" + str(stuid))


# 创建连接
connect = pymysql.connect('localhost', 'root', 'Password@2018', 'pythonlearn')

# 创建游标
cursor = connect.cursor()
# 操作数据库
# 查询
data = query_stu(cursor)
print(data)
# 插入
stu = Student(29, 'wangwu', 29, 1, 180)
insert_stu(cursor, stu)
data = query_stu(cursor)
print(data)
# 修改
stu.height = 10000
update_stu_by_id(cursor, stu)
data = query_stu(cursor)
print(data)
# 删除
del_stu(cursor, stu.stuid)
data = query_stu(cursor)
print(data)
# 提交数据库
connect.commit()
# 关闭游标、关闭数据库连接
cursor.close()
connect.close()

# 结果
#  (19, 'wangwu', 29, 1, 10000.0))
#  (19, 'wangwu', 29, 1, 10000.0), (29, 'wangwu', 29, 1, 180.0))
#  (19, 'wangwu', 29, 1, 10000.0), (29, 'wangwu', 29, 1, 10000.0))
#  (19, 'wangwu', 29, 1, 10000.0))
