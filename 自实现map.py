list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def map_gen(feature_fn, iter_data):
    """
    map函数：    
    :param feature_fn:功能函数
    :param iter_data:可迭代对象
    :return:迭代器
    """
    for item in iter_data:
        result = feature_fn(item)
        yield result


if __name__ == '__main__':
    res = map_gen(lambda x: x ** 2, list_test)
    print(res)
    for i in res:
        print('for循环', i)
