list_test = [5, 2, 4, 1, 5, 2, 9, 6]


def sorted_key_fn(param1):
    """
    sorted内置函数中参数打印    
    :return:返回类型必须是一个可比较的值
    """
    print('param1', param1)
    return param1


if __name__ == '__main__':
    print(sorted(list_test, key=sorted_key_fn))
