list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_gen(feature_fn, iter_data):
    """
    filter函数
    :param feature_fn:功能函数
    :param iter_data: 可迭代对象
    :return:迭代器
    """
    for item in iter_data:
        is_confirm = feature_fn(item)
        # 如果满足条件则返回当前的值(item)，否则则不返回值
        if is_confirm:
            yield item
        else:
            # 不满足条件则不进行返回，不yield
            pass


if __name__ == '__main__':
    res = filter_gen(lambda x: x % 2 == 0, list_test)
    print('filter',filter(lambda x: x % 2 == 0 ,list_test))
    print('res', res)
    for i in res:
        print('for 循环', i)
