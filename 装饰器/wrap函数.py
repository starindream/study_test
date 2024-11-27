from functools import wraps


# 理解：将函数的变量名，赋值给新函数的变量名，且不改变新函数的功能。

# 开始时运行，获取原函数
def wrap(func):
    # 实际装饰器，传入新函数
    def decorator(new_func):
        # 将新函数的函数名改为旧函数的函数名，且不改变函数功能，返回原函数，正常的装饰器，会返回一个新函数，新函数内部会添加新功能
        new_func.__name__ = func.__name__
        return new_func

    return decorator


def login_wrap(func):
    @wrap(func)
    def inner():
        print('新操作')
        return func()

    return inner


@login_wrap
def login():
    print(login.__name__)


login()
