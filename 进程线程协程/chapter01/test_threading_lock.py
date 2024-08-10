import threading
import time


# 获得一把锁
my_lock = threading.Lock()
your_lock = threading.RLock()

# 我的银行账户
balance = 0


def change_it(n):
    """ 改变我的余额 """
    global balance

    # 方式一，使用with
    with your_lock:
        balance = balance + n
        time.sleep(2)
        balance = balance - n
        time.sleep(1)
        print('-N---> {0}; balance: {1}'.format(n, balance))

    # 方式二
    # try:
    #     print('start lock')
    #     # 添加锁
    #     your_lock.acquire()
    #     print('locked one ')
    #     # 资源已经被锁住了，不能重复锁定, 产生死锁
    #     your_lock.acquire()
    #     print('locked two')
    #     balance = balance + n
    #     time.sleep(2)
    #     balance = balance - n
    #     time.sleep(1)
    #     print('-N---> {0}; balance: {1}'.format(n, balance))
    # finally:
    #     # 释放掉锁
    #     your_lock.release()
    #     your_lock.release()


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