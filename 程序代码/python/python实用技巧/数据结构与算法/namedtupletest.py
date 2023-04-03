from collections import namedtuple

# 名字,语文,数学
Students = [
    ["djm",10,20],
    ["dd",80,20],
    ["aa",10,90],
    ["cc",100,20],
]
# 求每个学生总分

# 使用下标
for student in Students:
    print(student[0],":",student[1]+student[2])

# 使用命名分组
Student = namedtuple("Student",["name","chinese","math"])
for student in Students:

    student = Student(*student) # 这里必须使用参数展开符
    
    print(student.name,":",student.chinese+student.math)

