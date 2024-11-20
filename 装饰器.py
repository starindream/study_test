import os
import time
from functools import wraps

time_start = time.time()


def log(func):
    print('log')

    @wraps(func)
    def wrapper():
        """
        log
        :return:
        """
        print('进入')
        func()
        print('退出')

    return wrapper


def log_two(func):
    print('log_two')

    @wraps(func)
    def wrapper():
        """
        log_two
        :return:
        """
        print('start')
        func()
        print('end')

    return wrapper


@log_two
@log
def test():
    """
    test
    :return:
    """
    print('触发')


if __name__ == '__main__':
    # print(os.environ)
    # test()
    # print(test.__doc__)
    # print('结束时间',time.time()-time_start)
    test()
