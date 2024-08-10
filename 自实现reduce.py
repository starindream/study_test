from functools import reduce, wraps

list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 问题：当init没有值时，feature_fn应该不能传入第一个参数，否则会出现数据类型错误。
# 解答：可以尝试使用装饰器来进行解决
# 错误：装饰器可以更改传参，但是函数体内部的参数没办法解决
# 再解答：如果初始值不存在，可以使用可迭代对象的第一个值来当作初始值


def reduce_util(feature_fn, iter_data, init=None):
    """
    reduce函数
    :param feature_fn:初始值或为上一个函数的返回值
    :param iter_data:可迭代对象
    :param init:初始值
    :return:最后的返回值
    """
    # 注意：python中没有块级作用域，只有全局作用域、局部作用域(函数作用域)、内置作用域
    # 函数作用域内部使用了全局作用域相同的变量是不会改变全局作用域的
    if init:
        result = init
    else:
        result = iter_data[0]
        iter_data = iter_data[1:]
    print('函数体内部的iter_data', iter_data)
    for item in iter_data:
        result = feature_fn(result, item)
    return result


test = [1, 2, 3]


def updateTest(test):
    test.append(1)
    print('函数内', test)


if __name__ == '__main__':
    res = reduce_util(lambda prev, item: prev if (prev + item) % 2 == 0 else prev + item, list_test)
    print('reduce =>', res)
    updateTest(test)
    print(test)
