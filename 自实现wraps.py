def wraps(props_fn):
    """
    实现传入函数的内置变量的赋值装饰器函数
    :param props_fn: 装饰器传入参数的函数，目标的函数内置变量
    :return:
    """

    def decorator(func):
        """
        实际的装饰器函数
        :param func:被装饰的函数，需要被覆盖的函数内置变量
        :return:
        """

        def wrapper():
            """
            我是wrapper函数
            """
            func()

        wrapper.__doc__ = props_fn.__doc__
        return wrapper

    return decorator


def source():
    """
    我是原函数
    """
    pass


@wraps(source)
def need_cover():
    """
    我是需要被覆盖的函数
    """
    pass


if __name__ == '__main__':
    print(need_cover.__doc__)
