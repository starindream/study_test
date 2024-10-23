import random


class Student:
    """
    学生的信息
    """

    students = []

    def __init__(self, students=[]):
        print(students)
        for item in students:
            info = {
                'name': item,
                's_number': random.randint(1, 10000)
            }
            self.students.append(info)
            

class CourseInfo:
    """
    课程信息
    """
    courses = []

    def __init__(self, courses=[]):
        for item in courses:
            info = {
                '课程名称': item
            }
            self.courses.append(info)


class Teacher:
    """
    教师信息
    """
    teachers = []

    def __init__(self, teachers=[]):
        for item in teachers:
            info = {
                '教师名称': item
            }
            self.teachers.append(info)


if __name__ == '__main__':
    student = Student(['刘一', '陈二', '张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十'])
    print(student.students)
