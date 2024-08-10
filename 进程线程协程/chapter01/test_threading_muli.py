import threading


# 我的银行账户
import time

balance = 0


def change_it(n):
    """ 改变我的余额 """
    global balance
    balance = balance + n
    time.sleep(2)
    balance = balance - n
    time.sleep(1)
    print('-N---> {0}; balance: {1}'.format(n, balance))


class ChangeBalanceThread(threading.Thread):
    """
    改变银行余额的线程
    """

    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self):
        for i in range(100):
            change_it(self.num)


if __name__ == '__main__':
    t1 = ChangeBalanceThread(5)
    t2 = ChangeBalanceThread(8)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('the last: {0}'.format(balance))