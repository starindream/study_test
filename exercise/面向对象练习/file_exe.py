from example import Student, CourseInfo, Teacher
from copy import deepcopy


def part_line(text=''):
    """
    分割线方法
    :param text:描述信息
    :return:
    """
    sign_str = ''
    for i in range(0, 10):
        sign_str = sign_str + '*'
    print(f'{sign_str}{text}{sign_str}')


def init_student(student_info):
    students = Student(student_info)
    return students


def init_course(course_info):
    """
    初始化课程信息
    :param course_info:课程名称列表
    :return:
    """
    course = CourseInfo(course_info)
    return course


def init_teacher(teacher_info):
    """
    初始化教师信息
    """
    teachers = Teacher(teacher_info)
    return teachers


def connect_course_to_teacher(course_info, teacher_info):
    new_course_info = deepcopy(course_info)
    print('course_info', course_info)
    for index in range(len(new_course_info)):
        new_course_info[index].update(teacher_info[index])
    return new_course_info


def student_to_course(student, course):
    info = []
    for index in range(len(student)):
        info.append({'Name': student[index].get('name',None), 'Selected': course[index]})
    return info


if __name__ == '__main__':
    part_line()
    student = init_student(['刘一', '陈二', '张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十'])
    teacher = init_teacher(
        ['教师一', '教师二', '教师三', '教师四', '教师五', '教师六', '教师七', '教师八', '教师九', '教师十'])
    course = init_course(
        ['课程一', '课程二', '课程三', '课程四', '课程五', '课程六', '课程七', '课程八', '课程九', '课程十'])
    print('courses', dir(course))
    connect_course = connect_course_to_teacher(course.courses, teacher.teachers)
    result = student_to_course(student.students, connect_course)
    print('connect_course =>', connect_course)
    print('course =>', course.courses)
    print('result =>', result)
