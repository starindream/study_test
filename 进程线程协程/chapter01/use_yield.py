

def count_down(n):
    """ 倒计时效果 """
    while n > 0:
        yield n
        n -= 1


def yield_test():
    """ 实现协程函数 """
    while True:
        n = (yield )
        print(n)


if __name__ == '__main__':
    # rest = count_down(5)
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    rest = yield_test()
    next(rest)
    rest.send('6666')
    rest.send('6666')
