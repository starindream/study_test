def exceptError():
    try:
        # return 1
        print('代码执行时')
        num = 1 / 0
    except:  # 异常执行语句
        print('执行except语句')
    else:  # 程序无异常执行语句，try中有return不执行
        print('执行else语句')
    finally:  # 无论是否有异常都会执行的语句  无论是否有return都会执行
        print('执行finally语句')
    print('函数末尾')  # 遇到return不会执行


if __name__ == '__main__':
    exceptError()
